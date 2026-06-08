"""
Router agent — classifies natural-language trading queries into structured intents.
This is the entry point for all natural-language commands.

The router outputs a RouterOutput schema. It does not execute anything.
Routing decisions are logged to the trade journal for future ML training.
"""

from __future__ import annotations

from .agent_runner import run_agent
from .schemas import (
    AssetType,
    RouterIntent,
    RouterOutput,
)
from ..utils.logging import get_logger

logger = get_logger(__name__)

# Intent → agents that will be needed downstream
INTENT_AGENT_MAP: dict[RouterIntent, list[str]] = {
    RouterIntent.GENERAL_MARKET_SCAN: ["research_agent", "strategy_agent", "skeptic_agent"],
    RouterIntent.KALSHI_MARKET_SCAN: ["research_agent", "strategy_agent", "skeptic_agent"],
    RouterIntent.EQUITY_ANALYSIS: ["research_agent", "strategy_agent", "skeptic_agent"],
    RouterIntent.CRYPTO_ANALYSIS: ["research_agent", "strategy_agent", "skeptic_agent"],
    RouterIntent.PORTFOLIO_RISK_QUESTION: ["risk_agent"],
    RouterIntent.TRADE_PROPOSAL_REQUEST: [
        "research_agent", "strategy_agent", "skeptic_agent", "risk_agent"
    ],
    RouterIntent.ORDER_EXECUTION_REQUEST: [
        "risk_agent", "execution_agent"
    ],
    RouterIntent.TRADE_REVIEW_REQUEST: ["review_agent"],
    RouterIntent.STRATEGY_PERFORMANCE_REQUEST: ["review_agent"],
    RouterIntent.SETTINGS_OR_CONFIG_REQUEST: [],
    RouterIntent.UNSAFE_OR_DISALLOWED: [],
    RouterIntent.UNCLEAR: [],
}


def route_query(user_query: str) -> RouterOutput:
    """
    Route a natural-language query to the correct intent.
    Returns a RouterOutput that the orchestrator uses to dispatch the workflow.
    """
    logger.info(f"Routing query: {user_query[:100]}")

    raw = run_agent("router_agent", user_query)

    # Parse intent safely
    intent_str = raw.get("intent", "unclear")
    try:
        intent = RouterIntent(intent_str)
    except ValueError:
        logger.warning(f"Router returned unknown intent '{intent_str}', defaulting to unclear")
        intent = RouterIntent.UNCLEAR

    # Parse asset type safely
    asset_type_str = raw.get("extracted_asset_type")
    asset_type = None
    if asset_type_str:
        try:
            asset_type = AssetType(asset_type_str)
        except ValueError:
            pass

    # Use agent map to fill required_agents if not provided
    required_agents = raw.get("required_agents") or INTENT_AGENT_MAP.get(intent, [])

    result = RouterOutput(
        intent=intent,
        confidence=float(raw.get("confidence", 0.5)),
        required_agents=required_agents,
        requires_live_data=bool(raw.get("requires_live_data", False)),
        requires_broker_access=bool(raw.get("requires_broker_access", False)),
        execution_requested=bool(raw.get("execution_requested", False)),
        risk_level=raw.get("risk_level", "medium"),
        clarifying_question=raw.get("clarifying_question"),
        reasoning_summary=raw.get("reasoning_summary", ""),
        extracted_asset=raw.get("extracted_asset"),
        extracted_asset_type=asset_type,
        raw_agent_output=raw.get("_raw_agent_output", ""),
    )

    logger.info(
        f"Routed to intent={intent.value}, confidence={result.confidence:.2f}, "
        f"asset={result.extracted_asset}, execution_requested={result.execution_requested}"
    )

    # Safety gate: never allow execution routing without explicit flag
    if result.execution_requested and not _confirm_execution_intent(user_query):
        logger.warning("Execution intent detected but query does not contain explicit execution language. Downgrading.")
        result.execution_requested = False
        result.risk_level = "medium"

    return result


def route_query_offline(user_query: str) -> RouterOutput:
    """
    Offline router for when ANTHROPIC_API_KEY is not set.
    Uses simple keyword matching — much less accurate, but allows CLI to work without API.
    Returns RouterOutput with low confidence.
    """
    query = user_query.lower()

    # Execution patterns
    if any(kw in query for kw in ["execute", "paper-execute", "open ticket", "fill ticket"]):
        intent = RouterIntent.ORDER_EXECUTION_REQUEST
    # Review patterns
    elif any(kw in query for kw in ["review", "my trades", "performance", "p&l", "pnl"]):
        intent = RouterIntent.TRADE_REVIEW_REQUEST
    # Kalshi patterns
    elif any(kw in query for kw in ["kalshi", "prediction market", "yes or no", "event market"]):
        intent = RouterIntent.KALSHI_MARKET_SCAN
    # Equity analysis
    elif any(kw in query for kw in ["analyze", "analysis", "research", "stock", "equity"]):
        intent = RouterIntent.EQUITY_ANALYSIS
    # Proposal
    elif any(kw in query for kw in ["propose", "trade idea", "should i buy", "should i sell", "opportunity"]):
        intent = RouterIntent.TRADE_PROPOSAL_REQUEST
    # Config/settings
    elif any(kw in query for kw in ["setting", "config", "risk limit", "allowlist"]):
        intent = RouterIntent.SETTINGS_OR_CONFIG_REQUEST
    # Scan
    elif any(kw in query for kw in ["scan", "what should i trade", "find me", "opportunities"]):
        intent = RouterIntent.GENERAL_MARKET_SCAN
    else:
        intent = RouterIntent.UNCLEAR

    # Extract ticker (simple heuristic — uppercase 1-5 char word)
    import re
    tickers = re.findall(r'\b[A-Z]{1,5}\b', user_query)
    extracted_asset = tickers[0] if tickers else None

    return RouterOutput(
        intent=intent,
        confidence=0.4,  # low confidence — offline mode
        required_agents=INTENT_AGENT_MAP.get(intent, []),
        requires_live_data=intent not in (
            RouterIntent.TRADE_REVIEW_REQUEST,
            RouterIntent.SETTINGS_OR_CONFIG_REQUEST,
            RouterIntent.UNCLEAR,
        ),
        requires_broker_access=intent == RouterIntent.ORDER_EXECUTION_REQUEST,
        execution_requested=intent == RouterIntent.ORDER_EXECUTION_REQUEST,
        risk_level="high" if intent == RouterIntent.ORDER_EXECUTION_REQUEST else "medium",
        clarifying_question="Could you be more specific?" if intent == RouterIntent.UNCLEAR else None,
        reasoning_summary="Offline keyword-based routing (low confidence). Set ANTHROPIC_API_KEY for accurate routing.",
        extracted_asset=extracted_asset,
    )


def _confirm_execution_intent(query: str) -> bool:
    """Check that query contains explicit execution language, not just analysis language."""
    query = query.lower()
    return any(kw in query for kw in [
        "execute", "fill", "open trade", "place", "paper-execute", "paper execute",
        "run ticket", "execute ticket"
    ])
