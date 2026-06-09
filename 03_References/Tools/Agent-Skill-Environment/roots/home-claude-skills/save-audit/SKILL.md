---
name: save-audit
description: Vault optimization skill that synthesizes Source to Analyst, updates Memory and indexes, fixes structure, and commits to git in one command
---

# /save-audit Skill

Combined vault optimization in a single command. Synthesizes new Source files to Analyst, maintains Memory and index files, repairs structural issues, and commits changes to git.

## When to Use This Skill

Invoke this skill when:
- Adding new Source files to a research topic
- Want to organize and refresh the entire vault structure
- Need to ensure all `_index.md` files stay current with folder contents
- Completed a major work phase and want to commit organized changes
- Running routine vault maintenance to improve token efficiency

## How to Invoke

```bash
/save-audit FEDVT                    # Synthesize FEDVT topic + audit + commit
/save-audit internships              # Synthesize internships topic + audit + commit
/save-audit                          # Full vault audit + fix structure + commit
```

## How the Skill Works

### Phase 1: Source Synthesis (if topic specified)

When invoked with a topic argument (e.g., `/save-audit FEDVT`):

1. **Detect new Source files** in `01_Source/[topic]/` created or modified since last sync
2. **Map to Analyst files** - Create or update corresponding files in `02_Analyst/[topic]/`
3. **Create wikilinks** - Link all claims back to Source: `[[01_Source/...]]`
4. **Update frontmatter** - Add `origin_dump`, `last_synced_dump`, `last_updated: YYYY-MM-DD`
5. **Handle conflicts** - Move contradictions to `## History [YYYY-MM-DD]` section, log to `.vault-conflicts`
6. **Update Memory** - Create `memory/project_[topic].md`, update `MEMORY.md` index (keep <200 lines)

### Phase 2: Vault Audit & Repair (always runs)

Regardless of topic, always scan and fix vault structure:

1. **Find missing indexes** - Identify folders without `_index.md`
2. **Validate root guides** - Ensure root `INDEX.md` and `CLAUDE.md` exist and are non-empty so fresh agents know what to load immediately
3. **Update stale indexes** - Refresh all `_index.md` files to match current folder contents (max 100 lines each)
4. **Find broken wikilinks** - Detect `[[...]]` links pointing to non-existent files
5. **Auto-fix issues** - Create missing indexes, seed or repair blank root guides, repair or flag broken links, consolidate duplicates
6. **Clean Memory** - Archive stale memories (>6 months old, status=complete), remove unreachable entries
7. **Archive old history** - Move `## History` sections >6 months to `/04_Archive/[topic]_history_YYYY.md`

### Phase 3: Git Commit

Commit all changes with descriptive message:

1. **Stage changes** - `git add -A`
2. **Create message** - If topic-specific: `vault optimization: [topic] synthesis + index updates`; else: `vault audit: structure fixes + memory cleanup + index updates`
3. **Commit** - With co-author line and change counts
4. **Report** - Show commit hash and summary of operations

## Implementation Details

To execute this skill, use the bundled Python script which handles:

- Detecting modified files by timestamp
- Parsing frontmatter and History sections
- Creating wikilinks with proper path formatting
- Validating index file structure and line counts
- Executing git commands safely with proper error handling
- Generating descriptive commit messages

See `scripts/save_audit.py` for the implementation and `references/OPTIMIZATION-RULES.md` for detailed vault organization principles.

## Token Efficiency Benefits

This skill improves token usage by:

- **Keeping active files lean** - Archives old History (>6 months) instead of storing in active files
- **Maintaining lean indexes** - MEMORY.md <200 lines, folder indexes <100 lines each
- **Auto-repairing structure** - Fixes issues before they compound and waste context
- **Removing duplicates** - Consolidates redundant content
- **Updating all frontmatter** - Ensures recent metadata for fast grepping and loading
- **One command instead of many** - Synthesis + audit + cleanup + commit in single invocation

## Output Example

```
============================================================
🔧 VAULT OPTIMIZATION: /save-audit
============================================================

📝 Synthesis Phase (FEDVT):
  ✓ Topic: FEDVT

📋 Vault Audit Phase:
  ✓ Created 2 missing index files
  ✓ Updated 5 stale index files
  ⚠️  Found 0 broken wikilinks

💾 Memory Cleanup:
  ✓ MEMORY.md validated

🔄 Git Commit Phase:
  ✓ Committed: abc1234 "vault optimization: FEDVT synthesis + index updates"

============================================================
✅ VAULT OPTIMIZATION COMPLETE
============================================================
```

## Files Included

- `scripts/save_audit.py` - Python implementation (detects Source, synthesizes Analyst, audits structure, commits git)
- `references/OPTIMIZATION-RULES.md` - Vault organization principles and philosophy
- Root `INDEX.md` and `CLAUDE.md` are also treated as first-class navigation artifacts and are repaired if blank or missing
