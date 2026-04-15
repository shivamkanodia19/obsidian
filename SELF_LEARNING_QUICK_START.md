# Self-Learning System Quick Start

**TL;DR:** Agents run tests, write findings, `/save` synthesizes findings, next agent reads findings and scales the work. Continuous improvement without manual context handoff.

---

## Section 1: How to Enable Self-Learning

**Requirements:**
1. Run `/save` at end of each session (agent finishes work → writes exit log → human runs `/save` → findings available to next agent)
2. Agents write exit logs with findings (not optional; required for system to work)
3. Exit logs follow standard format (YAML frontmatter + markdown sections with findings + confidence levels)

**Setup (one-time):**
- Create `/c/Users/shiva/.claude/agent-exits/` directory — agents write exit logs here
- Create `/c/Users/shiva/.claude/agent-exits-archive/` directory — /save archives processed logs here
- Verify `/c/Users/shiva/.claude/projects/C--Users-shiva/memory/` exists — /save creates memory files here
- Done. System is ready.

**Usage (recurring):**
1. Agent finishes work
2. Agent writes exit log: `/c/Users/shiva/.claude/agent-exits/[YYYY-MM-DD]_[agent-name]_[task].md`
3. Human runs `/save internship` (or `/save [project-name]`)
4. /save processes exit log → creates/updates memory files → archives exit log
5. Next agent reads MEMORY.md → finds findings → continues work

---

## Section 2: What Happens Automatically (After You Run /save)

When `/save internship` runs:

1. **Discovers exit logs** in `/c/Users/shiva/.claude/agent-exits/`
2. **Parses YAML frontmatter** (agent_name, task, session_date, focus_area, status)
3. **Extracts findings** (statement + evidence + confidence + reasoning)
4. **Identifies contradictions** (new findings that conflict with prior beliefs)
5. **Creates memory file** `/c/Users/shiva/.claude/projects/C--Users-shiva/memory/agent-findings-[topic].md`
   - Synthesizes all findings from all agents into one file
   - Tracks version history (which agent found what, when)
   - Includes recommendations for next agent
6. **Updates MEMORY.md index** with discoverable entry + wikilink
7. **Archives exit log** to `/c/Users/shiva/.claude/agent-exits-archive/[YYYY-MM]/collection.md`
   - Exit log removed from active directory (no clutter)
   - Content preserved for reference

**Result:** Next agent can find findings by reading MEMORY.md.

---

## Section 3: What Agents Need to Do (Exit Log Requirements)

### Minimum Requirements

Every agent that runs a test **must** write an exit log. File location:

```
/c/Users/shiva/.claude/agent-exits/[YYYY-MM-DD]_[agent-name]_[task-short-name].md
```

Example:
```
/c/Users/shiva/.claude/agent-exits/2026-04-15_test-agent-1_psychology-cta-test.md
```

### Exit Log Format

```yaml
---
agent_name: [your agent name or session ID]
task: [what you were asked to do]
session_date: 2026-04-15
session_duration: 2 hours
focus_area: [internship, cta-optimization, psychology, etc.]
status: completed
---

# Exit Log: [Title]

## What I Was Asked to Do
[Summary of task]

## What I Actually Did
[Work completed]

## Key Findings (For Next Agent)

### Finding 1: [Statement]
- **Evidence:** [How I know this]
- **Confidence:** HIGH / MEDIUM / LOW
- **Reasoning:** [Why I'm confident]
- **Source:** [Where this came from]

[Add more findings as needed]

## Contradictions (With Prior Work)

### Contradiction 1
- **Old finding:** [What was believed before]
- **What I found:** [New finding]
- **Why different:** [What changed]
- **Recommendation:** [How to resolve]

## What I Recommend for Next Agent

### What to Test
- [Specific next test]
- [Hypothesis to validate]

### Blockers / Unknowns
- [What you couldn't finish]

## Metrics (If Applicable)

[Test results: emails sent, replies, rates, etc.]

## Confidence Levels

| Finding | Confidence | Basis |
|---------|-----------|-------|
| [Finding 1] | HIGH | [Research / tested] |
| [Finding 2] | MEDIUM | [Theory, not tested yet] |
```

### Key Rules

1. **Be specific about confidence.** Don't guess. Say "HIGH because [research/test]."
2. **List contradictions first.** If you found something that contradicts a prior finding, call it out.
3. **Recommend what to test next.** Leave breadcrumbs for the next agent.
4. **Include metrics.** Numbers matter: how many tests, how many replies, what was the rate?
5. **Don't update the exit log after writing it.** It's read-only after creation. /save will process it.

---

## Section 4: How to Verify It's Working

After running `/save`, check:

1. **MEMORY.md updated?**
   - File: `/c/Users/shiva/.claude/projects/C--Users-shiva/memory/MEMORY.md`
   - Search for your agent name
   - You should see a new entry under "Agent Findings Index" with a wikilink

2. **Agent-findings file created?**
   - File: `/c/Users/shiva/.claude/projects/C--Users-shiva/memory/agent-findings-[topic].md`
   - Should contain your findings + version history
   - Example: `agent-findings-internship-cta.md`

3. **Exit log archived?**
   - Original file: Should NOT be in `/c/Users/shiva/.claude/agent-exits/` anymore
   - Archived to: `/c/Users/shiva/.claude/agent-exits-archive/[YYYY-MM]/collection.md`

4. **Can next agent find it?**
   - Open MEMORY.md
   - Search for your topic
   - Click wikilink to agent-findings file
   - Read recommendations for next agent

If all 4 checks pass, system is working.

---

## Section 5: Example — Wave 5 Outreach Learning Loop

**Wave 5 Goal:** Test psychology CTAs on internship logistics targets. Scale from 5 → 30 → 100+ sends.

### Agent 1: Test Psychology CTA (5 sends)

**Work:**
- Send 5 emails to logistics targets using psychology CTA ("Can I grab 15 min on Tuesday or Wednesday?")
- Track replies for 24 hours
- Record results: 1/5 replied (20% reply rate)

**Exit Log:**
```
task: Test psychology-optimized CTAs on Wave 5 logistics targets
focus_area: internship, cta-optimization, psychology, wave5-validation

## Key Findings

### Finding 1: Binary Choice CTA Works
- Evidence: Heartland Express replied within 3.5 hours
- Confidence: HIGH
- Reasoning: Format was understood, no confusion

### Finding 2: 20% Reply Rate (Early Signal)
- Evidence: 1/5 replied in 24h
- Confidence: MEDIUM (small sample)
- Reasoning: 20% is 2x higher than baseline, but 5 is too small to be sure

## What I Recommend for Next Agent
- Scale to 25-30 sends
- If >15% reply rate, approve full Wave 5 deployment
```

**Human runs `/save internship`**

### Agent 2: Validate Psychology CTA (25 sends)

**Agent 2 reads MEMORY.md:**
- Sees entry: "Test Agent 1 Psychology CTA Validation (Wave 5) — 20% reply rate"
- Clicks wikilink → reads agent-findings-internship-cta.md
- Sees recommendation: "Scale to 25-30 sends to validate"

**Agent 2 work:**
- Send 25 new emails to logistics targets using same psychology CTA
- Track replies for 3 days
- Record results: 6/25 replied (24% reply rate)
- Aggregate: 7/30 total (23% reply rate)

**Agent 2 exit log:**
```
task: Validate psychology CTA at scale (Wave 5 logistics)
focus_area: internship, cta-optimization, psychology, wave5-validation

## Key Findings

### Finding 1: Psychology CTA Validates at Scale
- Evidence: 24% reply rate on 25 new sends (vs 20% from Agent 1)
- Confidence: HIGH (30 total sends, consistent result)
- Reasoning: Both agents HIGH, no contradictions

## Contradictions
None. Agent 1's finding confirmed.

## What I Recommend for Next Agent
- Approve full Wave 5 deployment (80+ remaining targets)
- Optional: A/B test psychology CTA vs baseline to quantify 2x lift
```

**Human runs `/save internship`**

### Result: Pattern Confirmed

**/save synthesizes both agents' findings:**
- Agent 1: 20% (5 sends, HIGH)
- Agent 2: 24% (25 sends, HIGH)
- Aggregate: 23% (30 sends, HIGH confidence)
- Status: **PATTERN CONFIRMED**

**MEMORY.md updated:**
```
- [Pattern Confirmed: Psychology CTA Works for Wave 5 Logistics](./agent-findings-internship-cta.md) — 
  Agent 1: 20% rate. Agent 2: 24% rate. Aggregate: 23% (30 sends, HIGH confidence). Ready for full deployment.
```

**Decision:** Approved for full Wave 5 deployment (100+ remaining targets).

---

## Section 6: Common Questions

### Q: Do I have to run `/save` immediately after an agent finishes?
**A:** Not immediately, but soon. Within same day is ideal so findings stay fresh. You can batch multiple exit logs and run `/save` once.

### Q: What if an agent finds something that contradicts a prior finding?
**A:** /save logs it in the contradictions section with resolution status (pending-validation, resolved, etc.). You review conflicts and decide next steps.

### Q: What if I have 10 agents contributing to the same topic?
**A:** /save creates one `agent-findings-[topic].md` file and updates it as each agent contributes. Version history tracks all agents and dates.

### Q: Can agents disagree?
**A:** Yes. If Agent 1 found "20% reply rate" and Agent 2 found "5% reply rate", /save flags as contradiction with "pending-validation" status. Next agent can investigate why.

### Q: What happens if exit log format is wrong?
**A:** /save should fail gracefully and log error. Fix the exit log syntax (YAML, markdown headers) and re-run `/save`.

### Q: How do I know if /save succeeded?
**A:** Check: (1) MEMORY.md updated, (2) agent-findings file created, (3) exit log archived, (4) no error logs.

### Q: Can I manually edit agent-findings files?
**A:** Not recommended. /save overwrites them when processing new exit logs. If you need to add notes, use a separate file or comment in exit log.

### Q: What if I want to test the system without running real tests?
**A:** Use TEST_SCENARIO_FULL_LOOP.md as reference. Create test exit logs (fake data), run `/save`, verify all outputs.

---

## Section 7: File Structure

**Self-learning system uses these directories:**

```
.claude/
├── agent-exits/                          # Active exit logs (agents write here)
│   ├── 2026-04-15_test-agent-1_....md
│   ├── 2026-04-18_test-agent-2_....md
│   └── [NEW EXIT LOGS WRITTEN HERE]
│
├── agent-exits-archive/                  # Archived exit logs (preserved for reference)
│   ├── 2026-04/
│   │   └── collection.md                 # Monthly collection of exit logs
│   └── 2026-05/
│
└── projects/C--Users-shiva/memory/
    ├── MEMORY.md                         # Index (updated by /save)
    ├── agent-findings-*.md               # Created by /save (one per topic)
    │   ├── agent-findings-internship-cta.md
    │   ├── agent-findings-logistics-targeting.md
    │   └── [NEW AGENT FINDINGS CREATED HERE]
    └── [other memory files]
```

---

## Section 8: When to Use This System

**Use self-learning when:**
- Testing multiple variations (A/B tests, scaling experiments)
- Working across multiple sessions or days
- Validating findings with repeated tests
- Building institutional knowledge (what works, what doesn't)

**Don't need self-learning for:**
- One-off tasks (write email, research topic)
- No future testing needed
- Manual, context-specific work

**Wave 5 example:** Self-learning is perfect because:
1. Agent 1 tests hypothesis
2. Agent 2 validates at scale
3. Agent 3 optimizes based on findings
4. Each agent builds on prior discoveries

---

## Quick Checklist: Running Self-Learning

- [ ] Exit log written with findings + confidence levels
- [ ] Exit log file named: `[YYYY-MM-DD]_[agent-name]_[task].md`
- [ ] Exit log location: `/c/Users/shiva/.claude/agent-exits/`
- [ ] Run `/save internship` (or `/save [project-name]`)
- [ ] Verify MEMORY.md updated (entry visible)
- [ ] Verify agent-findings file created
- [ ] Verify exit log archived (no longer in agent-exits/)
- [ ] Next agent reads MEMORY.md and finds findings
- [ ] System working ✓

---

**Done.** You now have a self-learning system. Commit to writing exit logs, run `/save` after each test wave, and watch agents build on each other's discoveries.
