---
name: audit
description: Vault structural cleaner. Detects and auto-fixes orphaned folders, missing indexes, duplicates, broken wikilinks. Surfaces naming violations and consolidation opportunities.
user-invocable: true
---

# /audit

Vault structural cleaner. Runs automatically after `/save` (Step 10) or standalone to maintain vault organization.

## Core Goal

Vault health is maintained by two concurrent checks:

**Check 1: Structural Integrity**
1. Scan all folders in `/02_Analyst/`, `/03_References/`, `/04_Archive/`
2. Create missing `_index.md` files (non-destructive)
3. Delete empty folders (destructive, logged)
4. Consolidate duplicate files (destructive, logged)

**Check 2: Link & Metadata Validation**
1. Detect broken wikilinks in frontmatter (`origin_dump`, `last_synced_dump`, `references`)
2. Surface naming violations (case, spacing, underscore inconsistencies)
3. Archive stale memory files (>6 months, status=complete)
4. Update `.vault-conflicts` unreviewed count

Result: Your vault stays clean and navigable. Orphaned structures are removed. Broken links are visible. Missing documentation is auto-created.

---

## Steps

### 0. Locate vault root

Read CLAUDE.md for vault path. Typically `C:\Users\shiva\obsidian\`.

### 1. Build inventory of vault structure

Scan `/02_Analyst/`, `/03_References/`, `/04_Archive/` recursively:
- List all folders (full paths)
- Count files per folder
- Check which folders have `_index.md`
- Identify empty folders (zero files) vs. index-only folders (only `_index.md`)
- Flag misplaced files at wrong hierarchy level

**Token efficient:** Use glob patterns to list folder structure in parallel:
- `glob("02_Analyst/**/_index.md")` → files with index
- `glob("02_Analyst/**/*.md")` → all markdown files
- Compare to find missing indexes

### 2. Create missing `_index.md` files

For every folder in `/02_Analyst/` or `/03_References/` **without** `_index.md`:

**Create with frontmatter:**
```yaml
---
title: [Folder name in Title Case]
description: [Brief description of folder purpose]
last_updated: [Today's date YYYY-MM-DD]
---
```

**Content pattern:**
```markdown
# [Folder Name]

📂 **Folder:** `/02_Analyst/path/to/folder/`

## Files in This Folder

- [[file1.md]] — Brief description of file1
- [[file2.md]] — Brief description of file2

## Navigation

- **Parent:** [[parent-index.md]]
- **Related:** [[../sibling-index.md]]
```

**Log:** Track each created index in report (count + file list).

### 3. Delete empty folders

For every folder with **zero files** (or **only `_index.md` that is empty placeholder**):

**Exceptions (NEVER delete these structural placeholders):**
- `/04_Archive/history/` — reserved for archived history sections
- `/04_Archive/memory-archive/` — reserved for old memory files

**For all others:**
- Delete folder entirely (including its `_index.md`)
- Log deletion in report: "Deleted N empty folders: [list]"
- User can recover from git history if needed

### 4. Consolidate duplicate files

Detect files that exist at two hierarchy levels (root-level **and** subfolder canonical version):

**Pattern to identify:**
- Same filename at parent level: `02_Analyst/career/internships/email-optimization-strategy.md`
- Same filename in subfolder: `02_Analyst/career/internships/strategy/email-optimization-strategy.md`

**For each duplicate pair:**
1. Compare file size + last modified timestamp
2. Verify subfolder version is canonical (typically more recent, more complete)
3. Delete root-level version (older/preliminary)
4. Log consolidation: "Consolidated: deleted root-level X, kept subfolder version"

### 5. Check for broken wikilinks

Scan frontmatter fields in all Analyst files for wikilinks:
- `origin_dump: [[...]]`
- `last_synced_dump: [[...]]`
- `references: [[...]]`

For each wikilink:
1. Extract path (e.g., `01_Source/internships/targets.md`)
2. Check if file exists at that path
3. If NOT FOUND: Add to "Broken Links" section of report
4. **Do NOT auto-fix** (fix is ambiguous — user judgment required)

**Log:** "N broken wikilinks need review: [file → broken_link]"

### 6. Surface naming violations

Scan **folder names only** (not files) in `/02_Analyst/` and `/03_References/`:

**Rule:** Folder names must be lowercase with hyphens only (no spaces, underscores, ALLCAPS, TitleCase).

**Violations to flag:**
- TitleCase: `ClinicalHours`, `Physics 206`, `FEDVT`
- ALLCAPS: `ETAM`, `ACTION-ITEMS`, `REFERENCE`, `RESEARCH`
- Underscores: `Question_Analysis`, `Year_Breakdowns`
- Spaces: `Physics 206`

For each violation:
- Current name: `[folder-path]`
- Suggested rename: `[lowercase-hyphenated-equivalent]`
- Add to report: "Naming Issues: [current] → [suggested]"

**Do NOT auto-rename** — would break all wikilinks pointing to the folder. User must rename manually with find-replace.

### 7. Archive stale memory files

Scan `C:\Users\shiva\.claude\projects\C--Users-shiva\memory\` directory:

For each file with:
- `last_updated:` older than 6 months AND
- `status: complete`

**Action:**
1. Move file to `memory/archive/[filename]` (create archive subfolder if needed)
2. Remove its entry from MEMORY.md
3. Log move: "Archived N stale memory files"

**Preservation rule:** Keep `last_updated` date in the filename or a comment so user knows when it was archived.

### 8. Update `.vault-conflicts` metadata

Read `.vault-conflicts` file:
- Count unreviewed entries (status: `awaiting_review`)
- Count resolved entries (status: `resolved`)
- Surface count in report: "Unreviewed conflicts: N"

(Do not modify conflict content; only count and report.)

### 9. Generate report

Output a structured summary:

```
✅ /audit Complete [timestamp]

🔧 Auto-Fixed:
- Created N missing _index.md files in: [list folders]
- Deleted N empty folders: [list]
- Consolidated N duplicate files: [list]
- Archived N stale memory files: [list]

⚠️ Needs Your Review (Next Actions):
- N broken wikilinks: [file1 → broken_link; file2 → broken_link]
- N naming violations (folders): [Path] → [suggested-name]
- Consolidation candidates: [5 single-file folders in 03_References/]

📊 Vault Health Score: [9/10 if healthy, lower if issues]
```

**Report format:** Emit this summary in stdout + append to audit log file: `C:\Users\shiva\.claude\audit-logs\[YYYY-MM-DD]_audit.md`.

---

## Key Principles

**Vault Automation:**
1. **Non-destructive first** — Create missing files before deleting empty ones
2. **Log everything** — Every action is tracked in report so user can understand what was done
3. **Git recovery possible** — All deletions are logged; user can `git restore` if needed
4. **Source untouchable** — Never scan, modify, or delete files in `/01_Source/`
5. **Structural exceptions** — `/04_Archive/history/` and `/memory-archive/` are placeholders; never delete even if empty

**Safety & Limits:**
6. **Never auto-rename** — Renames break wikilinks; user must do manually
7. **Never auto-repair wikilinks** — Broken links are surfaced for user review (fix is ambiguous)
8. **Preserve all memories** — Archive stale ones, never delete
9. **Consolidation needs verification** — Only consolidate when subfolder version is clearly canonical
10. **Report surface issues** — Consolidation candidates and naming violations are suggestions, not auto-executed

---

## Token Efficiency

**Parallel scanning (use glob):**
- Scan folder structure once using parallel glob patterns (one pass, not directory traversal)
- Compare results to identify missing indexes, empty folders, duplicates

**Wikilink validation:**
- Grep for frontmatter patterns (`origin_dump:`, `last_synced_dump:`) once
- Extract paths, test existence in parallel
- Do not read full file content unless necessary

**Memory archival:**
- Read memory file frontmatter only (grep for `last_updated:` and `status:`)
- No full-file reads unless archiving specific file
- Update MEMORY.md index only (append deletion lines)

**Report generation:**
- Aggregate counts first, then format output
- Write report to both stdout and audit-logs/ file

---

## Workflow Decision Tree

**When `/audit` runs (standalone or from `/save` Step 10):**

1. Step 0: Locate vault
2. Step 1: Scan structure (parallel glob)
3. Step 2: Create missing indexes (non-blocking)
4. Step 3: Delete empty folders (safe — no wikilinks to broken paths)
5. Step 4: Consolidate duplicates (safe — move to canonical location)
6. Step 5: Check broken wikilinks (surface only, no fixes)
7. Step 6: Surface naming violations (suggest only, no renames)
8. Step 7: Archive stale memory (no blocking)
9. Step 8: Update conflict count (read-only)
10. Step 9: Report output

**No blocking points.** All steps complete; report summarizes what was done + what needs user review.

---

## Integration with /save

`/save` calls `/audit` as **Step 10** immediately after `/save` Step 9 (Confirm and summarize):

```
### 10. Run Vault Audit

After synthesis is complete, run /audit to ensure vault structure is clean:
- Any new folders created during synthesis → get missing indexes
- Any broken wikilinks created → surface in audit report
- Any empty folders created → delete
- Include audit report in final /save summary

Append audit report to /save completion message under "🏥 Vault Audit" section.
```

**Result:** Every `/save` automatically triggers `/audit` → user gets both synthesis + cleanup in one command.

---

## Example Scenario: First `/audit` Run

**Input:** Raw vault state with known issues from exploration.

**Step 1 — Scan:**
- Discover 7 folders missing `_index.md` in `03_References/`
- Discover 6 empty folders (`Operations`, `Sales`, `REFERENCE`, `RESEARCH`, `Untitled`, `history`)
- Discover 6 root-level duplicate files in `internships/`

**Step 2 — Create indexes:**
- Create `03_References/Best-Practices/_index.md`
- Create `03_References/Frameworks/_index.md`
- Create `03_References/Patterns/_index.md`
- Create `03_References/Tools/_index.md`
- Create `03_References/Voice-Style/_index.md`
- Create remaining needed indexes

**Step 3 — Delete empty:**
- Delete `/04_Archive/Untitled/` (completely empty, not structural)
- Delete `/02_Analyst/projects/ClinicalHours/Operations/` (empty)
- Delete `/02_Analyst/projects/ClinicalHours/Sales/` (empty)
- Delete `/02_Analyst/career/internships/outreach/wave-4/REFERENCE/` (index-only)
- Delete `/02_Analyst/career/internships/outreach/wave-4/RESEARCH/` (index-only)
- **Keep** `/04_Archive/history/` and `/04_Archive/memory-archive/` (structural exceptions)

**Step 4 — Consolidate duplicates:**
- Delete `internships/email-optimization-strategy.md` (keep `strategy/email-optimization-strategy.md`)
- Delete `internships/flower-mound-ai-ops-targets.md` (keep `research/flower-mound-targets.md`)
- Delete 4 more root-level duplicates

**Step 5 — Broken wikilinks:**
- Flag: `flower-mound-ai-ops-targets.md` → `origin_dump: [[01_Source/Research/2026-04-14_ai-ops-targets]]` (path doesn't exist)
- Flag: 3 more broken Source paths

**Step 6 — Naming violations:**
- Suggest: `ClinicalHours` → `clinical-hours`
- Suggest: `Physics 206` → `physics-206`
- Suggest: 14 more folder renames

**Step 7 — Archive stale:**
- None yet (vault too new)

**Output Report:**
```
✅ /audit Complete [2026-04-15 14:35]

🔧 Auto-Fixed:
- Created 7 missing _index.md files in: Best-Practices, Frameworks, Patterns, Tools, Voice-Style, ...
- Deleted 5 empty folders: Untitled, Operations, Sales, REFERENCE, RESEARCH
- Consolidated 6 duplicate files: email-optimization-strategy, flower-mound-targets, ...

⚠️ Needs Your Review:
- 4 broken wikilinks: flower-mound-ai-ops-targets → [[01_Source/Research/...]]
- 16 naming violations (folders): ClinicalHours → clinical-hours, Physics 206 → physics-206, ...
- Consolidation candidates: 5 single-file folders in 03_References (consider flattening)

📊 Vault Health: 8/10 (healthy after auto-fixes; naming violations remain)
```

User then:
1. Fixes 4 broken wikilinks manually
2. Optionally renames folders per suggestions
3. Optionally flattens single-file folders

On next `/save`, `/audit` runs again → fewer issues.

---

## Error Handling

**Missing CLAUDE.md:** Fallback to `C:\Users\shiva\obsidian\` (typical location)

**Permission denied on delete:** Log error, skip that folder, continue (don't block entire audit)

**Unreadable files (corrupt frontmatter):** Flag in report, skip that file

**Wikilink points to file with no extension:** Accept both `[[file]]` and `[[file.md]]` formats

---

## For /save Integration

When modifying `/save` SKILL.md, add this exactly after Step 9:

```markdown
### 10. Run Vault Audit

After synthesis and archival complete, trigger the vault audit:

**Purpose:** Ensure new folders created by this save get indexes, new broken wikilinks are surfaced, empty folders are cleaned.

**Execute /audit:**
- Scan new structure (Step 1)
- Create missing indexes (Step 2)
- Delete any new empty folders (Step 3)
- Report findings (Step 9)

**Append to report:** Include audit summary under "🏥 Vault Audit" section of /save output.

If audit finds breaking issues (deleted files, consolidated duplicates), flag them prominently so user knows what changed.
```

Then update Step 9 output section to include an empty "🏥 Vault Audit" placeholder that gets filled by this Step 10 call.
