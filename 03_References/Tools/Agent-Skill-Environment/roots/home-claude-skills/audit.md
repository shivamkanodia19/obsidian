# /audit Skill

## Purpose
Surface vault health issues passively. Identifies drift, staleness, orphans, broken wikilinks, and strategic file conflicts.

## Pre-flight Validation

- **Source immutability check:** All writes performed by /audit are limited to `/02_Analyst/`, `/04_Archive/`, and metadata files (`.vault-conflicts`, `_index.md`). NEVER write to `/01_Source/` file content. Throw error if attempted.

**Modes:**
- `/audit` — Report-only (no changes)
- `/audit --fix` — Interactive fixes (auto-handle safe issues, ask about judgment calls)

## Token Budget
Read frontmatter only across all Analyst files. Never load full content.

## Modes Explained

### Report Mode (`/audit`)
- Reads vault
- Reports all issues
- Makes no changes
- You decide what to fix

### Fix Mode (`/audit --fix`)
- Reads vault
- Auto-fixes safe issues (metadata, formatting)
- Asks interactively about judgment calls (contradictions, orphaned files, stale content)
- Updates Analyst files based on your responses
- Reports all changes made

## Steps

1. **READ `claude.md`** (vault root). Extract configuration.

2. **SCAN all files in `/02_Analyst/`** — read frontmatter only:
   - Extract `status`, `last_updated`, `last_synced_dump`, `strategic`

3. **CHECK WIKILINKS** (new):
   - For each `[[link]]` in Analyst frontmatter, verify the target file exists
   - Flag broken links (target file not found)
   - Flag orphaned dumps (Source files with zero backlinks from Analyst)

4. **CHECK STRATEGIC CONFLICTS** (new):
   - Read `.vault-conflicts` log if it exists
   - List all recent overwrites to `strategic: true` files
   - Flag as "awaiting review" if user hasn't acknowledged
   - Identify conflicts older than 90 days (ready for archival)

5. **CLEAN UP CONFLICT LOGS** (new):
   - Check if `.vault-conflicts` exists
   - Archive conflicts older than 90 days to `.vault-conflicts-archive`
   - Report archive actions in audit output
   - Maintain clean `.vault-conflicts` (only current/recent conflicts)

6. **COLLECT:**
   - Files where `status: drifted` (indicates unsynced dumps in 03_Inbox)
   - Files where `last_updated` > 30 days ago (potentially stale)
   - Files where `last_synced_dump` is empty, broken, or missing
   - Broken wikilinks (targets don't exist)
   - Orphaned dumps (Source files with zero backlinks)
   - Unreviewed strategic conflicts

7. **IF FIX MODE (`--fix`), HANDLE ISSUES INTERACTIVELY:**

   **Auto-fix (silent):**
   - Missing frontmatter fields → add with defaults
   - Malformed timestamps → correct to YYYY-MM-DD format
   - Empty `tags: []` → validate structure
   - Missing `last_updated` → set to today

   **Interactive prompts:**
   
   For each **broken wikilink:**
   ```
   [[02_Analyst/projects/fedvt.md]] references [[01_Source/nonexistent.md]]
   Delete link or mark as external? [d/mark/skip]: 
   ```
   
   For each **contradiction** (new Source vs. old Analyst state):
   ```
   Contradiction in clinicalhours.md:
   Old: "B2C pricing is $4.99/mo"
   New: "Testing B2C at $7.99" (from 2026-04-14)
   Keep new version? [y/n]: y
   → Updates Analyst, moves old to History [2026-04-14]
   ```
   
   For each **orphaned Source file:**
   ```
   Orphaned: [[01_Source/ClinicalHours/old-strategy-v1.md]]
   No backlinks from Analyst. Archive or delete? [a/d/skip]: a
   → Moves to /04_Archive/ or deletes (your choice)
   ```
   
   For each **stale file** (>30 days):
   ```
   Stale: [[02_Analyst/projects/csce120.md]] (last updated 2026-03-10)
   Update status to drifted? [y/n]: n
   ```

8. **OUTPUT:**
```
## Vault Audit — [date]

### Health Summary
- Links: [N] broken, [N] verified OK
- Dumps: [N] orphaned, [N] anchored
- Strategic conflicts: [N] awaiting review

### Drifted Files (need re-sync)
- [[02_Analyst/projects/clinicalhours.md]] (3 dumps in 03_Inbox waiting)
- [count: N]

### Potentially Stale (>30 days)
- [[02_Analyst/academics/csce120.md]] (last updated 2026-03-10)
- [count: N]

### Broken Wikilinks
- [[02_Analyst/projects/fedvt.md]] → references [[01_Source/Dumps/nonexistent]] (file not found)
- [count: N]

### Orphaned Dumps (not yet anchored)
- [[01_Source/Dumps/2026-04-12_random-note.md]] — no backlinks from Analyst files
- [count: N]

### Unreviewed Strategic Conflicts
- [[02_Analyst/projects/clinicalhours.md]] — overwritten 2026-04-14 by dump X (awaiting acknowledgment)
- [count: N]

### Conflict Log Archival (new)
- [N] old conflicts archived to .vault-conflicts-archive (>90 days old)
- Archival date: YYYY-MM-DD
- See .vault-conflicts-archive for historical record
```

7. **CREATE/UPDATE folder-level `index.md` files**:
   - For every folder scanned during audit, update or create `index.md` if missing
   - Same format as in `/save`: document contents, recent changes, navigation
   - Mark any folders with issues (orphaned files, broken links) in the index
   - This ensures agents can quickly understand vault state at each level

8. **UPDATE `_index.md`**:
   - Set `last_audited: YYYY-MM-DD`
   - Update `drifted_files`, `orphaned_dumps`, `broken_links`
   - Add `unreviewed_conflicts: []` (new field)
   - Add `conflict_archive_date: YYYY-MM-DD` (last archival run)

## Notes
- Wikilink check: validate syntax `[[path/to/file]]` and file existence
- Orphaned dumps: grep all Analyst files for backlinks to each Source dump
- Strategic conflicts: read `.vault-conflicts` log (created by `/save`)
