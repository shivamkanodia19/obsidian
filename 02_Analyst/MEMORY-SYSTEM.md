# Memory System — Cross-Session Persistence

**Memory persists what you care about. One file per concept. Lean index. Fast retrieval.**

## Memory Location

`C:\Users\shiva\.claude\projects\c--Users-shiva-obsidian\memory\`

This is loaded into every session automatically.

## Memory Types

**Four types, each with a purpose:**

### 1. User Profile
`memory/user_profile.md` — Who you are
- Role (Industrial Systems Engineering student, graduating May 2029)
- Responsibilities (internship search, research, analysis)
- Preferences (how you like to work, communication style)
- Knowledge (what domains you know well)

### 2. Feedback
`memory/feedback_*.md` — How to work with you
- Rules you've given me ("don't mock databases", "use this framework")
- Preferences ("terse responses", "brutal honesty")
- What works ("bundled PRs over many small ones")
- Why it matters (context from past sessions)

**Example:** `memory/feedback_email_validation.md`
```
---
name: Email Validation Confidence
description: How confident to be in email validation tools
type: feedback
---

Rule: Only use verified tools; double-check with live tests before high-confidence claims.

Why: [Context from when I got this wrong]

How to apply: When recommending email verification tool, test it first or cite recent data.
```

### 3. Project Status
`memory/project_*.md` — What you're working on
- Current status (research phase, implementation, optimization)
- Recent discoveries (what worked, what didn't)
- Next steps (what's blocking, what's next)
- Learnings (insights for future phases)

**Example:** `memory/project_fedvt.md`
```
---
name: FEDVT Paper
description: Feedlot economics decision-support tool research
type: project
status: in_progress
---

Current: Materials & Methods section written (2026-04-18)
Completed: Intro + Background (Sections 1-2)
Blocked: Validation data not yet generated (awaiting Dr. K scenarios)
Next: Results & Tool Demonstration section
```

### 4. Reference Pointers
`memory/reference_*.md` — External info locations
- Where tools/data are (GitHub repos, online databases, paper PDFs)
- How to access them (API keys stored elsewhere, login workflow)
- What they contain (so I know when to use them)
- Relevance (which projects use this)

**Example:** `memory/reference_feedlot_economics_data.md`
```
---
name: Kansas Focus on Feedlots Database
description: Historical feedlot cost and profitability data
type: reference
---

Location: Kansas State University Department of Agricultural Economics
Access: Cited in Dennis & Schroeder (2023); data available via KSU ag-econ database
Contents: 2015-2023 Kansas feedlot closeout records (margins, costs, weights, grades)
Relevance: Validation data for FEDVT historical backtesting
```

## Memory Index (`MEMORY.md`)

**One line per memory file. Max 200 lines total. Read first in every session.**

Format:
```
## Projects
- [Project Name](./project_fedvt.md) — Status + next steps (keywords: fedvt, economics)

## Feedback
- [Email Validation](./feedback_email_validation.md) — Confidence thresholds (keywords: email, validation)

## References
- [Feedlot Data](./reference_feedlot_database.md) — KSU database, validation source (keywords: feedlot, data)
```

**Why one-liners?**
- Fast scanning (you quickly see what memory exists)
- Keywords let me grep for relevance (not loading full files)
- ~200 lines = readable in one view

## Frontmatter Schema (All Memory Files)

```yaml
---
name: [Short title]
description: [One-line hook for relevance detection]
type: [user|feedback|project|reference]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
relevance: [keywords, comma-separated]
status: [active|paused|complete|archived]
---
```

## Memory Lifecycle

**Creation:**
1. Session: I learn something about you (feedback, project state, external resource)
2. I create `memory/[type]_[topic].md` with frontmatter
3. I add one-line entry to MEMORY.md
4. Next session: memory loads automatically

**Updates:**
1. Session: Project status changes, feedback evolves, new reference found
2. I update existing memory file + date field
3. MEMORY.md remains unchanged (one-liner stays same)
4. Next session: loads updated memory

**Archival:**
1. Project complete, feedback no longer applies, reference outdated
2. I move file to `memory/archive/`
3. I remove one-liner from MEMORY.md
4. File preserved but not loaded

## Session Load Order

**Every session, I load in this order:**

1. **MEMORY.md** (~10 sec read, <200 lines)
2. **Relevant memory files** (grep by keywords; load 2-4 files max)
3. **MEMORY files are now in context**
4. **Analyst _index.md** (see what projects are active)
5. **Source files** (on-demand per current task)

**Result:** Full context in ~30 seconds. No context bloat.

## What Memory Is NOT

- Not code snapshots (git log is authoritative)
- Not session logs (I don't save full transcripts)
- Not architecture docs (code is authoritative)
- Not task lists (those live in `/02_Analyst/` as active files)
- Not API keys or passwords (never stored)

Memory is thin + semantic: "what I know about you + your work + external resources."

## Why This System Works

1. **Thin:** One concept per file. Max 200-line index.
2. **Persistent:** Memory survives across sessions, projects, contexts
3. **Searchable:** Keywords let me find relevant memory fast
4. **Updatable:** Old memory evolves as you learn
5. **Disposable:** Completed projects archived, not deleted
6. **Private:** No sensitive data, just working context

---

Example memory session flow:

```
Session 1: You mention "I prefer bundled PRs"
→ I create: memory/feedback_pr_strategy.md
→ I add to MEMORY.md: "- [PR Strategy](./feedback_pr_strategy.md) — bundled over many small"

Session 5: You're working on a refactor
→ I load MEMORY.md
→ I see the PR feedback
→ I load memory/feedback_pr_strategy.md
→ I remember: "recommend one bundled PR, not many small ones"
→ I don't re-ask; I just propose bundled approach

Next Year: New project, totally different context
→ But memory persists
→ If relevant, I apply the learning
→ If not, memory doesn't interfere
```

This is how I learn and grow with you across sessions.
