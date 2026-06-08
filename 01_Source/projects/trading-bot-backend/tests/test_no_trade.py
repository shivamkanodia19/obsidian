"""Tests for NoTradeDecision as a first-class return value."""
from __future__ import annotations

import pytest

from src.agents.schemas import (
    AssetType,
    NoTradeDecision,
    NoTradeReason,
    TradeProposal,
    Direction,
)


def _make_proposal(**kwargs) -> TradeProposal:
    defaults = dict(
        research_id="test-research-id",
        asset_or_market="AAPL",
        asset_type=AssetType.EQUITY,
        trade_type="equity_long",
        direction=Direction.LONG,
        proposed_entry="170.00",
        target="185.00",
        stop_or_invalidation="165.00",
        thesis="Breakout above resistance",
        time_horizon="3 days",
        confidence=0.6,
        bull_case="Bull",
        bear_case="Bear",
        why_now="Now",
        what_would_change_my_mind="Close below 165",
    )
    defaults.update(kwargs)
    return TradeProposal(**defaults)


def _make_no_trade(reason: NoTradeReason = NoTradeReason.SPREAD_TOO_WIDE, **kwargs) -> NoTradeDecision:
    defaults = dict(
        asset_or_market="AAPL",
        asset_type=AssetType.EQUITY,
        reason=reason,
        explanation="Not enough edge given spread.",
    )
    defaults.update(kwargs)
    return NoTradeDecision(**defaults)


class TestNoTradeSchemas:
    def test_no_trade_has_required_fields(self):
        nt = _make_no_trade()
        assert nt.reason == NoTradeReason.SPREAD_TOO_WIDE
        assert nt.asset_or_market == "AAPL"
        assert nt.explanation

    def test_all_no_trade_reasons_are_valid(self):
        for reason in NoTradeReason:
            nt = _make_no_trade(reason=reason)
            assert nt.reason == reason

    def test_no_trade_is_not_a_proposal(self):
        nt = _make_no_trade()
        proposal = _make_proposal()
        assert not isinstance(nt, TradeProposal)
        assert isinstance(nt, NoTradeDecision)

    def test_what_would_change_this_is_optional(self):
        nt = NoTradeDecision(
            asset_or_market="TSLA",
            asset_type=AssetType.EQUITY,
            reason=NoTradeReason.RISK_ENGINE_REJECTED,
            explanation="Risk score too high",
        )
        assert not nt.what_would_change_this  # None or empty string both acceptable

    def test_no_trade_with_what_would_change_this(self):
        nt = NoTradeDecision(
            asset_or_market="TSLA",
            asset_type=AssetType.EQUITY,
            reason=NoTradeReason.SPREAD_TOO_WIDE,
            explanation="Edge smaller than spread",
            what_would_change_this="If spread narrows below 0.5%",
        )
        assert "spread" in nt.what_would_change_this

    def test_duplicate_position_reason(self):
        nt = _make_no_trade(reason=NoTradeReason.DUPLICATE_OPEN_POSITION)
        assert nt.reason == NoTradeReason.DUPLICATE_OPEN_POSITION

    def test_skeptic_rejection_reason(self):
        nt = _make_no_trade(reason=NoTradeReason.SKEPTIC_REJECTION)
        assert nt.reason == NoTradeReason.SKEPTIC_REJECTION

    def test_no_trade_serializes_to_dict(self):
        nt = _make_no_trade()
        d = nt.model_dump()
        assert d["reason"] == NoTradeReason.SPREAD_TOO_WIDE.value
        assert "explanation" in d

    def test_no_trade_round_trips_json(self):
        nt = _make_no_trade()
        json_str = nt.model_dump_json()
        restored = NoTradeDecision.model_validate_json(json_str)
        assert restored.reason == nt.reason
        assert restored.asset_or_market == nt.asset_or_market
