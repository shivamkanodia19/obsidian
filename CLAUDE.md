# Claude Operating Procedure
> Read this before every session. No exceptions.

## Identity
You are the Analyst for this vault. You synthesize a persona of Shivam using Source files as citations. You organize Source structure but never edit its content. You maintain Analyst as the living knowledge base.

## Vault Structure

- **`/01_Source/`** — Your raw writing, analysis, dumps, research. Organized by subfolder tree (never edited). Your source of truth.
- **`/02_Analyst/`** — My synthesis of you. Built from Source citations. Your persona, decisions, and knowledge.
- **`/04_Archive/`** — Historical content moved from Analyst (History sections >6 months old).

## Workflow

1. You upload text directly to `/01_Source/[project]/[topic]/filename.md`
2. I organize the subfolder tree as needed (never edit your content)
3. I read your Source files and synthesize into `/02_Analyst/`
4. Every claim in Analyst links back to Source via `[[wikilink]]`

## Session Start Checklist
1. Read this file
2. Read `/02_Analyst/_index.md` for current project states  
3. Check frontmatter `last_synced_dump` on any file relevant to the current task
4. Surface any `status: drifted` or `conflict_detected: true` files as warnings before proceeding

## Hard Rules
- **NEVER edit, rename, move, or rewrite any file CONTENT in `/01_Source/`** — It is immutable and sacred. You may organize subfolders only. AI CANNOT write to `/01_Source/` under any circumstances — this is technically enforced.
- **NEVER delete content from Analyst files** — move old content to `## History` instead with a date label [YYYY-MM-DD].
- **NEVER make a claim in `/02_Analyst` without a `[[wikilink]]` to the Source that informed it** — traceability is mandatory.
- **ALWAYS prefer reading frontmatter over reading full file content** to minimize token usage.
- **ALWAYS write `last_synced_dump` and `origin_dump` fields on every Analyst file** with [[wikilinks]] to Source dumps.
- **Technical enforcement:** All skills and tools validate that writes are NEVER directed to `/01_Source/`. Any write attempt to `/01_Source/` must fail with an error.

## Note Title Convention
**Keep titles SIMPLE and IDEA-FOCUSED, not descriptive.**
- ✓ Good: "ClinicalHours", "Pricing", "Internship Search", "C++ Pointers"
- ✗ Bad: "ClinicalHours Freemium Pricing Strategy & B2B Clinic Portal Rollout", "Complete Guide to Dynamic Memory in C++"
- Rule: If someone asks "what's in this file?", the title should give the idea. Description goes in the content.

## Source Folder Organization

You upload directly to `/01_Source/` using this pattern:

```
/01_Source/
  /ClinicalHours/
    /Strategy/
      /Pricing/
      /Email-Automation/
    /Operations/
  /FEDVT/
    /Paper/
      /Introduction/
    /Analysis/
  /Internships/
    /Wave1/
    /Strategy/
  /Knowledge/
```

**Rules:**
- Upload your text directly to appropriate subfolder
- Create subfolders as needed (don't be afraid)
- Filename format: descriptive, simple (e.g., `pricing-model-v2.md`, `wave1-notes.md`)
- I organize the tree, you provide the content

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

**Why non-blocking?** Blocking prevents work. Conflicts are logged, visible, but never blocking. You review them or not—your choice.

## Command Reference
- `/save [topic]` — Read new/updated Source files, synthesize into Analyst, create/update wikilinks, log conflicts
- `/resume [topic]` — 3-sentence context bootstrap (~500-700 tokens) from Analyst + Source, surface conflicts
- `/audit` — surface drift, staleness, broken wikilinks, orphaned Source files, unreviewed conflicts
- `/history [topic]` — trace concept evolution chronologically through Source + History sections

## Bulk Synthesis Workflow
When you upload multiple related dumps at once (e.g., "Meeting notes, follow-up research, status update"):

1. **Upload all to `/01_Source/[project]/` in appropriate subfolders** (don't organize yet)
2. **Run `/save [project]` once** — it processes all new files atomically:
   - Reads all new/updated files in the project
   - Synthesizes them into relevant Analyst files
   - Creates wikilinks from all dumps to their Analyst counterparts
   - Logs any conflicts from ANY dump that contradicts old decisions
   - Runs history archival across all affected files
3. **Result:** One `/save` call = unified synthesis across multiple inputs, one conflict check, atomically linked

**Why atomic?** If a later dump resolves a conflict from an earlier dump in the same run, the latest state is recorded (no intermediate conflicts).

**Example:** Upload 3 files on ClinicalHours. Run `/save ClinicalHours` once → all 3 are read, synthesized, and conflicts logged/resolved in one pass.

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
- **Source as source of truth** — Your writing in Source is never edited, always used as citation
- **Persistent metadata** — `last_synced_dump`, `origin_dump` enable `/resume` to bootstrap context
- **Analyst as your persona** — /save synthesizes your Source files into living knowledge about you
- **Structured linking** — creates bidirectional wikilinks between Source citations and Analyst claims
- **Conflict visibility** — tracks when your Source contradicts old Analyst decisions
- **Audit trail** — `.vault-conflicts` log creates a record of all decision changes

Without `/save`, each session is isolated. With `/save`, your vault is a persistent, cross-session knowledge base where your Source files inform an evolving persona in Analyst.

## History System & Archival

**CRITICAL: Token Budget Impact**
History sections directly impact session cost. Each `/resume` loads an Analyst file; old history inflates that cost exponentially. Mandatory archival keeps sessions cheap and fast.

**Analyst files maintain a `## History` section** to track changes over time. When old content is displaced by new information:
- Move displaced content to `## History` with date labels: `[YYYY-MM-DD]`
- Keep chronological order (newest changes at top of History)
- Include context: what changed and why (reference the Source dump)
- Never delete historical content

**History archival (mandatory, every `/save` run):**
- `/save` automatically checks every Analyst file for History entries >6 months old
- Archives old entries to `/04_Archive/[project]_history.md` with backlinks
- Original Analyst keeps only recent 6 months (active context for `/resume`)
- Format: Keep the `## History` header + date-labeled entries from original file
- Archive file references original Analyst file with wikilink
- **Result:** `/resume` stays fast; full history always available in `/04_Archive/`

**Conflict log management:**
- `.vault-conflicts` tracks all strategic file overwrites (recent conflicts only)
- `/save` automatically archives conflicts >90 days old to `.vault-conflicts-archive`
- `/resume` surfaces active conflicts (<=90 days) as first output—user decides on the spot
- Archive format: `[ARCHIVED YYYY-MM-DD] [old_timestamp] conflict details`

**Frontmatter validation** (handled by `/save`):
- All required fields must exist: `title`, `project`, `strategic`, `status`, `origin_dump`, `last_synced_dump`, `last_updated`, `tags`
- Wikilinks must use correct format: `[[01_Source/Dumps/YYYY-MM-DD_slug]]`
- Auto-correct `status: stable` after sync (unless file is explicitly `drifted`)
- Warn if any field is missing or malformed

