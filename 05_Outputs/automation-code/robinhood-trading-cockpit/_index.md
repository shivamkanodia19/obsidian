---
title: Robinhood Trading Cockpit
description: Vault-native testing harness for guarded trade proposals and mock execution
last_updated: 2026-06-07
---

# Robinhood Trading Cockpit

This bundle turns the Robinhood-agent idea into a safer local workflow inside the vault:

- structured trade proposals
- deterministic risk checks
- explicit approvals
- broker review
- mock execution
- Obsidian audit notes

## Files

- `trading_cockpit.py` - main CLI
- `config/risk_policy.toml` - deterministic policy limits
- `README.md` - setup and command reference
- `tests/test_trading_cockpit.py` - regression coverage for the mock flow

## Notes Surface

The human-readable notes live in `02_Analyst/stocks/agentic-trading/`.

Start with:

- `python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py demo --reset`
