# Claude Code Operating Guide — trading-bot-backend

## Architecture Model

**You are the intelligence layer. Python is the execution layer.**

Do not call `agent_runner.py` or `ANTHROPIC_API_KEY` for analysis. You do the research,
strategy, skepticism, and routing directly. The Python CLI handles risk checks, state
machine, database, and order tickets.

## MCP Connections Required

```bash
# Robinhood (run once, then complete OAuth in desktop browser)
claude mcp add robinhood-trading --transport http https://agent.robinhood.com/mcp/trading

# After adding: run /mcp in Claude Code and complete the auth flow
# This creates your dedicated Agentic Account (sandboxed from main account)
```

## Specialized Agent Roles

When Shivam asks about a trade or market, activate these roles yourself in sequence:

### 1. Research Agent
Read: `src/agents/prompts/research_agent.md`
- Analyze the asset or market
- Produce a structured research summary matching `ResearchSummary` schema (in schemas.py)
- Note: you cannot verify live prices — state assumptions clearly

### 2. Strategy Agent
Read: `src/agents/prompts/strategy_agent.md`
- Take research output → produce a trade proposal
- Output must match `TradeProposal` schema
- `expected_edge` must be `null` unless you have backtest data (you don't)

### 3. Skeptic Agent
Read: `src/agents/prompts/skeptic_agent.md`
- Challenge your own proposal from Strategy step
- Default posture is REJECTION, not approval
- Output matches `SkepticOutput` schema

### 4. Risk Engine (Python — mandatory gate)
```bash
trading risk-check <proposal_id>
```
This is deterministic code. Not negotiable. Do not skip it. Do not approve a trade
without running this command and seeing a passing result.

### 5. Create Order Ticket
```bash
trading create-order-ticket --proposal-id <id> --broker robinhood_mcp --side buy --limit-price <price> --quantity <n>
```

### 6. Execute
For Robinhood Agentic Account execution:
1. Run `trading execute <ticket_id>` — this runs final risk re-check and prompts for confirmation
2. Read the MCP instruction dict returned by `RobinhoodMCPClient.submit_order()`
3. Execute the two-step MCP sequence:
   ```
   # Step 1 — dry run, always
   mcp__robinhood-trading__review_equity_order(
       account_number="969132497",  # Agentic Account — verified agentic_allowed=true
       symbol=<ticker>,
       side="buy"|"sell",
       type="market"|"limit"|"stop_market"|"stop_limit",
       quantity="<n>",
       limit_price="<price>",  # only for limit/stop_limit
   )
   # Step 2 — present cost estimate + alerts to user, get explicit confirmation
   # Step 3 — place only after user says yes
   mcp__robinhood-trading__place_equity_order(
       account_number="969132497",
       symbol=<ticker>,
       side="buy"|"sell",
       type="market"|"limit"|"stop_market"|"stop_limit",
       quantity="<n>",
       limit_price="<price>",  # only if applicable
       ref_id="<fresh UUID>",  # generate once per order; reuse on retry
   )
   ```

For paper trading only:
```bash
trading paper-open <ticket_id>
```

## Workflow: Full Trade Proposal

```
User asks about a trade
  → You run Research Agent role (read prompts/research_agent.md)
  → You run Strategy Agent role (read prompts/strategy_agent.md)
  → You run Skeptic Agent role (read prompts/skeptic_agent.md)
  → Run: trading risk-check <proposal_id>
  → If approved: trading create-order-ticket ...
  → User confirms → trading execute <ticket_id>
  → You call Robinhood MCP tools to submit
```

## Workflow: Portfolio Check
```
trading show-open          # open paper trades
trading kalshi-positions   # Kalshi positions (if auth configured)

# Robinhood Agentic Account — call MCP tools directly:
mcp__robinhood-trading__get_portfolio(account_number="969132497")
mcp__robinhood-trading__get_equity_positions(account_number="969132497")
mcp__robinhood-trading__get_equity_quotes(symbols=["AAPL", "NVDA", ...])
```

## Hard Limits (enforced by code — do not override)

- `ALLOW_LIVE_TRADING` must be `true` in config for any real execution
- Risk engine must pass before any ticket is created
- Robinhood execution only works in the dedicated Agentic Account
- You cannot place orders without `trading execute` confirmation step
- Robinhood beta: equities only (no options, crypto, futures)

## Database Commands

```bash
trading init              # initialize DB (first run)
trading tickets           # all order tickets + status
trading show-open         # open paper trades
trading review            # performance summary
trading journal           # full trade journal
trading doctor            # health check — run this first
```

## Broker Reference

| Broker key | What it is | Live? |
|---|---|---|
| `paper` | In-memory paper trading | No |
| `robinhood_mcp` | Robinhood Agentic Account via MCP | Yes (real money) |
| `kalshi_demo` | Kalshi demo environment | No |
| `kalshi_production` | Kalshi production | Yes (real money) |

### Robinhood MCP — Verified Tool Names (2026-06-07)

| MCP Tool | Purpose |
|---|---|
| `mcp__robinhood-trading__get_accounts()` | List accounts; find agentic_allowed=true |
| `mcp__robinhood-trading__get_portfolio(account_number)` | Buying power, total value |
| `mcp__robinhood-trading__get_equity_positions(account_number)` | Open positions |
| `mcp__robinhood-trading__get_equity_quotes(symbols)` | Real-time quotes |
| `mcp__robinhood-trading__get_equity_tradability(symbol, account_number)` | Is it tradeable? |
| `mcp__robinhood-trading__review_equity_order(...)` | Dry-run cost estimate — call FIRST |
| `mcp__robinhood-trading__place_equity_order(...)` | Place real order |
| `mcp__robinhood-trading__get_equity_orders(account_number)` | Open/historical orders |
| `mcp__robinhood-trading__cancel_equity_order(order_id)` | Cancel open order |
| `mcp__robinhood-trading__search(query)` | Symbol search |
| `mcp__robinhood-trading__get_watchlists()` | List watchlists |
| `mcp__robinhood-trading__get_watchlist_items(watchlist_id)` | Items in a watchlist |

**Agentic Account number: `969132497`** (agentic_allowed=true, cash, $18 buying power)
**Main Account: `553333931`** — `agentic_allowed=false` — NEVER use for orders

## Do Not

- Call `agent_runner.py` directly — that's the old internal-LLM path
- Set `execution_requested=True` in the router for anything that isn't explicit user intent
- Bypass `trading risk-check` for any proposal
- Place trades in the user's main Robinhood account — only the Agentic Account
- Treat LLM research as ground truth — cite assumptions, flag uncertainty
