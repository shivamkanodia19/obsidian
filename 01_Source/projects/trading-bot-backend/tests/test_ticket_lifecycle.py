"""Tests for OrderTicket lifecycle state machine."""
from __future__ import annotations

from datetime import datetime, timezone, timedelta

import pytest

from src.agents.schemas import (
    AssetType,
    Direction,
    OrderSide,
    OrderTicket,
    OrderType,
    TicketStatus,
    TradeProposal,
)


def _make_ticket(**kwargs) -> OrderTicket:
    defaults = dict(
        proposal_id="prop-test-id",
        asset_or_market="AAPL",
        asset_type=AssetType.EQUITY,
        broker="paper",
        side=OrderSide.BUY,
        order_type=OrderType.LIMIT,
        limit_price=170.0,
        quantity=1.0,
        estimated_max_loss=5.0,
        requires_user_confirmation=True,
        risk_engine_result_id="risk-test-id",
        notes="test ticket",
    )
    defaults.update(kwargs)
    return OrderTicket(**defaults)


class TestTicketTransitions:
    def test_valid_draft_to_risk_pending(self):
        t = _make_ticket()
        assert t.ticket_status == TicketStatus.DRAFT
        t.transition(TicketStatus.RISK_PENDING, "starting risk check")
        assert t.ticket_status == TicketStatus.RISK_PENDING

    def test_valid_risk_pending_to_approved(self):
        t = _make_ticket()
        t.transition(TicketStatus.RISK_PENDING)
        t.transition(TicketStatus.RISK_APPROVED, "risk passed")
        assert t.ticket_status == TicketStatus.RISK_APPROVED

    def test_valid_approved_to_awaiting_confirmation(self):
        t = _make_ticket()
        t.transition(TicketStatus.RISK_PENDING)
        t.transition(TicketStatus.RISK_APPROVED)
        t.transition(TicketStatus.AWAITING_USER_CONFIRMATION, "ready")
        assert t.ticket_status == TicketStatus.AWAITING_USER_CONFIRMATION

    def test_invalid_transition_raises(self):
        t = _make_ticket()
        with pytest.raises(ValueError, match="Invalid ticket transition"):
            t.transition(TicketStatus.PAPER_EXECUTED, "skipping steps")

    def test_draft_cannot_go_to_live_executed(self):
        t = _make_ticket()
        with pytest.raises(ValueError):
            t.transition(TicketStatus.LIVE_EXECUTED)

    def test_cancelled_ticket_cannot_transition(self):
        t = _make_ticket()
        t.transition(TicketStatus.CANCELLED, "user cancelled")
        with pytest.raises(ValueError):
            t.transition(TicketStatus.RISK_PENDING)

    def test_audit_trail_is_populated(self):
        t = _make_ticket()
        t.transition(TicketStatus.RISK_PENDING, "starting")
        t.transition(TicketStatus.RISK_APPROVED, "passed")
        assert len(t.audit_trail) == 2
        assert t.audit_trail[0].from_status == TicketStatus.DRAFT
        assert t.audit_trail[0].to_status == TicketStatus.RISK_PENDING
        assert t.audit_trail[1].from_status == TicketStatus.RISK_PENDING

    def test_audit_trail_captures_reason(self):
        t = _make_ticket()
        t.transition(TicketStatus.CANCELLED, "user changed mind")
        assert "changed mind" in t.audit_trail[0].reason

    def test_risk_pending_to_rejected(self):
        t = _make_ticket()
        t.transition(TicketStatus.RISK_PENDING)
        t.transition(TicketStatus.RISK_REJECTED, "exceeded daily loss limit")
        assert t.ticket_status == TicketStatus.RISK_REJECTED

    def test_rejected_cannot_be_approved(self):
        t = _make_ticket()
        t.transition(TicketStatus.RISK_PENDING)
        t.transition(TicketStatus.RISK_REJECTED)
        with pytest.raises(ValueError):
            t.transition(TicketStatus.RISK_APPROVED)


class TestTicketExpiry:
    def test_not_expired_when_no_expiry_set(self):
        t = _make_ticket()
        assert not t.is_expired()

    def test_not_expired_when_future_expiry(self):
        t = _make_ticket()
        t.expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
        assert not t.is_expired()

    def test_expired_when_past_expiry(self):
        t = _make_ticket()
        t.expires_at = datetime.now(timezone.utc) - timedelta(seconds=1)
        assert t.is_expired()

    def test_is_executable_requires_correct_status_and_not_expired(self):
        t = _make_ticket()
        t.transition(TicketStatus.RISK_PENDING)
        t.transition(TicketStatus.RISK_APPROVED)
        t.transition(TicketStatus.AWAITING_USER_CONFIRMATION)
        t.expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
        assert t.is_executable()

    def test_is_not_executable_if_expired(self):
        t = _make_ticket()
        t.transition(TicketStatus.RISK_PENDING)
        t.transition(TicketStatus.RISK_APPROVED)
        t.transition(TicketStatus.AWAITING_USER_CONFIRMATION)
        t.expires_at = datetime.now(timezone.utc) - timedelta(seconds=1)
        assert not t.is_executable()

    def test_is_not_executable_in_draft_status(self):
        t = _make_ticket()
        assert not t.is_executable()
