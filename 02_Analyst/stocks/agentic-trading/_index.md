---
title: Agentic Trading Hub
project: stocks
status: active
last_updated: 2026-06-07
tags: [stocks, agentic-trading, risk-system, automation]
---

# Agentic Trading Hub

This is the note surface for the vault-native trading cockpit.

The code lives in `05_Outputs/automation-code/robinhood-trading-cockpit/`. The notes here are the human-readable trail created by that system.

## Workflow

1. Create a structured proposal.
2. Run deterministic risk checks.
3. Save an initial typed approval.
4. Run broker review.
5. Save a final typed approval.
6. Execute only after every gate passes.
7. Review the journal and account snapshot notes.

## Generated Folders

- `proposals/`
- `risk-checks/`
- `approvals/`
- `reviews/`
- `journal/`
- `snapshots/`

## Starter Command

```powershell
python .\05_Outputs\automation-code\robinhood-trading-cockpit\trading_cockpit.py demo --reset
```

That command creates a complete mock run here so you can inspect the vault flow before wiring anything to Robinhood.
