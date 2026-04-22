# Multi-Agent Portfolio Decision System

**System Version:** 1.0 | **Last Updated:** April 21, 2026 | **Next Iteration:** May 5, 2026 (or triggered earlier by catalysts)

---

## SYSTEM OVERVIEW

This is a **self-iterating consensus framework** where 5 specialized analytical agents (Bull, Bear, Fundamentals, Technical, Risk) debate each stock and reach consensus recommendations. The system **automatically updates** when:

1. **Earnings are released** (any holding)
2. **Catalyst windows close** (FDA approvals, contract awards, guidance misses)
3. **Technical support/resistance breaks** (price action signals)
4. **Risk parameters shift** (volatility spikes, liquidity changes)
5. **New research contradicts prior analysis** (agent reassessment)

---

## AGENT DEFINITIONS

Each agent has a fixed perspective and argues from that angle:

### Agent 1: BULL CASE ANALYST
**Role:** Find upside catalysts, price targets, positive scenarios
**Constraint:** Must cite 3+ catalysts per stock; targets must be 12-24 month horizon
**Bias:** Assumes best execution, favorable macro

### Agent 2: BEAR CASE ANALYST
**Role:** Identify worst-case risks, downside scenarios, failure modes
**Constraint:** Must quantify specific risks (regulatory, execution, competitive)
**Bias:** Assumes adversarial outcomes; flags tail risks

### Agent 3: FUNDAMENTAL ANALYST
**Role:** Value stocks using P/E, growth, profitability, FCF, guidance credibility
**Constraint:** Compares to sector averages; flags overvaluation/undervaluation
**Bias:** Prizes earnings visibility and sustainable margins

### Agent 4: TECHNICAL ANALYST
**Role:** Chart price trends, support/resistance, momentum, entry/exit signals
**Constraint:** Must identify 2+ price levels (entry/exit) with reasoning
**Bias:** Assumes price action precedes fundamental moves

### Agent 5: RISK MANAGER
**Role:** Assess portfolio concentration, liquidity, correlation, volatility, position sizing
**Constraint:** Recommends max position size based on risk metrics
**Bias:** Prioritizes capital preservation; flags concentration risk

---

## CONSENSUS SCORING SYSTEM

Each stock gets scored 0-5 on:

1. **Bull Score** (Bull Agent's conviction: 0=bankruptcy risk, 5=homerun)
2. **Bear Score** (Risk severity: 0=no risks, 5=existential threats)
3. **Fundamental Score** (Valuation: 0=overvalued garbage, 5=steal)
4. **Technical Score** (Trend strength: 0=broken down, 5=breakout confirmed)
5. **Risk Score** (Portfolio fit: 0=avoid, 5=essential core)

### DECISION RULE

**Consensus HOLD:** 4+ agents agree on buy/hold (score 3+)
**Consensus TRIM:** 3+ agents flag concentration/liquidity risk
**Consensus SELL:** 3+ agents score stock <2 OR risk score = 0
**Consensus BUY:** Bull + Fundamental + Technical all score 4+, Risk scores >2

---

## CURRENT CONSENSUS SCORECARD (April 21, 2026)

| Stock | Bull | Bear | Fund | Tech | Risk | **Action** | Position |
|-------|------|------|------|------|------|-----------|----------|
| **LMT** | 4 | 3 | 2 | 4 | 5 | **HOLD** | 40% |
| **ASML** | 4 | 4 | 1 | 2 | 2 | **TRIM** | 15% ↓ |
| **V** | 3 | 3 | 2 | 2 | 4 | **HOLD+** | 16% ↑ |
| **TSM** | 4 | 3 | 4 | 2 | 4 | **BUY dip** | 12% ↑ |
| **CRDO** | 4 | 3 | 4 | 3 | 4 | **BUY** | 9% ↑ |
| **ONDS** | 4 | 2 | 1 | 2 | 2 | **TRIM** | 6% ↓ |
| **AEVA** | 3 | 1 | 0 | 3 | 0 | **AVOID** | 0% |
| **RCAT** | 3 | 1 | 0 | 0 | 0 | **SELL** | 0% |
| **USO** | 2 | 1 | 0 | 2 | 0 | **SELL** | 0% |

---

## RECOMMENDED PORTFOLIO (Consensus Output)

```
CORE (55%):
├─ LMT 40% ($346K) — Defensive anchor, unanimous hold
└─ ASML 15% ($130K) — Semi-capex exposure, trimmed from 30%

GROWTH (30%):
├─ TSM 12% ($104K) — Fairly valued, buy $360-370 dip
├─ CRDO 9% ($78K) — Only profitable micro-cap, $144 support
├─ V 16% ($138K) — Diversifier, increased from 12%
└─ ONDS 6% ($52K) — Binary outcome, sized for risk

SPECULATIVE (0%):
└─ AEVA 0% ($0) — Death spiral risk, avoid

CASH (2%):
└─ Dry powder ($17K) — Dips, opportunities
```

**Total: $865 | Risk: MODERATE | Expected Return: 15-25% YTD**

---

## ITERATION RULES (Self-Improvement Protocol)

### AUTOMATIC RE-EVALUATION TRIGGERS

**Tier 1 (Update within 24 hours):**
- Stock breaks key technical support/resistance (>5% move)
- Earnings miss/beat guidance by >10%
- FDA approval/rejection announced
- Contract award/loss announced
- Insider trading alert (buying = bullish, selling = bearish)

**Tier 2 (Update within 1 week):**
- P/E ratio shifts >20% (revaluation)
- Cash burn or margin metrics deteriorate
- Major analyst downgrade (>$50 target cut)
- Sector rotation signal (rotation into/out of semis, defense)

**Tier 3 (Update monthly, May 5 2026):**
- Reassess all 5 agents against latest data
- Rebalance position sizes if Risk score changes
- Scan for new catalyst windows (Q2 earnings, product launches)
- Check for correlation shifts (are stocks moving together unexpectedly?)

---

## AGENT REASSESSMENT FRAMEWORK

When iteration is triggered, re-evaluate ONLY the affected agent(s):

**Example: LMT Earnings April 23**
- Bull Agent: "Did FCF guidance improve or worsen?"
- Bear Agent: "Is execution risk higher or lower post-earnings?"
- Fundamental Agent: "Did P/E multiple compress or expand?"
- Technical Agent: "Did price break resistance or consolidate?"
- Risk Agent: "Should position size adjust based on new volatility?"

**Output:** New scores for LMT; if any score changes >1 point, recalculate portfolio action.

---

## ITERATION LOG

**Version 1.0 (April 21, 2026):**
- Initial consensus scorecard
- Bull case: $780-850 LMT, $20-30 ONDS, $90-110 CRDO, $18-28 AEVA
- Bear case: China risk (ASML), geopolitical risk (TSM), dilution risk (RCAT), cash burn (AEVA)
- Fundamental: CRDO only profitable micro-cap; ASML/LMT overvalued
- Technical: TSM overbought (RSI 71), CRDO broken down but support at $144, ONDS -30% from peak
- Risk: RCAT liquidity nightmare (micro-cap), ONDS concentration risk at 15%

**Consensus Output:**
- HOLD LMT, TRIM ASML, INCREASE V, BUY TSM dip, BUY CRDO at $144, TRIM ONDS, SELL AEVA/RCAT/USO

---

## CATALYST CALENDAR (Iteration Watchlist)

| Date | Catalyst | Stock | Trigger Level | Impact |
|------|----------|-------|---------------|--------|
| **Apr 23** | Q1 Earnings | LMT | FCF guidance ±20% | Bull/Bear/Fund reassess |
| **Apr 29** | Q2 Earnings | KLIC | HBM4 demand signal | Tech/Fund reassess |
| **May 4** | Q1 Earnings | ICHR | Margin trend | Fund reassess |
| **May 10** | PDUFA Decision | VYVGART | Approval vs. Reject | N/A (not held) |
| **May 15** | Q2 Earnings | RCAT | Revenue guidance | Bear agent: "We told you so" |
| **May 20** | Phase 3 Data | EDSA | Clinical hit vs. miss | N/A (not held) |
| **May 30** | ASCO Update | CRBS | Data presentation | N/A (not held) |
| **Q2/Q3** | Various | ONDS, AEVA, CRDO | Guidance + orders | Bull/Tech/Risk reassess |

---

## DECISION THRESHOLDS (When to Act)

### SELL SIGNAL (Exit immediately, unless tax-loss harvesting concerns):
- Risk score drops to 0 (concentration risk unacceptable)
- Bear score = 5 + Fundamental score <1 (unrecoverable fundamentals)
- Technical breaks key support + volume confirms (momentum collapse)
- Insider selling spike (3+ C-suite selling, no insider buys)

### TRIM SIGNAL (Reduce position 25-50%):
- Risk score = 2 (concentration warning)
- Bull score drops 1+ points (upside thesis breaks)
- Technical trend breaks but fundamentals intact (wait for support)
- Valuation compression (P/E rises 20%+ on flat earnings)

### BUY SIGNAL (Increase position or deploy cash):
- Bull + Fundamental + Technical all score 4+ (alignment)
- Risk score 4+ (position sizing supports it)
- Technical: Confirmed support hold + RSI <50 (momentum reset)
- Insider buying spike (management confidence)

### HOLD SIGNAL (No action):
- 3+ agents unchanged scores (consensus stable)
- Catalyst window still open (don't front-run)
- Position within risk-adjusted size limits (no rebalancing needed)

---

## EXECUTION RULES (When Scores Change)

### IF Bull Score ↑ (upside increases):
- Do nothing if position already at target size
- If underweighted, consider adding on technical dips

### IF Bear Score ↑ (downside risk increases):
- Trim immediately if Risk score drops to 1-2
- If Risk score stays 3+, hold but stop buying dips

### IF Fundamental Score ↑ (valuation improves):
- Don't chase; wait for technical confirmation
- Fundamental alone is not a buy signal (Bull must agree)

### IF Technical Score ↑ (momentum improving):
- Momentum trades fastest; act within 24 hours if Risk allows
- Sell on overbought (RSI >70) unless Bull/Fundamental also improving

### IF Risk Score ↓ (position risk increases):
- This is the HIGHEST PRIORITY trigger
- Trim immediately, regardless of other agents
- Liquidity concerns (like RCAT) are non-negotiable

---

## SELF-IMPROVEMENT MECHANISMS

### Monthly Retrospective (May 5 review):
1. **Accuracy check**: Which agent predictions were closest? Which missed?
2. **Bias audit**: Did any agent systematically overestimate/underestimate?
3. **Recalibration**: Adjust agent confidence weights based on track record
4. **Feedback loop**: If Bear Agent is consistently too pessimistic, reduce weight; if Bull is too optimistic, same

### Example Retrospective (May 5, 2026):
- Bull Agent said ONDS $20-30 by May; actual: still $10-12 → **Bull recalibrated down**
- Technical Agent said CRDO holds $144 support; actual: bounced to $165 → **Bull Agent vindicated**
- Risk Agent said RCAT liquidity nightmare; actual: stock illiquid as predicted → **Risk recalibrated up**
- Fundamental Agent said ASML overvalued 50x; actual: China ban risk realized, down 15% → **Fundamental recalibrated accurate**

### Seasonal Adjustments:
- Q1 (Jan-Mar): Bull tends overoptimistic on earnings surprises; weight down 10%
- Q2 (Apr-Jun): Risk Agent most accurate on summer volatility spikes; weight up 10%
- Q3-Q4: Technical Agent outperforms on holiday seasonality; weight up 5%

---

## VAULT INTEGRATION

**File Updates:**
- `PORTFOLIO.md` — Current holdings snapshot (update weekly)
- `PORTFOLIO-DECISIONS.md` — Consensus scores (update on catalyst triggers)
- `MULTI-AGENT-CONSENSUS-SYSTEM.md` — This file (update monthly + iterate)
- `ITERATION-LOG.md` — Detailed agent reassessments (create separate file, linked below)

**Memory Index Update:**
- Tag: `#stock-portfolio`, `#multi-agent`, `#self-iterating`
- Next review: May 5, 2026 (monthly iteration)
- Catalyst watch: April 23 LMT earnings (Tier 1 trigger)

---

## QUARTERLY SYSTEM AUDIT (Advanced Self-Improvement)

**Every Q (May 5, Aug 5, Nov 5):**

1. **Accuracy Score**: Did portfolio hit 15-25% return target?
   - If YES: Keep agent weightings; scale positions up
   - If NO: Debug which agent caused miss; adjust weights

2. **Risk Management Score**: Did max drawdown stay <15%?
   - If YES: Portfolio risk-adjusted correctly
   - If NO: Risk Agent was too aggressive; re-weight down

3. **Catalyst Prediction Accuracy**: Did agents forecast catalyst outcomes correctly?
   - Bull predicted 80% accuracy? Good. 40% accuracy? Recalibrate.
   - Technical predicted breakouts? Did they happen? (Measure win rate)

4. **Correlation Accuracy**: Did agents correctly predict stock correlations?
   - ONDS-RCAT moved together? Agents said 0.7-0.8; did they?
   - Adjust Risk Agent's correlation assumptions accordingly

5. **System Drift**: Are agents becoming groupthink or remaining independent?
   - If all agents score 3-4 on everything → system is lazy, add noise
   - If agents never agree → system is broken, re-examine decision rules

---

## HOW TO USE THIS SYSTEM

**Weekly Workflow:**
1. Check catalyst calendar for that week
2. If catalyst hits, pull latest data; update relevant agent scores
3. If any score changes >1 point, recalculate portfolio action
4. Execute trades per decision thresholds
5. Log the update to iteration log

**Monthly Workflow (May 5):**
1. Run full retrospective (see section above)
2. Reassess all 5 agents against latest data
3. Update consensus scorecard
4. Rebalance portfolio if Risk scores changed
5. Update this file with V2.0 learnings

**Quarterly Workflow (May 5, Aug 5, Nov 5):**
1. Run system audit (see section above)
2. Recalibrate agent weightings based on accuracy
3. Update decision thresholds if needed
4. Document lessons learned in iteration log

---

## AGENT COMMUNICATION PROTOCOL

When agents disagree on a score:

**Example: Bull says LMT = 4, Bear says 2, Fund says 2**
- **Consensus:** 2 agents (Bear + Fund) align; Bull is outlier
- **Decision:** Downgrade LMT to 3 (consensus average 2.67 rounds to 3)
- **Action:** HOLD, not BUY (only 1 agent bullish isn't enough)

**Example: All agents except Risk score CRDO = 4, Risk scores 2**
- **Consensus:** 4 agents (Bull + Bear + Fund + Tech) align; Risk is outlier
- **Decision:** BUY, but size to Risk's constraint (only 8-10%, not 15%)
- **Action:** Deploy $78K, not $130K

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Apr 21, 2026 | Initial system launch |
| 2.0 | May 5, 2026 | Post-earnings recalibration (TBD) |
| 3.0 | Aug 5, 2026 | Q2 learnings + agent re-weighting (TBD) |
| 4.0 | Nov 5, 2026 | Q3 system audit + seasonal adjustments (TBD) |

---

## NEXT ITERATION CHECKPOINT

**Date:** May 5, 2026 (2 weeks)
**Triggers before then:**
- LMT Q1 earnings (April 23) → update Bull/Bear/Fund/Tech agents
- TSM technical break below $370 → update Technical/Risk agents
- CRDO support hold at $144 → update Technical/Risk agents

**What to monitor:**
1. Does LMT beat or miss guidance? (Bull/Bear threshold)
2. Does CRDO hold $144 or crash? (Technical threshold)
3. Does ONDS break below $9 or recovery to $12+? (Risk threshold)
4. Does AEVA show cash runway extension or funding news? (Bear threshold)

**If any threshold breached before May 5:**
- Re-run affected agents immediately
- Update portfolio decision
- Execute trades per decision thresholds
- Log to iteration log

---

**System Status: ACTIVE & SELF-ITERATING** ✅
**Next Review: April 23, 2026 (LMT Earnings Trigger)**
**Final System Audit: May 5, 2026**
