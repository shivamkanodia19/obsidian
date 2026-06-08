"""
SQLAlchemy ORM models. SQLite in V0.
All raw_json columns store the full Pydantic model_dump_json() so nothing is lost.
Key fields are extracted as columns for querying.
"""

from __future__ import annotations

from datetime import datetime
from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ResearchRecord(Base):
    __tablename__ = "research"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    asset_or_market: Mapped[str] = mapped_column(String, nullable=False)
    asset_type: Mapped[str] = mapped_column(String, nullable=False)
    research_summary: Mapped[str] = mapped_column(Text, default="")
    raw_json: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class ProposalRecord(Base):
    __tablename__ = "proposals"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    research_id: Mapped[str] = mapped_column(String, nullable=False)
    asset_or_market: Mapped[str] = mapped_column(String, nullable=False)
    direction: Mapped[str] = mapped_column(String, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    thesis: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String, default="proposed")
    raw_json: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class NoTradeRecord(Base):
    __tablename__ = "no_trade_decisions"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    asset_or_market: Mapped[str] = mapped_column(String, nullable=False)
    reason: Mapped[str] = mapped_column(String, nullable=False)
    explanation: Mapped[str] = mapped_column(Text, default="")
    research_id: Mapped[str | None] = mapped_column(String, nullable=True)
    proposal_id: Mapped[str | None] = mapped_column(String, nullable=True)
    raw_json: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class RiskResultRecord(Base):
    __tablename__ = "risk_results"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    proposal_id: Mapped[str] = mapped_column(String, nullable=False)
    approved: Mapped[bool] = mapped_column(Boolean, nullable=False)
    risk_score: Mapped[int] = mapped_column(Integer, nullable=False)
    final_decision: Mapped[str] = mapped_column(String, default="")
    rejection_reasons: Mapped[str] = mapped_column(Text, default="")
    warnings: Mapped[str] = mapped_column(Text, default="")
    checked_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class OrderTicketRecord(Base):
    __tablename__ = "order_tickets"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    proposal_id: Mapped[str] = mapped_column(String, nullable=False)
    broker: Mapped[str] = mapped_column(String, nullable=False)
    asset_or_market: Mapped[str] = mapped_column(String, nullable=False)
    side: Mapped[str] = mapped_column(String, nullable=False)
    order_type: Mapped[str] = mapped_column(String, nullable=False)
    limit_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    estimated_max_loss: Mapped[float] = mapped_column(Float, nullable=False)
    ticket_status: Mapped[str] = mapped_column(String, default="draft")
    execution_status: Mapped[str] = mapped_column(String, default="pending_approval")
    expires_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    raw_json: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class TicketAuditRecord(Base):
    __tablename__ = "ticket_audit"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ticket_id: Mapped[str] = mapped_column(String, nullable=False, index=True)
    from_status: Mapped[str] = mapped_column(String, nullable=False)
    to_status: Mapped[str] = mapped_column(String, nullable=False)
    reason: Mapped[str] = mapped_column(Text, default="")
    timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class PaperTradeRecord(Base):
    __tablename__ = "paper_trades"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    ticket_id: Mapped[str] = mapped_column(String, nullable=False)
    proposal_id: Mapped[str] = mapped_column(String, default="")
    asset_or_market: Mapped[str] = mapped_column(String, nullable=False)
    asset_type: Mapped[str] = mapped_column(String, nullable=False)
    direction: Mapped[str] = mapped_column(String, nullable=False)
    entry_price: Mapped[float] = mapped_column(Float, nullable=False)
    exit_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    strategy_name: Mapped[str] = mapped_column(String, default="")
    thesis: Mapped[str] = mapped_column(Text, default="")
    notes: Mapped[str] = mapped_column(Text, default="")
    opened_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    closed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    pnl: Mapped[float | None] = mapped_column(Float, nullable=True)
    status: Mapped[str] = mapped_column(String, default="paper_open")


class TradeJournalRecord(Base):
    __tablename__ = "trade_journal"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    original_user_question: Mapped[str] = mapped_column(Text, default="")
    router_intent: Mapped[str | None] = mapped_column(String, nullable=True)
    research_id: Mapped[str | None] = mapped_column(String, nullable=True)
    proposal_id: Mapped[str | None] = mapped_column(String, nullable=True)
    ticket_id: Mapped[str | None] = mapped_column(String, nullable=True)
    trade_id: Mapped[str | None] = mapped_column(String, nullable=True)
    review_id: Mapped[str | None] = mapped_column(String, nullable=True)
    agents_used: Mapped[str] = mapped_column(Text, default="")       # JSON list
    thesis: Mapped[str] = mapped_column(Text, default="")
    skeptic_summary: Mapped[str] = mapped_column(Text, default="")
    risk_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    risk_approved: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    entry_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    exit_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    pnl: Mapped[float | None] = mapped_column(Float, nullable=True)
    outcome: Mapped[str] = mapped_column(String, default="")
    notes: Mapped[str] = mapped_column(Text, default="")
    raw_json: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class TradeReviewRecord(Base):
    __tablename__ = "trade_reviews"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    trade_id: Mapped[str] = mapped_column(String, nullable=False, index=True)
    journal_entry_id: Mapped[str] = mapped_column(String, default="")
    result: Mapped[str] = mapped_column(String, nullable=False)
    pnl: Mapped[float] = mapped_column(Float, nullable=False)
    thesis_accuracy: Mapped[str] = mapped_column(Text, default="")
    execution_quality: Mapped[str] = mapped_column(Text, default="")
    risk_management_quality: Mapped[str] = mapped_column(Text, default="")
    lessons: Mapped[str] = mapped_column(Text, default="")            # JSON list
    strategy_adjustments: Mapped[str] = mapped_column(Text, default="")  # JSON list
    reviewed_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    raw_json: Mapped[str] = mapped_column(Text, default="")
