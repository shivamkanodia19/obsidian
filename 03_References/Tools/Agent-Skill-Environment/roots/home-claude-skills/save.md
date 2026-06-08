# /save Skill

## Purpose
Ingest dumps (from 03_Inbox or personal_inbox_path) into the vault, sync Analyst files, log conflicts for strategic files, and maintain cross-session organization. Enables persistent knowledge management across Claude sessions.

## Cross-Session Value
- **Persistent organization:** Not ephemeral in-session file writes, but *durable* organization that survives session restart
- **Metadata maintenance:** Updates `last_synced_dump`, `origin_dump` fields so `/resume` can bootstrap context
- **Multi-file coordination:** One dump can update multiple Analyst files atomically (coordinated decisions)
- **Structured wikilinks:** Creates bidirectional links, not just forward references
- **Conflict visibility:** Tracks overwrites to strategic files, surfaces them in `/resume` (non-blocking)

## Token Budget
Read only: the new dump file + directly relevant Analyst files. Load nothing else.

## Pre-flight Validation

- **Source immutability check:** Validate that NO write operations will target `/01_Source/` (except folder organization). Reject any operation that would write content to Source files. Throw error if attempted.

## Steps

1. **READ `claude.md` FIRST** (from vault root). Extract:
   - `personal_inbox_path` (if configured — external inbox folder Claude can read but not write)
   - All frontmatter rules

2. **SCAN for dumps** (in order of priority):
   - First: `/.claude/session-summaries/` for new session summary files (generated at end of each session)
   - Second: `/03_Inbox/` for new `.md` files
   - Third: `personal_inbox_path` for new notes to ingest (if configured)
   - Process oldest-first.
   - If multiple sources, process session-summaries first, then `/03_Inbox/`, then personal inbox.

3. **READ the dump**. Extract:
   - Project(s) referenced
   - Explicit decisions or pivots
   - Numbers, dates, named entities
   - Status changes, blockers, next steps

4. **MOVE dump to `/01_Source/Dumps/YYYY-MM-DD_[slug].md`**:
   - Do not alter content
   - Add single frontmatter block:
   ```yaml
   ---
   ingested: YYYY-MM-DD
   topics: [project1, project2]
   ---
   ```

5. **IDENTIFY affected Analyst files** from `_index.md` using project tags.

6. **FOR EACH relevant Analyst file:**
   
   a. Read frontmatter only (grep for --- blocks)
   
   b. Check if `strategic: true`:
      - If YES and dump contradicts current content:
        - **DO NOT BLOCK** (remove interactive halt)
        - Instead: log conflict to `.vault-conflicts` file:
          ```
          [2026-04-14 09:15] CONFLICT: clinicalhours.md
          Old: Pricing was $5.99/mo
          New: Changed to $4.99/mo
          Dump: 01_Source/Dumps/2026-04-14_clinicalhours-pricing
          Status: awaiting_review
          ```
        - Add `conflict_detected: true` to frontmatter
        - Proceed with update (non-blocking)
   
   c. Move contradicted content to `## History` with date label [YYYY-MM-DD]
   
   d. Integrate new information into main content sections
   
   e. Add wikilink to new Source dump in `## Sources` section
   
   f. Update frontmatter:
      - `last_synced_dump: [[01_Source/Dumps/YYYY-MM-DD_slug]]`
      - `last_updated: YYYY-MM-DD`
      - `status: stable`
      - `conflict_detected: false` (only true if strategic override happened)

7. **VALIDATE FRONTMATTER** (new):
   - For each updated Analyst file, verify all required fields present:
     - `title`, `project`, `strategic`, `status`, `origin_dump`, `last_synced_dump`, `last_updated`, `tags`
   - If any field missing, log warning to session output
   - Auto-correct `status` to `stable` after sync, unless file is `drifted`
   - Ensure wikilinks use correct format: `[[01_Source/Dumps/YYYY-MM-DD_slug]]`

8. **ARCHIVE STALE HISTORY ENTRIES** (mandatory):
   - For each Analyst file updated, check its `## History` section
   - Find all entries older than 6 months (check date labels [YYYY-MM-DD])
   - Move old entries to `/04_Archive/[project]_history.md`
   - Format: Keep `## History` header + date-labeled entries
   - Add backlink in archive file: `See original: [[02_Analyst/...]]`
   - Keep recent 6 months in original file (active context for `/resume`)
   - **Why:** Token cost—old history inflates session loads. This keeps `/resume` cheap.

9. **ARCHIVE STALE CONFLICTS**:
   - Read `.vault-conflicts` file if it exists
   - Find conflicts older than 90 days
   - Move them to `.vault-conflicts-archive` with timestamp
   - Keep recent conflicts (<=90 days) in active `.vault-conflicts`
   - Log archival action to `.vault-conflicts-archive` with: `[ARCHIVED 2026-04-14] Old conflicts moved from .vault-conflicts`

10. **HANDLE personal_inbox_path** (if configured):
    - Read notes from personal inbox folder
    - Recommend which to ingest (don't force)
    - If user approves, organize them into appropriate Analyst folders
    - Log organization decisions to a `.vault-ingestion-log`

11. **CREATE SESSION SUMMARY** (at end of session, Claude-generated meta-work):
    If `/save` is run at session end (detected by absence of new dumps AND multiple Analyst files updated), automatically generate:
    
    **File:** `/.claude/session-summaries/YYYY-MM-DD-session-summary.md`
    
    **Content:**
    ```markdown
    ---
    title: Session Summary — [YYYY-MM-DD]
    type: session-summary
    projects: [project1, project2]
    date: YYYY-MM-DD
    duration_estimate: [e.g., "2 hours"]
    ---
    
    # Session Summary [YYYY-MM-DD]
    
    ## What We Discovered
    - [Finding 1 with context]
    - [Finding 2 with context]
    
    ## Decisions Made
    - [Decision 1: rationale + next step]
    - [Decision 2: rationale + next step]
    
    ## Artifacts Created
    - [[artifact-1]] — description
    - [[artifact-2]] — description
    
    ## Blockers Identified
    - [Blocker 1]: impact + resolution needed
    - [Blocker 2]: impact + resolution needed
    
    ## Next Session Should
    - [ ] Action item 1
    - [ ] Action item 2
    
    ## Files Updated
    - [[02_Analyst/...]] (status change)
    - [[02_Analyst/...]] (decision logged)
    ```
    
    **Rules:**
    - Auto-generate from conversation if `/save` is called without new Source dumps (indicates end-of-session synthesis)
    - Save to `/.claude/session-summaries/` (NOT in `/01_Source/` — session summaries are my meta-work, not your source material)
    - Ask user to approve/edit before saving
    - Once approved, `/save` processes it as a regular dump and synthesizes into Analyst + memory
    - Enables next session to load session context via `/resume`

12. **COMPREHENSIVE FOLDER CLEANUP & AUDIT** (at end of `/save`):
    After all synthesis complete, run aggressive cleanup to maintain vault health:
    
    **AUDIT PHASE 1: Folder Structural Cleanup**
    - **Delete orphaned folders:** Any folder with no `.md` files (only subdirectories or empty)
    - **Delete empty archive folders:** Any folder in `/04_Archive/` that's empty
    - **Consolidate single-file folders:** If a folder contains only 1 file and 1 index.md, move file to parent folder + delete empty folder
    - **Cleanup recursive:** Apply rules bottom-up (deepest folders first)
    - **Safe:** Never delete `/02_Analyst/`, `/03_References/`, `/04_Archive/`, `/01_Source/` root folders or any folder explicitly referenced in `.claude/CLAUDE.md`
    
    **AUDIT PHASE 2: Link Validation & Orphan Detection**
    - **Check all Source dumps are linked:** Scan `/01_Source/Dumps/` — every `.md` file must be referenced in at least one Analyst `last_synced_dump` link
      - Orphaned dumps = not synced, flag for manual review + log to `.vault-orphaned-sources`
    - **Remove broken wikilinks:** Check all frontmatter links (`origin_dump`, `last_synced_dump`, `references`) — if they point to deleted files, remove the link
    - **Report findings:** List all broken links + orphaned sources to user at end
    
    **AUDIT PHASE 3: Metadata Consistency**
    - **Validate frontmatter:** Every Analyst file must have: `title`, `project`, `strategic`, `status`, `origin_dump`, `last_synced_dump`, `last_updated`, `tags`
      - Missing field = log to `.vault-frontmatter-issues` with file path + missing fields
    - **Check project tags:** Every Analyst file's `project` tag must match one in `/02_Analyst/_index.md` active_projects list
      - Mismatch = likely file from old/deleted project, flag for review
    - **Memory file validation:** Every entry in MEMORY.md must link to existing file in `./`
      - Dead index entry = remove from MEMORY.md, log to `.vault-cleanup-log`
    
    **AUDIT PHASE 4: Stale Content Detection**
    - **Flag stale folders:** Any folder in `/02_Analyst/` NOT updated in 6+ months
      - Log to `.vault-stale-folders` with last-modified date
      - Don't delete (preservation for historical context) but surface for potential archival
    - **Identify unused files:** Any Analyst file NOT synced with new Source in 6+ months
      - Log to `.vault-inactive-files` 
    
    **AUDIT PHASE 5: Index & Navigation Repair**
    - **Re-index all parent folders:** Refresh every parent folder's `_index.md` to match actual contents
    - **Update `/02_Analyst/_index.md`:**
      - `last_audited: YYYY-MM-DD`
      - `active_projects:` — list all projects with active files
      - `drifted_files:` — files with `conflict_detected: true`
      - `orphaned_sources:` — count from `.vault-orphaned-sources`
      - `unreviewed_conflicts:` — count from `.vault-conflicts` (≤90 days old)
      - `structural_issues:` — count of metadata/link problems found
    
    **AUDIT PHASE 6: File Reorganization for Fast Retrieval**
    Goal: Minimize hops needed to find info; reduce context cost on next load.
    
    - **Flatten deep folder hierarchies:** If path is `/02_Analyst/project/subtopic/subtopic/file.md` (4+ levels), move to `/02_Analyst/project/subtopic-file.md` (2 levels)
      - Exception: Keep hierarchies if they have meaningful index.md files at each level
    - **Consolidate single-project folders:** If a project has only 1-2 active files, move them to parent `/02_Analyst/` level (not orphaned, still tagged by project)
    - **Create root-level lookup index:** Generate `/02_Analyst/QUICK_INDEX.md` listing:
      - Active projects (with file count + status)
      - Recent Analyst files (modified <30 days)
      - Strategic files (marked `strategic: true`)
      - Active memory files (from MEMORY.md)
      - One-line hook for each (what it contains, not full description)
    - **Memory file consolidation (optional):** If memory/ has >20 files, suggest grouping by topic (e.g., `memory/system_*.md` → `memory/_systems/`, `memory/feedback_*.md` → `memory/_feedback/`)
      - Only if user approves; don't force restructuring
    - **Update MEMORY.md index:** Ensure it lists ONLY active memory files; remove entries for archived files
    - **Prune forgotten index references:** Audit every folder's `index.md` — remove entries for deleted files
    
    **Reorganization Log:**
    - Log all moves to `.vault-reorganization-log` with timestamp + paths moved
    - Example: `[2026-04-16 15:00] MOVED /02_Analyst/old-project/deep/nested/file.md → /02_Analyst/old-project-file.md`
    
    **Cleanup Logs Generated:**
    - `.vault-cleanup-log` — deleted folders + reason (e.g., "empty", "consolidated")
    - `.vault-orphaned-sources` — Source dumps with zero Analyst links
    - `.vault-frontmatter-issues` — files with missing/invalid metadata
    - `.vault-stale-folders` — folders not modified in 6+ months
    - `.vault-inactive-files` — Analyst files not synced in 6+ months
    - `.vault-reorganization-log` — file moves for flattening + consolidation

13. **CREATE/UPDATE folder-level `index.md` files** (new):
    For every subfolder touched during organization or synthesis, create/update an `index.md`:
    
    **Pattern:**
    ```
    /01_Source/Internships/
      index.md          ← documents what's in Internships/
      Wave1/
        index.md        ← documents what's in Wave1/
        tracking.md
      Strategy/
        index.md        ← documents what's in Strategy/
        research.md
    ```
    
    **Index format:**
    ```markdown
    ---
    title: [Folder name] Index
    folder: [path/to/folder]
    last_updated: YYYY-MM-DD
    ---
    
    # [Folder name]
    
    ## Contents
    
    - [[filename.md]] — one-line description
    - [[subfolder/]] — subfolder with X files
    
    ## Recent Changes
    
    [YYYY-MM-DD] Added/updated [item]
    
    ## Navigation
    
    Parent: [[../index.md]]
    ```
    
    **Rules:**
    - Create index.md in every subfolder you touch
    - List direct children (files + subfolders with brief descriptions)
    - Update "Recent Changes" when files are added/modified
    - Keep it scannable for agents
    - Do this for **both** `/01_Source/` and `/02_Analyst/` folder hierarchies

11. **UPDATE `_index.md`**:
    - Update `last_audited` to today
    - Refresh `active_projects` list
    - Update `unreviewed_conflicts` count from `.vault-conflicts`

13. **PRINT detailed audit summary**:
   ```
   ✓ Vault synthesis complete
   
   📁 Organization:
   → Moved to 01_Source/Dumps/YYYY-MM-DD_slug.md
   → Updated [N] Analyst files
   → Created/updated [N] folder index.md files
   
   🔗 Validation:
   → Validated [N] frontmatter blocks
   → [N] broken wikilinks removed
   → [N] orphaned Source dumps found (see .vault-orphaned-sources)
   
   📋 Conflicts & Issues:
   → [N] strategic conflicts logged (review in /resume)
   → Archived [N] stale conflicts (>90 days)
   → [N] metadata issues flagged (see .vault-frontmatter-issues)
   → [N] stale folders identified (see .vault-stale-folders)
   
   🧹 Cleanup:
   → Deleted [N] empty folders
   → Consolidated [N] single-file folders
   → Removed [N] dead index entries from MEMORY.md
   → See .vault-cleanup-log for full deletion record
   
   ⚠️ Action Items (if any):
   - Review .vault-orphaned-sources if count > 0
   - Check .vault-frontmatter-issues for metadata gaps
   - Consider archiving folders in .vault-stale-folders
   
   ✓ Vault is lean and ready for next agent
   ```

## Notes
- Use wikilinks: `[[01_Source/Dumps/YYYY-MM-DD_slug]]`
- Strategic files are now non-blocking but logged. User reviews conflicts in next `/resume`.
- Every Source dump must be linked from at least one Analyst file (checked by `/audit`)
- Never orphan a dump—link it immediately or flag for manual review
- Frontmatter validation ensures metadata consistency across sessions
- Conflict archival prevents `.vault-conflicts` from growing unbounded
