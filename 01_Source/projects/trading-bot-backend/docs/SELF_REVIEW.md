# SELF_REVIEW.md — V0 Completion Pass Honest Assessment

**Date:** 2026-06-07
**Review scope:** V0 baseline + V0 completion pass

---

## What Was Built

### V0 Baseline (first pass)
- Full CLI with `init`, `scan-kalshi`, `scan-watchlist`, `propose-trade`, `risk-check`, `create-order-ticket`, `paper-open`, `paper-close`, `review`, `show-open`, `show-risk-settings`
- Deterministic risk engine with 9 hard gates (asset class, position limits, spread, thesis age, etc.)
- Paper trader with open/close/P&L tracking
- SQLite persistence for all objects
- Pydantic v2 schemas for all agent I/O
- 30 tests for risk engine and paper trader

### V0 Completion Pass (this session)
- **Router Agent**: Natural language query classification via `route_query()` (LLM) and `route_query_offline()` (keyword fallback)
- **Orchestrator**: Full workflow pipeline for `trade_proposal_request`, `market_scan`, `trade_review`, `portfolio_risk_query`
- **CLI expansion**: Added `ask`, `route`, `doctor`, `tickets`, `execute` commands
- **NoTradeDecision**: First-class return value throughout the pipeline (not an error)
- **Ticket lifecycle state machine**: 10 statuses with explicit allowed transition graph, audit trail, expiry
- **ModelScorer stub**: Honest — always returns `not_available`. Never fakes scores.
- **Skeptic Agent v2**: 11 adversarial challenges + explicit LLM self-awareness section
- **Risk engine hardening**: Duplicate position check, stale ticket check, `final_decision` field, `live_trading_allowed` field
- **Trade journal**: `TradeJournalEntry` links all objects in a pipeline run
- **Database**: 4 new tables (NoTradeRecord, TicketAuditRecord, TradeJournalRecord, TradeReviewRecord)
- **Tests**: 75 total (30 original + 45 new across router, no-trade, ticket lifecycle, model scorer)

---

## What Is Fully Working

- Risk engine: deterministic, no LLM, all 30 original tests pass + new tests
- Paper trader: open/close/P&L logic correct, all tests pass
- Ticket state machine: transitions enforced in code, invalid ones raise
- NoTradeDecision: schema clean, serializes/deserializes correctly
- ModelScorer: correctly refuses to fake scores
- Offline router: keyword-based fallback, never claims execution intent without explicit trigger
- CLI `doctor`: checks all config, credentials, database, and risk settings
- All 75 tests pass

---

## What Is Stubbed (Intentionally)

| Component | State | Why |
|---|---|---|
| LLM agents | Interface defined, calls real API if key set | No fake responses |
| Kalshi authenticated trading | Stub | V0 = no real orders |
| Robinhood | Stub | ToS issue with unofficial API |
| ML scorer | Stub, always not_available | No labeled data to train on |
| Live trading | Hard-gated in risk engine + config | Will not execute without explicit enable |
| CandidateTrade.expected_edge | Always None | No backtest data; lying would be worse |
| ResearchSummary.data_sources | Always empty list | No real market data feed in V0 |

---

## Known Technical Debt

### High Priority (fix before V1)
1. **Agent prompts are not versioned** — `prompts/*.md` has no hash or version field. If a prompt changes and a stored research summary was generated with the old prompt, there is no way to know. This will cause silent inconsistency.

2. **Orchestrator `execute_workflow()` and `Orchestrator.run()` are only partially tested** — the pipeline requires a real API key to test end-to-end. There are no mock LLM responses. All orchestrator tests would need mocking to be meaningful.

3. **`save_order_ticket()` in market_store.py** — the `raw_json` column stores full Pydantic JSON. The `ticket_status` column is updated on `save_order_ticket()` but the audit trail in `raw_json` will be stale if status changes between saves. The ticket record and the raw_json blob can drift.

4. **Router offline fallback is very basic** — keyword matching is weak. "I want to assess my portfolio risk" and "should I add more AAPL" both route to UNCLEAR. This is honest but means the offline path is nearly useless for anything non-obvious.

### Medium Priority
5. **`PaperTrader` state is in-memory only** — `_open_trades` dict resets on every CLI invocation. The CLI `paper-close` command works around this by re-hydrating from SQLite, but it is fragile. The trader and the database should be the same source of truth.

6. **`create-order-ticket` CLI command uses clunky inline `__import__`** — should be a proper import with a helper function.

7. **No watchlist scanner integration with real data** — `scan-watchlist` shows the allowlist YAML but has no prices. The Kalshi scanner hits a real endpoint but has no filtering or scoring logic.

### Low Priority
8. **No structured logging format** — logs go to console. A rotating file log would make it possible to audit past decisions.

9. **Config is file-based only** — no environment variable override for individual risk limits (only the full API key and broker credentials). Makes containerized deployment awkward.

10. **`TradeJournalEntry.pnl` is set post-close** — if the system crashes between paper-open and paper-close, the journal entry's P&L will be None permanently. No reconciliation logic exists.

---

## What Was Not Built (By Design)

- Real live trading execution (blocked by code gate)
- Web interface or API server
- Backtesting engine
- Options or crypto strategies
- ML model or trained scorer
- Real-time data feed
- Any unofficial API integrations

These are V1+ features. They were not stubbed carelessly — they were deliberately excluded to keep V0 within a verifiable scope.

---

## Honest Assessment: Is This System Safe to Use?

**For paper trading: Yes, with caveats.**
- The risk engine has no LLM calls and enforces limits deterministically
- Live trading cannot happen without setting `allow_live_trading: true` AND having a non-paper broker
- All LLM outputs are advisory only; no agent can place an order
- Tickets expire; stale tickets are blocked from execution

**For live trading: No. V0 explicitly blocks it.**
- The risk engine rejects any non-paper broker unless `allow_live_trading: true`
- `allow_live_trading` defaults to `false` in all configs
- Even if enabled, Robinhood is a stub and Kalshi authenticated trading is not implemented

**For trusting LLM research: Treat it as a starting point, not ground truth.**
- The skeptic agent is designed to challenge, not to verify
- The research agent can hallucinate sources, statistics, and market dynamics
- `CandidateTrade.expected_edge` is always null for this reason
- The model scorer is explicitly `not_available` — there is no signal there

---

## What Changed From V0 Baseline

The biggest architectural addition was the Orchestrator and Router layer, which converts the CLI from a command-by-command workflow into a natural-language interface. This is cleaner for the user but adds complexity to the code path:

Before: `CLI → Agent → Risk → Ticket`
After: `CLI → Router → Orchestrator → [Agent... → Risk → Ticket]`

The orchestrator pattern is correct for this use case. The router is the weakest link — offline routing is barely functional, and LLM routing adds an API call that can fail.

The ticket lifecycle state machine was a good addition — it prevents tickets from being executed twice, expired tickets from being run, and makes the audit trail automatic.

NoTradeDecision as a first-class return type was the right call. The alternative (raising an exception for "no trade") would have made the orchestrator harder to reason about.
