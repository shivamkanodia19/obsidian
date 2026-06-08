"""
Paper trading engine.

Opens and closes paper trades from approved order tickets.
All state is persisted to SQLite via the data layer.
No real money. No real broker calls. Every trade is logged.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..agents.schemas import (
    Direction,
    ExecutionStatus,
    OrderTicket,
    PaperTrade,
    TradeStatus,
)
from ..utils.logging import get_logger
from ..utils.ids import new_id

logger = get_logger(__name__)


class PaperTrader:
    """
    Manages paper trades in memory (and persisted to db via trade_store).
    In V0 this holds state in a dict; the DB layer is called separately by the CLI.
    """

    def __init__(self) -> None:
        self._open_trades: dict[str, PaperTrade] = {}
        self._closed_trades: dict[str, PaperTrade] = {}

    def open_trade(
        self,
        ticket: OrderTicket,
        fill_price: float,
        direction: Direction,
        strategy_name: str = "",
        thesis: str = "",
        notes: str = "",
    ) -> PaperTrade:
        """
        Open a paper trade from an approved order ticket.
        fill_price is the simulated fill — for V0, use the limit_price or a provided price.
        """
        # Hard check: ticket must be in pending_approval or paper status
        if ticket.execution_status not in (
            ExecutionStatus.PENDING_APPROVAL,
            ExecutionStatus.PAPER,
        ):
            raise ValueError(
                f"Cannot open paper trade from ticket {ticket.id} with "
                f"status '{ticket.execution_status}'. Must be pending_approval."
            )

        trade = PaperTrade(
            id=new_id(),
            ticket_id=ticket.id,
            asset_or_market=ticket.asset_or_market,
            asset_type=ticket.asset_type,
            direction=direction,
            entry_price=fill_price,
            quantity=ticket.quantity,
            strategy_name=strategy_name,
            thesis=thesis,
            notes=notes,
            opened_at=datetime.now(timezone.utc),
            status=TradeStatus.PAPER_OPEN,
        )

        self._open_trades[trade.id] = trade
        logger.info(
            f"Paper trade opened: {trade.id} | {trade.asset_or_market} | "
            f"{direction.value} | entry={fill_price} | qty={ticket.quantity}"
        )
        return trade

    def close_trade(
        self,
        trade_id: str,
        exit_price: float,
        notes: str = "",
    ) -> PaperTrade:
        """Close an open paper trade and compute P&L."""
        if trade_id not in self._open_trades:
            raise KeyError(f"No open paper trade with id '{trade_id}'")

        trade = self._open_trades.pop(trade_id)

        if trade.direction == Direction.LONG:
            pnl = (exit_price - trade.entry_price) * trade.quantity
        elif trade.direction == Direction.SHORT:
            pnl = (trade.entry_price - exit_price) * trade.quantity
        else:
            pnl = 0.0

        trade.exit_price = exit_price
        trade.closed_at = datetime.now(timezone.utc)
        trade.pnl = round(pnl, 4)
        trade.status = TradeStatus.PAPER_CLOSED
        if notes:
            trade.notes = (trade.notes + "\n" + notes).strip()

        self._closed_trades[trade.id] = trade
        logger.info(
            f"Paper trade closed: {trade.id} | {trade.asset_or_market} | "
            f"exit={exit_price} | pnl={trade.pnl:.4f}"
        )
        return trade

    def get_open_trades(self) -> list[PaperTrade]:
        return list(self._open_trades.values())

    def get_closed_trades(self) -> list[PaperTrade]:
        return list(self._closed_trades.values())

    def get_trade(self, trade_id: str) -> PaperTrade | None:
        return self._open_trades.get(trade_id) or self._closed_trades.get(trade_id)

    def total_open_risk(self) -> float:
        """Sum of estimated max losses on open positions — approximate."""
        return sum(
            abs(t.entry_price * t.quantity) for t in self._open_trades.values()
        )

    def daily_pnl(self) -> float:
        """Sum of P&L on trades closed today (UTC)."""
        today = datetime.now(timezone.utc).date()
        return sum(
            t.pnl
            for t in self._closed_trades.values()
            if t.closed_at and t.closed_at.date() == today and t.pnl is not None
        )
