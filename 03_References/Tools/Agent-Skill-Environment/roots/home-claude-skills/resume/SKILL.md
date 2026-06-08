---
name: resume
description: Vault-efficient context bootstrap. Read INDEX.md, route to project, load STATUS + 1 key file. Fresh agent perfectly oriented in 500-700 tokens.
user-invocable: true
---

# /resume

Load vault context, route fresh agent to task, launch perfectly oriented.

**Goal:** Minimal tokens, maximum clarity. Fresh agent reads this, understands scope + latest decisions + next steps, starts working.

---

## Steps

### 0. Read master INDEX.md

Read `~/obsidian/INDEX.md` (your vault map).

- Understand vault structure (projects, research, academics, career, knowledge)
- Identify which section matches user's task intent

Takes **300-400 tokens**. Establishes the map.

### 1. Route to project

From INDEX.md, identify which project/folder is relevant:
- **ClinicalHours** → working on startup
- **FEDVT** → research on feedlot economics
- **Academics** → coursework
- **Career** → internship/resume
- **Knowledge** → general concepts

If ambiguous, ask user: "Should I load context for [A] or [B]?"

### 2. Load project STATUS.md

Read `projects/[project]/STATUS.md` (or `research/[project]/STATUS.md`, etc.)

This file contains:
- **Latest decisions** (date + 1-2 bullets)
- **Current blockers** (what's stuck)
- **Next steps** (numbered, clear actions)
- **Metrics** (progress, traction)
- **Last session date**

Takes **100-150 tokens**. Agent now knows: what happened, what's next, what's stuck.

### 3. Load project INDEX.md

Read `projects/[project]/INDEX.md` (if it exists).

This file maps all sections in the project:
- Major folders (Strategy, Sales, Market Research, Operations)
- Key topics within each
- Wikilinks to files agent might need

Takes **150-200 tokens**. Agent now sees the full project structure.

### 4. Load 1-2 key contextual files

Based on task intent, read ONLY the most relevant file(s):

**Example workflows:**

**User:** "Help with ClinicalHours email automation"
- Route: ClinicalHours
- Load: STATUS.md (latest decisions on email)
- Load: `Strategy/Email-Automation/cold-email-strategy.md` (the playbook)
- **Total: 500-600 tokens**

**User:** "What's the status of FEDVT?"
- Route: FEDVT
- Load: STATUS.md (latest progress, next steps)
- Load: `Introduction/` or latest section from project INDEX
- **Total: 450-550 tokens**

**User:** "Internship search update"
- Route: Career
- Load: STATUS.md (latest apps, next outreach)
- Load: `career/internships/STATUS.md` or target list file
- **Total: 400-500 tokens**

**Rule:** NO reading entire projects. NO reading narrative sections. Only STATUS + 1 actionable file based on task.

### 5. Present brief

Show agent what they're working on. Format:

```
📍 Project: [Project Name]
Status: [Latest 1-line summary from STATUS.md]

🎯 Latest Decisions:
- [1-2 bullets from STATUS]

🚧 Current Blockers:
- [Any blockers from STATUS]

📋 Next Steps:
- [Top 2-3 actions from STATUS]

📁 Full project structure: See [[projects/[project]/INDEX.md]]
```

That's it. Agent is ready to work.

---

## Token Budget

- INDEX.md: **300-400 tokens** (one read, establishes map)
- Project STATUS.md: **100-150 tokens** (decisions + blockers + next steps)
- 1 contextual file: **100-200 tokens** (the actual work file)

**Total: 500-700 tokens max**

vs. old approach: 1000+ tokens guessing folder structure, reading narrative sections, extracting metadata manually.

---

## Key Rules

1. **Always read master INDEX.md first** — it's your router
2. **Always read project STATUS.md** — it's the source of truth for that project
3. **Load only 1-2 files max** — pick the most relevant file for the task
4. **No narrative sections** — agent should read only decisions, next steps, blockers
5. **NO full project reads** — don't load everything just because it exists
6. **Wikilinks point the way** — if agent needs more context, they click wikilinks in the files

---

## Fresh Agent Perfect Orientation

After `/resume`, agent knows:
- ✅ What project they're working on
- ✅ What happened last (latest decisions)
- ✅ What's blocking progress
- ✅ What to do next (concrete, clear actions)
- ✅ Where to find more context (wikilinks in loaded files + INDEX.md)

Agent starts working immediately. No "what am I doing here?" moments.

---

## Cross-Project Tasks

If task spans multiple projects (e.g., "FEDVT research informs ClinicalHours pricing"):

1. Load master INDEX.md (5 min read)
2. Load primary project STATUS.md
3. Load secondary project STATUS.md
4. Load 1 file from each that's directly relevant

**Total: 700-800 tokens** for two-project context.

Don't exceed 800 tokens. Agent gets the map, the status of both, and enough to start. Wikilinks handle the rest.
