# PROJECT_PLAN.md

## What We Are Building

A backend-first trading research and execution-prep system. The system helps with:
- Researching assets and prediction markets (via LLM agents)
- Converting research into structured trade proposals
- Running deterministic risk checks against hard-coded limits
- Generating order tickets from approved proposals
- Executing paper trades and tracking performance
- Reviewing closed trades and extracting lessons

## What We Are NOT Building (V0)

- A web app or dashboard
- Autonomous trading of any kind
- Live execution (blocked by code, not just config)
- ML-based signal generation or backtesting
- Options or crypto trading
- Unofficial API integrations (no robin_stocks or scrapers)

## V0 Scope

| Component | Status |
|---|---|
| CLI commands (10+) | ✅ Built |
| Agent prompt files (6) | ✅ Built |
| Pydantic schemas | ✅ Built |
| Deterministic risk engine | ✅ Built |
| Paper trading engine | ✅ Built |
| Config (risk_limits.yaml, assets_allowlist.yaml) | ✅ Built |
| SQLite persistence | ✅ Built |
| Kalshi public market data | ✅ (requires API test) |
| Robinhood adapter | ✅ Stub (no real API) |
| LLM agent runner | ✅ (requires ANTHROPIC_API_KEY) |
| Tests (risk engine + paper trader) | ✅ Built |
| Docs | ✅ Built |

## Risks

1. **LLM hallucination risk**: Agents generate confident-sounding analysis that may be wrong.
   Mitigation: LLM output is advisory. Code enforces limits. Skeptic agent challenges output.

2. **No real Robinhood API**: Robinhood has no official public REST API for retail users.
   Mitigation: Robinhood adapter is a stub. V1 will integrate only if official API exists.

3. **Kalshi liquidity risk**: Most Kalshi markets are thin. Spreads can be 5-20%.
   Mitigation: Spread check in risk engine. max_spread_percent=3.0 default will block most contracts.

4. **Overfit strategies**: LLM-generated strategies may look reasonable but have no real edge.
   Mitigation: Paper trade everything. Track expectancy over 50+ trades before scaling.

5. **Credential security**: .env contains API keys. Never commit .env.
   Mitigation: .env in .gitignore. .env.example has no real values.

## Assumptions

- User is trading paper money only in V0
- ANTHROPIC_API_KEY is required to run agent commands (propose-trade, review-trades)
- Kalshi public endpoints are accessible without authentication
- SQLite is sufficient for V0 (no concurrent access needed)

## Open Questions

- When does an official Robinhood API become available?
- What strategy types show real edge in Kalshi prediction markets?
- What market data source will we use for equity quotes in V1?
  (Alpha Vantage, Polygon.io, or Yahoo Finance are candidates)
- Should we add a Kalshi demo account for authenticated paper trading?
