"""Tests for ModelScorer — ensures stub is honest and never returns fake scores."""
from __future__ import annotations

import pytest

from src.agents.model_scorer import ModelScorer, get_scorer
from src.agents.schemas import AssetType, Direction, ModelScore, TradeProposal


def _make_proposal() -> TradeProposal:
    return TradeProposal(
        research_id="test-research-id",
        asset_or_market="AAPL",
        asset_type=AssetType.EQUITY,
        trade_type="equity_long",
        direction=Direction.LONG,
        proposed_entry="170.00",
        target="185.00",
        stop_or_invalidation="165.00",
        thesis="Test thesis",
        time_horizon="3 days",
        confidence=0.6,
        bull_case="Breakout",
        bear_case="Fails support",
        why_now="Earnings upcoming",
        what_would_change_my_mind="Close below 165",
    )


class TestModelScorer:
    def test_is_available_returns_false(self):
        scorer = ModelScorer()
        assert not scorer.is_available()

    def test_score_returns_model_score(self):
        scorer = ModelScorer()
        result = scorer.score(_make_proposal())
        assert isinstance(result, ModelScore)

    def test_score_available_is_false(self):
        scorer = ModelScorer()
        result = scorer.score(_make_proposal())
        assert not result.available

    def test_probability_is_none(self):
        scorer = ModelScorer()
        result = scorer.score(_make_proposal())
        assert result.probability_of_positive_outcome is None

    def test_expected_value_is_none(self):
        scorer = ModelScorer()
        result = scorer.score(_make_proposal())
        assert result.expected_value is None

    def test_model_version_is_not_available(self):
        scorer = ModelScorer()
        result = scorer.score(_make_proposal())
        assert result.model_version == "not_available"

    def test_note_warns_against_treating_as_signal(self):
        scorer = ModelScorer()
        result = scorer.score(_make_proposal())
        assert "not" in result.note.lower() or "no" in result.note.lower()

    def test_get_scorer_returns_singleton(self):
        a = get_scorer()
        b = get_scorer()
        assert a is b

    def test_setup_quality_is_none(self):
        scorer = ModelScorer()
        result = scorer.score(_make_proposal())
        assert result.setup_quality is None

    def test_liquidity_risk_is_none(self):
        scorer = ModelScorer()
        result = scorer.score(_make_proposal())
        assert result.liquidity_risk is None
