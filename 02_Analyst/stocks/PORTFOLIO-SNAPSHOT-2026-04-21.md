---
title: Portfolio Snapshot - 2026-04-21
project: stocks
strategic: true
status: snapshot
scope: stocks/portfolio-state
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-04-21
as_of: 2026-04-21
tags: [stocks, portfolio, robinhood, screenshot]
---

# Portfolio Snapshot - 2026-04-21

Status: original Robinhood screenshot snapshot. Use [[PORTFOLIO-REFRESH-2026-04-29]] for the latest known portfolio-state note in the vault.
Context: User invested in everything today except LMT, ASML, USO, and TSM.

## Visible Invested Value

The screenshot shows per-share prices and share counts, not position values. Reconstructed value is `shares * shown price`.

| Ticker | Shares | Screenshot Price | Reconstructed Value | Bought Today? |
|---|---:|---:|---:|---|
| LMT | 0.567249 | $574.51 | $325.89 | No |
| ASML | 0.084667 | $1,473.33 | $124.74 | No |
| TSM | 0.262240 | $370.54 | $97.17 | No |
| STM | 1.670000 | $45.03 | $75.20 | Yes |
| TSLA | 0.128020 | $392.54 | $50.25 | Yes |
| COF | 0.238894 | $207.89 | $49.66 | Yes |
| USO | 0.393251 | $121.98 | $47.97 | No |
| CAR | 0.070423 | $645.78 | $45.48 | Yes |
| **Total Visible Invested** |  |  | **$816.37** |  |

Live quote check during Codex review put the same visible shares at about $818.98, so the screenshot was close to current market value.

Important caveat: this is visible invested value only. It does not include any Robinhood cash, buying power, unsettled funds, or positions below the visible portion of the list. The prior vault snapshot listed $40.48 buying power, so total account value may be roughly $856-$862 if that cash is still present.

## News-Driven Strategy Rule

Future portfolio advice must follow [[STOCK-ADVICE-PROTOCOL]]. Check Yahoo Finance first for the absolute latest available quote, chart context, financial data, and news. If Yahoo Finance is unavailable or delayed, say that before using backup sources.

Future portfolio advice must reference current news and primary context before recommendations. Separate:

1. Confirmed facts: earnings dates, filings, company releases, settlement rules, official injury reports.
2. Market context: short squeezes, macro/geopolitics, rates, oil, sector rotation, analyst revisions.
3. Inference: what the facts imply for sizing, timing, risk, or whether to avoid a contract/trade.

## Current Event Map

| Ticker | Current Event Lens | Strategy Implication |
|---|---|---|
| LMT | Reports Q1 2026 before market open on 2026-04-23. FY2025 had $75.0B sales, $6.9B FCF, and $194B backlog. | Position is too large for a single earnings event. Trim toward 28-30% of invested value before earnings if day-trade/PDT and spreads allow. |
| ASML | Q1 2026 reported EUR8.8B net sales, 53.0% gross margin, EUR2.8B net income, and raised 2026 sales guidance to EUR36B-EUR40B. | Quality semi anchor, but do not chase after strength. |
| TSM | Q1 2026 revenue $35.90B, +40.6% YoY in USD; Q2 guide $39.0B-$40.2B, gross margin 65.5%-67.5%. | Strong AI foundry thesis; hold, no add unless pullback improves entry. |
| STM | Reports Q1 2026 on 2026-04-23 before European market open. | New position has near-term earnings risk. Do not add before the event. |
| TSLA | Q1 2026 results due 2026-04-22 after close. Q1 production 408,386 vs deliveries 358,023, with 8.8 GWh storage deployed. | Keep tiny only; event risk and inventory gap make this a speculative position. |
| COF | Q1 2026 earnings scheduled 2026-04-21 after close. Discover acquisition completed 2025-05-18, creating integration and credit-quality watch items. | Hold tiny through event only if comfortable with earnings gap risk. |
| USO | Futures-based oil product. January 2026 onward roll period shortened to five days; roll/contango mechanics can affect returns. | Tactical hedge only, not a permanent oil investment. Keep small. |
| CAR | Current move is being driven by short-squeeze dynamics, high short interest, concentrated ownership, and volatile market mechanics. | Treat as a trade, not a core holding. Consider shrinking or exiting when possible. |

## Immediate Portfolio Call

Best risk-adjusted action after the screenshot:

- Do not add more today.
- Raise cash first.
- Trim about $75-$90 of LMT, roughly 0.13-0.16 shares at the checked price range, to bring LMT closer to 28-30%.
- Keep ASML and TSM as quality semi exposure.
- Do not add to STM, TSLA, COF, or LMT before their earnings events.
- Keep USO capped around 4-6%.
- Keep CAR capped around 0-3% unless explicitly treating it as a momentum gamble.

Target post-cleanup allocation:

| Sleeve | Target |
|---|---:|
| LMT | 28-30% |
| ASML + TSM | 25-30% |
| STM | 5-7% |
| TSLA | 5-7% |
| COF | 5-7% |
| USO | 4-6% |
| CAR | 0-3% |
| Cash | 12-18% |

## Sources Checked

- ASML Q1 2026 results: https://www.asml.com/en/news/press-releases/2026/q1-2026-financial-results
- TSMC Q1 2026 results: https://investor.tsmc.com/english/quarterly-results/2026/q1
- Tesla Q1 2026 production/deliveries and earnings timing: https://ir.tesla.com/press-release/tesla-first-quarter-2026-production-deliveries-and-deployments
- Lockheed Martin Q1 2026 earnings timing: https://news.lockheedmartin.com/2026-04-01-Lockheed-Martin-Announces-First-Quarter-2026-Earnings-Results-Webcast
- Lockheed Martin FY2025 results: https://news.lockheedmartin.com/2026-01-29-Lockheed-Martin-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results
- STMicroelectronics Q1 2026 earnings timing: https://newsroom.st.com/media-center/press-item.html/c3390.html
- Capital One Q1 2026 earnings timing: https://investor.capitalone.com/news-releases/news-release-details/capital-one-financial-corporation-webcast-conference-call-83
- Capital One completes Discover acquisition: https://ir-capitalone.gcs-web.com/static-files/cf27ad75-15b9-49f4-8c44-7f0d4fde0ec9
- USO prospectus supplement / roll mechanics: https://secure.alpsinc.com/MarketingAPI/api/v1/Content/uscfinvestments/united-states-oil-fund-pro-20251230.pdf
- CAR short-squeeze context: https://www.investing.com/news/stock-market-news/avis-budget-stock-surges-on-short-squeeze-dynamics-4625811
- FINRA day trading rule: https://www.finra.org/investors/investing/investment-products/stocks/day-trading
- Robinhood pattern day trading: https://robinhood.com/support/articles/pattern-day-trading/
