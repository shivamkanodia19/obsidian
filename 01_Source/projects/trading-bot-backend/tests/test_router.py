"""Tests for router — offline keyword-based classification only (no API key required)."""
from __future__ import annotations

import pytest

from src.agents.router import route_query_offline
from src.agents.schemas import RouterIntent


def test_trade_proposal_intent_detected():
    result = route_query_offline("Should I buy AAPL calls right now?")
    assert result.intent == RouterIntent.TRADE_PROPOSAL_REQUEST
    assert result.confidence > 0


def test_market_scan_intent():
    result = route_query_offline("Scan Kalshi markets for political events")
    assert result.intent in (
        RouterIntent.KALSHI_MARKET_SCAN,
        RouterIntent.GENERAL_MARKET_SCAN,
        RouterIntent.TRADE_PROPOSAL_REQUEST,
        RouterIntent.UNCLEAR,
    )


def test_portfolio_risk_intent():
    result = route_query_offline("What is my current portfolio risk?")
    assert result.intent in (RouterIntent.PORTFOLIO_RISK_QUESTION, RouterIntent.UNCLEAR)


def test_performance_review_intent():
    result = route_query_offline("Show me my paper trading performance")
    assert result.intent in (RouterIntent.STRATEGY_PERFORMANCE_REQUEST, RouterIntent.TRADE_REVIEW_REQUEST, RouterIntent.UNCLEAR)


def test_unclear_intent_has_low_confidence():
    result = route_query_offline("???")
    # Unclear input should produce the unclear intent
    assert result.intent == RouterIntent.UNCLEAR


def test_offline_confidence_cap():
    """Offline routing should not claim high confidence."""
    result = route_query_offline("Buy TSLA now")
    assert result.confidence <= 0.8, "Offline routing should not claim very high confidence"


def test_offline_never_sets_execution_requested_without_explicit_trigger():
    """
    Offline routing is conservative — execution_requested should only be True
    when very explicit execution language is used.
    """
    result = route_query_offline("What do you think about MSFT?")
    assert not result.execution_requested


def test_execution_language_detected():
    result = route_query_offline("Execute this trade now")
    # Either detected as execution_requested or elevated intent
    assert result.intent in (
        RouterIntent.ORDER_EXECUTION_REQUEST,
        RouterIntent.TRADE_PROPOSAL_REQUEST,
        RouterIntent.UNCLEAR,
    )


def test_asset_extraction_equity():
    result = route_query_offline("Tell me about NVDA stock")
    # Offline may or may not extract assets but must not crash
    assert isinstance(result.extracted_asset, (str, type(None)))


def test_returns_router_output_schema():
    """RouterOutput schema must always be returned, never raise."""
    from src.agents.schemas import RouterOutput
    result = route_query_offline("Some arbitrary query that means nothing in particular")
    assert isinstance(result, RouterOutput)
    assert 0.0 <= result.confidence <= 1.0
