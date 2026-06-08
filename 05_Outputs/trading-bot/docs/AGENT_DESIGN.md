# AGENT_DESIGN.md

## What LLM Agents Are (And Are Not)

**They are:**
- Structured reasoning tools that process text and return formatted output
- Useful for synthesizing information, generating hypotheses, and writing critiques
- Good at identifying what questions to ask

**They are not:**
- Trained traders
- Predictive models
- Sources of alpha
- Reliable fact-checkers (they hallucinate)
- Decision-makers (code is the decision-maker)

An LLM that produces a compelling trade thesis is not evidence that the trade is good.
It is evidence that the thesis sounds plausible given the LLM's training data.
Plausible ≠ profitable.

## Agent Roles

### 1. Research Agent
- Reads a symbol/market and returns structured research
- Does NOT recommend trades
- Must flag stale data and settlement ambiguity
- Output feeds Strategy Agent

### 2. Strategy Agent
- Converts research into a trade proposal with specific parameters
- Must say "no setup" if research doesn't support a trade
- The distinction between "interesting idea" and "tradeable setup" is enforced in the prompt

### 3. Risk Agent
- Adversarial reviewer — looks for reasons NOT to trade
- Not the final gate (code is)
- Identifies categories of risk the code can't check (narrative risk, thesis quality)

### 4. Execution Agent
- Mechanical ticket generator
- Does NOT evaluate whether a trade is good
- Always sets requires_user_confirmation=true
- Blocked by risk engine before any ticket is valid

### 5. Review Agent
- Post-mortem analyst
- Separates thesis accuracy from execution quality
- Tracks patterns across trades over time

### 6. Skeptic Agent
- Adversarial system-level challenger
- Challenges the entire premise of a trade and the system
- Rewrites "profitable in all markets" as "positive expectancy in specific regimes"
- Runs independently of other agents

## How Agents Are Called

All LLM calls go through `src/agents/agent_runner.py`:
1. Load prompt from `src/agents/prompts/<agent_name>.md`
2. Format user message with structured context
3. Call Anthropic Claude API
4. Parse JSON response
5. Return parsed dict for Pydantic model construction

There is no fine-tuning, no RLHF, no special training. These are vanilla Claude API calls
with carefully designed system prompts. The quality of output depends entirely on prompt
quality and input data quality.

## Prompt-Based vs. ML Models

This system uses prompt-based agents, not trained ML models. The difference matters:

| Prompt-based agents | ML prediction models |
|---|---|
| Reason about current context | Learn from historical patterns |
| Good at synthesis and critique | Good at pattern recognition |
| Hallucinate when uncertain | Overfit when data is small |
| Easy to debug (read the prompt) | Hard to debug (interpret the weights) |
| No historical data required | Require substantial labeled data |
| No alpha by themselves | May have alpha if features are predictive |

V4 will explore ML scoring. V0-V2 use prompt-based agents only.

## LLM Risk in This System

The biggest risk from using LLMs is **false confidence**. An LLM will:
- Generate coherent theses for trades that lose money
- Confirm a hypothesis when asked to validate it (sycophancy)
- Overstate certainty about macro conditions
- Miss settlement edge cases in Kalshi markets

Mitigations:
- Skeptic agent is explicitly adversarial
- Risk agent defaults to "reject"
- Research agent is instructed to flag uncertainty, not hide it
- Code enforces limits regardless of agent output
- You (the user) are the final reader and approver
