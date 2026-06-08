"""
Tests for the paper trading engine.
No network calls. No LLM calls. Pure state logic.
"""

import pytest
from src.agents.schemas import (
    AssetType, Direction, ExecutionStatus, OrderSide, OrderTicket, OrderType,
    PaperTrade, TradeStatus,
)
from src.execution import PaperTrader
from src.utils.ids import new_id


def make_ticket(**kwargs) -> OrderTicket:
    defaults = dict(
        id=new_id(),
        proposal_id=new_id(),
        broker="paper",
        asset_or_market="SPY",
        asset_type=AssetType.EQUITY,
        side=OrderSide.BUY,
        order_type=OrderType.LIMIT,
        limit_price=100.0,
        quantity=2.0,
        estimated_max_loss=10.0,
        requires_user_confirmation=True,
        execution_status=ExecutionStatus.PENDING_APPROVAL,
    )
    defaults.update(kwargs)
    return OrderTicket(**defaults)


class TestPaperTraderOpen:

    def test_open_trade_creates_entry(self):
        trader = PaperTrader()
        ticket = make_ticket()
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.LONG)
        assert trade.entry_price == 100.0
        assert trade.status == TradeStatus.PAPER_OPEN
        assert trade.pnl is None
        assert trade.closed_at is None

    def test_open_trade_appears_in_open_list(self):
        trader = PaperTrader()
        ticket = make_ticket()
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.LONG)
        assert trade.id in [t.id for t in trader.get_open_trades()]

    def test_open_trade_records_quantity(self):
        trader = PaperTrader()
        ticket = make_ticket(quantity=5.0)
        trade = trader.open_trade(ticket, fill_price=50.0, direction=Direction.LONG)
        assert trade.quantity == 5.0

    def test_open_trade_records_strategy_name(self):
        trader = PaperTrader()
        ticket = make_ticket()
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.LONG, strategy_name="test_strat")
        assert trade.strategy_name == "test_strat"

    def test_cannot_open_from_live_status_ticket(self):
        ticket = make_ticket(execution_status=ExecutionStatus.LIVE)
        trader = PaperTrader()
        with pytest.raises(ValueError):
            trader.open_trade(ticket, fill_price=100.0, direction=Direction.LONG)


class TestPaperTraderClose:

    def test_close_long_win(self):
        trader = PaperTrader()
        ticket = make_ticket(quantity=2.0)
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.LONG)
        closed = trader.close_trade(trade.id, exit_price=110.0)
        # (110 - 100) * 2 = 20
        assert closed.pnl == pytest.approx(20.0)
        assert closed.status == TradeStatus.PAPER_CLOSED
        assert closed.exit_price == 110.0

    def test_close_long_loss(self):
        trader = PaperTrader()
        ticket = make_ticket(quantity=2.0)
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.LONG)
        closed = trader.close_trade(trade.id, exit_price=90.0)
        # (90 - 100) * 2 = -20
        assert closed.pnl == pytest.approx(-20.0)

    def test_close_short_win(self):
        trader = PaperTrader()
        ticket = make_ticket(side=OrderSide.SELL, quantity=3.0)
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.SHORT)
        closed = trader.close_trade(trade.id, exit_price=80.0)
        # (100 - 80) * 3 = 60
        assert closed.pnl == pytest.approx(60.0)

    def test_close_short_loss(self):
        trader = PaperTrader()
        ticket = make_ticket(side=OrderSide.SELL, quantity=1.0)
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.SHORT)
        closed = trader.close_trade(trade.id, exit_price=120.0)
        # (100 - 120) * 1 = -20
        assert closed.pnl == pytest.approx(-20.0)

    def test_close_removes_from_open_list(self):
        trader = PaperTrader()
        ticket = make_ticket()
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.LONG)
        trader.close_trade(trade.id, exit_price=105.0)
        assert trade.id not in [t.id for t in trader.get_open_trades()]

    def test_close_appears_in_closed_list(self):
        trader = PaperTrader()
        ticket = make_ticket()
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.LONG)
        closed = trader.close_trade(trade.id, exit_price=105.0)
        assert closed.id in [t.id for t in trader.get_closed_trades()]

    def test_close_nonexistent_trade_raises(self):
        trader = PaperTrader()
        with pytest.raises(KeyError):
            trader.close_trade("nonexistent-id", exit_price=100.0)

    def test_close_breakeven(self):
        trader = PaperTrader()
        ticket = make_ticket(quantity=1.0)
        trade = trader.open_trade(ticket, fill_price=100.0, direction=Direction.LONG)
        closed = trader.close_trade(trade.id, exit_price=100.0)
        assert closed.pnl == pytest.approx(0.0)


class TestPaperTraderMetrics:

    def test_daily_pnl_sums_closed_today(self):
        trader = PaperTrader()

        t1 = make_ticket(quantity=1.0)
        t2 = make_ticket(quantity=1.0)
        trade1 = trader.open_trade(t1, fill_price=100.0, direction=Direction.LONG)
        trade2 = trader.open_trade(t2, fill_price=100.0, direction=Direction.LONG)
        trader.close_trade(trade1.id, exit_price=110.0)   # +10
        trader.close_trade(trade2.id, exit_price=95.0)    # -5

        assert trader.daily_pnl() == pytest.approx(5.0)

    def test_open_positions_count(self):
        trader = PaperTrader()
        t1 = make_ticket()
        t2 = make_ticket()
        trader.open_trade(t1, fill_price=100.0, direction=Direction.LONG)
        trader.open_trade(t2, fill_price=200.0, direction=Direction.LONG)
        assert len(trader.get_open_trades()) == 2
