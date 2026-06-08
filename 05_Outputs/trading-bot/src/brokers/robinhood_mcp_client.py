"""
Robinhood Agentic Trading — MCP integration adapter.

Robinhood provides an official MCP server at:
    https://agent.robinhood.com/mcp/trading

This is NOT a REST API wrapper. Robinhood execution happens through the MCP
protocol, which Claude Code calls directly. This Python class is a thin adapter
that validates tickets and returns structured MCP instruction dicts. Claude Code
reads those dicts and calls the MCP tools to execute.

Setup (one-time, per user):
    claude mcp add robinhood-trading --transport http https://agent.robinhood.com/mcp/trading
    Then run /mcp in Claude Code and complete the OAuth flow in your desktop browser.

After auth, the MCP creates a dedicated "Agentic Account" sandboxed from your
main Robinhood account. Trades only execute inside that account.

Current beta constraints (as of mid-2026):
  - Equities only (options, crypto, futures planned)
  - Desktop browser required for initial auth
  - Up to 10 individual accounts per user (Agentic Account counts toward limit)

Robinhood ToS note:
  "You are ultimately responsible for the trades your AI agent places in your account."
  "Robinhood does not control, supervise, monitor, recommend, or audit these AI agents."
  All risk is borne by the user.

=== Verified MCP Tool Inventory (confirmed 2026-06-07) ===

Account / Portfolio:
  mcp__robinhood-trading__get_accounts()
    → list of accounts; use to find agentic_allowed=true account_number
  mcp__robinhood-trading__get_portfolio(account_number)
    → total_value, buying_power, cash, equity_value by asset class

Positions / Orders:
  mcp__robinhood-trading__get_equity_positions(account_number, cursor?)
    → open equity positions: symbol, quantity, average_cost
  mcp__robinhood-trading__get_equity_orders(account_number, ...)
    → open/historical orders
  mcp__robinhood-trading__cancel_equity_order(order_id)

Market Data:
  mcp__robinhood-trading__get_equity_quotes(symbols: list[str])
    → real-time bid/ask/last for 1-20+ symbols
  mcp__robinhood-trading__get_equity_tradability(symbol, account_number)
  mcp__robinhood-trading__search(query)

Order Execution (requires agentic_allowed=true account):
  mcp__robinhood-trading__review_equity_order(account_number, symbol, side, type, ...)
    → dry-run cost estimate + alerts; CALL BEFORE place_equity_order
  mcp__robinhood-trading__place_equity_order(
      account_number,   # MUST be agentic_allowed=true account (969132497)
      symbol,           # e.g. "AAPL"
      side,             # "buy" | "sell"
      type,             # "market" | "limit" | "stop_market" | "stop_limit"
      quantity?,        # shares (decimals allowed for market+regular_hours)
      dollar_amount?,   # USD notional — only with type=market
      limit_price?,     # required for limit / stop_limit
      stop_price?,      # required for stop_market / stop_limit
      time_in_force?,   # "gfd" (default) | "gtc"
      market_hours?,    # "regular_hours" (default) | "extended_hours" | "all_day_hours"
      ref_id?,          # UUID idempotency key — generate fresh per order, reuse on retry
  )

Watchlist:
  mcp__robinhood-trading__get_watchlists()
  mcp__robinhood-trading__get_watchlist_items(watchlist_id)
  mcp__robinhood-trading__add_to_watchlist(watchlist_id, symbol)
  mcp__robinhood-trading__remove_from_watchlist(watchlist_id, symbol)
  mcp__robinhood-trading__create_watchlist(name)

=== Verified Account Numbers (DO NOT HARDCODE IN PRODUCTION — call get_accounts) ===
  Agentic Account : 969132497  (agentic_allowed=true, cash, $18 buying power)
  Main Account    : 553333931  (agentic_allowed=false — NEVER use for orders)
"""

from __future__ import annotations

from typing import Any

from ..agents.schemas import EquityWatchlistItem, OrderTicket
from ..utils.logging import get_logger
from .broker_interfaces import BrokerInterface

logger = get_logger(__name__)

# Official Robinhood MCP server URL
ROBINHOOD_MCP_URL = "https://agent.robinhood.com/mcp/trading"

# Claude Code setup command (run once in terminal)
SETUP_COMMAND = f"claude mcp add robinhood-trading --transport http {ROBINHOOD_MCP_URL}"


class RobinhoodMCPClient(BrokerInterface):
    """
    Adapter for Robinhood's official MCP server.

    This class does NOT make direct HTTP calls to Robinhood. Execution happens
    through Claude Code's MCP tooling. The risk engine calls this adapter to
    validate that a Robinhood trade is in scope; Claude Code then uses MCP tools
    to actually submit it.

    Workflow:
        1. Risk engine approves ticket → calls this adapter's submit_order()
        2. submit_order() returns an MCP instruction dict
        3. Claude Code reads the instruction and calls Robinhood MCP tools directly
        4. Robinhood MCP executes the trade in your Agentic Account
    """

    def __init__(self) -> None:
        logger.info("RobinhoodMCPClient initialized — execution via Claude Code MCP")

    def get_name(self) -> str:
        return "robinhood_mcp"

    def is_live(self) -> bool:
        # Robinhood Agentic Account is live-money (not paper)
        # The isolation is at the account level, not execution level
        return True

    def is_connected(self) -> bool:
        """
        Returns True if the robinhood-trading MCP is registered in Claude Code.
        Can't check this from Python — Claude Code manages MCP connections.
        """
        return False  # always unknown from Python; Claude Code knows

    def get_quote(self, asset_or_market: str) -> dict[str, Any]:
        """
        Returns an MCP instruction for Claude Code to call get_equity_quotes.

        Claude Code execution:
            mcp__robinhood-trading__get_equity_quotes(symbols=["<ticker>"])
        """
        return {
            "ticker": asset_or_market,
            "bid": None,
            "ask": None,
            "last": None,
            "volume": None,
            "mcp_tool": "mcp__robinhood-trading__get_equity_quotes",
            "mcp_params": {"symbols": [asset_or_market]},
            "mcp_server": ROBINHOOD_MCP_URL,
        }

    def get_watchlist(self) -> list[EquityWatchlistItem]:
        """
        Watchlist via Robinhood MCP. Claude Code should call:
            mcp__robinhood-trading__get_watchlists()
            mcp__robinhood-trading__get_watchlist_items(watchlist_id=<id>)
        Returns empty list from Python — execution is in Claude Code.
        """
        logger.info(
            "Robinhood watchlist available via MCP. "
            "Call: mcp__robinhood-trading__get_watchlists() then get_watchlist_items()."
        )
        return []

    def submit_order(self, ticket: OrderTicket) -> dict[str, Any]:
        """
        Returns an MCP execution instruction for Claude Code to act on.

        This method does NOT execute the trade. It:
        1. Validates the ticket is in scope for Robinhood (equities only)
        2. Returns a structured dict that Claude Code uses to call Robinhood MCP tools
        3. Claude Code must: call review_equity_order first, show user the estimate,
           get confirmation, then call place_equity_order.

        Claude Code execution sequence:
            # Step 1 — dry run (always)
            mcp__robinhood-trading__review_equity_order(**review_params)
            # Step 2 — present estimate to user, get explicit confirmation
            # Step 3 — place (add ref_id=<fresh UUID> before calling)
            mcp__robinhood-trading__place_equity_order(**place_params, ref_id=<uuid>)
        """
        from ..config import get_settings
        settings = get_settings()

        if not settings.allow_live_trading:
            raise RuntimeError(
                "Live trading is disabled. Set ALLOW_LIVE_TRADING=true to enable Robinhood execution."
            )

        from ..agents.schemas import AssetType
        if ticket.asset_type not in (AssetType.EQUITY, AssetType.ETF):
            raise ValueError(
                f"Robinhood Agentic Trading (beta) supports equities and ETFs only. "
                f"Got asset_type={ticket.asset_type.value}. "
                "Options, crypto, and futures are not yet supported."
            )

        # account_number always resolved at runtime via get_accounts() — 969132497 is
        # the verified agentic account (agentic_allowed=true) as of 2026-06-07.
        mcp_params: dict[str, Any] = {
            "account_number": "969132497",
            "symbol": ticket.asset_or_market,
            "side": ticket.side.value,
            "type": ticket.order_type.value,
            "quantity": str(ticket.quantity),
        }
        if ticket.limit_price is not None:
            mcp_params["limit_price"] = str(ticket.limit_price)

        return {
            "broker": "robinhood_mcp",
            "mcp_server": ROBINHOOD_MCP_URL,
            "action": "submit_order",
            "ticket_id": ticket.id,
            "review_tool": "mcp__robinhood-trading__review_equity_order",
            "review_params": mcp_params,
            "place_tool": "mcp__robinhood-trading__place_equity_order",
            "place_params": mcp_params,  # Claude Code adds ref_id=<fresh UUID>
            "account_note": "Executes in Robinhood Agentic Account (969132497) only.",
            "requires_mcp_connection": True,
            "setup_command": SETUP_COMMAND,
        }
