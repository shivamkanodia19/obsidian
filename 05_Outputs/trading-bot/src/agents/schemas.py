"""
Pydantic schemas for all agent inputs and outputs.
These are the contracts — agents must return data matching these shapes.
The risk engine works on these types, not raw strings.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional
from uuid import uuid4

from pydantic import BaseModel, Field


def _now() -> datetime:
    return datetime.now(timezone.utc)


# ---------------------------------------------------------------------------
# Shared enums
# ---------------------------------------------------------------------------

class Direction(str, Enum):
    LONG = "long"
    SHORT = "short"
    NEUTRAL = "neutral"


class AssetType(str, Enum):
    EQUITY = "equity"
    PREDICTION_MARKET = "prediction_market"
    CRYPTO = "crypto"
    OPTIONS = "options"
    ETF = "etf"


class OrderType(str, Enum):
    LIMIT = "limit"
    MARKET = "market"   # rejected by risk engine by default


class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"
    YES = "yes"          # Kalshi
    NO = "no"            # Kalshi


class TradeStatus(str, Enum):
    PROPOSED = "proposed"
    RISK_APPROVED = "risk_approved"
    RISK_REJECTED = "risk_rejected"
    TICKET_CREATED = "ticket_created"
    PAPER_OPEN = "paper_open"
    PAPER_CLOSED = "paper_closed"
    AWAITING_CONFIRMATION = "awaiting_confirmation"
    LIVE_EXECUTED = "live_executed"   # V4+ only


class TicketStatus(str, Enum):
    """Full lifecycle for order tickets."""
    DRAFT = "draft"
    RISK_PENDING = "risk_pending"
    RISK_REJECTED = "risk_rejected"
    RISK_APPROVED = "risk_approved"
    AWAITING_USER_CONFIRMATION = "awaiting_user_confirmation"
    PAPER_EXECUTED = "paper_executed"
    DEMO_EXECUTED = "demo_executed"
    LIVE_EXECUTED = "live_executed"   # V4+ only — requires explicit config change + separate PR
    CANCELLED = "cancelled"
    EXPIRED = "expired"

    def can_transition_to(self, next_status: "TicketStatus") -> bool:
        allowed: dict[TicketStatus, set[TicketStatus]] = {
            TicketStatus.DRAFT: {TicketStatus.RISK_PENDING, TicketStatus.CANCELLED},
            TicketStatus.RISK_PENDING: {
                TicketStatus.RISK_APPROVED, TicketStatus.RISK_REJECTED
            },
            TicketStatus.RISK_REJECTED: {TicketStatus.CANCELLED},
            TicketStatus.RISK_APPROVED: {
                TicketStatus.AWAITING_USER_CONFIRMATION,
                TicketStatus.EXPIRED,
                TicketStatus.CANCELLED,
            },
            TicketStatus.AWAITING_USER_CONFIRMATION: {
                TicketStatus.PAPER_EXECUTED,
                TicketStatus.DEMO_EXECUTED,
                TicketStatus.CANCELLED,
                TicketStatus.EXPIRED,
            },
            TicketStatus.PAPER_EXECUTED: set(),
            TicketStatus.DEMO_EXECUTED: set(),
            TicketStatus.LIVE_EXECUTED: set(),
            TicketStatus.CANCELLED: set(),
            TicketStatus.EXPIRED: {TicketStatus.RISK_PENDING},  # allow re-checking
        }
        return next_status in allowed.get(self, set())


class RiskRecommendation(str, Enum):
    APPROVE = "approve"
    REJECT = "reject"
    REVISE = "revise"


# Keep legacy ExecutionStatus for backward compat with existing paper_trader.py
class ExecutionStatus(str, Enum):
    PENDING_APPROVAL = "pending_approval"
    PAPER = "paper"
    LIVE = "live"
    CANCELLED = "cancelled"


class RouterIntent(str, Enum):
    GENERAL_MARKET_SCAN = "general_market_scan"
    KALSHI_MARKET_SCAN = "kalshi_market_scan"
    EQUITY_ANALYSIS = "equity_analysis"
    CRYPTO_ANALYSIS = "crypto_analysis"
    PORTFOLIO_RISK_QUESTION = "portfolio_risk_question"
    TRADE_PROPOSAL_REQUEST = "trade_proposal_request"
    ORDER_EXECUTION_REQUEST = "order_execution_request"
    TRADE_REVIEW_REQUEST = "trade_review_request"
    STRATEGY_PERFORMANCE_REQUEST = "strategy_performance_request"
    SETTINGS_OR_CONFIG_REQUEST = "settings_or_config_request"
    UNSAFE_OR_DISALLOWED = "unsafe_or_disallowed"
    UNCLEAR = "unclear"


class SkepticRecommendation(str, Enum):
    APPROVE = "approve"
    REVISE = "revise"
    REJECT = "reject"


# ---------------------------------------------------------------------------
# Router Agent
# ---------------------------------------------------------------------------

class RouterOutput(BaseModel):
    intent: RouterIntent
    confidence: float = Field(ge=0.0, le=1.0)
    required_agents: list[str]              # e.g. ["research_agent", "strategy_agent"]
    requires_live_data: bool
    requires_broker_access: bool
    execution_requested: bool
    risk_level: str                          # "low" | "medium" | "high"
    clarifying_question: str | None = None
    reasoning_summary: str
    extracted_asset: str | None = None      # parsed ticker/market from query
    extracted_asset_type: AssetType | None = None
    raw_agent_output: str = ""
    created_at: datetime = Field(default_factory=_now)


# ---------------------------------------------------------------------------
# No-trade recommendation — first-class output, not an error state
# ---------------------------------------------------------------------------

class NoTradeReason(str, Enum):
    NO_SETUP = "no_setup"
    SPREAD_TOO_WIDE = "spread_too_wide"
    LIQUIDITY_INSUFFICIENT = "liquidity_insufficient"
    THESIS_STALE = "thesis_stale"
    RISK_REWARD_POOR = "risk_reward_poor"
    MISSING_DATA = "missing_data"
    ASSET_CLASS_DISABLED = "asset_class_disabled"
    UNSAFE_REQUEST = "unsafe_request"
    RISK_ENGINE_REJECTED = "risk_engine_rejected"
    SKEPTIC_REJECTION = "skeptic_rejection"
    DUPLICATE_OPEN_POSITION = "duplicate_open_position"
    OUTSIDE_TRADING_HOURS = "outside_trading_hours"
    MARKET_CLOSED = "market_closed"
    MANUAL = "manual"                        # user or reviewer explicitly said no


class NoTradeDecision(BaseModel):
    """Explicit no-trade — always preferred over a forced weak proposal."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    asset_or_market: str
    reason: NoTradeReason
    explanation: str
    what_would_change_this: str = ""        # conditions that would make a trade possible
    created_at: datetime = Field(default_factory=_now)
    research_id: str | None = None
    proposal_id: str | None = None


# ---------------------------------------------------------------------------
# Research Agent
# ---------------------------------------------------------------------------

class ResearchRequest(BaseModel):
    asset_or_market: str
    asset_type: AssetType
    context_notes: str = ""
    requested_at: datetime = Field(default_factory=_now)


class ResearchSummary(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    asset_or_market: str
    asset_type: AssetType
    research_summary: str
    key_facts: list[str]
    catalysts: list[str]
    uncertainty: list[str]
    data_sources_needed: list[str]
    stale_data_warnings: list[str]
    market_specific_risks: list[str]
    created_at: datetime = Field(default_factory=_now)
    raw_agent_output: str = ""


# ---------------------------------------------------------------------------
# Strategy Agent
# ---------------------------------------------------------------------------

class TradeProposal(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    research_id: str
    asset_or_market: str
    asset_type: AssetType
    trade_type: str
    direction: Direction
    proposed_entry: str
    target: str
    stop_or_invalidation: str
    time_horizon: str
    confidence: float = Field(ge=0.0, le=1.0)
    thesis: str
    bull_case: str
    bear_case: str
    why_now: str
    what_would_change_my_mind: str
    status: TradeStatus = TradeStatus.PROPOSED
    created_at: datetime = Field(default_factory=_now)
    raw_agent_output: str = ""


# ---------------------------------------------------------------------------
# Candidate trade (ranked output from scanner workflows)
# ---------------------------------------------------------------------------

class CandidateTrade(BaseModel):
    rank: int
    asset_or_market: str
    broker: str
    trade_type: str
    direction: Direction | None = None
    setup_quality_score: float | None = None   # 0-1, null = not computed
    risk_score: int | None = None              # from risk engine, null = not checked
    liquidity_score: float | None = None       # 0-1, null = no data
    confidence: float | None = None
    expected_edge: None = None                 # always null in V0 — no backtest data
    reason_for_rank: str
    why_not_higher: str
    no_trade_reason: str | None = None        # set if this candidate was rejected


# ---------------------------------------------------------------------------
# Risk Agent (LLM advisory)
# ---------------------------------------------------------------------------

class RiskAgentOutput(BaseModel):
    proposal_id: str
    risk_rating: str
    reject_reasons: list[str]
    required_revisions: list[str]
    max_position_size_recommendation: str
    key_risks: list[str]
    final_recommendation: RiskRecommendation
    raw_agent_output: str = ""


class RiskEngineResult(BaseModel):
    """Output of the DETERMINISTIC risk engine (not the LLM risk agent)."""
    proposal_id: str
    approved: bool
    rejection_reasons: list[str]
    warnings: list[str]
    required_user_confirmation: bool
    max_allowed_size: float
    risk_score: int = Field(ge=0, le=100)
    live_trading_allowed: bool = False
    final_decision: str = ""               # "approved" | "rejected" | "revise"
    checked_at: datetime = Field(default_factory=_now)

    def model_post_init(self, __context: Any) -> None:
        if not self.final_decision:
            self.final_decision = "approved" if self.approved else "rejected"


# ---------------------------------------------------------------------------
# Order Ticket — full lifecycle
# ---------------------------------------------------------------------------

class TicketAuditEntry(BaseModel):
    from_status: TicketStatus
    to_status: TicketStatus
    reason: str = ""
    timestamp: datetime = Field(default_factory=_now)


class OrderTicket(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    proposal_id: str
    risk_engine_result_id: str = ""
    broker: str
    asset_or_market: str
    asset_type: AssetType
    side: OrderSide
    order_type: OrderType
    limit_price: float | None = None
    quantity: float
    estimated_max_loss: float
    requires_user_confirmation: bool = True
    ticket_status: TicketStatus = TicketStatus.DRAFT
    # Keep legacy field for backward compat with existing paper_trader / tests
    execution_status: ExecutionStatus = ExecutionStatus.PENDING_APPROVAL
    notes: str = ""
    audit_trail: list[TicketAuditEntry] = Field(default_factory=list)
    expires_at: datetime | None = None
    created_at: datetime = Field(default_factory=_now)
    raw_agent_output: str = ""

    def transition(self, new_status: TicketStatus, reason: str = "") -> None:
        """Perform a lifecycle transition, recording audit trail."""
        if not self.ticket_status.can_transition_to(new_status):
            raise ValueError(
                f"Invalid ticket transition: {self.ticket_status} → {new_status}"
            )
        entry = TicketAuditEntry(
            from_status=self.ticket_status,
            to_status=new_status,
            reason=reason,
        )
        self.audit_trail.append(entry)
        self.ticket_status = new_status

    def is_expired(self) -> bool:
        if self.expires_at is None:
            return False
        return datetime.now(timezone.utc) > self.expires_at

    def is_executable(self) -> bool:
        return (
            self.ticket_status == TicketStatus.AWAITING_USER_CONFIRMATION
            and not self.is_expired()
        )


# ---------------------------------------------------------------------------
# Paper Trade
# ---------------------------------------------------------------------------

class PaperTrade(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    ticket_id: str
    proposal_id: str = ""
    asset_or_market: str
    asset_type: AssetType
    direction: Direction
    entry_price: float
    exit_price: float | None = None
    quantity: float
    strategy_name: str = ""
    thesis: str = ""
    notes: str = ""
    opened_at: datetime = Field(default_factory=_now)
    closed_at: datetime | None = None
    pnl: float | None = None
    status: TradeStatus = TradeStatus.PAPER_OPEN


# ---------------------------------------------------------------------------
# Trade Journal Entry — links every step of a trade lifecycle
# ---------------------------------------------------------------------------

class TradeJournalEntry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    original_user_question: str = ""
    router_intent: RouterIntent | None = None
    research_id: str | None = None
    proposal_id: str | None = None
    ticket_id: str | None = None
    trade_id: str | None = None
    review_id: str | None = None
    agents_used: list[str] = Field(default_factory=list)
    thesis: str = ""
    skeptic_summary: str = ""
    risk_score: int | None = None
    risk_approved: bool | None = None
    entry_price: float | None = None
    exit_price: float | None = None
    pnl: float | None = None
    outcome: str = ""                        # "win" | "loss" | "breakeven" | "no_trade" | "open"
    notes: str = ""
    created_at: datetime = Field(default_factory=_now)
    updated_at: datetime = Field(default_factory=_now)


# ---------------------------------------------------------------------------
# Review Agent
# ---------------------------------------------------------------------------

class TradeReview(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    trade_id: str
    journal_entry_id: str = ""
    result: str
    pnl: float
    thesis_accuracy: str
    execution_quality: str
    risk_management_quality: str
    lessons: list[str]
    strategy_adjustments: list[str]
    reviewed_at: datetime = Field(default_factory=_now)
    raw_agent_output: str = ""


# ---------------------------------------------------------------------------
# Skeptic Agent (v2 — strengthened)
# ---------------------------------------------------------------------------

class SkepticOutput(BaseModel):
    proposal_id: str
    strongest_argument_against_trade: str
    hidden_assumptions: list[str]
    missing_data: list[str]
    overfitting_or_story_risk: str
    liquidity_and_execution_risk: str
    no_trade_case: str
    required_changes_before_trade: list[str]
    skeptic_recommendation: SkepticRecommendation
    # Legacy field kept for backward compat
    recommendation: str = ""
    raw_agent_output: str = ""
    created_at: datetime = Field(default_factory=_now)

    def model_post_init(self, __context: Any) -> None:
        if not self.recommendation:
            self.recommendation = self.skeptic_recommendation.value


# ---------------------------------------------------------------------------
# ML Model Scorer — honest stub
# ---------------------------------------------------------------------------

class ModelScore(BaseModel):
    """
    Placeholder output from a future ML scoring model.
    In V0 this is always 'not_available'.
    Do not fake scores. Do not pretend this has been trained.
    """
    proposal_id: str
    available: bool = False
    probability_of_positive_outcome: float | None = None
    expected_value: float | None = None
    setup_quality: float | None = None
    liquidity_risk: float | None = None
    confidence_calibration: float | None = None
    model_version: str = "not_available"
    note: str = (
        "ML scoring not available in V0. No model has been trained. "
        "No historical data exists. Do not use placeholder values as signals."
    )


# ---------------------------------------------------------------------------
# Scan results
# ---------------------------------------------------------------------------

class KalshiMarketScan(BaseModel):
    ticker: str
    title: str
    yes_price: float | None = None
    no_price: float | None = None
    volume: float | None = None
    open_interest: float | None = None
    close_time: datetime | None = None
    notes: str = ""
    scanned_at: datetime = Field(default_factory=_now)


class EquityWatchlistItem(BaseModel):
    ticker: str
    last_price: float | None = None
    daily_change_pct: float | None = None
    volume: float | None = None
    notes: str = ""
    scanned_at: datetime = Field(default_factory=_now)
