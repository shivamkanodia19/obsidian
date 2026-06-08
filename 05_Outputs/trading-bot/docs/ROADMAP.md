# ROADMAP.md

## Honest Framing

This roadmap is not a promise of profitability. It is a structured path to discovering
whether any strategy has real edge. Each version gates on the previous one being validated —
not just built.

**Rule: do not proceed to the next version until the current version's paper trading shows
positive expectancy over at least 30-50 trades in the specific setup type you are trading.**

---

## V0 — Backend Scaffold (CURRENT)

**Goal**: Build the infrastructure to start paper trading safely.

- [x] CLI-driven backend
- [x] 6 LLM agents (research, strategy, risk, execution, review, skeptic)
- [x] Deterministic risk engine with YAML config
- [x] Paper trading engine (open, close, P&L tracking)
- [x] SQLite persistence
- [x] Kalshi public market data (read-only)
- [x] Robinhood adapter stub
- [x] Tests for risk engine and paper trader
- [x] All documentation

**Gate to V1**: 20+ paper trades logged. At least basic familiarity with system behavior.

---

## V1 — Real Market Data + Stronger Research

**Goal**: Connect real data so research agents have actual information.

- [ ] Equity quotes via Polygon.io or Alpha Vantage API
- [ ] Kalshi authenticated market data (order book depth)
- [ ] Market data caching layer (avoid re-fetching same data)
- [ ] Research agent enrichment with live prices, IV, earnings dates
- [ ] Robinhood watchlist integration (read-only, official API if available)
- [ ] Better trade journal with tagging and search
- [ ] Performance analytics dashboard (CLI table form)

**Gate to V2**: Positive expectancy demonstrated in at least one specific setup type over 30+ paper trades.

---

## V2 — Manual Live Execution (Kalshi Only First)

**Goal**: Enable real-money execution with strict confirmation gates.

- [ ] Kalshi authenticated trading (RSA key auth)
- [ ] Final risk re-check at execution time (re-fetch quote, check spread)
- [ ] Live order confirmation flow (double-confirm with current quote shown)
- [ ] Live trade logging in DB (separate from paper trades)
- [ ] Position monitoring alerts (thesis invalidation conditions)
- [ ] Kill switch (close all open positions immediately)

**Gate to V3**: 6 months of live trading with controlled drawdown. Strategy proven to be profitable, not just break-even.

---

## V3 — Web Dashboard

**Goal**: Replace CLI with a usable interface.

- [ ] FastAPI backend
- [ ] Simple React or Next.js frontend
- [ ] Live position view
- [ ] Trade history + performance charts
- [ ] Agent output viewer

---

## V4 — Backtesting + Strategy Analytics

**Goal**: Test hypotheses on historical data before paper trading.

- [ ] Historical market data ingestion (Kalshi historical, equity OHLCV)
- [ ] Backtesting framework for rule-based strategies
- [ ] Strategy performance metrics (Sharpe, Sortino, max drawdown)
- [ ] Hypothesis testing framework (statistical significance checking)
- [ ] Feature engineering for ML scoring (V5 prep)

---

## V5 — Limited Automation with Hard Constraints

**Goal**: Allow system to propose and queue (NOT execute) trades automatically.

- [ ] Scheduled market scans
- [ ] Automatic proposal queuing (no auto-execution)
- [ ] Risk engine runs automatically on queued proposals
- [ ] User reviews queue and approves/rejects manually
- [ ] Hard-coded circuit breakers (e.g., no trading during high-volatility windows)

---

## V6 — Cloud Hosting (Only If Justified)

**Goal**: Run the system 24/7 without a local machine.

- [ ] Containerize (Docker)
- [ ] Cloud deployment (Railway, Render, or VPS)
- [ ] Secure credential management (Vault or cloud secrets)
- [ ] Monitoring and alerting

Only do this if V5 is proven profitable. Running a losing system in the cloud is just
losing money faster.
