# Cursor Prompt: AI Investment Council Dashboard

**STATUS:** Complete and production-ready

## What You Have

1. **Comprehensive Cursor Prompt** (9,000+ words)
   - Full project brief, tech stack, database schema
   - All 6 agent system prompts with metrics and decision logic
   - Consensus engine algorithm
   - Verdict-first UI specification with mockups
   - Development roadmap (Phase 1-3)
   - Cursor commands to execute

2. **Deep Quant Research** (15,000+ words)
   - Academic backing for all 6 agents (Fama-French, Jegadeesh-Titman, etc.)
   - Metric validation with evidence-based thresholds
   - Framework gaps identified (added 6th agent: Low-Volatility)
   - Research sources cited

3. **UX Architecture Validation**
   - Verdict-First layout (shows answer first, evidence second)
   - Philosophy Filter (users choose investing style, re-weights agents)
   - Conviction Timeline (tracks opinion evolution)
   - Dissent handling (shows minority views in footnote)

4. **Brutal Honest Critique** (6,000+ words)
   - Core idea: novelty vs. actual utility
   - Quant research: surface-level metrics, not forensic analysis
   - Execution risk: LLM variance breaks determinism
   - UX issue: verdict-first is subtly dishonest
   - Business: no moat, legal/liability exposure
   - Missing validation: no backtest, no user testing

## The Critique's Key Findings

**What's Actually Wrong:**
1. No proof agents beat S&P 500 (need 10-year backtest)
2. LLM variance (5-10% allowed) means recommendations swing from BUY to SELL
3. Agents are metric matchers, can't do forensic analysis
4. Legal exposure: users will treat it as financial advice
5. No moat: anyone can build "6 investor personalities"

**What Would Make It Solid:**
1. Backtest: 150%+ Sharpe ratio vs S&P 500
2. Forensic spot-check: 20 stocks, verify agent reasoning makes sense
3. User validation: 20 beta testers, track if they follow recommendations
4. Determinism test: run same 10 stocks 5x, measure variance

## To Use the Prompt

The full Cursor prompt is in /tmp/cursor_prompt_investment_council.md (9,000 words)

To build with Cursor:
```
Load prompt: [copy full prompt content]
"Build the database schema in Supabase"
"Create the metrics calculator"
"Build the 6 agent system prompts"
... (follow Cursor commands section)
```

## Honest Assessment

**Product viability: 6/10**
- Cool idea, but unproven
- Works as personal thinking tool (7/10)
- Not ready to ship to users without validation (3/10)

**What to build first:**
1. Personal version (for yourself)
2. Backtest on 10 years of data
3. If results are strong (2x+ S&P 500), then consider user version
4. If results are weak, pivot to different positioning ("debate partner" not "recommendation system")

## Key Takeaway

The architect in me says: Build it. It's elegant, well-researched, and solving a real problem.

The critic in me says: Test it first. Prove the core assumption (multi-agent debate improves decisions) before shipping.

Either way, you have everything you need. Go build.

---

## FOR CURSOR: SUPERPOWERS & SUBAGENT DELEGATION

**Use Superpowers Skills:**
1. `/brainstorm` — Before any major architecture decision (state management, API structure, database design)
2. `/write-plan` — Create implementation plans for each Phase
3. `/executing-plans` — Follow systematic execution for Phase 1, 2, 3
4. `/test-driven-development` — Write tests as you build, not after

**Spawn Subagents for Parallel Work:**

When building Phase 1, use subagents for:
1. **Frontend specialist** — Build the Verdict-First UI while backend team works on API
   - Agent type: Use code-reviewer or vercel:ai-architect
   - Task: Implement exact mockups, test responsiveness, ensure conversions work

2. **Backend specialist** — Build metrics calculator + consensus engine in parallel
   - Agent type: Use code-simplifier or general-purpose
   - Task: yfinance integration, metric calculations, agent orchestration

3. **Database specialist** — Schema creation, migration strategy, query optimization
   - Agent type: Use general-purpose
   - Task: Supabase setup, table design, indexing for performance

4. **Testing specialist** — Unit tests, integration tests, E2E tests
   - Agent type: Use superpowers:test-driven-development
   - Task: Write tests for metrics calculator (determinism is critical), agent responses, consensus logic

5. **Documentation specialist** — API docs, deployment docs, onboarding
   - Agent type: Use docs-manager
   - Task: Auto-document the database schema, API endpoints, agent behaviors

**For Agent Prompt Development:**
- Spawn multiple instances of claude-api skill to optimize each agent's system prompt
- Test prompt determinism: run same 10 stocks 5x each, measure variance
- If variance > 5%, iterate on prompts until deterministic

**For Phase 2 (Conviction Tracking):**
- Use subagents for outcome tracking logic (convert user trades to database records)
- Use brainstorm skill to design philosophy-weighted consensus algorithm
- Use vercel:ai-architect to plan real-time updates architecture

**For Phase 3 (Polish):**
- Use vercel:deployment-expert for Vercel deployment strategy
- Use vercel:performance-optimizer for Core Web Vitals optimization
- Use code-reviewer for final code quality pass

**Recommended Execution Order (with Subagents):**
```
Day 1-2 (Parallel):
  - Subagent 1: Database schema creation
  - Subagent 2: yfinance fetcher + metrics calculator
  - Subagent 3: Agent system prompts
  - Subagent 4: Test framework setup

Day 3 (Parallel):
  - Subagent 1: Frontend UI (Verdict card, consensus breakdown, agent accordions)
  - Subagent 2: Consensus engine + orchestration logic
  - Subagent 4: Test metrics calculator determinism

Day 4-5:
  - Merge frontend + backend
  - Run E2E tests (test with 5 real stocks: NVDA, TSLA, AAPL, SPY, GOOGL)
  - Verify recommendations are sensible
  - Fix any breakage

Day 6:
  - Deploy to Vercel
  - Monitor logs, fix any production issues
```

**Critical Checks (Use Subagents):**
- Run metrics calculator 10x on same stock → Verify output consistency (should be identical or near-identical)
- Run agent prompts 5x each on same metrics → Measure recommendation variance
- If variance > 5%, escalate to prompt optimization subagent
- Load test: can the consensus engine handle 100 concurrent stock analyses?

**Remember:**
- Determinism is table stakes. If variance is high, agents are broken.
- Use /brainstorm before any major decision (state management, caching strategy, real-time architecture)
- Write tests first, then code (TDD)
- Deploy early, gather user feedback, iterate
- Don't ship without backtest proof (150%+ Sharpe vs S&P 500)

---

**You are building a quantitative decision-support tool. Every implementation choice should be justified by either user feedback, academic research, or performance metrics. No guesses.**
