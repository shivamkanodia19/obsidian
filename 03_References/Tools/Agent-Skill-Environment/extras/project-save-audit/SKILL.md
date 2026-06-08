---
name: save-audit
description: Combined vault optimization - synthesizes Source to Analyst, updates Memory, fixes structure, and commits to git
type: skill
---

# /save-audit Workflow

Complete vault maintenance in one command. Synthesizes new Source files, updates all Analyst/Memory files, fixes structural issues, and commits changes to git.

## Invocation

```
/save-audit [topic]     # Save topic (e.g. /save-audit FEDVT)
/save-audit             # Audit entire vault and commit
```

## What It Does

### Phase 1: Source Detection & Synthesis (if topic specified)

1. **Scan for new Source files** in `/01_Source/[topic]/`
   - List all files in topic folder
   - Check for files created/modified since last sync
   
2. **Synthesize to Analyst:**
   - Read all new Source files
   - Create or update `/02_Analyst/[topic]/` files
   - Link all claims back to Source via wikilinks: `[[01_Source/...]]`
   - Add frontmatter: `origin_dump`, `last_synced_dump`, `references`, `last_updated: YYYY-MM-DD`
   
3. **Handle conflicts:**
   - If new Source contradicts old Analyst decision:
     - Move old content to `## History [YYYY-MM-DD]` section
     - Log conflict to `.vault-conflicts` file
     - Set `conflict_detected: true` in frontmatter (non-blocking)
   
4. **Update Memory:**
   - Create `memory/project_[topic].md` if new project
   - Update existing project memory with current status
   - Create `memory/feedback_[topic].md` if new feedback discovered
   - Add/update one-liner in `MEMORY.md` under 200 lines

5. **Create/update indexes:**
   - Create `_index.md` in every new folder (max 100 lines)
   - Update all parent folder indexes
   - Ensure navigation is current
   
6. **Archive old history:**
   - Move `## History` sections >6 months to `/04_Archive/[topic]_history_YYYY.md`
   - Keep active files lean

### Phase 2: Audit & Repair (always)

1. **Scan vault structure:**
   - Find orphaned folders
   - Find duplicates
   - Find misplaced files
   - Find broken wikilinks
   - Find missing `_index.md` files
   - Check whether root `INDEX.md` and `CLAUDE.md` are present and usable
   - Check all `_index.md` files are up-to-date

2. **Auto-fix structural issues:**
   - Delete orphaned folders
   - Seed or repair blank root `INDEX.md` and `CLAUDE.md`
   - Consolidate duplicates
   - Move misplaced files
   - Create missing `_index.md` files
   - Update stale indexes
   - Repair broken wikilinks

3. **Memory cleanup:**
   - Archive stale memories (>6 months, status=complete)
   - Remove unreachable memories
   - Validate frontmatter
   - Update MEMORY.md if needed

### Phase 3: Git Commit

1. Stage all changes
2. Create descriptive commit message with counts
3. Commit with co-author line
4. Report summary of changes

## When to Run

- After adding new Source files to a topic
- After major section/feature completion
- Weekly if high-volume work
- Before important analysis
