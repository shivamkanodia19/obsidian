"""
Deterministic risk engine.

Contains NO LLM calls. Every decision is code.
This is the hard gate — no agent output can override it.

Design intent: LLMs reason narratively. Code enforces limits numerically.
Both are necessary. Neither alone is sufficient.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING

from ..agents.schemas import (
    AssetType,
    OrderType,
    RiskEngineResult,
    TicketStatus,
    TradeProposal,
    OrderTicket,
)
from ..utils.logging import get_logger
from .rules import RiskLimits

logger = get_logger(__name__)

_CONFIG_PATH = Path(__file__).parent.parent / "config" / "risk_limits.yaml"


def _load_limits() -> RiskLimits:
    if _CONFIG_PATH.exists():
        return RiskLimits.from_yaml(_CONFIG_PATH)
    logger.warning("risk_limits.yaml not found — using hardcoded defaults (conservative)")
    return RiskLimits()


def check_proposal(
    proposal: TradeProposal,
    estimated_risk_dollars: float,
    current_open_positions: int,
    research_age_minutes: float,
    spread_percent: float | None = None,
    daily_loss_so_far: float = 0.0,
    volume: float | None = None,
    paper_account_size: float = 1000.0,
    has_existing_position: bool = False,
    limits: RiskLimits | None = None,
) -> RiskEngineResult:
    """
    Run all deterministic risk checks against a trade proposal.
    Returns RiskEngineResult. approved=True only if ALL hard checks pass.
    """
    if limits is None:
        limits = _load_limits()

    rejections: list[str] = []
    warnings: list[str] = []
    risk_score = 0

    # --- Hard gate 1: live trading gate ---
    # Live trading is a config-level gate enforced here too.
    # Paper trades are always allowed regardless.

    # --- Hard gate 2: asset class ---
    asset_type_allowed = {
        AssetType.EQUITY: limits.allow_equities,
        AssetType.ETF: limits.allow_equities,
        AssetType.PREDICTION_MARKET: limits.allow_prediction_markets,
        AssetType.CRYPTO: limits.allow_crypto,
        AssetType.OPTIONS: limits.allow_options,
    }.get(proposal.asset_type, False)

    if not asset_type_allowed:
        rejections.append(
            f"Asset type '{proposal.asset_type.value}' is disabled in risk_limits.yaml. "
            "Enable it explicitly before trading."
        )
        risk_score += 30

    # --- Hard gate 3: duplicate open position ---
    if has_existing_position:
        rejections.append(
            f"Open position already exists for {proposal.asset_or_market}. "
            "Close the existing position before opening a new one."
        )
        risk_score += 25

    # --- Hard gate 4: max trade risk ---
    if estimated_risk_dollars > limits.max_trade_risk_dollars:
        rejections.append(
            f"Estimated trade risk ${estimated_risk_dollars:.2f} exceeds max "
            f"${limits.max_trade_risk_dollars:.2f} per trade."
        )
        risk_score += 25

    # --- Hard gate 5: daily loss limit ---
    if daily_loss_so_far + estimated_risk_dollars > limits.max_daily_loss_dollars:
        rejections.append(
            f"Adding this trade's risk ${estimated_risk_dollars:.2f} to today's losses "
            f"${daily_loss_so_far:.2f} would exceed daily limit ${limits.max_daily_loss_dollars:.2f}."
        )
        risk_score += 25

    # --- Hard gate 6: max open positions ---
    if current_open_positions >= limits.max_open_positions:
        rejections.append(
            f"Already at max open positions ({limits.max_open_positions}). "
            "Close a position before opening a new one."
        )
        risk_score += 20

    # --- Hard gate 7: position sizing ---
    allocation_pct = (estimated_risk_dollars / paper_account_size) * 100
    if allocation_pct > limits.max_allocation_per_trade_percent:
        rejections.append(
            f"Trade risk is {allocation_pct:.1f}% of account, exceeds max "
            f"{limits.max_allocation_per_trade_percent:.1f}%."
        )
        risk_score += 20

    # --- Hard gate 8: thesis age ---
    if research_age_minutes > limits.max_thesis_age_minutes:
        rejections.append(
            f"Research is {research_age_minutes:.0f} minutes old. Max is "
            f"{limits.max_thesis_age_minutes} minutes. Re-run research before trading."
        )
        risk_score += 15

    # --- Hard gate 9: spread ---
    if spread_percent is not None:
        if spread_percent > limits.max_spread_percent:
            rejections.append(
                f"Spread {spread_percent:.1f}% exceeds max {limits.max_spread_percent:.1f}%. "
                "This trade has negative expected value before any price movement."
            )
            risk_score += 20
        elif spread_percent > limits.max_spread_percent * 0.7:
            warnings.append(
                f"Spread {spread_percent:.1f}% is approaching the max {limits.max_spread_percent:.1f}%."
            )
            risk_score += 5

    # --- Warning: liquidity ---
    if volume is not None and volume < limits.min_liquidity_threshold:
        warnings.append(
            f"Volume/open interest {volume:.0f} is below minimum {limits.min_liquidity_threshold:.0f}. "
            "Exit may be difficult."
        )
        risk_score += 10

    # --- Warning: LLM overconfidence ---
    if proposal.confidence > 0.85:
        warnings.append(
            f"Proposal confidence is {proposal.confidence:.0%}. Very high confidence from an LLM "
            "is a red flag — not a green light. LLMs generate confident-sounding analysis that may be wrong."
        )
        risk_score += 10

    risk_score = min(risk_score, 100)
    approved = len(rejections) == 0 and risk_score < limits.reject_above

    if approved and risk_score >= limits.warn_above:
        warnings.append(
            f"Risk score {risk_score}/100 is in the warning zone. Review warnings before proceeding."
        )

    max_allowed = min(
        limits.max_trade_risk_dollars,
        paper_account_size * limits.max_allocation_per_trade_percent / 100,
    )

    result = RiskEngineResult(
        proposal_id=proposal.id,
        approved=approved,
        rejection_reasons=rejections,
        warnings=warnings,
        required_user_confirmation=limits.require_manual_confirmation,
        max_allowed_size=max_allowed,
        risk_score=risk_score,
        live_trading_allowed=limits.allow_live_trading,
        final_decision="approved" if approved else "rejected",
    )

    logger.info(
        f"Risk check: proposal={proposal.id[:8]} | approved={approved} | "
        f"score={risk_score} | rejections={len(rejections)} | warnings={len(warnings)}"
    )

    return result


def check_ticket(ticket: OrderTicket, limits: RiskLimits | None = None) -> list[str]:
    """
    Final ticket-level checks before any execution (paper or live).
    Returns list of blocking errors. Empty list = ticket is valid.

    These checks run AGAIN at execution time even if they passed before,
    because conditions may have changed since the ticket was created.
    """
    if limits is None:
        limits = _load_limits()

    errors: list[str] = []

    # Stale ticket
    if ticket.is_expired():
        errors.append(
            f"Ticket {ticket.id} has expired. Re-run risk check with fresh market data."
        )

    # Status check
    if ticket.ticket_status in (TicketStatus.RISK_REJECTED, TicketStatus.CANCELLED, TicketStatus.EXPIRED):
        errors.append(
            f"Ticket status is '{ticket.ticket_status.value}' — cannot execute. "
            "Create a new ticket."
        )

    if ticket.ticket_status == TicketStatus.PAPER_EXECUTED:
        errors.append(f"Ticket {ticket.id} has already been paper-executed.")

    if ticket.ticket_status == TicketStatus.LIVE_EXECUTED:
        errors.append(f"Ticket {ticket.id} has already been live-executed.")

    # Market order check
    if ticket.order_type == OrderType.MARKET and limits.reject_market_orders:
        errors.append(
            "Market orders are disabled. Use a limit order with a specific price."
        )

    # Broker check
    if ticket.broker not in limits.allowed_brokers:
        errors.append(
            f"Broker '{ticket.broker}' is not in allowed_brokers: {limits.allowed_brokers}. "
            "Add it explicitly to risk_limits.yaml."
        )

    # Max loss check
    if ticket.estimated_max_loss > limits.max_trade_risk_dollars:
        errors.append(
            f"Ticket estimated_max_loss ${ticket.estimated_max_loss:.2f} exceeds "
            f"max trade risk ${limits.max_trade_risk_dollars:.2f}."
        )

    # Live trading gate
    if not limits.allow_live_trading and ticket.broker not in ("paper", "kalshi_demo"):
        errors.append(
            f"Live trading is disabled. Broker '{ticket.broker}' requires live trading to be enabled. "
            "Set allow_live_trading: true in risk_limits.yaml (V4+ only)."
        )

    # Confirmation gate
    if not ticket.requires_user_confirmation and limits.require_manual_confirmation:
        errors.append(
            "requires_user_confirmation is false but config requires it. "
            "This ticket cannot be submitted without manual confirmation."
        )

    return errors
