"""
CLI entry point — `trading` command.

Architecture: Claude Code is the intelligence layer. Python handles risk, state,
and execution. Run from the vault with Claude Code for the full workflow.

Robinhood: uses official MCP server (https://agent.robinhood.com/mcp/trading).
  Setup: claude mcp add robinhood-trading --transport http https://agent.robinhood.com/mcp/trading

Core commands:
  trading ask "<question>"        — natural language → full workflow (Claude Code drives)
  trading route "<question>"      — classify only, no workflow
  trading risk-check <id>         — run deterministic risk engine on a proposal
  trading tickets                 — list all order tickets
  trading execute <ticket_id>     — final risk re-check + execute (paper or Robinhood MCP)
  trading paper-open <id>         — open paper trade from a ticket
  trading paper-close <id>        — close a paper trade
  trading review                  — performance summary of closed trades
  trading journal                 — view trade journal entries
  trading show-open               — view open paper trades
  trading kalshi-balance          — Kalshi account balance (requires auth)
  trading kalshi-positions        — Kalshi open positions (requires auth)
  trading show-risk-settings      — display current risk config
  trading init                    — initialize database and validate config
  trading doctor                  — system health check + Robinhood MCP setup instructions
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()
BASE = Path(__file__).parent.parent


# ---------------------------------------------------------------------------
# CLI group
# ---------------------------------------------------------------------------

@click.group()
def cli():
    """trading-bot-backend — vault-native trading assistant. V0: paper trading only."""
    pass


# ---------------------------------------------------------------------------
# init
# ---------------------------------------------------------------------------

@cli.command()
def init():
    """Initialize database and validate config."""
    from ..data.db import init_db
    from ..config import get_settings

    settings = get_settings()
    init_db()
    console.print("[green]Database initialized.[/green]")

    risk_yaml = BASE / "config" / "risk_limits.yaml"
    if risk_yaml.exists():
        console.print(f"[green]Risk config:[/green] {risk_yaml}")
    else:
        console.print(f"[red]WARNING: risk_limits.yaml not found[/red]")

    if not settings.anthropic_api_key:
        console.print(
            "[yellow]ANTHROPIC_API_KEY not set — LLM agents disabled. "
            "Offline routing will be used.[/yellow]"
        )
    console.print(
        f"[blue]Live trading:[/blue] "
        f"{'ENABLED — check this!' if settings.allow_live_trading else 'DISABLED (safe)'}"
    )
    console.print("[green]Init complete.[/green]")


# ---------------------------------------------------------------------------
# doctor
# ---------------------------------------------------------------------------

@cli.command()
def doctor():
    """Check config, credentials, API stubs, risk settings, and system health."""
    from ..config import get_settings
    from ..data.db import init_db
    from ..risk.rules import RiskLimits

    settings = get_settings()

    issues: list[str] = []
    warnings: list[str] = []
    ok: list[str] = []

    # API key — not needed when running from Claude Code (Claude Code IS the intelligence layer)
    if settings.anthropic_api_key:
        ok.append("ANTHROPIC_API_KEY configured (standalone mode)")
    else:
        ok.append("ANTHROPIC_API_KEY not set — expected when running from Claude Code (recommended)")

    # Database
    try:
        init_db()
        ok.append("SQLite database initialized")
    except Exception as e:
        issues.append(f"Database init failed: {e}")

    # Risk config
    risk_yaml = BASE / "config" / "risk_limits.yaml"
    if risk_yaml.exists():
        try:
            limits = RiskLimits.from_yaml(risk_yaml)
            ok.append(f"risk_limits.yaml loaded (max_trade_risk=${limits.max_trade_risk_dollars})")
            if limits.allow_live_trading:
                warnings.append("LIVE TRADING ENABLED — real orders will execute (require_manual_confirmation=True)")
            else:
                ok.append("Live trading disabled (safe)")
        except Exception as e:
            issues.append(f"risk_limits.yaml parse error: {e}")
    else:
        warnings.append("risk_limits.yaml not found — using hardcoded defaults")

    # Assets allowlist
    allowlist = BASE / "config" / "assets_allowlist.yaml"
    if allowlist.exists():
        ok.append("assets_allowlist.yaml found")
    else:
        warnings.append("assets_allowlist.yaml not found — scan commands will return empty results")

    # Logs dir
    logs_dir = BASE.parent / "logs"
    if logs_dir.exists():
        ok.append(f"Log directory: {logs_dir}")
    else:
        warnings.append("Log directory not found — logs will be created on first run")

    # Kalshi
    kalshi_url = settings.kalshi_base_url
    if "demo" in kalshi_url:
        ok.append(f"Kalshi environment: demo ({kalshi_url[:50]})")
    else:
        warnings.append(f"Kalshi environment may be production: {kalshi_url}")

    if settings.kalshi_api_key_id and settings.kalshi_private_key_path:
        from pathlib import Path as _Path
        key_path = _Path(settings.kalshi_private_key_path)
        if key_path.exists():
            ok.append(f"Kalshi auth: key ID set, private key found at {key_path}")
        else:
            warnings.append(f"Kalshi private key not found at: {settings.kalshi_private_key_path} (Kalshi trading unavailable)")
    else:
        ok.append("Kalshi auth: not configured (public market data only)")

    # Robinhood MCP
    # Execution happens via Claude Code MCP, not direct HTTP credentials.
    # Can't check MCP connection status from Python — user must verify in Claude Code.
    console.print("\n[dim]── Robinhood Agentic Trading ──[/dim]")
    console.print("  MCP server: https://agent.robinhood.com/mcp/trading")
    console.print("  Setup (run once in terminal):")
    console.print("    [cyan]claude mcp add robinhood-trading --transport http https://agent.robinhood.com/mcp/trading[/cyan]")
    console.print("  Then run [cyan]/mcp[/cyan] in Claude Code and complete OAuth in your desktop browser.")
    console.print("  [dim]Connection status not checkable from Python — verify in Claude Code with /mcp[/dim]")

    # Print results
    for msg in ok:
        console.print(f"[green]✓[/green] {msg}")
    for msg in warnings:
        console.print(f"[yellow]⚠[/yellow] {msg}")
    for msg in issues:
        console.print(f"[red]✗[/red] {msg}")

    if issues:
        console.print("\n[red]System has issues that must be resolved.[/red]")
        sys.exit(1)
    elif warnings:
        console.print("\n[yellow]System has warnings — review before trading.[/yellow]")
    else:
        console.print("\n[green]All checks passed.[/green]")


# ---------------------------------------------------------------------------
# route — classify only
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("question")
def route(question: str):
    """Classify a natural-language question into routing intent (no workflow execution)."""
    from ..config import get_settings
    from ..agents.router import route_query, route_query_offline

    settings = get_settings()

    if settings.anthropic_api_key:
        try:
            result = route_query(question)
        except Exception as e:
            console.print(f"[yellow]LLM routing failed ({e}), falling back to offline routing[/yellow]")
            result = route_query_offline(question)
    else:
        console.print("[dim]No API key — using offline keyword routing (low confidence)[/dim]")
        result = route_query_offline(question)

    console.print(Panel(
        f"[bold]Intent:[/bold] {result.intent.value}\n"
        f"[bold]Confidence:[/bold] {result.confidence:.0%}\n"
        f"[bold]Asset:[/bold] {result.extracted_asset or '—'} ({result.extracted_asset_type.value if result.extracted_asset_type else '—'})\n"
        f"[bold]Risk Level:[/bold] {result.risk_level}\n"
        f"[bold]Execution Requested:[/bold] {result.execution_requested}\n"
        f"[bold]Requires Live Data:[/bold] {result.requires_live_data}\n"
        f"[bold]Required Agents:[/bold] {', '.join(result.required_agents) or 'none'}\n"
        f"[bold]Reasoning:[/bold] {result.reasoning_summary}",
        title="Router Classification",
    ))

    if result.clarifying_question:
        console.print(f"\n[yellow]Needs clarification:[/yellow] {result.clarifying_question}")


# ---------------------------------------------------------------------------
# ask — full natural-language workflow
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("question")
def ask(question: str):
    """Run full workflow for a natural-language trading question."""
    from ..config import get_settings
    from ..agents.router import route_query, route_query_offline
    from ..agents.orchestrator import execute_workflow
    from ..agents.schemas import NoTradeDecision, TradeProposal, CandidateTrade
    from ..data.db import init_db

    init_db()
    settings = get_settings()

    # Route
    console.print(f"[dim]Routing: {question[:80]}...[/dim]")
    if settings.anthropic_api_key:
        try:
            route_result = route_query(question)
        except Exception as e:
            console.print(f"[yellow]LLM routing failed, using offline routing: {e}[/yellow]")
            route_result = route_query_offline(question)
    else:
        console.print("[yellow]No API key — using offline routing. LLM agents will not run.[/yellow]")
        route_result = route_query_offline(question)

    console.print(f"[dim]Intent: {route_result.intent.value} ({route_result.confidence:.0%} confidence)[/dim]")

    if route_result.clarifying_question:
        console.print(f"\n[yellow]Clarification needed:[/yellow] {route_result.clarifying_question}")
        return

    # Execute workflow
    result = execute_workflow(question, route_result)

    # Display result
    _display_workflow_result(result)


def _display_workflow_result(result) -> None:
    from ..agents.schemas import NoTradeDecision, TradeProposal, CandidateTrade

    if isinstance(result, NoTradeDecision):
        console.print(Panel(
            f"[bold red]NO TRADE[/bold red]\n\n"
            f"[bold]Asset:[/bold] {result.asset_or_market}\n"
            f"[bold]Reason:[/bold] {result.reason.value}\n"
            f"[bold]Explanation:[/bold] {result.explanation}\n"
            + (f"\n[bold]What would change this:[/bold] {result.what_would_change_this}" if result.what_would_change_this else ""),
            title="No Trade Decision",
            border_style="red",
        ))

    elif isinstance(result, TradeProposal):
        direction_color = "green" if result.direction.value == "long" else "red"
        console.print(Panel(
            f"[bold]Asset:[/bold] {result.asset_or_market} ({result.asset_type.value})\n"
            f"[bold]Direction:[/bold] [{direction_color}]{result.direction.value.upper()}[/{direction_color}]\n"
            f"[bold]Entry:[/bold] {result.proposed_entry}\n"
            f"[bold]Target:[/bold] {result.target}\n"
            f"[bold]Stop:[/bold] {result.stop_or_invalidation}\n"
            f"[bold]Time Horizon:[/bold] {result.time_horizon}\n"
            f"[bold]Confidence:[/bold] {result.confidence:.0%}\n"
            f"[bold]Thesis:[/bold] {result.thesis}\n"
            f"[bold]What would change my mind:[/bold] {result.what_would_change_my_mind}\n\n"
            f"Proposal ID: [dim]{result.id}[/dim]\n"
            f"Status: [green]{result.status.value}[/green]",
            title="Trade Proposal",
            border_style="blue",
        ))
        console.print(f"\nNext step: [cyan]trading risk-check {result.id}[/cyan]")

    elif isinstance(result, list) and result and isinstance(result[0], CandidateTrade):
        table = Table(title="Candidate Trades")
        table.add_column("Rank")
        table.add_column("Asset")
        table.add_column("Type")
        table.add_column("Direction")
        table.add_column("Broker")
        table.add_column("Why ranked here")
        table.add_column("No-trade reason")

        for c in result:
            table.add_row(
                str(c.rank),
                c.asset_or_market,
                c.trade_type,
                c.direction.value if c.direction else "—",
                c.broker,
                c.reason_for_rank[:50],
                c.no_trade_reason or "—",
            )
        console.print(table)
        console.print("[dim]Expected edge: unknown (no backtest data). Run propose-trade for full analysis.[/dim]")

    elif isinstance(result, dict):
        if result.get("type") == "clarification_needed":
            console.print(f"[yellow]Clarification needed:[/yellow] {result.get('question')}")
        elif result.get("type") == "performance_summary":
            data = result.get("data", {})
            console.print(Panel(
                "\n".join(f"[bold]{k}:[/bold] {v}" for k, v in data.items()),
                title="Performance Summary",
            ))
        elif result.get("type") == "portfolio_risk":
            console.print(Panel(
                f"[bold]Open positions:[/bold] {result.get('open_positions')} / {result.get('max_open_positions')}\n"
                f"[bold]Approx exposure:[/bold] ${result.get('approx_total_exposure', 0):.2f}\n"
                f"[bold]Daily loss limit:[/bold] ${result.get('max_daily_loss_dollars')}",
                title="Portfolio Risk",
            ))
        else:
            console.print(json.dumps(result, indent=2, default=str))
    else:
        console.print(str(result))


# ---------------------------------------------------------------------------
# propose — alias for direct trade proposal
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("asset")
@click.option("--type", "asset_type", default="equity",
              type=click.Choice(["equity", "prediction_market", "etf", "crypto"]))
@click.option("--context", default="")
def propose(asset: str, asset_type: str, context: str):
    """Propose a trade for a specific asset (runs full research→strategy→skeptic→risk pipeline)."""
    from ..agents.schemas import AssetType
    from ..agents.orchestrator import Orchestrator
    from ..data.db import init_db

    init_db()

    orch = Orchestrator(user_question=f"Propose a trade for {asset}")
    result = orch._workflow_propose_trade(asset, AssetType(asset_type), context)
    _display_workflow_result(result)


# ---------------------------------------------------------------------------
# risk-check
# ---------------------------------------------------------------------------

@cli.command("risk-check")
@click.argument("proposal_id")
@click.option("--estimated-risk", default=10.0, type=float)
@click.option("--research-age-minutes", default=15.0, type=float)
@click.option("--spread-pct", default=None, type=float)
@click.option("--volume", default=None, type=float)
@click.option("--open-positions", default=0, type=int)
@click.option("--daily-loss", default=0.0, type=float)
def risk_check(proposal_id, estimated_risk, research_age_minutes, spread_pct, volume, open_positions, daily_loss):
    """Run the deterministic risk engine against a proposal."""
    from ..risk import check_proposal
    from ..data.db import init_db, get_session
    from ..data.models import ProposalRecord
    from ..data.market_store import save_risk_result
    from ..agents.schemas import TradeProposal

    init_db()

    with get_session() as session:
        record = session.query(ProposalRecord).filter_by(id=proposal_id).first()
        if not record:
            console.print(f"[red]Proposal {proposal_id} not found.[/red]")
            sys.exit(1)
        raw = json.loads(record.raw_json)
        proposal = TradeProposal(**raw)

    result = check_proposal(
        proposal=proposal,
        estimated_risk_dollars=estimated_risk,
        current_open_positions=open_positions,
        research_age_minutes=research_age_minutes,
        spread_percent=spread_pct,
        daily_loss_so_far=daily_loss,
        volume=volume,
    )
    risk_result_id = save_risk_result(result)

    status_color = "green" if result.approved else "red"
    console.print(Panel(
        f"Decision: [{status_color}]{result.final_decision.upper()}[/{status_color}]\n"
        f"Risk Score: {result.risk_score}/100\n"
        f"Live Trading: {'allowed' if result.live_trading_allowed else 'disabled'}\n"
        f"Max Allowed Size: ${result.max_allowed_size:.2f}",
        title="Risk Engine Result",
        border_style=status_color,
    ))

    if result.rejection_reasons:
        console.print("\n[red]Rejection Reasons:[/red]")
        for r in result.rejection_reasons:
            console.print(f"  • {r}")

    if result.warnings:
        console.print("\n[yellow]Warnings:[/yellow]")
        for w in result.warnings:
            console.print(f"  ⚠ {w}")

    if result.approved:
        console.print(f"\nRisk result ID: [dim]{risk_result_id}[/dim]")
        console.print(
            f"Next: [cyan]trading create-order-ticket {proposal_id} "
            f"--risk-result-id {risk_result_id} --side buy --limit-price <price> --quantity <qty>[/cyan]"
        )


# ---------------------------------------------------------------------------
# create-order-ticket
# ---------------------------------------------------------------------------

@cli.command("create-order-ticket")
@click.argument("proposal_id")
@click.option("--risk-result-id", default="")
@click.option("--broker", default="paper", type=click.Choice(["paper", "kalshi_demo", "kalshi_production", "robinhood_mcp"]))
@click.option("--side", required=True, type=click.Choice(["buy", "sell", "yes", "no"]))
@click.option("--limit-price", required=True, type=float)
@click.option("--quantity", required=True, type=float)
@click.option("--stop-price", default=None, type=float)
@click.option("--expiry-minutes", default=60, type=int, help="Ticket expires after N minutes")
@click.option("--notes", default="")
def create_order_ticket_cmd(proposal_id, risk_result_id, broker, side, limit_price,
                             quantity, stop_price, expiry_minutes, notes):
    """Create an order ticket from an approved proposal."""
    from ..execution import create_order_ticket
    from ..data.db import init_db, get_session
    from ..data.models import ProposalRecord
    from ..data.market_store import save_order_ticket
    from ..agents.schemas import TradeProposal, OrderSide, TicketStatus
    from datetime import timedelta, timezone

    init_db()

    with get_session() as session:
        record = session.query(ProposalRecord).filter_by(id=proposal_id).first()
        if not record:
            console.print(f"[red]Proposal {proposal_id} not found.[/red]")
            sys.exit(1)
        raw = json.loads(record.raw_json)
        proposal = TradeProposal(**raw)

    ticket, errors = create_order_ticket(
        proposal=proposal,
        risk_engine_result_id=risk_result_id,
        broker=broker,
        side=OrderSide(side),
        limit_price=limit_price,
        quantity=quantity,
        stop_price=stop_price,
        notes=notes,
    )

    if errors:
        console.print("[red]Ticket validation failed:[/red]")
        for e in errors:
            console.print(f"  • {e}")
        sys.exit(1)

    # Set expiry and advance to awaiting confirmation
    ticket.expires_at = (
        __import__("datetime").datetime.now(__import__("datetime").timezone.utc)
        + __import__("datetime").timedelta(minutes=expiry_minutes)
    )
    ticket.transition(TicketStatus.RISK_PENDING, "Created via CLI")
    ticket.transition(TicketStatus.RISK_APPROVED, "Passed ticket validation")
    ticket.transition(TicketStatus.AWAITING_USER_CONFIRMATION, "Ready for paper execution")

    save_order_ticket(ticket)
    console.print(f"[green]Order ticket created: {ticket.id}[/green]")
    console.print(f"  {ticket.side.value} {ticket.quantity} {ticket.asset_or_market} @ {ticket.limit_price} via {ticket.broker}")
    console.print(f"  Est. max loss: ${ticket.estimated_max_loss:.2f}")
    console.print(f"  Status: {ticket.ticket_status.value}")
    console.print(f"  Expires: {ticket.expires_at}")
    console.print(f"\nNext: [cyan]trading execute {ticket.id} --fill-price {limit_price}[/cyan]")


# ---------------------------------------------------------------------------
# tickets
# ---------------------------------------------------------------------------

@cli.command()
def tickets():
    """List all order tickets and their statuses."""
    from ..data.db import init_db
    from ..data.market_store import load_all_tickets

    init_db()
    all_tickets = load_all_tickets()

    if not all_tickets:
        console.print("[yellow]No tickets found.[/yellow]")
        return

    table = Table(title="Order Tickets")
    table.add_column("ID", style="dim")
    table.add_column("Asset")
    table.add_column("Side")
    table.add_column("Price")
    table.add_column("Qty")
    table.add_column("Broker")
    table.add_column("Status")
    table.add_column("Expires")

    for t in all_tickets:
        status = t.get("ticket_status", "")
        color = "green" if status == "awaiting_user_confirmation" else (
            "red" if status in ("cancelled", "expired", "risk_rejected") else "white"
        )
        table.add_row(
            (t.get("id") or "")[:8],
            t.get("asset_or_market", ""),
            t.get("side", ""),
            f"{t['limit_price']:.4f}" if t.get("limit_price") else "—",
            str(t.get("quantity", "")),
            t.get("broker", ""),
            f"[{color}]{status}[/{color}]",
            str(t.get("expires_at") or "—")[:16],
        )
    console.print(table)


# ---------------------------------------------------------------------------
# execute — paper-execute an existing ticket
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("ticket_id")
@click.option("--fill-price", required=True, type=float, help="Simulated fill price")
@click.option("--strategy-name", default="")
def execute(ticket_id: str, fill_price: float, strategy_name: str):
    """Paper-execute an existing approved order ticket."""
    from ..agents.schemas import OrderTicket, Direction, TicketStatus
    from ..agents.orchestrator import execute_ticket_paper
    from ..data.db import init_db
    from ..data.market_store import load_ticket_by_id

    init_db()

    ticket_data = load_ticket_by_id(ticket_id)
    if not ticket_data:
        console.print(f"[red]Ticket {ticket_id} not found.[/red]")
        sys.exit(1)

    try:
        ticket = OrderTicket(**json.loads(ticket_data["raw_json"]))
    except Exception as e:
        console.print(f"[red]Failed to load ticket: {e}[/red]")
        sys.exit(1)

    if ticket.is_expired():
        console.print(f"[red]Ticket {ticket_id} has expired. Create a new one.[/red]")
        sys.exit(1)

    direction = Direction.LONG if ticket.side.value in ("buy", "yes") else Direction.SHORT

    result = execute_ticket_paper(
        ticket=ticket,
        fill_price=fill_price,
        direction=direction,
        strategy_name=strategy_name,
        confirm_fn=click.confirm,
    )

    _display_workflow_result(result)


# ---------------------------------------------------------------------------
# paper-open (legacy direct command)
# ---------------------------------------------------------------------------

@cli.command("paper-open")
@click.argument("ticket_id")
@click.option("--fill-price", required=True, type=float)
@click.option("--strategy-name", default="")
@click.option("--notes", default="")
def paper_open(ticket_id, fill_price, strategy_name, notes):
    """Open a paper trade directly from a ticket (alias for execute)."""
    from ..agents.schemas import OrderTicket, Direction, TicketStatus
    from ..agents.orchestrator import execute_ticket_paper
    from ..data.db import init_db
    from ..data.market_store import load_ticket_by_id, save_paper_trade

    init_db()

    ticket_data = load_ticket_by_id(ticket_id)
    if not ticket_data:
        console.print(f"[red]Ticket {ticket_id} not found.[/red]")
        sys.exit(1)

    ticket = OrderTicket(**json.loads(ticket_data["raw_json"]))
    direction = Direction.LONG if ticket.side.value in ("buy", "yes") else Direction.SHORT

    result = execute_ticket_paper(
        ticket=ticket,
        fill_price=fill_price,
        direction=direction,
        strategy_name=strategy_name,
        confirm_fn=click.confirm,
    )
    _display_workflow_result(result)


# ---------------------------------------------------------------------------
# paper-close
# ---------------------------------------------------------------------------

@cli.command("paper-close")
@click.argument("trade_id")
@click.option("--exit-price", required=True, type=float)
@click.option("--notes", default="")
def paper_close(trade_id, exit_price, notes):
    """Close an open paper trade."""
    from ..data.db import init_db, get_session
    from ..data.models import PaperTradeRecord
    from ..data.market_store import save_paper_trade
    from ..agents.schemas import PaperTrade, TradeStatus, Direction, AssetType
    from ..execution import PaperTrader

    init_db()

    with get_session() as session:
        record = session.query(PaperTradeRecord).filter_by(id=trade_id).first()
        if not record:
            console.print(f"[red]Trade {trade_id} not found.[/red]")
            sys.exit(1)
        if record.status != "paper_open":
            console.print(f"[red]Trade {trade_id} is not open (status: {record.status}).[/red]")
            sys.exit(1)

        trade = PaperTrade(
            id=record.id,
            ticket_id=record.ticket_id,
            asset_or_market=record.asset_or_market,
            asset_type=AssetType(record.asset_type),
            direction=Direction(record.direction),
            entry_price=record.entry_price,
            quantity=record.quantity,
            strategy_name=record.strategy_name or "",
            thesis=record.thesis or "",
            notes=record.notes or "",
            opened_at=record.opened_at,
        )

    trader = PaperTrader()
    trader._open_trades[trade.id] = trade
    closed = trader.close_trade(trade_id=trade.id, exit_price=exit_price, notes=notes)
    save_paper_trade(closed)

    pnl_color = "green" if (closed.pnl or 0) >= 0 else "red"
    console.print(Panel(
        f"[bold]Asset:[/bold] {closed.asset_or_market}\n"
        f"[bold]Entry:[/bold] {closed.entry_price:.4f}\n"
        f"[bold]Exit:[/bold] {exit_price:.4f}\n"
        f"[bold]P&L:[/bold] [{pnl_color}]${closed.pnl:.4f}[/{pnl_color}]",
        title="Paper Trade Closed",
        border_style=pnl_color,
    ))
    console.print(f"\nNext: [cyan]trading review[/cyan]")


# ---------------------------------------------------------------------------
# show-open
# ---------------------------------------------------------------------------

@cli.command("show-open")
def show_open_trades():
    """Show all open paper trades."""
    from ..data import load_open_paper_trades
    from ..data.db import init_db
    init_db()

    trades = load_open_paper_trades()
    if not trades:
        console.print("[yellow]No open paper trades.[/yellow]")
        return

    table = Table(title="Open Paper Trades")
    table.add_column("ID", style="dim")
    table.add_column("Asset")
    table.add_column("Direction")
    table.add_column("Entry")
    table.add_column("Qty")
    table.add_column("Opened")
    table.add_column("Strategy")

    for t in trades:
        table.add_row(
            (t.get("id") or "")[:8],
            t.get("asset_or_market", ""),
            t.get("direction", ""),
            f"{t['entry_price']:.4f}",
            str(t.get("quantity", "")),
            str(t.get("opened_at", ""))[:16],
            t.get("strategy_name", ""),
        )
    console.print(table)


# ---------------------------------------------------------------------------
# review
# ---------------------------------------------------------------------------

@cli.command()
def review():
    """Show performance summary for closed trades."""
    from ..data import load_closed_paper_trades
    from ..data.db import init_db
    from ..review.performance_review import compute_performance
    from ..config import get_settings

    init_db()
    trades = load_closed_paper_trades()

    if not trades:
        console.print("[yellow]No closed paper trades to review.[/yellow]")
        return

    perf = compute_performance(trades)

    console.print(Panel(
        "\n".join(f"[bold]{k}:[/bold] {v}" for k, v in perf.items()),
        title="Performance Summary",
    ))

    table = Table(title="Closed Trades")
    table.add_column("ID", style="dim")
    table.add_column("Asset")
    table.add_column("Dir")
    table.add_column("Entry")
    table.add_column("Exit")
    table.add_column("P&L")

    for t in trades:
        pnl = t.get("pnl") or 0
        pnl_color = "green" if pnl >= 0 else "red"
        table.add_row(
            (t.get("id") or "")[:8],
            t.get("asset_or_market", ""),
            t.get("direction", ""),
            f"{t['entry_price']:.4f}",
            f"{t['exit_price']:.4f}" if t.get("exit_price") else "—",
            f"[{pnl_color}]${pnl:.4f}[/{pnl_color}]",
        )
    console.print(table)


# ---------------------------------------------------------------------------
# journal
# ---------------------------------------------------------------------------

@cli.command()
@click.option("--limit", default=20, type=int)
def journal(limit: int):
    """Show recent trade journal entries."""
    from ..data.db import init_db
    from ..data.market_store import load_journal_entries

    init_db()
    entries = load_journal_entries(limit=limit)

    if not entries:
        console.print("[yellow]No journal entries.[/yellow]")
        return

    table = Table(title="Trade Journal")
    table.add_column("ID", style="dim")
    table.add_column("Question")
    table.add_column("Intent")
    table.add_column("Outcome")
    table.add_column("P&L")
    table.add_column("Risk Score")
    table.add_column("Created")

    for e in entries:
        pnl = e.get("pnl")
        pnl_str = f"${pnl:.2f}" if pnl is not None else "—"
        table.add_row(
            (e.get("id") or "")[:8],
            (e.get("question") or "")[:40],
            e.get("intent") or "—",
            e.get("outcome") or "—",
            pnl_str,
            str(e.get("risk_score") or "—"),
            str(e.get("created_at") or "")[:16],
        )
    console.print(table)


# ---------------------------------------------------------------------------
# show-risk-settings
# ---------------------------------------------------------------------------

@cli.command("show-risk-settings")
def show_risk_settings():
    """Display current risk configuration."""
    from ..risk.rules import RiskLimits

    yaml_path = BASE / "config" / "risk_limits.yaml"
    limits = RiskLimits.from_yaml(yaml_path) if yaml_path.exists() else RiskLimits()

    table = Table(title="Risk Settings")
    table.add_column("Parameter", style="cyan")
    table.add_column("Value")

    for field, value in vars(limits).items():
        style = "red bold" if field == "allow_live_trading" and value else None
        table.add_row(field, str(value), style=style)

    console.print(table)


# ---------------------------------------------------------------------------
# scan-kalshi
# ---------------------------------------------------------------------------

@cli.command("scan-kalshi")
@click.option("--series", default=None)
@click.option("--limit", default=20, type=int)
def scan_kalshi(series, limit):
    """Scan Kalshi public markets."""
    from ..brokers import KalshiClient

    console.print("[blue]Scanning Kalshi public markets...[/blue]")
    client = KalshiClient()
    markets = client.get_markets(series_ticker=series, limit=limit)

    if not markets:
        console.print("[yellow]No markets returned (check network or Kalshi API availability).[/yellow]")
        return

    table = Table(title="Kalshi Markets")
    table.add_column("Ticker")
    table.add_column("Title")
    table.add_column("YES")
    table.add_column("NO")
    table.add_column("Volume")

    for m in markets:
        table.add_row(
            m.ticker,
            m.title[:60],
            f"{m.yes_price:.2f}" if m.yes_price is not None else "—",
            f"{m.no_price:.2f}" if m.no_price is not None else "—",
            str(m.volume) if m.volume is not None else "—",
        )
    console.print(table)


# ---------------------------------------------------------------------------
# scan-watchlist
# ---------------------------------------------------------------------------

@cli.command("scan-watchlist")
def scan_watchlist():
    """Show equity watchlist (no live prices in V0)."""
    import yaml as _yaml
    allowlist = BASE / "config" / "assets_allowlist.yaml"
    equities = []
    if allowlist.exists():
        with open(allowlist) as f:
            data = _yaml.safe_load(f)
        equities = data.get("equities", [])

    console.print("[yellow]No live prices in V0. Showing allowlist only.[/yellow]")
    table = Table(title="Equity Watchlist")
    table.add_column("Ticker")
    table.add_column("Name")
    table.add_column("Notes")
    for e in equities:
        table.add_row(e.get("ticker", ""), e.get("name", ""), e.get("notes", ""))
    console.print(table)
    console.print("[dim]V1: Real quotes via Polygon.io or similar.[/dim]")


# ---------------------------------------------------------------------------
# kalshi-balance  (authenticated)
# ---------------------------------------------------------------------------

@cli.command("kalshi-balance")
def kalshi_balance():
    """Fetch Kalshi account balance (requires KALSHI_API_KEY_ID + KALSHI_PRIVATE_KEY_PATH)."""
    from ..brokers import KalshiClient

    client = KalshiClient()
    if not client._is_authenticated():
        console.print("[red]Kalshi credentials not configured.[/red]")
        console.print("Set KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY_PATH in your .env file.")
        console.print("[dim]Keys are generated at: https://kalshi.com/account/api[/dim]")
        sys.exit(1)

    try:
        data = client.get_balance()
        balance_cents = data.get("balance", 0)
        console.print(Panel(
            f"[green]Balance: ${balance_cents / 100:.2f}[/green]\n"
            f"Environment: [yellow]{client._env}[/yellow]",
            title="Kalshi Account Balance",
        ))
    except Exception as e:
        console.print(f"[red]Error fetching balance: {e}[/red]")
        sys.exit(1)


# ---------------------------------------------------------------------------
# kalshi-positions  (authenticated)
# ---------------------------------------------------------------------------

@cli.command("kalshi-positions")
def kalshi_positions():
    """List open Kalshi positions (requires authentication)."""
    from ..brokers import KalshiClient

    client = KalshiClient()
    if not client._is_authenticated():
        console.print("[red]Kalshi credentials not configured.[/red]")
        sys.exit(1)

    try:
        positions = client.get_positions()
        if not positions:
            console.print("[dim]No open Kalshi positions.[/dim]")
            return

        table = Table(title="Kalshi Open Positions")
        table.add_column("Ticker", style="cyan")
        table.add_column("Side")
        table.add_column("Quantity", justify="right")
        table.add_column("Avg Price", justify="right")
        table.add_column("Market Value", justify="right")

        for pos in positions:
            table.add_row(
                pos.get("ticker", ""),
                pos.get("side", ""),
                str(pos.get("quantity", "")),
                f"${pos.get('average_price', 0) / 100:.2f}" if pos.get("average_price") else "—",
                f"${pos.get('market_value', 0) / 100:.2f}" if pos.get("market_value") else "—",
            )
        console.print(table)
    except Exception as e:
        console.print(f"[red]Error fetching positions: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    cli()
