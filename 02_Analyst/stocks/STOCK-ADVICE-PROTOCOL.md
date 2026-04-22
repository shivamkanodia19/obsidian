---
title: Stock Advice Protocol
project: stocks
strategic: true
status: stable
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-04-21
tags: [stocks, portfolio, yahoo-finance, investing-protocol]
---

# Stock Advice Protocol

## Mandatory Data Rule

User instruction from 2026-04-21:

Every time the user asks for stock or portfolio advice, check Yahoo Finance first for the absolute latest available quote, chart context, financial data, and news.

If Yahoo Finance is unavailable, blocked, or visibly delayed, say that explicitly before using backup sources such as company investor relations, SEC filings, Nasdaq, market data APIs, broker screenshots, or reputable financial news.

## Recommendation Format

For any stock advice response, separate:

1. Latest Yahoo Finance data checked.
2. Current news, earnings dates, filings, and catalysts.
3. Fundamental quality and balance sheet context.
4. Market mechanics, technical setup, squeeze risk, or event risk.
5. Portfolio fit and position-sizing risk.
6. Practical action: add, hold, trim, exit, wait, or avoid.

## Portfolio Bias

Do not give stale stock advice. Use current market data every time.

For high-volatility names, especially short squeezes, event trades, biotech catalysts, micro-caps, and earnings gaps, default to risk control first. If the upside is mostly market mechanics rather than fundamentals, label it as a trade rather than a core holding.

## Related Notes

- [[PORTFOLIO-SNAPSHOT-2026-04-21]]
- [[PORTFOLIO]]
- [[PORTFOLIO-DECISIONS]]
