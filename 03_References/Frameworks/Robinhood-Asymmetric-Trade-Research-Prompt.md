---
title: Robinhood Asymmetric Trade Research Prompt
project: references
strategic: true
status: active
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-05-06
tags: [codex, prompts, robinhood, crypto, stocks, research]
---

# Robinhood Asymmetric Trade Research Prompt

Reusable prompt for deep research on Robinhood-tradable crypto and stock ideas, with explicit tradability checks, catalyst work, tokenomics/fundamentals, bear-case analysis, and execution planning.

## Master Prompt

```text
You are Codex acting as a multi-agent research team.

Objective: Find the best asymmetric high-upside trades I can actually place on Robinhood, prioritizing crypto. If crypto opportunities are weak, overhyped, or not currently tradable on Robinhood, include stocks instead and let the stronger ideas win. I want deep research, not cheerleading.

Default assumptions if I do not specify them:
- Location: United States
- State: unknown, so flag any state restrictions separately, especially New York and Texas
- Account size: $5,000
- Holding period: 2 weeks to 6 months
- Risk tolerance: aggressive but not reckless
- Instrument set: spot crypto and common stocks only, no options unless I explicitly ask

Hard rules:
- Use current data only and cite exact dates in the report.
- Verify Robinhood tradability with official Robinhood sources before recommending any asset.
- Exclude anything that is only viewable or has market data on Robinhood but is not currently tradable.
- Prefer liquid names that a retail trader can realistically enter and exit.
- Do not use influencer content, Reddit threads, Telegram chatter, or X posts as core evidence.
- Use primary sources first: Robinhood official pages, SEC filings, investor relations pages, earnings materials, project docs, token docs, on-chain sources, exchange filings, reputable market data providers.
- Use probability-weighted language. Do not promise gains.
- If no setup is strong enough, say that clearly and return a watchlist instead of forcing picks.

Use multi-agent reasoning:
If sub-agents are available, run these workstreams in parallel. If not, emulate them sequentially.

Agent 1: Robinhood Tradability and Universe Builder
- Build the investable universe from currently tradable Robinhood crypto first.
- Separate tradable assets from market-data-only assets.
- Note state restrictions and platform limitations.
- For stock fallback, focus on US-listed names that Robinhood supports.

Agent 2: Catalyst Hunter
- Find 30, 90, and 180 day catalysts that could drive repricing.
- For crypto: token launches, major upgrades, ETF or treasury demand, ecosystem growth, listings, unlock changes, regulatory shifts, partnerships, fee growth, user growth.
- For stocks: earnings revisions, product launches, major contracts, guidance changes, sector tailwinds, balance-sheet inflections, index inclusion, AI/crypto exposure, short squeeze conditions only if fundamentals do not look broken.

Agent 3: Fundamental and Tokenomics Analyst
- For crypto: circulating supply, FDV, unlock schedule, insider and VC overhang, token utility, fees, revenue, developer activity, active users, treasury health, concentration risk.
- For stocks: revenue growth, margins, cash flow, debt, dilution risk, valuation versus peers, estimate revisions, insider activity, balance-sheet quality.

Agent 4: Market Structure and Technicals
- Study trend, relative strength, volume expansion, liquidity, volatility, key support and resistance, breakout quality, and whether momentum is sustainable.
- Reject illiquid traps unless clearly labeled speculative and still tradable.

Agent 5: Bear Case and Risk Agent
- Write the strongest case against each candidate.
- Check for fraud risk, governance issues, regulatory risk, unlock overhang, customer concentration, accounting concerns, dilution, security issues, or narrative fragility.

Agent 6: Portfolio and Execution Agent
- Build a practical trading plan with entry ranges, invalidation levels, scaling plan, position sizing, and risk-reward.
- Keep correlation in mind so the final list is not just five versions of the same bet.

Research process:
1. Build a broad shortlist.
2. Cut it to the top 8 after tradability and liquidity checks.
3. Deep-dive the top 5.
4. Rank the final 3 to 5 best opportunities.
5. Include a separate reject list showing what looked exciting but failed scrutiny.

Output format:
1. Executive summary
- Best 3 to 5 opportunities ranked from strongest to weakest
- One sentence on why each made the list now

2. Comparison table
Columns:
- Rank
- Asset
- Crypto or stock
- Robinhood tradable now
- Source for tradability
- Key catalyst
- Time horizon
- Bull case
- Bear case
- Liquidity quality
- Risk level
- Entry zone
- Invalidation level
- Base case return estimate
- High-upside scenario
- Confidence score out of 10

3. Deep dives
For each final candidate include:
- What the asset is
- Why it could outperform sharply
- What must happen for the thesis to work
- What could break the thesis
- Why now instead of later
- Specific catalysts with dates where available
- Evidence from sources
- A concrete trading plan

4. Reject list
- Names rejected because they were not Robinhood tradable, too illiquid, too crowded, too promotional, or had poor risk-reward

5. Final action plan
- Best single idea
- Best lower-risk idea
- Best speculative flyer
- Best stock if crypto is not attractive
- What to monitor over the next 7, 30, and 90 days

Extra instructions:
- Prefer quality asymmetric opportunities over meme-heavy garbage.
- However, if a meme or narrative-driven asset truly has strong market structure, liquidity, and a catalyst, you may include it, but label it clearly as speculative.
- Be willing to conclude that stocks currently offer better upside than crypto if that is what the evidence says.
- Every recommendation must include at least one official tradability source and multiple current supporting sources.
- Use exact dates, not words like "recently" or "soon."
```

## Companion Workstreams

### Crypto catalysts plus tokenomics

```text
Workstream: Crypto catalysts + tokenomics. Date anchor: May 6, 2026 US. Research only Robinhood-tradable crypto from the official Robinhood Coin availability page. Focus this shortlist unless evidence strongly suggests swapping one: HYPE, ONDO, SUI, SYRUP, AERO, SOL, ENA, AAVE. For each, use primary sources first (official project docs/blogs, token docs, governance, project dashboards) plus reputable current market/on-chain data providers if needed. Find 30/90/180-day catalysts with exact dates where available, token utility, supply/circulating/FDV, unlock/overhang, fee/revenue/user growth, and current risks. Output: ranked top 5 crypto candidates, a short reject list, and source links with exact dates. Do not use Reddit, X, Telegram, or influencer content.
```

### Bear case plus market structure

```text
Workstream: Bear case + market structure. Date anchor: May 6, 2026 US. For this candidate list: HYPE, ONDO, SUI, SYRUP, AERO, SOL, ENA, AAVE, HOOD, COIN, MSTR. Build the strongest case against each and assess market structure/liquidity using reputable current sources. Look for unlock overhang, insider/VC concentration, governance/regulatory/security issues, accounting or dilution concerns, customer concentration, and whether momentum looks sustainable versus overextended. Output: top warning flags by asset, any names that should be cut, and a ranking of the cleanest setups versus the most dangerous traps, with source links.
```

### Stock fallback ideas

```text
Workstream: Stock fallback ideas tradable on Robinhood. Date anchor: May 6, 2026 US. Focus US-listed common stocks with crypto/AI/high-beta upside suitable for 2 weeks to 6 months and realistic for a $5,000 account. Start with HOOD, COIN, MSTR, CLSK, IREN, CRWV, NVDA, and any one stronger substitute if evidence supports it. Use official IR pages, SEC filings, earnings materials, and reputable current market data only. For each: verify Robinhood tradability from official Robinhood pages if possible, identify 30/90/180-day catalysts with exact dates where available, valuation/fundamentals, liquidity, bear case, and rank top 3 stock fallback names. Exclude broken or illiquid stories. Output structured findings with links.
```

## Why Keep It

The 2026-05-06 session cluster produced a useful reusable research scaffold, not a clean final trade memo. This note preserves the scaffold so it can be reused with up-to-date browsing later.
