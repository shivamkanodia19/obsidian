# RISK_POLICY.md

## Non-Negotiable Rules

These rules are enforced by code, not by trust, not by agent output, not by config alone.
Changing them requires editing source code and tests.

### 1. No Autonomous Live Trading
The system will never place a real-money order without explicit user command.
`trading paper-open` and `trading paper-close` are the only execution commands in V0.
Live broker clients raise NotImplementedError.

### 2. No Market Orders By Default
`reject_market_orders: true` in risk_limits.yaml.
Only limit orders are valid. This prevents catastrophic fills in thin markets.

### 3. No Options By Default
`allow_options: false` in risk_limits.yaml.
Options add leverage and complexity. Not enabled until explicitly approved and V2 built.

### 4. No Crypto By Default
`allow_crypto: false` in risk_limits.yaml.
Crypto has 24/7 volatility, exchange risk, and no circuit breakers.
Not enabled until explicitly approved.

### 5. No Leverage
The system does not support margin, leverage, or borrowing.
Quantity × price must never exceed available paper account balance.

### 6. No Credential Leakage
API keys are loaded from .env only.
.env is in .gitignore.
No key ever appears in logs, CLI output, or agent prompts.
The logging module must never log settings values.

### 7. No Trades Without Logs
Every paper trade is persisted to SQLite before any confirmation is printed.
If persistence fails, the trade is considered not executed.

### 8. Manual Confirmation Always Required
`require_manual_confirmation: true` in both settings.py and risk_limits.yaml.
CLI prompts before any paper-open.
No API endpoint will ever bypass this in V0.

## Kill Switch Logic (V2)

When implemented:
1. `trading kill-switch` command closes all open positions immediately at market.
2. Kill switch can be triggered by any of:
   - User command
   - Daily loss limit breached
   - API connectivity failure lasting > 30 seconds
3. After kill switch: trading is suspended until manually re-enabled.

## Max Loss Rules (Configured in risk_limits.yaml)

| Rule | Default | Purpose |
|---|---|---|
| max_trade_risk_dollars | $25 | Max you can lose on a single trade |
| max_daily_loss_dollars | $50 | Hard stop for the entire trading day |
| max_open_positions | 5 | Prevents over-diversification and tracking difficulty |
| max_allocation_per_trade_percent | 10% | Position sizing discipline |
| max_spread_percent | 3% | Prevents trading in illiquid markets |
| max_thesis_age_minutes | 60 | Prevents acting on stale research |

## What the Risk Engine Cannot Catch

Be honest: there are failure modes the deterministic engine cannot detect.

- **Thesis quality**: The engine doesn't read the thesis. A great-sounding thesis from an LLM
  may be factually wrong. You must read every thesis before approving.

- **Correlation risk**: Two seemingly unrelated trades may be correlated (e.g., NASDAQ-linked
  Kalshi markets and tech stocks). The engine doesn't know your entire portfolio.

- **Black swan events**: No risk engine predicts flash crashes, circuit breakers, or exchange
  outages. Always have dry powder and never bet money you need.

- **Model hallucination**: The research agent can produce confident-sounding nonsense.
  The skeptic agent challenges this, but you are the final reader.
