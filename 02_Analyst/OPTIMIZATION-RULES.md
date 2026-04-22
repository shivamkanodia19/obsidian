# Vault Optimization Rules

**How `/save` and `/audit` keep context lean and findable.**

## Core Principle

**Atomic synthesis, not incremental bloat.**

Every `/save` call reads new Source, synthesizes to Analyst, updates Memory, optimizes structure. One call maintains the entire vault in lean state.

## `/save [topic]` Workflow

**Syntax:** `/save FEDVT` or `/save internships` or `/save clinicalhours`

**What it does:**

1. **Detect new Source files** in `/01_Source/[topic]/` (even if multiple dumps uploaded)
2. **Synthesize to Analyst:**
   - Reads all new Source files in that project
   - Creates/updates relevant `/02_Analyst/` files
   - Links all claims back to Source via wikilinks
   - Adds frontmatter: `origin_dump`, `last_synced_dump`, `references`
3. **Handle conflicts** (when new Source contradicts old Analyst decision):
   - Move old content to `## History [YYYY-MM-DD]` in Analyst file
   - Log conflict to `.vault-conflicts` with old vs. new states
   - Set `conflict_detected: true` flag on file (non-blocking)
4. **Update Memory:**
   - Create `memory/project_[topic].md` if new project
   - Update existing project memory with current status
   - Create `memory/feedback_[topic].md` if new feedback discovered
   - Add/update one-liner in `MEMORY.md`
5. **Create/update indexes:**
   - Every new folder gets `_index.md` with navigation
   - All parent folders updated to reflect new files
6. **Archive old history:**
   - History sections >6 months → move to `/04_Archive/[project]_history.md`
   - Keeps active Analyst files lean

**Result:** Single `/save` call = full synthesis, conflict resolution, memory updates, organization.

## `/audit` Workflow

**Syntax:** `/audit`

**What it does:**

1. **Scan vault structure:**
   - Find orphaned folders (no files, only index)
   - Find duplicates (same content in multiple places)
   - Find misplaced files (wrong folder for content)
   - Find broken wikilinks
   - Find missing indexes
2. **Auto-fix structural issues:**
   - Delete orphaned folders (empty)
   - Consolidate duplicates (delete redundant version, keep authoritative copy)
   - Move misplaced files to correct folder
   - Create missing indexes
   - Repair broken wikilinks (flag ones that need manual review)
3. **Report critical issues only:**
   - Never report naming/depth/cosmetic issues
   - Only flag: broken links, misplaced content, orphaned data
   - Suggest fixes; don't ask permission (structural fixes are safe)
4. **Memory cleanup:**
   - Archive stale memories (>6 months, status=complete)
   - Surface unreviewed conflicts at session start
   - Remove unreachable memories (referenced but not found)

**Result:** Vault stays structurally sound. Critical issues surfaced. You focus on work, not maintenance.

## Optimization Principles

### 1. One Concept Per File

**In Analyst:**
- One project, one file (not bundled projects in one file)
- One decision, one conflict log entry
- One research area, one Research file

**In Memory:**
- One feedback rule per file
- One project per file
- One reference per file

**Benefit:** Fast searching, easy updating, no unnecessary re-reading.

### 2. Lean Indexes (Max 200 Lines)

**MEMORY.md stays <200 lines:**
- One-liners only
- Old entries archived when list gets long
- Keywords enable grep-based relevance
- First file loaded in every session

**Analyst `_index.md` stays <100 lines:**
- Navigation only
- Quick reference
- Links to detailed files

**Benefit:** Fast session bootstraps, no context bloat.

### 3. History Moves, Not Deletes

**Old content lifecycle:**

- **Active:** File body contains current state
- **Stale (not in use):** Move to `## History [YYYY-MM-DD]` with context
- **Very old (>6 months):** `/save` moves History to `/04_Archive/`
- **Queried later:** Archive files are still searchable

**Benefit:** You can trace decisions over time; active files stay lean.

### 4. Frontmatter Tells the Story

**Analyst files frontmatter:**
```yaml
origin_dump: [[01_Source/...]]  # Where did this synthesis come from?
last_synced_dump: [[01_Source/...]]  # Latest Source incorporated
conflict_detected: true/false  # Any decision conflicts?
last_updated: YYYY-MM-DD  # When did I last touch this?
```

**Benefit:** I know which Source files to re-read, which conflicts need review, how fresh the info is.

**Memory files frontmatter:**
```yaml
relevance: [keywords]  # How do I find this in future sessions?
status: active|paused|complete  # Is this still load-bearing?
created: YYYY-MM-DD  # How old is this?
```

**Benefit:** I grep by keywords, prioritize active memories, archive completed ones.

### 5. Wikilinks = Traceability

**Every claim links back:**
- `According to [[01_Source/fedvt/...]], X is true` (cites your source)
- `See [[03_References/...]] for framework` (cites discovery)
- `Related: [[02_Analyst/related_file.md]]` (cross-references)

**Benefit:** I can trace any conclusion back to where it came from. You can verify claims.

## Context Bloat Prevention

**What causes bloat:**
- Loading all MEMORY.md entries (should load only relevant ones)
- Loading full Analyst files when I only need frontmatter
- Preloading skill files (should invoke on-demand)
- Keeping History in active files >6 months
- Creating unnecessary intermediate files

**How we prevent it:**

| Problem | Solution | Owned By |
|---------|----------|----------|
| Full MEMORY load | Load one-liners only, grep for keywords | `/save` automation |
| Frontmatter slows reads | Read frontmatter-only first, load full file if needed | My workflow |
| Skill bloat | Invoke on-demand, never preload | My behavior |
| Old History clogs | `/save` auto-archives History >6 months | `/save` automation |
| Orphaned files | `/audit` finds + deletes orphaned content | `/audit` automation |

**Result:** Sessions stay fast. Context loads in seconds, not minutes.

## Token Efficiency Checklist

- [ ] `/save` runs automatically after major work (feature complete, section done, research finished)
- [ ] `/audit` runs weekly to catch structural bloat
- [ ] MEMORY.md stays <200 lines (old entries archived)
- [ ] Analyst frontmatter is current (last_updated recent)
- [ ] No orphaned folders (every folder has files + index)
- [ ] No broken wikilinks (audit catches these)
- [ ] History >6 months is archived (not in active files)
- [ ] Source files are never edited (immutable guarantee)

## When to Run Commands

**`/save [topic]`** after:
- Adding new Source files to that project
- Major section/feature completion
- Multiple dumps uploaded at once

**`/audit`** periodically:
- Weekly if high-volume work
- After large refactors
- Before running important analysis

**`/compact`** to signal:
- Section/paper complete
- Research phase finished
- Feature implemented and tested

## Example Optimization Over Time

**Day 1:** Initial FEDVT research
- You upload 5 Source files
- I synthesize to Analyst
- `/save FEDVT` reads all 5, creates cohesive structure
- Memory created: project_fedvt.md

**Week 1:** FEDVT progressing
- You add Methods section
- I update Analyst file
- `/save FEDVT` incorporates new Source
- History moves old content
- Memory updated: project_fedvt.md (status = in_progress)

**Month 1:** FEDVT research phase complete
- You signal `/compact`
- `/save FEDVT` archives old History
- Memory updated: project_fedvt.md (status = methods_complete)

**Later:** New project in unrelated domain
- `/save [NewProject]` creates fresh space
- Old FEDVT memory remains loaded, but isn't intrusive
- New memory files created only for new project
- Context stays clean

---

**Philosophy:** Optimization is automatic. You work; `/save` and `/audit` maintain the vault. No manual cleanup needed.
