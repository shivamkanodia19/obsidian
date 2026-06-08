"""
Trade journal — narrative summaries of completed trades.
In V0: basic summary from closed trade data. LLM review is optional.
"""

from __future__ import annotations

from ..agents.schemas import PaperTrade, TradeReview
from ..utils.ids import new_id
from ..utils.logging import get_logger

logger = get_logger(__name__)


def summarize_trade(trade: PaperTrade) -> dict:
    """Basic summary without LLM — always available."""
    if trade.pnl is None:
        return {"error": "Trade not closed yet"}

    duration_minutes = None
    if trade.closed_at and trade.opened_at:
        duration_minutes = (trade.closed_at - trade.opened_at).total_seconds() / 60

    return {
        "id": trade.id,
        "asset": trade.asset_or_market,
        "direction": trade.direction.value,
        "entry": trade.entry_price,
        "exit": trade.exit_price,
        "pnl": trade.pnl,
        "result": "win" if trade.pnl > 0 else ("loss" if trade.pnl < 0 else "breakeven"),
        "duration_minutes": duration_minutes,
        "thesis": trade.thesis,
        "strategy": trade.strategy_name,
    }


def llm_review_trade(trade: PaperTrade) -> TradeReview:
    """
    Run the review agent on a closed trade.
    Requires ANTHROPIC_API_KEY.
    """
    from ..agents.agent_runner import run_agent

    summary = summarize_trade(trade)
    result = run_agent("review_agent", f"Review this closed trade:\n{summary}", extra_context=summary)

    return TradeReview(
        id=new_id(),
        trade_id=trade.id,
        result=result.get("result", "unknown"),
        pnl=trade.pnl or 0.0,
        thesis_accuracy=result.get("thesis_accuracy", ""),
        execution_quality=result.get("execution_quality", ""),
        risk_management_quality=result.get("risk_management_quality", ""),
        lessons=result.get("lessons", []),
        strategy_adjustments=result.get("strategy_adjustments", []),
        raw_agent_output=result.get("_raw_agent_output", ""),
    )
