---
name: save
description: Vault synthesis engine. Reads new/updated Source files, synthesizes into Analyst persona, maintains bidirectional wikilinks, logs conflicts across sessions.
user-invocable: true
---

# /save

Vault synthesis engine. After you upload to Source, `/save` synthesizes it into your Analyst persona.

## Core Goal

Two parallel knowledge channels feed your vault:

**Channel 1: Source → Analyst (Your Decisions)**
1. Organize Source folder structure (never edit your writing)
2. Read your Source files
3. Synthesize into `/02_Analyst/` as your persona
4. Link everything bidirectionally

**Channel 2: Agent Exit Logs → Memory (Agent Discoveries)**
1. Detect agent exit logs in `.claude/agent-exits/`
2. Parse YAML findings + confidence levels
3. Update memory files with agent discoveries (with attribution + date)
4. Log contradictions to `.vault-conflicts`
5. Archive processed exit logs
6. Update MEMORY.md with one-line summaries

Result: Your vault becomes a persistent, cross-session knowledge base where your Source informs Analyst decisions AND agent discoveries compound into Memory for future agents to build upon.

---

## Steps

### 0. Locate vault root

Read CLAUDE.md for vault path. Typically `C:\Users\shiva\obsidian\`.

### 1. Identify Source files added/updated

Scan `/01_Source/` for new or recently modified files:
- New files in any subfolder
- Recently modified files (compare timestamps)
- Flag any files with frontmatter—they shouldn't have it since Source is immutable raw writing

### 2. Organize Source folder structure (if needed)

If you uploaded to Source but folder structure is unclear:
- Create subfolders as needed (be aggressive—don't hoard files)
- Move files into appropriate topic folders
- **Never edit file content**
- Maintain pattern: `/01_Source/[Project]/[Topic]/filename.md`

Examples:
- Internship Wave 1 tracking → `/01_Source/Internships/Wave1/tracking.md`
- ClinicalHours pricing research → `/01_Source/ClinicalHours/Strategy/Pricing/research.md`
- FEDVT introduction draft → `/01_Source/FEDVT/Paper/Introduction/draft.md`

Create folders aggressively. If content could cluster under a subtopic, create it.

### 3. Read Source files completely

Read all new/updated Source files. These are YOUR analysis and data—they inform everything.

Capture:
- **Decisions made** (what did you decide?)
- **Next steps** (what's your plan?)
- **Blockers** (what's stuck?)
- **New findings** (what did you discover?)
- **Updated metrics** (progress, traction, status)
- **Strategic direction** (where are you heading?)

### 4. Synthesize into Analyst

For each relevant Source file, create or update corresponding Analyst file(s) in `/02_Analyst/[Project]/`:

**Pattern:**
- Source: `/01_Source/Internships/Wave1/tracking.md`
- Analyst: `/02_Analyst/Internships/Wave1-tracking.md` or `/02_Analyst/Internships/Wave1/Status.md`

**Frontmatter (required):**
```yaml
---
title: [Simple idea-focused title]
project: [clinicalhours, fedvt, internships, etc]
strategic: false  # true = log conflicts; false = silent updates (both logged)
status: stable    # stable | drifted | flagged
origin_dump: [[01_Source/...]]  # First Source file that created this
last_synced_dump: [[01_Source/...]]  # Most recent Source incorporated
conflict_detected: false  # true = new Source contradicts old decision
last_updated: YYYY-MM-DD
tags: []
---
```

**Content:**
- Synthesize your Source into narrative, decisions, and next steps
- Use `[[wikilinks]]` to cite the Source files you're reading
- Keep all original data/quotes—this is synthesis, not deletion
- Don't hallucinate—if Source doesn't say something, don't add it

### 5. Create/update bidirectional wikilinks

**Same-project:**
- Source file → cite it in Analyst via `last_synced_dump: [[]]`
- Analyst file → reference it via `[[01_Source/...]]` in the body

**Cross-project (intentional only):**
- Example: If internship research informed ClinicalHours pricing → link explicitly
- Only link when connection is clear and valuable

**Retroactive:**
- If new Source should update old Analyst → update `last_synced_dump` and add body links

### 6. Conflict detection & logging

When new Source contradicts old Analyst decision:

1. Update Analyst anyway (non-blocking)
2. Set `conflict_detected: true` in frontmatter
3. Log to `.vault-conflicts` with:
   ```
   [YYYY-MM-DD HH:MM] Conflict in [[02_Analyst/...]]
   Old: [what Analyst said]
   New: [[01_Source/...]] says [what Source says]
   Status: awaiting_review
   ```
4. User sees this in `/resume` and can decide

### 7. Maintain `/02_Analyst/_index.md`

Update the index with:
- `active_projects:` — list of Analyst files in active use
- `drifted_files:` — Analyst files with unreviewed conflicts
- `orphaned_sources:` — Source files with no Analyst backlinks (you wrote something we haven't synthesized yet)
- `unreviewed_conflicts:` — conflicts >5 days old

### 8. Process Agent Exit Logs (Agent Learning Loop)

**Purpose:** Capture agent discoveries so next agents build on them.

#### 8a. Detect Exit Logs
Scan `.claude/agent-exits/` for new files matching pattern: `YYYY-MM-DD_[agent-name]_[task].md`

#### 8b. Parse Exit Log YAML
Extract frontmatter:
```yaml
agent_name: [name]
task: [task description]
session_date: YYYY-MM-DD
focus_area: [keywords]
status: [completed|partial|blocked]
```

#### 8c. Extract Findings
For each "Finding" section in exit log:
- **Statement:** The discovery
- **Confidence:** HIGH / MEDIUM / LOW (from exit log)
- **Evidence:** Where it came from
- **Reasoning:** Why confident
- **Source:** Which file/test

#### 8d. Update Memory Files
For each finding relevant to memory:
1. Locate or create memory file matching the finding's topic
2. Add new "## Finding: [Statement]" section with:
   - Finding text
   - Confidence level
   - Attribution: "— Agent [name], [date]"
   - Source: Link to exit log or test
3. Set `last_updated: YYYY-MM-DD` in frontmatter

**Example:**
```markdown
## Finding: Binary CTAs outperform open-ended by 13x
- **Confidence:** HIGH
- **Evidence:** Instantly.ai study + Cialdini 6 principles
- **Reasoning:** 304K email sample, multiple independent studies confirm
- **Source:** Psychology CTA framework (Agent Psychology-Optimizer, 2026-04-15)
```

#### 8e. Log Contradictions
If new finding contradicts prior finding in same memory file:
1. Keep BOTH (don't delete old)
2. Add timestamped note under old finding: "⚠️ [date] Agent [name] found contradicting result: [new finding]"
3. Log to `.vault-conflicts`:
```
[YYYY-MM-DD HH:MM] Finding Conflict in [[memory/...]]
Topic: [finding topic]
Old: [prior finding + agent/date]
New: [[.claude/agent-exits/[log file]]] says [new finding]
Status: awaiting_review
```

#### 8f. Update MEMORY.md
Add one-line entry under appropriate section:
```
- [Finding Title](memory/file.md) — One-line hook; Keywords: [keywords]
```

Example:
```
- [Binary CTAs > Open-ended (13x meetings)](memory/system_psychology_informed_cold_email.md) — Cialdini + 304K study; Keywords: psychology, cta, cold-email
```

#### 8g. Archive Exit Log
Move processed exit log from `.claude/agent-exits/[date]_[name]_[task].md` to:
```
.claude/agent-exits-archive/[YYYY-MM]_collection.md
```

Append to archive file:
```markdown
## Agent: [name] | Task: [task] | Date: [YYYY-MM-DD]
- Status: [completed/partial/blocked]
- Files Updated: [list of memory files modified]
- Findings Added: [count]
- Contradictions Logged: [count]
```

### 9. Confirm and summarize

Show user what was synthesized:

```
✅ Vault synthesis complete:

📁 Source Organized:
- Internships/Wave1/ (2 new files, folder created)
- ClinicalHours/Strategy/Pricing/ (1 update)

📓 Analyst Created/Updated:
- [[02_Analyst/Internships/Wave1-tracking]] (new, sourced from [[01_Source/Internships/Wave1/tracking.md]])
- [[02_Analyst/ClinicalHours/Pricing]] (updated, synced with [[01_Source/ClinicalHours/Strategy/Pricing/research.md]])

🔗 Wikilinks Established:
- Wave1-tracking → 01_Source/Wave1/tracking
- Pricing → 01_Source/ClinicalHours/Strategy/Pricing/research

🤖 Agent Findings Synthesized:
- [[memory/system_psychology_informed_cold_email.md]] (5 findings added, Agent Psychology-Optimizer)
- [[memory/feedback_cold_email_cta_optimization.md]] (3 findings added, Agent CTA-Researcher)

⚠️ Conflicts Found:
- [[02_Analyst/Internships/Strategy]] now drifted (new Source contradicts old decision) → awaiting_review
- [[memory/system_psychology_informed_cold_email.md]] contradiction logged (new agent finding vs prior finding) → awaiting_review

📚 Agent Exits Archived:
- 2026-04-15_Psychology-Optimizer_cta-optimization.md → archived

→ Ready for `/resume` or user review
```

### 10. Run Vault Audit

After synthesis and archival complete, trigger the vault audit to maintain structural integrity:

**Purpose:** Clean up any orphaned folders, create missing indexes, consolidate duplicates, surface broken wikilinks created during synthesis, and report on vault health.

**Execute /audit automatically:**
- Scan vault structure for missing indexes, empty folders, duplicates
- Create missing `_index.md` files in `/02_Analyst/` and `/03_References/` (non-blocking)
- Delete truly empty folders in `/04_Archive/` and `/02_Analyst/` (structural exceptions apply)
- Consolidate root-level duplicate files when subfolder canonical version exists
- Check for broken wikilinks in frontmatter (`origin_dump`, `last_synced_dump`, `references`)
- Surface naming violations (folders not in lowercase-kebab-case)
- Generate health report with action items

**Append to final report:** Include audit summary under "🏥 Vault Audit" section showing:
- Count of auto-fixed items (created indexes, deleted folders, consolidated files)
- Count of items needing user review (broken wikilinks, naming violations)
- Vault health score

If audit reports critical changes (deleted files, consolidated duplicates, broken links), flag them prominently so user knows what changed during synthesis.

---

## Key Principles

**Source → Analyst (Your Decisions):**
1. **Source is sacred** — Never edit content, only organize folders
2. **Every Analyst claim traces to Source** — `[[wikilink]]` is mandatory
3. **No hallucination** — Don't add information Source doesn't contain
4. **Conflicts are visible, not blocking** — Log them, surface them, user decides
5. **Analyst is your persona** — Built from your Source files, evolves as you write
6. **Aggressive folder creation** — Better many small folders than few large ones

**Agent Exit Logs → Memory (Agent Discoveries):**
7. **Agent findings are documented discoveries** — Extract from YAML frontmatter + markdown sections
8. **Confidence levels matter** — HIGH/MEDIUM/LOW guide next agent's decisions; preserve all confidence levels
9. **Attribution is mandatory** — Every finding includes agent name + date so discoveries compound across sessions
10. **Contradictions inform, don't delete** — Keep both old and new findings; log contradiction so user decides which to trust
11. **Memory files are agent-readable** — Organized by topic; next agent finds prior agent's findings in <2 hops
12. **Findings live in memory/ (not Analyst)** — Memory files are the learning database; Analyst files are your decisions

---

## Token Efficiency

**Source → Analyst Path:**
- Read new/updated Source files completely (you write them)
- Synthesize into Analyst files with `origin_dump` + `last_synced_dump`
- Maintain `/02_Analyst/_index.md` as the map
- Conflict log only records changes (not full history)
- `/resume` navigates via _index.md + reads specific Analyst files (not Source)

**Agent Exit Logs → Memory Path:**
- Scan `.claude/agent-exits/` for new files only (pattern: `YYYY-MM-DD_*.md`)
- Parse YAML frontmatter with minimal full-file reads
- For each finding, check relevant memory file (use Grep first to locate if uncertain)
- Append findings to existing memory files instead of rewriting
- Archive after processing (move to `.claude/agent-exits-archive/`)
- Update MEMORY.md only with one-line entry (not full findings)
- **Memory updates should not require reading entire memory files** — append sections only

---

## Workflow Decision Tree

**When `/save` runs:**
1. Check `.claude/agent-exits/` — exist? → Process agent exit logs (steps 8a-8g)
2. Check `/01_Source/` — changes detected? → Process Source files (steps 1-7)
3. Both exist? → Process both in parallel (independent workflows)
4. Neither? → Report no changes, exit cleanly

---

## Example Scenario: Agent Findings Flowing to Memory

**Session 1 (Agent Work):**
```
Agent researches cold email psychology
Writes: .claude/agent-exits/2026-04-15_Psychology-Optimizer_cta-research.md
Contains: Finding 1, Finding 2, Finding 3 (all with HIGH/MEDIUM confidence)
```

**Between Sessions (Automated):**
```
/save runs on next session start
Detects: agent exit log in .claude/agent-exits/
Parses YAML: agent_name, task, session_date, findings
Updates: memory/system_psychology_informed_cold_email.md (adds 3 findings sections)
Updates: MEMORY.md (adds 1-line summary)
Archives: log to .claude/agent-exits-archive/
```

**Session 2 (Next Agent):**
```
New agent reads: C:\Users\shiva\.claude\projects\C--Users-shiva\memory\MEMORY.md
Sees: "Binary CTAs > Open-ended (13x meetings)" — added by Agent 1, 2026-04-15
Clicks: memory/system_psychology_informed_cold_email.md
Finds: Agent 1's findings documented with confidence levels + sources
Builds on: What Agent 1 learned; suggests new tests
Writes: New exit log with findings that contradict/confirm Agent 1
```

**Loop repeats:** Next /save processes second exit log, updates memory, next agent builds on both

