# ARCHITECTURE.md

## System Diagram (V0 Completion Pass)

```
User (CLI)
    │
    ▼
src/cli/main.py          ← CLI entry point (click)
    │
    ├─── ask / route ──► Router Agent (LLM or keyword fallback)
    │                        │
    │                    RouterOutput (intent, asset, confidence)
    │                        │
    │                    Orchestrator.execute_workflow()
    │                        │
    │          ┌─────────────┴──────────────────────────────┐
    │          │  trade_proposal_request workflow:           │
    │          │  duplicate check → Research Agent (LLM)    │
    │          │       → Strategy Agent (LLM)               │
    │          │       → Skeptic Agent (LLM)                │
    │          │       → Risk Engine (CODE)                 │
    │          │       → TradeProposal or NoTradeDecision   │
    │          └─────────────────────────────────────────── ┘
    │
    ├─── tickets ────────────────────────────── list all OrderTickets
    │
    ├─── execute <id> ───────────────────────── paper-execute a ticket
    │                        │
    │                    Ticket lifecycle check (CODE)
    │                        │
    │                    Risk check re-run (CODE)
    │                        │
    │                    Manual confirmation (CLI prompt)
    │                        │
    │                    PaperTrade (paper only in V0)
    │
    ├─── doctor ─────────────────────────────── system health check
    │
    └─── [legacy direct commands: propose, risk-check, create-order-ticket,
          paper-open, paper-close, review, journal, show-open,
          show-risk-settings, scan-kalshi, scan-watchlist, init]


Data flow — all objects are Pydantic models:
    ResearchSummary → TradeProposal → SkepticOutput → RiskEngineResult
        → OrderTicket (with lifecycle state machine + audit trail)
        → PaperTrade → TradeReview
        → TradeJournalEntry (links all of the above by ID)

    NoTradeDecision can be returned at any stage (not an exception — a value)

Persistence:
    SQLite (trading.db) via SQLAlchemy ORM
    Tables: ResearchRecord, ProposalRecord, RiskResultRecord, OrderTicketRecord,
            PaperTradeRecord, TradeReviewRecord, NoTradeRecord,
            TicketAuditRecord, TradeJournalRecord

Broker layer (V0):
    KalshiClient — public market data (httpx, no auth)
    RobinhoodMCPClient — STUB (no real API)
    PaperBroker — implicit (PaperTrader handles this directly)
```

## Module Responsibilities

| Module | Responsibility |
|---|---|
| `src/agents/schemas.py` | Pydantic types for all domain objects |
| `src/agents/agent_runner.py` | ALL LLM calls (Anthropic API) — nowhere else |
| `src/agents/router.py` | NL query → RouterOutput (LLM + offline fallback) |
| `src/agents/orchestrator.py` | Workflow pipeline: router → agents → risk → ticket |
| `src/agents/model_scorer.py` | ML scorer stub — always not_available in V0 |
| `src/agents/prompts/*.md` | Agent system prompts (versioned by filename) |
| `src/risk/risk_engine.py` | Deterministic risk checks — no LLM |
| `src/risk/rules.py` | RiskLimits loaded from YAML |
| `src/execution/paper_trader.py` | Open/close/track paper trades |
| `src/execution/order_ticket.py` | Create order tickets from proposals |
| `src/execution/manual_approval.py` | Confirmation gate for any execution |
| `src/brokers/` | Broker client wrappers and stubs |
| `src/data/` | SQLAlchemy models + persistence helpers |
| `src/config/` | Settings (env vars) + YAML configs |
| `src/cli/main.py` | Click CLI commands (ask, route, doctor, tickets, execute + legacy) |
| `src/review/` | Trade journal + performance math |
| `src/strategies/` | Market scanners |
| `src/utils/` | Logging, IDs, time |

## Key Design Decisions

1. **LLM agents are advisory, not authoritative**
   Agent output is parsed and passed to deterministic code. Risk engine runs independently.
   An agent cannot approve its own trade.

2. **Single LLM call point**
   All Anthropic API calls go through `agent_runner.run_agent()`. This makes it easy to
   add rate limiting, retry logic, cost tracking, or swap models in one place.

3. **Config-as-code risk limits**
   `risk_limits.yaml` defines all hard limits. Changing a limit requires editing a file and
   restarting the CLI — no hot-patching via API or agent output.

4. **Live trading disabled in code, not just config**
   `allow_live_trading=false` is the default. Broker clients raise NotImplementedError for
   live submission. Even if config is changed, broker clients need V2 implementation.

5. **SQLite for V0**
   One file, no server, no connection pool. Good enough for single-user CLI paper trading.
   Easy to inspect with DB Browser for SQLite. Upgrade to Postgres in V3 when needed.
