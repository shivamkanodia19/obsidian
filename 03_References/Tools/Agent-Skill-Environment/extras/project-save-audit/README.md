# /save-audit Skill

Combined vault optimization skill that synthesizes Source → Analyst, updates Memory, fixes structure, and commits to git.

## Usage

### Synthesis + Audit + Commit
```bash
/save-audit FEDVT        # Synthesize FEDVT, audit vault, commit
/save-audit internships  # Synthesize internships, audit vault, commit
```

### Full Audit + Commit (no synthesis)
```bash
/save-audit              # Audit entire vault, fix structure, commit
```

## What It Does

### Phase 1: Synthesis (if topic specified)
- Detects new files in `01_Source/[topic]/`
- Maps to Analyst files with wikilinks
- Creates/updates Analyst files
- Updates Memory (project + feedback files)
- Updates MEMORY.md index

### Phase 2: Audit (always)
- Finds and creates missing `_index.md` files
- Seeds or repairs blank root `INDEX.md` and `CLAUDE.md`
- Updates stale indexes with current folder contents
- Finds broken wikilinks
- Reports structural issues

### Phase 3: Git Commit
- Stages all changes: `git add -A`
- Creates descriptive commit message
- Commits with topic context

## Files

- `SKILL.md` - Skill specification and documentation
- `save_audit.py` - Python implementation
- `save-audit.sh` - Shell wrapper script
- `README.md` - This file

## Token Optimization Benefits

- Keeps active files lean (archives old history)
- Maintains lean indexes (MEMORY.md <200 lines)
- Auto-repairs structural issues before they compound
- Updates all `_index.md` files for consistent navigation
- Removes duplicates and orphaned content
- Ensures all frontmatter stays current

## Example Output

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
  ✓ Committed: abc1234

============================================================
✅ VAULT OPTIMIZATION COMPLETE
============================================================
```
