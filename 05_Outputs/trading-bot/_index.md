# Trading Bot — Agent Index

**Status:** Live (ALLOW_LIVE_TRADING=true as of 2026-06-07)
**Location:** `05_Outputs/trading-bot/`
**Source mirror:** `01_Source/projects/trading-bot-backend/` (canonical code)

## What This Is

A Claude Code-native trading research and execution system. Claude Code IS the intelligence layer — it reads prompt files and does the reasoning directly. Python handles risk, state, and execution mechanics.

**Brokers connected:**
- Robinhood Agentic Account `969132497` — live equities, MCP-authenticated, $18 buying power
- Kalshi production — configured, awaiting API credentials (see `.env`)
- Paper trader — always available, no config needed

## Read First

1. `CLAUDE.md` — full agent operating guide, workflow, MCP tool names, hard limits
2. `docs/SELF_REVIEW.md` — honest status of what's complete vs stubbed

## How to Run a Trade (Agent Instructions)

```
User asks about a trade
  → Read src/agents/prompts/research_agent.md → produce ResearchSummary
  → Read src/agents/prompts/strategy_agent.md → produce TradeProposal
  → Read src/agents/prompts/skeptic_agent.md  → produce SkepticOutput
  → cd to this folder, run: trading risk-check <proposal_id>
  → If approved: trading create-order-ticket <proposal_id> --broker robinhood_mcp --side buy --limit-price <p> --quantity <q>
  → trading execute <ticket_id> --fill-price <p>
  → Call mcp__robinhood-trading__review_equity_order(...) → show user → confirm → mcp__robinhood-trading__place_equity_order(...)
```

## Key CLI Commands

```bash
cd "c:\Users\shiva\obsidian\05_Outputs\trading-bot"
PYTHONUTF8=1 python -c "from src.cli.main import cli; cli(['doctor'])"      # health check
PYTHONUTF8=1 python -c "from src.cli.main import cli; cli(['show-open'])"   # open paper trades
PYTHONUTF8=1 python -c "from src.cli.main import cli; cli(['tickets'])"     # all order tickets
```

> All CLI commands need `PYTHONUTF8=1` prefix on Windows to avoid encoding errors.

## Robinhood MCP Tools (verified 2026-06-07)

| Tool | Purpose |
|---|---|
| `mcp__robinhood-trading__get_accounts()` | List accounts |
| `mcp__robinhood-trading__get_portfolio(account_number="969132497")` | Balance + buying power |
| `mcp__robinhood-trading__get_equity_positions(account_number="969132497")` | Open positions |
| `mcp__robinhood-trading__get_equity_quotes(symbols=[...])` | Real-time quotes |
| `mcp__robinhood-trading__review_equity_order(...)` | Dry run — ALWAYS call before placing |
| `mcp__robinhood-trading__place_equity_order(...)` | Place real order |

## Hard Limits (enforced in code — do not bypass)

- `ALLOW_LIVE_TRADING=true` is set — real orders WILL execute
- `REQUIRE_MANUAL_CONFIRMATION=true` — Shivam must confirm before any execution
- Risk engine must pass before any ticket is created
- Robinhood Agentic Account only — never `553333931` (main account)
- Equities and ETFs only in Robinhood beta

## Kalshi Setup (pending)

Kalshi production is configured but needs credentials:
1. Go to kalshi.com/account/api
2. Generate RSA key: `openssl genrsa -out certs/kalshi_private.pem 2048`
3. Upload public key to Kalshi dashboard
4. Paste the Key ID into `.env` → `KALSHI_API_KEY_ID=...`
