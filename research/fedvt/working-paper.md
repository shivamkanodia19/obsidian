---
title: FEDVT Working Paper
type: research
status: active
last-updated: 2026-04-13
tags: [fedvt, feedlot, cattle-futures, machine-learning, texas-am]
---

# AI-Driven Feedlot Economics: FEDVT Working Paper

**Authors:** Adekunle, A.; Tiwari, K.; Garg, H.; Kaniyamattam, K.
**Presented at:** ASAS-CSAS Annual Meeting 2025, Hollywood, Florida
**Affiliation:** Texas A&M University, Department of Animal Science — AI for Sustainable Livestock Systems Lab

## Abstract

Reviews and synthesizes the Feedlot Economic Decision Visualization Tool (FEDVT). The tool integrates 65 operational cost parameters across a dynamic Excel/VBA dashboard and couples that cost framework with ML models (ARIMA, SARIMA, LSTM) to forecast CME feeder cattle futures prices. Core output: break-even price (BEP) directly informing hedging decisions.

## 1. Background

- U.S. beef industry: $112B enterprise, 11.4M head on feed at any time
- Feedlot = final, most capital-intensive stage of beef supply chain
- Feeder cattle placed at 600–800 lbs; committed for 100–240 days
- In a representative 1,000-head Texas operation: $2.12M expenses vs $2.31M revenue → $182,454 gross profit (~8.6% margin)
- A few $/cwt shift can turn profit into loss
- Industry pressures: drought, corn price volatility, labor shortages, disease risk

## 2. FEDVT Architecture

**Workflow:** Input Data → Details → Analysis → Summary → Dashboard

**Platform:** Microsoft Excel + VBA macros + Tableau visualization layer

### Cost Framework (65 parameters → 80+ calculated fields)

| Category | % of Total Expenses |
|---|---|
| Feeder Cost (purchase price, trucking, commission, insurance) | 86% |
| Other Operations (vet, marketing, transport, death loss) | 5% |
| Interest (operating + investment) | 4% |
| Feed (barley, corn silage, hay, supplements) | 2% |
| Labor (manual + manure removal) | 2% |
| Fixed Costs (depreciation, machinery) | <1% |

**Key insight:** Feeder cattle acquisition cost dominates at 80–86%. Getting the buy price right matters far more than feed efficiency optimization.

## 3. Feedlot Pricing Calculator

**Inputs:** # heads, start weight, target finish weight, days to finish, finished % shrink, bid price, cattle finish price, basis

**Outputs:**
- Break-Even Price (BEP): min $/cwt to recover all costs → $178.88/cwt in example
- Profit per Head: $147.89/head
- Total Revenue: $2,527.00
- Rate of Gain: 3.33 lbs/day

**Hedging connection:** Dashboard shows CME futures price ($240.48/cwt as of Aug 30, 2024) alongside BEP. Spread of ~$61.60/cwt = protected margin. Producer can lock in by selling Live Cattle futures on CME at placement.

## 4. ML Forecasting Models

Data source: Yahoo Finance feeder cattle ticker (GF=F), 2002–2024

| Model | Strength | Weakness | Verdict |
|---|---|---|---|
| ARIMA | Stable; interpretable | Flat-line predictions; misses volatility | Baseline only |
| SARIMA | Captures seasonal cattle cycles | Struggles with sharp non-linear shocks | Best classical; recommended for deployment |
| LSTM | Highest accuracy (R² = 0.975) | Complex; needs more data/compute | Best overall; target for next iteration |
| Random Forest / SVR | Handles multivariate inputs | Moderate vs LSTM | Useful for feature importance |

**Key metrics:** 65 parameters | 80+ calculated fields | 14 optimization fields | LSTM R² = 0.975

## 5. Limitations & Future Directions

**Current limitations:**
1. Yahoo Finance free data feed — lower quality/fidelity than direct CME data
2. Excel/VBA limits scalability and real-time ingestion
3. Univariate forecasting — no exogenous variables (USDA reports, corn futures, drought indices)

**Future directions:**
1. CME live data integration (highest priority)
2. Hybrid SARIMA + LSTM models
3. Real-time operational data input
4. Extension to other livestock categories and geographies

## 6. Conclusions

Core contribution: accurate, fully-loaded BEP from 65 cost parameters displayed in real time against CME futures curve → rational hedging decisions without pure experience-based judgment.

LSTM R² = 0.975 proves high-accuracy cattle futures prediction is achievable. Next step: translate forecast trajectories into hedge recommendation framework — specifying when to place/lift a hedge given specific cost structure and risk tolerance.

## References

- Adekunle et al. (2025). ASAS-CSAS Annual Meeting, Hollywood, FL.
- CME Group. (2024). Feeder Cattle Futures and Options.
- USDA. (2025). Cattle on Feed Report.
- Yahoo Finance. (2024). GF=F ticker data.

## Links
- [[research-tracker]] — FEDVT research overview
- [[paper-outline]] — Paper 1 full outline
- [[Literature Summaries.pdf]] — source PDF (literature review)
