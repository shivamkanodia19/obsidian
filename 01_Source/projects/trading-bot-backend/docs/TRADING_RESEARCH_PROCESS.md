# TRADING_RESEARCH_PROCESS.md

## How Quant Researchers Think

This is not a "secret formula" — it's a disciplined process that most retail traders skip,
which is why most retail traders lose money.

### The 10-Step Process

1. **Hypothesis**
   "I believe X relationship exists in the data."
   Must be falsifiable. Must have a plausible causal mechanism (not just correlation).
   Example: "Fed rate cut probability on Kalshi is systematically underpriced 2 weeks before FOMC."
   Not example: "SPY goes up when I feel bullish."

2. **Data**
   What data would confirm or deny the hypothesis?
   Where does it come from? How fresh is it? Is it survivorship-biased?
   If you can't get the data, you can't test the hypothesis.

3. **Features**
   What specific signals encode the hypothesis?
   Example: Kalshi YES price vs. CME Fed Funds futures implied probability, 14 days before event.
   Features must be computable from available data.

4. **Backtest**
   Test the hypothesis on historical data.
   Use out-of-sample validation (don't test on the same data you used to design the feature).
   A backtest that only looks good in-sample is worthless — it's just memorization.

5. **Transaction Costs / Spreads**
   Most retail backtests ignore spread cost. This is fatal.
   On Kalshi: typical spread is 2-5 cents on a $1 contract. On thin markets, 10-20 cents.
   On equities: add commission + spread. For small positions, this dominates.
   If your edge is smaller than your spread cost, you have no edge.

6. **Risk**
   What is the maximum drawdown? What is the worst case?
   Does the strategy blow up in specific regimes?
   What is the Kelly criterion position size? (And then trade a fraction of it.)

7. **Paper Trading**
   Implement exactly as you would in live trading.
   Use real market prices, not theoretical fills.
   Track every trade. Minimum 30-50 trades for statistical signal.

8. **Small Live Deployment**
   Start with minimum possible size.
   Verify that real fills match paper fills.
   Verify that the edge is still present (markets adapt).

9. **Monitoring**
   Is the strategy still working? Is the edge decaying?
   What changed in market conditions since the backtest?
   Have transaction costs changed?

10. **Kill or Scale Decision**
    If positive expectancy is holding: scale up carefully.
    If edge is gone: kill the strategy. Don't "average down" on a broken thesis.
    Sunk cost fallacy kills more trading accounts than bad strategies.

---

## Applying This to Kalshi

**What makes Kalshi interesting:**
- Binary outcomes — easier to reason about than equity prices
- Clear settlement criteria (if you read them carefully)
- Potential for informational edge if you have better priors than the market

**What makes Kalshi hard:**
- Very thin liquidity on most contracts
- Spreads of 3-15% are common — this kills most strategies
- Market resolves at 0 or 1 — no partial recovery
- Settlement ambiguity is real (read the criteria carefully, every time)
- Small market size means your own trades move the price

**Realistic edge sources (hypotheses worth testing):**
1. "Public prediction models systematically underestimate tails"
2. "Institutional traders on CME are better calibrated than Kalshi retail on Fed policy"
3. "Near-expiry YES contracts at 70-90% are systematically overpriced vs. true probability"
4. "Macro surprise index has predictive power for Kalshi economic markets"

**Not realistic edges:**
- "I think the Fed will cut" (everyone has an opinion; you need an advantage)
- "ChatGPT says 80% probability" (ChatGPT has no special macro insight)

---

## Applying This to Robinhood (Equities)

**The hard truth:**
Equity markets are among the most competitive in the world. Retail traders systematically
lose to algorithmic market makers and institutional traders on short time horizons.

**Where retail might have edge:**
- Long time horizons (months/years) where institutional pressure is lower
- Small-cap stocks where institutional coverage is sparse
- Fundamental research that is more thorough than consensus
- Position sizing and behavioral discipline (not overtrading, not panic selling)

**Where retail definitely doesn't have edge:**
- Day trading liquid large-caps against HFT
- Predicting short-term earnings surprises
- "Technical analysis" without backtested statistical evidence
- Following social media sentiment

**The correct V0 approach:**
Use the system to track your thesis quality over time.
After 30-50 paper trades, ask: was my research actually informative?
Did the setup I identified actually play out?
Only proceed to live trading if the answer is consistently yes.
