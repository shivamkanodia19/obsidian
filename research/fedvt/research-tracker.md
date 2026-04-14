---
title: FEDVT — Feedlot Economic Decision and Valuation Tool
type: research
status: in-progress
last-updated: 2026-04-13
advisor: Dr. Kaniyamattam
institution: Texas A&M
paper-1-status: poster-presented, not-yet-published
paper-2-status: scoped, not-started
tags: [research, agriculture, economics, ML, forecasting, cattle]
---

# FEDVT Research Overview

## What it is
Undergraduate research coauthoring papers on feedlot cattle economics and futures forecasting with advisor Dr. Kaniyamattam at Texas A&M. The project is called FEDVT (Feedlot Economic Decision and Valuation Tool).

## Paper 1: Excel/VBA Cost Modeling Framework
The first paper documents a dual-platform economic modeling tool built in Microsoft Excel with VBA macros, paired with Tableau for visualization.

### Architecture
- Excel/VBA = the calculator and data repository. All cost modeling lives here.
- Tableau = interactive visualization front-end that reads from Excel outputs
- Google Sheets = middleware carrying live CME futures prices from a Python/yfinance API into Tableau
- Data pipeline: CME → Yahoo Finance API → Python → Google Sheets → Tableau

### The 5-Stage Excel Workflow
Input → Details → Analysis → Summary → Dashboard
Each stage maps to a separate worksheet tab. VBA macros cascade recalculations across all stages when any input changes.

### 65 Inputs Across 6 Cost Categories
1. Feeder Costs (~86% of total cost): purchase price, buying commission, insurance, trucking
2. Feed Costs: 10 parameters, each with price × daily consumption rate × days fed
3. Fixed Costs: 15 capital items, each running straight-line depreciation divided by feedlot capacity
4. Labor: hours per head × rate per hour
5. Interest: operating interest on variable costs, investment interest on fixed assets
6. Other Costs: 24 parameters covering vet, fuel, utilities, marketing, death loss, etc.

### Core Formulas
- TG = TFW - ASW (total gain)
- DTF = TG / RoG (days to finish)
- TC = sum of all 6 cost categories
- BEP = (TC / TFW) × 100 + FB (break-even price, primary output)
- Profit per Head = (Live Price - BEP) × TFW / 100

BEP is the most important output. It tells a feedlot operator the minimum $/cwt needed to break even against live CME futures price.

### Status
In progress. Poster presented at Student Research Week. Paper not yet published.

## Paper 2: ML Forecasting Models
Scoped but separate from Paper 1. Incorporates SARIMA, LSTM, and XGBoost models for futures price forecasting. Tableau and ML components are the focus. Not yet started.

## Advisor
Dr. Kaniyamattam, Texas A&M

## Links
- [[paper-outline]] — Paper 1 full outline
- [[working-paper]] — ASAS-CSAS working paper synthesis
- [[resume-current]] — resume (FEDVT research entry)
