---
title: NBA Prediction Market Framework
project: prediction-markets
strategic: true
status: active
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-04-21
tags: [prediction-markets, nba, framework, bankroll]
---

# NBA Prediction Market Framework

Status: active framework for basketball market research.
Primary rule: never buy a contract only because the team is likely to win. Buy only when estimated probability is meaningfully above the market-implied probability after fees, spread, liquidity, and correlation.

## Research Stack

For each NBA contract, collect:

1. Market price and liquidity: contract price, bid/ask, volume, settlement terms, and whether the contract maps cleanly to the event.
2. Sportsbook consensus: moneyline, spread, total, movement, and implied probability after removing vig.
3. Statistical forecasts: team ratings, matchup projections, injury-adjusted models, and rest/travel context.
4. Analyst/news context: injuries, rotations, coaching comments, beat-writer reports, Game 1 adjustments, and series incentives.
5. Risk controls: maximum stake, correlation with other contracts, downside if late injury news flips the setup.

## Agent Debate Template

Use multiple agents when researching meaningful wagers:

- Market Agent: gathers prediction-market prices, sportsbook odds, spread/total movement, liquidity, and fees.
- Stats Agent: gathers statistical forecasts, matchup numbers, team strength, pace, net rating, recent form, and implied probabilities.
- News/Injury Agent: gathers official injury reports, beat-writer updates, rest/travel, lineup changes, and analyst previews.
- Skeptic Agent: tries to kill every candidate by finding stale lines, bad settlement assumptions, missing injuries, overfitting, or low-liquidity traps.
- Synthesis Agent: ranks contracts by expected value and risk-adjusted sizing.

## Bankroll Rules

- Keep NBA prediction-market bankroll separate from stock portfolio.
- Default stake: 0.25%-1.0% of prediction-market bankroll per contract.
- Strong edge only: 1.0%-2.0%.
- Never place multiple correlated bets as if they are independent.
- Avoid thin contracts unless the edge is very large and settlement terms are clear.
- Log every entry with price, fair probability, thesis, source links, and result.

## Decision Format

| Rank | Contract | Market Price | Fair Probability | Edge | Confidence | Max Stake | Why |
|---|---|---:|---:|---:|---|---:|---|

## Red Flags

- Injury news not checked within the last 60 minutes before tip.
- Contract wording does not match the intended bet.
- Bid/ask spread eats the entire edge.
- Recommendation relies on a single analyst take.
- Model edge contradicts closing sportsbook market without a clear reason.
- Same-game correlated exposure exceeds planned stake.
