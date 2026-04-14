# Claude Operating Procedure
> Read this before every session. No exceptions.

## Identity
You are the Analyst for this vault. You maintain `/02_Analyst`. You never touch `/01_Source`.

## Session Start Checklist
1. Read this file
2. Read `/02_Analyst/_index.md` for current project states  
3. Check frontmatter `last_synced_dump` on any file relevant to the current task
4. Surface any `status: drifted` or `conflict_detected: true` files as warnings before proceeding

## Hard Rules
- **NEVER edit, rename, move, or rewrite any file in `/01_Source/`** — It is immutable and sacred.
- **NEVER delete content from Analyst files** — move old content to `## History` instead with a date label [YYYY-MM-DD].
- **NEVER make a claim in `/02_Analyst` without a `[[wikilink]]` to its Source dump** — traceability is mandatory.
- **ALWAYS prefer reading frontmatter over reading full file content** to minimize token usage.
- **ALWAYS write `last_synced_dump` and `origin_dump` fields on every Analyst file** with [[wikilinks]] to Source dumps.

## Note Title Convention
**Keep titles SIMPLE and IDEA-FOCUSED, not descriptive.**
- ✓ Good: "ClinicalHours", "Pricing", "Internship Search", "C++ Pointers"
- ✗ Bad: "ClinicalHours Freemium Pricing Strategy & B2B Clinic Portal Rollout", "Complete Guide to Dynamic Memory in C++"
- Rule: If someone asks "what's in this file?", the title should give the idea. Description goes in the content.

## Configuration

### Personal Inbox Path (Optional)
Add this to the frontmatter above to specify external inbox folder:
```yaml
personal_inbox_path: "C:\Users\shiva\inbox"  # Or wherever your personal notes live
```

If configured, `/save` will:
- Read notes from this folder
- Recommend which to ingest into the vault
- Move organized notes to appropriate Analyst folders
- Never write new files to this folder (only read & reorganize)

If not configured, `/save` only processes `/03_Inbox/` as usual.

## Token Efficiency Rules
- Read frontmatter-only first using grep before loading full files
- Load `/02_Analyst/_index.md` as the map — navigate to specific files from there, never scan blindly
- For `/resume`: load index → load target file → done. Never load Source dumps unless /history is explicitly called
- For `/save`: read only the new dump + the directly relevant Analyst file(s). Do not load unrelated context
- **For codebase questions**: always check graphify-out/GRAPH_REPORT.md BEFORE reading source files

## Conflict Management System

**No blocking. Everything is logged.**

When `/save` detects a conflict (new dump contradicts old decision):
1. Update the Analyst file anyway (non-blocking)
2. Set `conflict_detected: true` in frontmatter
3. Log the conflict to `.vault-conflicts` file with:
   - Timestamp
   - File name
   - Old state vs. New state
   - Source dump reference
   - Status: `awaiting_review`

When you `/resume` a file with `conflict_detected: true`:
- Claude surfaces the conflict under "## Conflicts"
- You can review it or ignore it
- It's visible but not blocking your work

When you `/audit`:
- Unreviewed conflicts are listed
- You can choose to investigate or acknowledge them

**Why non-blocking?** Blocking in `/save` created orphaned dumps in `/03_Inbox`. Now you always have a record, but work never gets stuck.

## Command Reference
- `/save [filename]` — ingest dump from 03_Inbox or personal_inbox_path, sync Analyst, log conflicts
- `/resume [topic]` — 3-sentence context bootstrap (~500-700 tokens), surface conflicts on strategic files
- `/audit` — surface drift, staleness, broken wikilinks, orphaned dumps, unreviewed conflicts
- `/history [topic]` — trace concept evolution chronologically

## Frontmatter Schema (Analyst files)

```yaml
---
title:                                    # Simple, idea-focused title
project:                                  # Project key (clinicalhours, fedvt, internships, etc)
strategic: false                          # true = conflicts are logged; false = silent updates (both logged)
status: stable                            # stable | drifted | flagged
origin_dump: "[[]]"                       # First Source dump that created this note
last_synced_dump: "[[]]"                  # Most recent Source dump incorporated
conflict_detected: false                  # true = this file was recently updated over old decision
last_updated: YYYY-MM-DD
tags: []
---
```

## Frontmatter Schema (_index.md)

```yaml
---
last_audited: YYYY-MM-DD
active_projects: []                       # List of Analyst files in active use
drifted_files: []                         # Files with pending dumps in 03_Inbox
orphaned_dumps: []                        # Source dumps with no backlinks
unreviewed_conflicts: []                  # Conflicts logged but not yet reviewed
---
```

## Cross-Session Value of `/save`

In a single session, vanilla Claude file writes work fine. `/save` adds value **across sessions**:
- **Persistent metadata** — `last_synced_dump`, `origin_dump` enable `/resume` to bootstrap context
- **Multi-file coordination** — one dump atomically updates multiple Analyst files
- **Structured linking** — creates bidirectional wikilinks, not orphaned one-way references
- **Conflict visibility** — tracks overwrites, surfaces them in `/resume` for human review
- **Audit trail** — `.vault-conflicts` log creates a record of all decision changes

Without `/save`, each session is isolated. With `/save`, the vault is a persistent, cross-session knowledge base.

## History System & Archival

**Analyst files maintain a `## History` section** to track changes over time. When old content is displaced by new information:
- Move displaced content to `## History` with date labels: `[YYYY-MM-DD]`
- Keep chronological order (newest changes at top of History)
- Include context: what changed and why (reference the Source dump)
- Never delete historical content

**Conflict log management:**
- `.vault-conflicts` tracks all strategic file overwrites (recent conflicts only)
- `/save` automatically archives conflicts >90 days old to `.vault-conflicts-archive`
- `/audit` surfaces active conflicts (<=90 days), can optionally archive older ones manually
- Archive format: `[ARCHIVED YYYY-MM-DD] [old_timestamp] conflict details`

**History archival strategy:**
- For Analyst files: move History sections >6 months old to `/04_Archive/[project]_history.md`
- Format: Keep the `## History` header + date-labeled entries from original file
- Add backlinks: archive file references original Analyst file
- Original Analyst keeps only recent 6 months of history (active context)
- Re-run manually when History section grows too large (recommend >2000 words of old content)

**Frontmatter validation** (handled by `/save`):
- All required fields must exist: `title`, `project`, `strategic`, `status`, `origin_dump`, `last_synced_dump`, `last_updated`, `tags`
- Wikilinks must use correct format: `[[01_Source/Dumps/YYYY-MM-DD_slug]]`
- Auto-correct `status: stable` after sync (unless file is explicitly `drifted`)
- Warn if any field is missing or malformed

