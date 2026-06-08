"""
Aggregate performance metrics across all paper trades.
No LLM calls — pure math.
"""

from __future__ import annotations

from typing import Any


def compute_performance(trades: list[dict]) -> dict[str, Any]:
    """
    Input: list of closed trade dicts from market_store.load_closed_paper_trades()
    """
    if not trades:
        return {"total_trades": 0, "note": "No closed trades yet."}

    pnls = [t.get("pnl") or 0.0 for t in trades]
    wins = [p for p in pnls if p > 0]
    losses = [p for p in pnls if p < 0]

    win_rate = len(wins) / len(trades) if trades else 0
    avg_win = sum(wins) / len(wins) if wins else 0
    avg_loss = sum(losses) / len(losses) if losses else 0
    expectancy = (win_rate * avg_win) + ((1 - win_rate) * avg_loss) if trades else 0
    profit_factor = abs(sum(wins) / sum(losses)) if sum(losses) != 0 else float("inf")
    max_drawdown = min(pnls) if pnls else 0

    return {
        "total_trades": len(trades),
        "wins": len(wins),
        "losses": len(losses),
        "win_rate": round(win_rate, 4),
        "total_pnl": round(sum(pnls), 4),
        "avg_win": round(avg_win, 4),
        "avg_loss": round(avg_loss, 4),
        "expectancy_per_trade": round(expectancy, 4),
        "profit_factor": round(profit_factor, 4) if profit_factor != float("inf") else "∞",
        "max_single_loss": round(max_drawdown, 4),
        "edge_note": (
            "Positive expectancy suggests potential edge. "
            "Needs 50+ trades for statistical significance."
        ) if expectancy > 0 else (
            "Negative expectancy. Strategy is losing money on average. "
            "Do not scale. Review and revise."
        ),
    }
