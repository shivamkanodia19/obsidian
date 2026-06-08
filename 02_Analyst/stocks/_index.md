---
description: "Navigation hub for stocks"
title: Stocks Index
project: stocks
strategic: true
scope: stocks/portfolio-workflow
status: active
agent_context: true
surface_in_root: true
current_focus:
  - treat the latest portfolio refresh as the canonical state snapshot
  - use live market context before any new trade idea or recommendation
active_tasks:
  - refresh state and rationale before changing a position
  - separate long-term quality exposure from squeeze or hedge trades in any recommendation
prompt_context:
  - "[[02_Analyst/stocks/PORTFOLIO-REFRESH-2026-04-29]]"
  - "[[02_Analyst/stocks/STOCK-ADVICE-PROTOCOL]]"
  - "[[02_Analyst/stocks/DIP-WATCHLIST-2026-04-29]]"
definition_of_done:
  - any recommendation references the latest portfolio state and current market context
  - tactical trade types are distinguished instead of being blended together
blocked_by:
  - stale quotes, stale earnings context, or missing news checks invalidate the recommendation
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-05-28
tags: [stocks, portfolio, investing]
---

# Stocks Index

## Current Canonical Notes

- [[PORTFOLIO-REFRESH-2026-04-29]] - latest known portfolio-state note in the vault as of 2026-04-29
- [[STOCK-ADVICE-PROTOCOL]] - mandatory first-check rule for any new stock advice or trade idea
- [[DIP-WATCHLIST-2026-04-29]] - dated watchlist built from the same market context

## Historical and Supporting Notes

- [[PORTFOLIO-SNAPSHOT-2026-04-21]] - original Robinhood screenshot reconstruction used as the base holdings snapshot
- [[PORTFOLIO]] - longer-form strategy and decision-history note
- [[PORTFOLIO-DECISIONS]] - prior decision log
- [[ITERATION-LOG]] - iteration history
- [[speculative-high-upside-screen-2026-05-12]] - dated backfill for the unsaved May 11-12 speculative stock screen, split into upside-vs-risk scopes
- [[MULTI-AGENT-CONSENSUS-SYSTEM]] - research and debate structure for future stock decisions
- [[PREMARKET-OPEN-MEMO-2026-04-29]] - tactical premarket memo for the Apr 29, 2026 open
- [[agentic-trading/_index]] - vault-native guarded trading cockpit for proposal, approval, and mock execution testing

## Current Strategy

Use Yahoo Finance first for the latest quote, chart context, financial data, and news before making any buy or sell recommendation. If Yahoo Finance is unavailable or delayed, state that and then use backup sources.

Use current news, earnings dates, filings, and market events before recommendations. CAR is treated as a squeeze trade, LMT as a large earnings-risk position, ASML/TSM as quality semiconductor exposure, and USO as a small oil/geopolitical hedge.
