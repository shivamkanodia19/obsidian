# Robinhood Trading Cockpit

This is a vault-native testing system for the safer workflow we discussed:

1. create a structured trade proposal
2. run deterministic risk checks
3. require explicit typed approvals
4. review the order through a broker adapter
5. execute only after all guards pass
6. write the full trail back into Obsidian notes

For initial testing, the broker is a local mock broker. That lets you test the whole pipeline without touching real money or Robinhood.

## Folder Split

- `trading_cockpit.py` - main CLI
- `config/risk_policy.toml` - deterministic trade limits
- `runtime/` - machine-readable state and records
- `tests/test_trading_cockpit.py` - smoke and risk tests
- `../../../../02_Analyst/stocks/agentic-trading/` - human-readable proposal, approval, review, journal, and snapshot notes

## Commands

From `c:\Users\shiva\obsidian`:

```powershell
python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py init
python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py demo --reset
python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py status
```

Manual flow:

```powershell
python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py propose `
  --ticker IBIT `
  --usd 50 `
  --limit 42 `
  --thesis "Starter BTC-linked ETF position with capped risk." `
  --invalidation "Cancel if the setup becomes a chase before execution."

python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py check --proposal-id TP-YYYYMMDDTHHMMSS-IBIT
python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py approve --proposal-id TP-YYYYMMDDTHHMMSS-IBIT --stage initial --phrase "APPROVE TRADE: IBIT BUY 50.00 USD LIMIT 42.00 [TP-YYYYMMDDTHHMMSS-IBIT]"
python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py review --proposal-id TP-YYYYMMDDTHHMMSS-IBIT
python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py approve --proposal-id TP-YYYYMMDDTHHMMSS-IBIT --stage final --phrase "FINAL APPROVE TRADE: IBIT BUY 50.00 USD LIMIT 42.00 [TP-YYYYMMDDTHHMMSS-IBIT]"
python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py execute --proposal-id TP-YYYYMMDDTHHMMSS-IBIT
```

## What This Already Gives You

- explicit, structured proposals instead of vague "buy this" notes
- a deterministic risk gate that blocks oversized or disallowed trades
- typed approval phrases for both initial and final signoff
- a mock broker review and execution path
- Obsidian notes for proposals, risk checks, approvals, reviews, journals, and account snapshots

## What It Does Not Yet Do

- talk directly to Robinhood MCP
- fetch live quotes
- do research generation from an LLM
- place real trades

That is deliberate. The vault now acts as the safety layer first. Once you trust the workflow, we can swap the mock broker for a Robinhood MCP adapter.
