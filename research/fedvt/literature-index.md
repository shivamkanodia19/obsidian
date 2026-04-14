---
title: FEDVT Literature Index — 20 Sources
type: research
status: complete
last-updated: 2026-04-13
tags: [fedvt, feedlot, literature, sources, citations]
---

# FEDVT Literature Index

20 verified sources. Full summaries from Literature Summaries.pdf. Section placement corrected against source document.

---

## Section 1 — Introduction

- **Dennis & Schroeder (2023)** — Kansas Focus on Feedlots data Jan 2015–Dec 2023. Net returns swung +$457 to -$489/head over the period. Feed price changes drive both direct costs and biological performance via substitution effects (feed conversion, ADG, days on feed). *JAAE 55(4), 546–566.*
- **Langemeier, Schroeder & Mintert (1992)** — 98% of profit variability explained by 6 variables: fed cattle price, feeder price, corn price, interest rates, feed conversion, ADG. Used standardized regression coefficients. Placement weight affects which variables dominate. *JAAE 24(2), 41–47.*
- **Bang, Laugen & Dreyer (2023)** — Systematic review of 110 DSS studies for beef/dairy (2016–2022). Gap between model complexity and on-farm usability is the most persistent problem; most tools never move beyond proof-of-concept. *ITOR 30(5), 2214–2244.*
- **Awasthi et al. (2024)** — Systematic review of 105 beef production simulation studies through June 2023. Most models are deterministic and dynamic; <50% include formal validation. Excel, R, Python, STELLA most common. Inconsistent reporting limits adoption. *Animals 14(11), 1632.* → Also Section 2.
- **Flores et al. (2017)** — Analytics-based DSS predicting individual animal growth and optimal slaughter timing using ultrasound backfat, marbling, and feeding data. Individual-animal level (contrast: FEDVT is enterprise-level). *Computers and Electronics in Agriculture 143, 273–285.* → Also Section 2.
- **Stika (2025)** — Python simulation on Kansas feedlot data. Optimal placement: ~704 lbs, 166 days on feed, ~$119/head net return. Feeder price and feed cost dominate sensitivity results. *KSU thesis.* → Also Section 2.
- **Lawrence, Wang & Loy (1999)** — 1,600+ pens across 220+ Midwest feedlots. Sex, placement weight, facility design, and placement season all significantly affect net returns beyond price variables alone. Justifies FEDVT's 65-parameter breadth. *JAAE 31(2), 349–357.* → Primary cite Section 3.
- **Mark, Schroeder & Jones (2000)** — Two western Kansas feedlots. Price risk dominates overall; performance risk proportionally larger for fall placements and lighter cattle. Standardized beta coefficients across placement scenarios. *Journal of Agribusiness 18(3), 331–344.* → Also Section 4.

---

## Section 2 — Background and Literature Review

- **Bina & Schroeder (2022)** — Weekly auction data from 32 U.S. feeder cattle markets (1992–2021). Feeder cattle market volatility significantly influences basis risk. Basis peaked 2014–2015, declined by 2018 but remains elevated. Lot characteristics, seasonality, and regional conditions all contribute. Supports need for operation-specific tools over national signals. *JAAE 54(1), 1–21.*
- **Coffey, Tonsor & Schroeder (2018)** — Basis prediction errors for live cattle across 5 USDA Mandatory Livestock Price Reporting regions. Cost-of-gain volatility and delivery cost variation drive hedging difficulty more than price momentum. Results differ significantly by region → local conditions matter more than national signals. **⚠️ DOI in source PDF (10.1017/aae.2018.31) is incorrect — that's a Cambridge/JAAE prefix. Paper is published in JARE; use jareonline.org link.** *JARE 43(1), 18–33.*
- **Herrington & Tonsor (2013)** — Kansas Focus on Feedlots dataset, multi-decade span. ADG and feed conversion efficiency improved over time (genetic/nutritional advances), but margin volatility did not decrease. Feedlot complexity grew; static tools did not keep pace. Core knowledge gap citation. *The Professional Animal Scientist 29(4), 435–442.*
- **Dixon et al. (2022)** — Scoping review of 113 feedlot trials from 91 peer-reviewed articles. Only 28% of trials fully reported economic outcomes, methodology, prices, and data sources together. Eight economic assessment types identified; break-even and partial budgeting most practically relevant. Validates FEDVT's deterministic BEP design. *Translational Animal Science 6(3), txac077.* → Also Section 5.
- **Bang, Laugen & Dreyer (2023)** — See Section 1. Primary positioning citation for Section 2. Most important citation establishing the gap FEDVT fills.
- **Karle, Toth & White (2017)** — Multi-market partial equilibrium model of U.S. ag industry. NAHMS data: 21.2% of placed cattle (2.29M head) affected by BRD annually; direct treatment cost $23.60/case. BRD causes ~45–55% of all feedlot deaths. Market-level analysis shows reduced BRD benefits consumers (lower beef prices) but partially offsets producer gains. *Frontiers in Veterinary Science 4, 189.*
- **Blakebrough-Hall, McMeniman & González (2020)** — 898 crossbred steers through Australian feedlot. 18% morbidity rate, 2.1% BRD mortality rate. Cattle treated 3+ times: 39.6 kg lighter carcasses, AUD $385 less/head. Subclinical BRD (lung lesions at slaughter, no treatment record): AUD $67 less/head. BRD costs often invisible to pen-level tracking. *Journal of Animal Science 98(2), skaa045.* → Primary cite Section 4 (disease scenario).
- **Feuz, Feuz & Johnson (2021)** — ML models (logistic regression, decision trees, random forest, KNN, naïve Bayes) trained on 4,400+ cattle for mortality prediction and culling decisions. Logistic regression: 95.6% accuracy. Net return improvement: $14.01/head (standard) → $45.27/head (cost-sensitive learning), <1% loss probability. *JARE 46(2), 242–255.* → Also Section 4.
- **Awasthi et al. (2024)** — See Section 1. Cite in Section 2 for standardized tool justification.
- **Flores et al. (2017)** — See Section 1. Cite in Section 2 to establish analytics-in-feedlots precedent.
- **Stika (2025)** — See Section 1. Cite in Section 2 as recent peer-reviewed parallel to FEDVT's approach.
- **Harrison (2022)** — Davis Growth Model applied to 120 Angus-cross steers (automated + conventional feeding). Modern cattle have higher maintenance energy than historical models suggest. Cost and profit curves for optimal harvest timing; sorting by predicted days-on-feed improves carcass uniformity and reduces overfeeding costs. *ProQuest Diss. 29995958.* → Also Section 5.

---

## Section 3 — Materials and Methods

- **Lawrence, Wang & Loy (1999)** — Primary citation for parameter selection breadth. See Section 1.
- **Dhuyvetter & Schroeder (2000)** — Canadian feeder cattle auction data. Price-per-pound declines as weight increases; price slide steepens with high feed costs (heavier cattle carry more cost risk). Provides empirically estimated slide coefficients for break-even calculations. Directly relevant to FEDVT's feeder cattle cost parameterization (~86% of total cost). *CJAE 48(3), 299–310.*

---

## Section 4 — Results

- **Mark, Schroeder & Jones (2000)** — See Section 1/2. Cite in sensitivity analysis discussion.
- **Blakebrough-Hall et al. (2020)** — Primary BRD benchmarks for disease outbreak scenario. See Section 2.
- **Feuz et al. (2021)** — Per-head dollar figures for health decisions context. See Section 2.
- **Dennis & Schroeder (2023)** — Validates feed cost sensitivity scenarios with real recent data. See Section 1.

---

## Section 5 — Discussion

- **McKendree, Tonsor & Schulz (2021)** — Split-sample choice experiment surveying feedlot operators on joint management of price risk and animal health risk. Operators sourcing from single known ranch less likely to rely exclusively on spot markets → risk strategies are complementary, not independent. Rare empirical data on actual operator behavior. Validates FEDVT's multi-scenario design. *JAAE 53(1), 75–93.*
- **Dixon et al. (2022)** — See Section 2. Cite in Discussion for economic transparency argument.
- **Harrison (2022)** — See Section 2. Cite for precision livestock / IoT integration future work.

---

## Section 6 — Conclusion and Future Work

- **Tonsor & Schroeder (2011)** — Operators simultaneously exposed to live cattle, feeder cattle, and corn price risk, yet most tools model these independently. Multivariate simulation of joint price distribution significantly outperforms univariate approaches. Directly motivates FEDVT's next development phase. *Applied Economics 43(11), 1329–1339.*
- **Rahmani, Khatami & Stephens (2024)** — ARIMA/SARIMA/SARIMAX vs. SVR/random forest/AdaBoost for fed steer prices (Alberta, 2005–2023). Random forest and AdaBoost outperform univariate models. Probabilistic layer added to generate prediction intervals rather than point estimates. *Sustainability 16(5), 1789.*

---

## Known Citation Issues

1. **Coffey et al. (2018)**: DOI in Literature Summaries PDF (`10.1017/aae.2018.31`) is a Cambridge/JAAE prefix — incorrect for a JARE paper. Verify DOI before submission; use jareonline.org record.
2. **Blakebrough-Hall et al. (2020) figures are in AUD**, not USD. Do not present as USD in the paper. If using in scenarios, convert or note currency.
3. **Stika (2025) is a thesis**, not a peer-reviewed journal article. Some journals restrict thesis citations. Check AJAE submission guidelines.

---

## Links
- [[research-tracker]] — FEDVT research overview
- [[paper-outline]] — Full paper structure
- [[working-paper]] — ASAS 2025 working paper
- [[introduction-v3]] — Current introduction draft
