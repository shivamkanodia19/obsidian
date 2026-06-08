# trading-bot-backend

Backend-first trading research and execution-prep system. CLI-driven. Paper-trading only in V0.
No autonomous live trading. All real-money execution requires explicit manual confirmation.

## Honest scope warning

This is a research scaffolding system, not an alpha-generating machine. LLM agents help with
research and reasoning. Deterministic code handles risk. Whether any strategy has edge must be
discovered empirically through paper trading and careful review — not assumed.

## Requirements

- Python 3.11+
- `pip install -e ".[dev]"`

## Setup

```bash
cp .env.example .env
# Fill in .env — never commit it
pip install -e ".[dev]"
trading init
```

## CLI commands

| Command | Description |
|---|---|
| `trading init` | Initialize database and config |
| `trading scan-kalshi` | Scan Kalshi public markets (stub in V0) |
| `trading scan-watchlist` | Scan equity watchlist (stub in V0) |
| `trading propose-trade ASSET` | Run research + strategy agents for an asset |
| `trading risk-check TICKET_ID` | Run deterministic risk engine on a proposal |
| `trading create-order-ticket PROPOSAL_ID` | Create order ticket from approved proposal |
| `trading paper-open TICKET_ID` | Open a paper trade from an approved ticket |
| `trading paper-close TRADE_ID` | Close a paper trade and log the result |
| `trading review-trades` | Run review agent on closed trades |
| `trading show-open` | Show all open paper trades |
| `trading show-risk-settings` | Print current risk config |

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## Live trading

Disabled by default. `ALLOW_LIVE_TRADING=false` in `.env`. Do not change this until V2.

## Tests

```bash
pytest tests/ -v
```
