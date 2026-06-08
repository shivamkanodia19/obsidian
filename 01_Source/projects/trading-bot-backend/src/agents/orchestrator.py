"""
Orchestrator — turns routed intents into end-to-end workflows.

This is the central coordinator. It:
- Receives a RouterOutput
- Dispatches the right sequence of agents
- Runs the deterministic risk engine
- Returns a structured result for the CLI to display

Design rules:
- No LLM calls directly in this file — delegates to agent_runner
- No broker calls directly — delegates to broker clients
- No execution without explicit confirmation — delegates to manual_approval
- No-trade is a first-class return value
- Journal entry created for every workflow run
"""

from __future__ import annotations

from datetime import datetime, timezone, timedelta
from typing import Union

from .agent_runner import run_agent
from .schemas import (
    AssetType,
    CandidateTrade,
    Direction,
    ExecutionStatus,
    NoTradeDecision,
    NoTradeReason,
    OrderSide,
    OrderTicket,
    OrderType,
    PaperTrade,
    ResearchSummary,
    RouterIntent,
    RouterOutput,
    SkepticOutput,
    SkepticRecommendation,
    TicketStatus,
    TradeJournalEntry,
    TradeProposal,
    TradeStatus,
)
from ..config import get_settings
from ..data import (
    has_open_position_for,
    save_journal_entry,
    save_no_trade,
    save_proposal,
    save_research,
    save_risk_result,
)
from ..execution import PaperTrader, create_order_ticket, require_confirmation
from ..risk import check_proposal
from ..utils.ids import new_id
from ..utils.logging import get_logger
from ..utils.time import minutes_ago

logger = get_logger(__name__)

# Result type that workflows return
WorkflowResult = Union[
    TradeProposal,
    NoTradeDecision,
    list[CandidateTrade],
    PaperTrade,
    dict,
]


class Orchestrator:
    """
    Routes intent → workflow → result.
    Instantiate once per CLI command invocation.
    """

    def __init__(self, user_question: str = "") -> None:
        self._question = user_question
        self._journal = TradeJournalEntry(
            original_user_question=user_question,
            agents_used=[],
        )
        self._settings = get_settings()

    def run(self, route: RouterOutput) -> WorkflowResult:
        """Dispatch workflow based on route intent."""
        self._journal.router_intent = route.intent

        if route.intent == RouterIntent.UNSAFE_OR_DISALLOWED:
            return self._no_trade(
                asset_or_market=route.extracted_asset or "unknown",
                reason=NoTradeReason.UNSAFE_REQUEST,
                explanation=f"Request classified as unsafe or disallowed. {route.reasoning_summary}",
            )

        if route.intent == RouterIntent.UNCLEAR:
            return {
                "type": "clarification_needed",
                "question": route.clarifying_question or "Could you be more specific?",
                "routing_confidence": route.confidence,
            }

        if route.intent in (RouterIntent.TRADE_REVIEW_REQUEST, RouterIntent.STRATEGY_PERFORMANCE_REQUEST):
            return self._workflow_review()

        if route.intent == RouterIntent.SETTINGS_OR_CONFIG_REQUEST:
            return {"type": "settings", "note": "Use `trading show-risk-settings` to view config."}

        if route.intent in (RouterIntent.GENERAL_MARKET_SCAN, RouterIntent.KALSHI_MARKET_SCAN):
            return self._workflow_market_scan(route)

        if route.intent in (
            RouterIntent.EQUITY_ANALYSIS,
            RouterIntent.CRYPTO_ANALYSIS,
            RouterIntent.TRADE_PROPOSAL_REQUEST,
        ):
            if not route.extracted_asset:
                return {
                    "type": "clarification_needed",
                    "question": "Which asset or market would you like me to analyze?",
                }
            asset_type = route.extracted_asset_type or (
                AssetType.EQUITY if route.intent == RouterIntent.EQUITY_ANALYSIS
                else AssetType.CRYPTO if route.intent == RouterIntent.CRYPTO_ANALYSIS
                else AssetType.EQUITY
            )
            return self._workflow_propose_trade(route.extracted_asset, asset_type)

        if route.intent == RouterIntent.ORDER_EXECUTION_REQUEST:
            return {
                "type": "execution_pending",
                "note": (
                    "Execution requests require an existing approved ticket. "
                    "Use `trading execute <ticket_id>` to paper-execute a specific ticket."
                ),
            }

        if route.intent == RouterIntent.PORTFOLIO_RISK_QUESTION:
            return self._workflow_portfolio_risk()

        return {"type": "unhandled_intent", "intent": route.intent.value}

    # ------------------------------------------------------------------
    # Workflow: propose a single trade for a specific asset
    # ------------------------------------------------------------------

    def _workflow_propose_trade(
        self,
        asset: str,
        asset_type: AssetType,
        context: str = "",
    ) -> Union[TradeProposal, NoTradeDecision]:

        # Check for duplicate open position
        if has_open_position_for(asset):
            return self._no_trade(
                asset_or_market=asset,
                reason=NoTradeReason.DUPLICATE_OPEN_POSITION,
                explanation=f"Already have an open paper trade for {asset}. Close it first.",
            )

        # Step 1: Research
        research = self._run_research(asset, asset_type, context)
        if research is None:
            return self._no_trade(
                asset_or_market=asset,
                reason=NoTradeReason.MISSING_DATA,
                explanation="Research agent failed or API key not configured.",
            )

        # Step 2: Strategy
        proposal_or_notrade = self._run_strategy(research)
        if isinstance(proposal_or_notrade, NoTradeDecision):
            return proposal_or_notrade

        proposal: TradeProposal = proposal_or_notrade

        # Step 3: Skeptic review
        skeptic = self._run_skeptic(proposal, research)
        if skeptic and skeptic.skeptic_recommendation == SkepticRecommendation.REJECT:
            no_trade = self._no_trade(
                asset_or_market=asset,
                reason=NoTradeReason.SKEPTIC_REJECTION,
                explanation=f"Skeptic agent rejected: {skeptic.no_trade_case}",
                proposal_id=proposal.id,
                research_id=research.id,
            )
            self._journal.skeptic_summary = skeptic.no_trade_case[:300]
            self._save_journal(outcome="no_trade")
            return no_trade

        if skeptic:
            self._journal.skeptic_summary = skeptic.no_trade_case[:300]

        # Step 4: Deterministic risk engine
        research_age = minutes_ago(research.created_at)
        risk_result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,    # CLI will override via options
            current_open_positions=0,
            research_age_minutes=research_age,
        )
        risk_result_id = save_risk_result(risk_result)

        self._journal.risk_score = risk_result.risk_score
        self._journal.risk_approved = risk_result.approved
        self._journal.proposal_id = proposal.id
        self._journal.thesis = proposal.thesis

        if not risk_result.approved:
            no_trade = self._no_trade(
                asset_or_market=asset,
                reason=NoTradeReason.RISK_ENGINE_REJECTED,
                explanation=f"Risk engine rejected: {'; '.join(risk_result.rejection_reasons)}",
                proposal_id=proposal.id,
                research_id=research.id,
            )
            self._save_journal(outcome="no_trade")
            return no_trade

        # Step 5: Update proposal status and persist
        proposal.status = TradeStatus.RISK_APPROVED
        save_proposal(proposal)
        self._save_journal(outcome="proposed")
        return proposal

    # ------------------------------------------------------------------
    # Workflow: market scan → candidate list
    # ------------------------------------------------------------------

    def _workflow_market_scan(self, route: RouterOutput) -> list[CandidateTrade]:
        from ..brokers import KalshiClient
        from ..strategies import KalshiMarketScanner, EquityWatchlistScanner

        candidates: list[CandidateTrade] = []

        if route.intent == RouterIntent.KALSHI_MARKET_SCAN:
            scanner = KalshiMarketScanner()
            markets = scanner.scan()
            for i, m in enumerate(markets[:10]):
                candidates.append(CandidateTrade(
                    rank=i + 1,
                    asset_or_market=m.ticker,
                    broker="kalshi_demo",
                    trade_type="prediction_market",
                    direction=None,
                    setup_quality_score=None,
                    risk_score=None,
                    liquidity_score=(
                        min(1.0, (m.volume or 0) / 1000) if m.volume else None
                    ),
                    confidence=None,
                    reason_for_rank="Returned by Kalshi public API scan",
                    why_not_higher=(
                        "No analysis performed — scan only. Run propose-trade for full analysis."
                    ),
                ))
            self._save_journal(outcome="scan")
            return candidates

        else:  # general scan — equity watchlist
            scanner = EquityWatchlistScanner()
            items = scanner.scan()
            for i, item in enumerate(items):
                candidates.append(CandidateTrade(
                    rank=i + 1,
                    asset_or_market=item.ticker,
                    broker="paper",
                    trade_type="equity",
                    direction=None,
                    setup_quality_score=None,
                    risk_score=None,
                    liquidity_score=None,
                    confidence=None,
                    reason_for_rank="On allowlist watchlist",
                    why_not_higher="No live price data or analysis in V0. Run propose-trade for full analysis.",
                    no_trade_reason="No live data available" if item.last_price is None else None,
                ))
            self._save_journal(outcome="scan")
            return candidates

    # ------------------------------------------------------------------
    # Workflow: trade review summary
    # ------------------------------------------------------------------

    def _workflow_review(self) -> dict:
        from ..data import load_closed_paper_trades
        from ..review.performance_review import compute_performance

        trades = load_closed_paper_trades()
        perf = compute_performance(trades)
        self._save_journal(outcome="review")
        return {"type": "performance_summary", "data": perf}

    # ------------------------------------------------------------------
    # Workflow: portfolio risk question
    # ------------------------------------------------------------------

    def _workflow_portfolio_risk(self) -> dict:
        from ..data import load_open_paper_trades
        from ..risk.rules import RiskLimits
        from pathlib import Path

        trades = load_open_paper_trades()
        yaml_path = Path(__file__).parent.parent / "config" / "risk_limits.yaml"
        limits = RiskLimits.from_yaml(yaml_path) if yaml_path.exists() else RiskLimits()

        total_risk = sum(t.get("entry_price", 0) * t.get("quantity", 0) for t in trades)

        self._save_journal(outcome="risk_review")
        return {
            "type": "portfolio_risk",
            "open_positions": len(trades),
            "max_open_positions": limits.max_open_positions,
            "approx_total_exposure": total_risk,
            "max_daily_loss_dollars": limits.max_daily_loss_dollars,
            "trades": trades,
        }

    # ------------------------------------------------------------------
    # Internal: run individual agents
    # ------------------------------------------------------------------

    def _run_research(
        self, asset: str, asset_type: AssetType, context: str = ""
    ) -> ResearchSummary | None:
        self._journal.agents_used.append("research_agent")
        try:
            raw = run_agent(
                "research_agent",
                f"Research this asset: {asset} (type: {asset_type.value}). {context}",
            )
        except (ValueError, RuntimeError) as e:
            logger.warning(f"Research agent error: {e}")
            return None

        research = ResearchSummary(
            id=new_id(),
            asset_or_market=asset,
            asset_type=asset_type,
            research_summary=raw.get("research_summary", ""),
            key_facts=raw.get("key_facts", []),
            catalysts=raw.get("catalysts", []),
            uncertainty=raw.get("uncertainty", []),
            data_sources_needed=raw.get("data_sources_needed", []),
            stale_data_warnings=raw.get("stale_data_warnings", []),
            market_specific_risks=raw.get("market_specific_risks", []),
            raw_agent_output=raw.get("_raw_agent_output", ""),
        )
        save_research(research)
        self._journal.research_id = research.id
        return research

    def _run_strategy(
        self, research: ResearchSummary
    ) -> TradeProposal | NoTradeDecision:
        self._journal.agents_used.append("strategy_agent")
        try:
            raw = run_agent(
                "strategy_agent",
                "Based on this research, propose a trade or say no setup exists.",
                extra_context={
                    "research_summary": research.research_summary,
                    "key_facts": research.key_facts,
                    "catalysts": research.catalysts,
                    "uncertainty": research.uncertainty,
                    "market_specific_risks": research.market_specific_risks,
                },
            )
        except (ValueError, RuntimeError) as e:
            return self._no_trade(
                asset_or_market=research.asset_or_market,
                reason=NoTradeReason.MISSING_DATA,
                explanation=f"Strategy agent error: {e}",
                research_id=research.id,
            )

        if raw.get("no_setup"):
            return self._no_trade(
                asset_or_market=research.asset_or_market,
                reason=NoTradeReason.NO_SETUP,
                explanation=raw.get("reason", "Strategy agent found no tradeable setup."),
                research_id=research.id,
            )

        try:
            proposal = TradeProposal(
                id=new_id(),
                research_id=research.id,
                asset_or_market=research.asset_or_market,
                asset_type=research.asset_type,
                trade_type=raw.get("trade_type", ""),
                direction=Direction(raw.get("direction", "neutral")),
                proposed_entry=raw.get("proposed_entry", ""),
                target=raw.get("target", ""),
                stop_or_invalidation=raw.get("stop_or_invalidation", ""),
                time_horizon=raw.get("time_horizon", ""),
                confidence=float(raw.get("confidence", 0.5)),
                thesis=raw.get("thesis", ""),
                bull_case=raw.get("bull_case", ""),
                bear_case=raw.get("bear_case", ""),
                why_now=raw.get("why_now", ""),
                what_would_change_my_mind=raw.get("what_would_change_my_mind", ""),
                raw_agent_output=raw.get("_raw_agent_output", ""),
            )
        except Exception as e:
            return self._no_trade(
                asset_or_market=research.asset_or_market,
                reason=NoTradeReason.MISSING_DATA,
                explanation=f"Strategy agent returned malformed output: {e}",
                research_id=research.id,
            )

        save_proposal(proposal)
        return proposal

    def _run_skeptic(
        self, proposal: TradeProposal, research: ResearchSummary
    ) -> SkepticOutput | None:
        self._journal.agents_used.append("skeptic_agent")
        try:
            raw = run_agent(
                "skeptic_agent",
                "Challenge this trade proposal.",
                extra_context={
                    "proposal": {
                        "asset": proposal.asset_or_market,
                        "direction": proposal.direction.value,
                        "thesis": proposal.thesis,
                        "confidence": proposal.confidence,
                        "bear_case": proposal.bear_case,
                        "stop_or_invalidation": proposal.stop_or_invalidation,
                    },
                    "research": {
                        "uncertainty": research.uncertainty,
                        "market_specific_risks": research.market_specific_risks,
                        "stale_data_warnings": research.stale_data_warnings,
                    },
                },
            )
        except (ValueError, RuntimeError) as e:
            logger.warning(f"Skeptic agent error (non-blocking): {e}")
            return None

        try:
            rec_str = raw.get("skeptic_recommendation", raw.get("recommendation", "revise"))
            recommendation = SkepticRecommendation(rec_str)
        except ValueError:
            recommendation = SkepticRecommendation.REVISE

        return SkepticOutput(
            proposal_id=proposal.id,
            strongest_argument_against_trade=raw.get("strongest_argument_against_trade", raw.get("strongest_argument_against", "")),
            hidden_assumptions=raw.get("hidden_assumptions", []),
            missing_data=raw.get("missing_data", []),
            overfitting_or_story_risk=raw.get("overfitting_or_story_risk", raw.get("overfitting_risks", [""])[0] if raw.get("overfitting_risks") else ""),
            liquidity_and_execution_risk=raw.get("liquidity_and_execution_risk", ""),
            no_trade_case=raw.get("no_trade_case", raw.get("recommendation", "")),
            required_changes_before_trade=raw.get("required_changes_before_trade", []),
            skeptic_recommendation=recommendation,
            raw_agent_output=raw.get("_raw_agent_output", ""),
        )

    # ------------------------------------------------------------------
    # Internal: no-trade helper
    # ------------------------------------------------------------------

    def _no_trade(
        self,
        asset_or_market: str,
        reason: NoTradeReason,
        explanation: str,
        proposal_id: str | None = None,
        research_id: str | None = None,
        what_would_change_this: str = "",
    ) -> NoTradeDecision:
        decision = NoTradeDecision(
            asset_or_market=asset_or_market,
            reason=reason,
            explanation=explanation,
            what_would_change_this=what_would_change_this,
            proposal_id=proposal_id,
            research_id=research_id,
        )
        save_no_trade(decision)
        logger.info(f"No-trade decision: {asset_or_market} | {reason.value} | {explanation[:80]}")
        return decision

    def _save_journal(self, outcome: str) -> None:
        self._journal.outcome = outcome
        self._journal.updated_at = datetime.now(timezone.utc)
        save_journal_entry(self._journal)


def execute_workflow(user_question: str, route: RouterOutput) -> WorkflowResult:
    """Convenience function for CLI use."""
    orch = Orchestrator(user_question=user_question)
    return orch.run(route)


def execute_ticket_paper(
    ticket: OrderTicket,
    fill_price: float,
    direction: Direction,
    strategy_name: str = "",
    confirm_fn=None,
) -> PaperTrade | NoTradeDecision:
    """
    Paper-execute an approved order ticket.
    This is the only path to creating a paper trade from the orchestrator.
    Manual confirmation is always required.
    """
    from ..data import save_paper_trade, save_order_ticket

    # Ticket lifecycle check
    if not ticket.is_executable():
        return NoTradeDecision(
            asset_or_market=ticket.asset_or_market,
            reason=NoTradeReason.RISK_ENGINE_REJECTED,
            explanation=(
                f"Ticket {ticket.id} is not in executable state "
                f"(status={ticket.ticket_status.value}, expired={ticket.is_expired()}). "
                f"Re-run risk check."
            ),
        )

    # Re-run risk engine on ticket before execution
    from ..risk import check_ticket
    ticket_errors = check_ticket(ticket)
    if ticket_errors:
        ticket.transition(TicketStatus.RISK_REJECTED, reason="; ".join(ticket_errors))
        save_order_ticket(ticket)
        return NoTradeDecision(
            asset_or_market=ticket.asset_or_market,
            reason=NoTradeReason.RISK_ENGINE_REJECTED,
            explanation=f"Final ticket risk check failed: {'; '.join(ticket_errors)}",
        )

    # Manual confirmation gate
    confirmed = require_confirmation(ticket, prompt_fn=confirm_fn)
    if not confirmed:
        ticket.transition(TicketStatus.CANCELLED, reason="User declined confirmation")
        save_order_ticket(ticket)
        return NoTradeDecision(
            asset_or_market=ticket.asset_or_market,
            reason=NoTradeReason.MANUAL,
            explanation="User declined trade confirmation.",
        )

    # Execute paper trade
    trader = PaperTrader()
    trade = trader.open_trade(
        ticket=ticket,
        fill_price=fill_price,
        direction=direction,
        strategy_name=strategy_name,
    )
    save_paper_trade(trade)

    # Update ticket status
    ticket.transition(TicketStatus.PAPER_EXECUTED, reason=f"Paper fill at {fill_price}")
    save_order_ticket(ticket)

    logger.info(f"Paper trade executed: {trade.id} | {trade.asset_or_market} | entry={fill_price}")
    return trade
