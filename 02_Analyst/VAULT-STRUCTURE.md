---
title: Vault Structure — Three Layers
description: How Source, Analyst, and References work together
last_updated: 2026-04-14
---

# Vault Structure: Three Layers

Your vault is built in three layers, each with a different purpose. Together they form a persistent knowledge system.

---

## The Three Layers

### 1. `/01_Source/` — Your Raw Writing (Immutable)

**What goes here:**
- Your notes, research, brainstorms, status updates
- Anything you write directly (never edited by AI)
- Raw ideas before synthesis

**Who uses it:**
- You (write here)
- I (read from here)

**Example files:**
- Internship goals
- Meeting notes
- Research dumps
- Strategy sketches

**Rules:**
- ✅ You can write anything anytime
- ✅ I can read and cite it
- ❌ I never edit content
- ❌ I only organize folder structure

**Why it matters:**
- Your truth is preserved
- I can cite your actual thinking
- Future sessions can trace decisions back to your writing

---

### 2. `/02_Analyst/` — My Memory of You (Your Persona)

**What goes here:**
- My synthesis of your Source files
- Your outputs, decisions, progress
- Synthesis of your work + learnings applied to you

**Who uses it:**
- Me (write here, remember across sessions)
- You (refer to it for context)

**Example files:**
- Project status files
- Strategy documents based on your source
- Email campaigns you requested
- Progress tracking

**Frontmatter schema:**
```yaml
origin_dump: [[01_Source/...]]  # Where this came from
last_synced_dump: [[01_Source/...]]  # Latest source incorporated
references: [[[03_References/...]]]  # Frameworks used
```

**Why it matters:**
- I remember your goals, decisions, progress
- I can cite what you've told me
- Links to References show what frameworks I used
- Persistent across sessions

---

### 3. `/03_References/` — Shared Knowledge Base (My Learnings)

**What goes here:**
- Frameworks I discover while working with you
- Tools and how to use them
- Patterns that emerge across projects
- Best practices with real sources

**Who uses it:**
- Me (save learnings here)
- You (reference for your own work)

**Example files:**
- Cold email optimization framework
- Email verification tools + workflow
- Recipient psychology patterns
- Sales/outreach best practices

**Frontmatter schema:**
```yaml
source: [URL, author, tool name]  # REQUIRED - cite real sources
relevance: [which projects apply to]
type: [framework | tool | pattern | resource]
```

**Rules:**
- ✅ I can write here (save learnings)
- ✅ Everything must be sourced (real URL, tool, author, research)
- ✅ You can read + reference for your own work
- ❌ No unsourced speculation
- ❌ No personal info (that goes in Analyst)

**Why it matters:**
- I don't re-learn the same thing each session
- You get curated frameworks + tools
- Everything is sourced (traceable, credible)
- Shared across all your projects

---

## How They Work Together

### Scenario 1: Cold Email Campaign

```
1. You ask me to optimize emails → Analyst file created
2. I apply copywriting principles → Reference framework created
3. Email Analyst file links to Copywriting Reference in frontmatter + body
4. Next session on sales pitch? → I remember the framework, don't re-learn
5. You want to apply to Wave 2? → You read both Analyst (your campaign) + Reference (the framework)
```

### Scenario 2: New Project

```
1. You write goal/strategy in Source → I synthesize into Analyst
2. I discover new tools + patterns → Save to References with sources
3. Analyst file links to References showing what I used
4. Next project in same domain → I reference the framework, apply it faster
```

### Scenario 3: Future Session Resume

```
1. You type /resume → I load Analyst index
2. I see active projects + linked References
3. I remember your progress + learnings from last session
4. I don't re-ask "what are your goals?" because they're in Analyst
5. I don't re-discover frameworks because they're in References
```

---

## Wikilink Map

```
01_Source/Internships/Goal.md
  ↓ (cited by)
02_Analyst/career/internships/_index.md
  ↓ (links to)
02_Analyst/career/internships/wave-3-optimized-emails.md
  ↓ (uses frameworks from)
03_References/Frameworks/Cold-Email-Optimization.md
  ↓ (sources from)
[HubSpot, Copywriting skill, Sales psychology]
```

All bidirectional — each layer knows what informed it.

---

## Quick Reference: What Goes Where

| Question | Answer | Location |
|----------|--------|----------|
| Where do I write notes? | Write directly | `/01_Source/` |
| Where does Claude remember my goals? | I synthesize it | `/02_Analyst/` |
| Where does Claude save what it learned? | I save frameworks + tools | `/03_References/` |
| What gets cited + linked? | Everything | Wikilinks in all layers |
| Can Claude edit my writing? | No, never | Source is immutable |
| Can Claude edit References? | Yes, save learnings | Reference entries are mine to curate |
| Will I lose progress? | No | Three backup layers + cross-links |

---

## Session Flow

**Session start:**
1. You share goal or ask
2. I load Analyst index → remember your context
3. I check References → remember what I learned
4. I read relevant Source → your latest thinking
5. I synthesize into work

**During work:**
1. I create Analyst output (your deliverable)
2. I save framework/tool to References (my learning)
3. Analyst links to References (traceability)
4. You get deliverable + I get curated knowledge

**At end:**
1. `/save` updates Analyst with new Source
2. References remain persistent (no cleanup needed)
3. Next session, I remember everything

---

## Rules Summary

| Layer | You Write? | I Write? | Immutable? | Sourced? |
|-------|-----------|----------|-----------|----------|
| Source | ✅ Always | ❌ Never | ✅ Yes | N/A |
| Analyst | ❌ Refer to | ✅ Synthesize | ❌ No | Via backlinks |
| References | ❌ Read | ✅ Save | ❌ No | ✅ Required |

---

## Why This Structure Works

1. **Your writing is safe** — Source never touched by me
2. **Progress is persistent** — Analyst remembers your goals + decisions
3. **Learning accumulates** — References grow each session, avoid re-learning
4. **Everything is traced** — Wikilinks show what informed what
5. **All layers are integrated** — Analyst links to Source + References

---

## History

[2026-04-14] Three-layer vault structure documented. Wave 3 work demonstrates the flow: Source (your goal) → Analyst (my synthesis + your output) → References (frameworks + tools I discovered, sourced for reuse).
