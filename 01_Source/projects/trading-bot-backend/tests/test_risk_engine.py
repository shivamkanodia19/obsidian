"""
Tests for the deterministic risk engine.
No LLM calls. No network calls. Pure logic.
"""

import pytest
from src.agents.schemas import AssetType, Direction, TradeProposal, TradeStatus
from src.risk import check_proposal, check_ticket
from src.risk.rules import RiskLimits
from src.agents.schemas import OrderTicket, OrderType, OrderSide, ExecutionStatus
from src.utils.ids import new_id


def make_proposal(**kwargs) -> TradeProposal:
    defaults = dict(
        id=new_id(),
        research_id=new_id(),
        asset_or_market="SPY",
        asset_type=AssetType.EQUITY,
        trade_type="equity long",
        direction=Direction.LONG,
        proposed_entry="450",
        target="460",
        stop_or_invalidation="440",
        time_horizon="1 week",
        confidence=0.6,
        thesis="Test thesis",
        bull_case="Goes up",
        bear_case="Goes down",
        why_now="Test",
        what_would_change_my_mind="Stop hit",
    )
    defaults.update(kwargs)
    return TradeProposal(**defaults)


def default_limits() -> RiskLimits:
    return RiskLimits(
        max_trade_risk_dollars=25.0,
        max_daily_loss_dollars=50.0,
        max_open_positions=5,
        max_allocation_per_trade_percent=10.0,
        max_thesis_age_minutes=60,
        allow_live_trading=False,
        require_manual_confirmation=True,
        allow_equities=True,
        allow_options=False,
        allow_crypto=False,
        allow_prediction_markets=True,
        reject_market_orders=True,
        max_spread_percent=3.0,
        reject_above=70,
        warn_above=40,
    )


class TestRiskEngineApproval:

    def test_clean_proposal_approved(self):
        proposal = make_proposal()
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,
            current_open_positions=0,
            research_age_minutes=5.0,
            limits=default_limits(),
        )
        assert result.approved is True
        assert result.rejection_reasons == []

    def test_approved_result_has_risk_score(self):
        proposal = make_proposal()
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,
            current_open_positions=0,
            research_age_minutes=5.0,
            limits=default_limits(),
        )
        assert 0 <= result.risk_score <= 100

    def test_approved_has_max_allowed_size(self):
        proposal = make_proposal()
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,
            current_open_positions=0,
            research_age_minutes=5.0,
            limits=default_limits(),
        )
        assert result.max_allowed_size > 0


class TestRiskEngineRejections:

    def test_rejects_crypto_when_disabled(self):
        proposal = make_proposal(asset_type=AssetType.CRYPTO)
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,
            current_open_positions=0,
            research_age_minutes=5.0,
            limits=default_limits(),
        )
        assert result.approved is False
        assert any("crypto" in r.lower() or "asset type" in r.lower() for r in result.rejection_reasons)

    def test_rejects_options_when_disabled(self):
        proposal = make_proposal(asset_type=AssetType.OPTIONS)
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,
            current_open_positions=0,
            research_age_minutes=5.0,
            limits=default_limits(),
        )
        assert result.approved is False

    def test_rejects_trade_exceeding_max_risk(self):
        proposal = make_proposal()
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=100.0,   # way over $25 limit
            current_open_positions=0,
            research_age_minutes=5.0,
            limits=default_limits(),
        )
        assert result.approved is False
        assert any("risk" in r.lower() and "25" in r for r in result.rejection_reasons)

    def test_rejects_when_daily_loss_limit_would_be_breached(self):
        proposal = make_proposal()
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=20.0,
            current_open_positions=0,
            research_age_minutes=5.0,
            daily_loss_so_far=40.0,   # $40 + $20 = $60 > $50 limit
            limits=default_limits(),
        )
        assert result.approved is False
        assert any("daily" in r.lower() for r in result.rejection_reasons)

    def test_rejects_when_max_positions_reached(self):
        proposal = make_proposal()
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,
            current_open_positions=5,   # at limit
            research_age_minutes=5.0,
            limits=default_limits(),
        )
        assert result.approved is False
        assert any("position" in r.lower() for r in result.rejection_reasons)

    def test_rejects_stale_thesis(self):
        proposal = make_proposal()
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,
            current_open_positions=0,
            research_age_minutes=90.0,   # over 60 minute limit
            limits=default_limits(),
        )
        assert result.approved is False
        assert any("research" in r.lower() or "stale" in r.lower() or "old" in r.lower()
                   for r in result.rejection_reasons)

    def test_rejects_excessive_spread(self):
        proposal = make_proposal()
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,
            current_open_positions=0,
            research_age_minutes=5.0,
            spread_percent=5.0,   # over 3% limit
            limits=default_limits(),
        )
        assert result.approved is False

    def test_warns_on_high_confidence(self):
        proposal = make_proposal(confidence=0.95)
        result = check_proposal(
            proposal=proposal,
            estimated_risk_dollars=10.0,
            current_open_positions=0,
            research_age_minutes=5.0,
            limits=default_limits(),
        )
        # Should warn about overconfidence even if approved
        assert any("confidence" in w.lower() or "llm" in w.lower() for w in result.warnings)


class TestOrderTicketChecks:

    def _make_ticket(self, **kwargs) -> OrderTicket:
        defaults = dict(
            id=new_id(),
            proposal_id=new_id(),
            broker="paper",
            asset_or_market="SPY",
            asset_type=AssetType.EQUITY,
            side=OrderSide.BUY,
            order_type=OrderType.LIMIT,
            limit_price=100.0,
            quantity=1.0,
            estimated_max_loss=10.0,
            requires_user_confirmation=True,
            execution_status=ExecutionStatus.PENDING_APPROVAL,
        )
        defaults.update(kwargs)
        return OrderTicket(**defaults)

    def test_valid_paper_ticket_passes(self):
        ticket = self._make_ticket()
        errors = check_ticket(ticket, default_limits())
        assert errors == []

    def test_market_order_rejected(self):
        ticket = self._make_ticket(order_type=OrderType.MARKET)
        errors = check_ticket(ticket, default_limits())
        assert any("market order" in e.lower() for e in errors)

    def test_unknown_broker_rejected(self):
        ticket = self._make_ticket(broker="robinhood_live")
        errors = check_ticket(ticket, default_limits())
        assert any("broker" in e.lower() for e in errors)

    def test_ticket_exceeding_max_loss_rejected(self):
        ticket = self._make_ticket(estimated_max_loss=100.0)
        errors = check_ticket(ticket, default_limits())
        assert any("max" in e.lower() and "loss" in e.lower() or "risk" in e.lower() for e in errors)
