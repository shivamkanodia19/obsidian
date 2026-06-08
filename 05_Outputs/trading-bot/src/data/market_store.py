"""
Persistence helpers for all domain objects.
Thin wrappers around SQLAlchemy sessions — no business logic here.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

from ..agents.schemas import (
    NoTradeDecision,
    OrderTicket,
    PaperTrade,
    RiskEngineResult,
    ResearchSummary,
    SkepticOutput,
    TradeJournalEntry,
    TradeProposal,
    TradeReview,
    TicketAuditEntry,
)
from .db import get_session
from .models import (
    NoTradeRecord,
    OrderTicketRecord,
    PaperTradeRecord,
    ProposalRecord,
    ResearchRecord,
    RiskResultRecord,
    TicketAuditRecord,
    TradeJournalRecord,
    TradeReviewRecord,
)
from ..utils.ids import new_id


def save_research(research: ResearchSummary) -> None:
    with get_session() as session:
        record = ResearchRecord(
            id=research.id,
            asset_or_market=research.asset_or_market,
            asset_type=research.asset_type.value,
            research_summary=research.research_summary,
            raw_json=research.model_dump_json(),
            created_at=research.created_at,
        )
        session.merge(record)
        session.commit()


def save_proposal(proposal: TradeProposal) -> None:
    with get_session() as session:
        record = ProposalRecord(
            id=proposal.id,
            research_id=proposal.research_id,
            asset_or_market=proposal.asset_or_market,
            direction=proposal.direction.value,
            confidence=proposal.confidence,
            thesis=proposal.thesis,
            status=proposal.status.value,
            raw_json=proposal.model_dump_json(),
            created_at=proposal.created_at,
        )
        session.merge(record)
        session.commit()


def save_no_trade(decision: NoTradeDecision) -> None:
    with get_session() as session:
        record = NoTradeRecord(
            id=decision.id,
            asset_or_market=decision.asset_or_market,
            reason=decision.reason.value,
            explanation=decision.explanation,
            research_id=decision.research_id,
            proposal_id=decision.proposal_id,
            raw_json=decision.model_dump_json(),
            created_at=decision.created_at,
        )
        session.merge(record)
        session.commit()


def save_risk_result(result: RiskEngineResult) -> str:
    rid = new_id()
    with get_session() as session:
        record = RiskResultRecord(
            id=rid,
            proposal_id=result.proposal_id,
            approved=result.approved,
            risk_score=result.risk_score,
            final_decision=result.final_decision,
            rejection_reasons=json.dumps(result.rejection_reasons),
            warnings=json.dumps(result.warnings),
            checked_at=result.checked_at,
        )
        session.add(record)
        session.commit()
    return rid


def save_order_ticket(ticket: OrderTicket) -> None:
    with get_session() as session:
        record = OrderTicketRecord(
            id=ticket.id,
            proposal_id=ticket.proposal_id,
            broker=ticket.broker,
            asset_or_market=ticket.asset_or_market,
            side=ticket.side.value,
            order_type=ticket.order_type.value,
            limit_price=ticket.limit_price,
            quantity=ticket.quantity,
            estimated_max_loss=ticket.estimated_max_loss,
            ticket_status=ticket.ticket_status.value,
            execution_status=ticket.execution_status.value,
            expires_at=ticket.expires_at,
            raw_json=ticket.model_dump_json(),
            created_at=ticket.created_at,
        )
        session.merge(record)
        session.commit()

    # Persist audit trail entries
    if ticket.audit_trail:
        _save_ticket_audit(ticket.id, ticket.audit_trail[-1])


def _save_ticket_audit(ticket_id: str, entry: TicketAuditEntry) -> None:
    with get_session() as session:
        record = TicketAuditRecord(
            ticket_id=ticket_id,
            from_status=entry.from_status.value,
            to_status=entry.to_status.value,
            reason=entry.reason,
            timestamp=entry.timestamp,
        )
        session.add(record)
        session.commit()


def save_paper_trade(trade: PaperTrade) -> None:
    with get_session() as session:
        record = PaperTradeRecord(
            id=trade.id,
            ticket_id=trade.ticket_id,
            proposal_id=trade.proposal_id,
            asset_or_market=trade.asset_or_market,
            asset_type=trade.asset_type.value,
            direction=trade.direction.value,
            entry_price=trade.entry_price,
            exit_price=trade.exit_price,
            quantity=trade.quantity,
            strategy_name=trade.strategy_name,
            thesis=trade.thesis,
            notes=trade.notes,
            opened_at=trade.opened_at,
            closed_at=trade.closed_at,
            pnl=trade.pnl,
            status=trade.status.value,
        )
        session.merge(record)
        session.commit()


def save_journal_entry(entry: TradeJournalEntry) -> None:
    with get_session() as session:
        record = TradeJournalRecord(
            id=entry.id,
            original_user_question=entry.original_user_question,
            router_intent=entry.router_intent.value if entry.router_intent else None,
            research_id=entry.research_id,
            proposal_id=entry.proposal_id,
            ticket_id=entry.ticket_id,
            trade_id=entry.trade_id,
            review_id=entry.review_id,
            agents_used=json.dumps(entry.agents_used),
            thesis=entry.thesis,
            skeptic_summary=entry.skeptic_summary,
            risk_score=entry.risk_score,
            risk_approved=entry.risk_approved,
            entry_price=entry.entry_price,
            exit_price=entry.exit_price,
            pnl=entry.pnl,
            outcome=entry.outcome,
            notes=entry.notes,
            raw_json=entry.model_dump_json(),
            created_at=entry.created_at,
            updated_at=entry.updated_at,
        )
        session.merge(record)
        session.commit()


def save_trade_review(review: TradeReview) -> None:
    with get_session() as session:
        record = TradeReviewRecord(
            id=review.id,
            trade_id=review.trade_id,
            journal_entry_id=review.journal_entry_id,
            result=review.result,
            pnl=review.pnl,
            thesis_accuracy=review.thesis_accuracy,
            execution_quality=review.execution_quality,
            risk_management_quality=review.risk_management_quality,
            lessons=json.dumps(review.lessons),
            strategy_adjustments=json.dumps(review.strategy_adjustments),
            reviewed_at=review.reviewed_at,
            raw_json=review.model_dump_json(),
        )
        session.merge(record)
        session.commit()


def load_open_paper_trades() -> list[dict]:
    with get_session() as session:
        records = session.query(PaperTradeRecord).filter(
            PaperTradeRecord.status == "paper_open"
        ).all()
        return [
            {
                "id": r.id,
                "asset_or_market": r.asset_or_market,
                "direction": r.direction,
                "entry_price": r.entry_price,
                "quantity": r.quantity,
                "opened_at": r.opened_at,
                "thesis": r.thesis,
                "strategy_name": r.strategy_name,
            }
            for r in records
        ]


def load_closed_paper_trades() -> list[dict]:
    with get_session() as session:
        records = session.query(PaperTradeRecord).filter(
            PaperTradeRecord.status == "paper_closed"
        ).all()
        return [
            {
                "id": r.id,
                "asset_or_market": r.asset_or_market,
                "direction": r.direction,
                "entry_price": r.entry_price,
                "exit_price": r.exit_price,
                "pnl": r.pnl,
                "opened_at": r.opened_at,
                "closed_at": r.closed_at,
            }
            for r in records
        ]


def load_journal_entries(limit: int = 50) -> list[dict]:
    with get_session() as session:
        records = (
            session.query(TradeJournalRecord)
            .order_by(TradeJournalRecord.created_at.desc())
            .limit(limit)
            .all()
        )
        return [
            {
                "id": r.id,
                "question": r.original_user_question,
                "intent": r.router_intent,
                "outcome": r.outcome,
                "pnl": r.pnl,
                "risk_score": r.risk_score,
                "risk_approved": r.risk_approved,
                "thesis": r.thesis[:120] if r.thesis else "",
                "created_at": r.created_at,
            }
            for r in records
        ]


def load_all_tickets() -> list[dict]:
    with get_session() as session:
        records = (
            session.query(OrderTicketRecord)
            .order_by(OrderTicketRecord.created_at.desc())
            .limit(100)
            .all()
        )
        return [
            {
                "id": r.id,
                "asset_or_market": r.asset_or_market,
                "side": r.side,
                "limit_price": r.limit_price,
                "quantity": r.quantity,
                "broker": r.broker,
                "ticket_status": r.ticket_status,
                "estimated_max_loss": r.estimated_max_loss,
                "created_at": r.created_at,
                "expires_at": r.expires_at,
            }
            for r in records
        ]


def has_open_position_for(asset_or_market: str) -> bool:
    """Check if an open paper trade already exists for this asset."""
    with get_session() as session:
        count = (
            session.query(PaperTradeRecord)
            .filter(
                PaperTradeRecord.asset_or_market == asset_or_market,
                PaperTradeRecord.status == "paper_open",
            )
            .count()
        )
        return count > 0


def load_ticket_by_id(ticket_id: str) -> dict | None:
    with get_session() as session:
        record = session.query(OrderTicketRecord).filter_by(id=ticket_id).first()
        if not record:
            return None
        return {"raw_json": record.raw_json, "ticket_status": record.ticket_status}
