---
description: "Navigation hub for prediction markets"
title: Prediction Markets Index
project: prediction-markets
strategic: true
scope: prediction-markets/nba-workflow
status: active
agent_context: true
surface_in_root: true
current_focus:
  - use the NBA framework only when estimated edge beats price after risk and fees
  - keep the Kalshi validation log current when live contract reasoning changes
active_tasks:
  - price contracts with skepticism instead of betting because an outcome feels likely
  - separate same-day memo work from reusable framework rules
prompt_context:
  - "[[02_Analyst/prediction-markets/NBA-MARKET-FRAMEWORK]]"
  - "[[02_Analyst/prediction-markets/kalshi-validation-log]]"
definition_of_done:
  - contract reasoning includes market price, injury/news context, and pass discipline
  - framework rules stay distinct from date-specific memos
blocked_by:
  - no-bet discipline fails if the market price is not compared against estimated probability
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-05-21
tags: [prediction-markets, nba, betting, research]
---

# Prediction Markets Index

## Active Framework

- [[NBA-MARKET-FRAMEWORK]] - research stack, agent debate template, and bankroll rules for NBA contracts
- [[kalshi-validation-log]] - Kalshi Austin high-temp validation log and contract reasoning notes

## Daily Memos

- [[NBA-2026-04-21]] - Apr 21 NBA slate, agent debate, fair-price thresholds, and pass list
- [[NBA-2026-04-23]] - Apr 23 NBA slate and best same-day contract pricing
- [[NBA-2026-04-28]] - Apr 28 NBA slate, multi-agent bet calibration, and consensus thresholds
- [[NBA-2026-04-30]] - Apr 30 live Timberwolves-Nuggets closeout read driven by possession edges
- [[NBA-2026-05-02]] - May 2 live Sixers-Celtics memo after Tatum's absence reshaped the comeback path
- [[NBA-2026-05-03]] - May 3 Magic-Pistons Game 7 memo with Cade PRA and under leans

## Operating Rule

Use market price, sportsbook consensus, injury/news context, statistical forecasts, liquidity, settlement terms, and a skeptic pass before buying a contract. Do not buy only because the outcome is likely; buy only when estimated probability beats the market price after risk and fees.
