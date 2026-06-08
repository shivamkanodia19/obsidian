# Vault Optimization Rules

**How `/save-audit` keeps context lean and findable.**

## Core Principle

**Atomic synthesis, not incremental bloat.**

Every `/save-audit` call reads new Source, synthesizes to Analyst, updates Memory, optimizes structure. One call maintains the entire vault in lean state.

## Key Metrics

- **MEMORY.md**: Must stay <200 lines (one-liners with keywords)
- **Folder indexes**: Must stay <100 lines each
- **Active files**: No History sections >6 months (archived instead)
- **Wikilinks**: Every claim links back to Source [[01_Source/...]]

## Structure

```
vault/
├── 01_Source/          [immutable, raw files]
├── 02_Analyst/         [synthesized, linked, one topic per file]
├── 03_References/      [curated frameworks, external citations]
├── 04_Archive/         [old history >6 months, completed projects]
└── MEMORY.md           [index of memory files, <200 lines]
```

## Principles

1. **One Concept Per File**
   - One project = one Analyst file
   - One decision = one memory file
   - One research area = one Research file

2. **Frontmatter Tells the Story**
   ```yaml
   origin_dump: [[01_Source/...]]      # Where did this come from?
   last_synced_dump: [[01_Source/...]] # Latest Source incorporated
   conflict_detected: true/false        # Any contradictions?
   last_updated: YYYY-MM-DD             # When was this refreshed?
   ```

3. **Wikilinks = Traceability**
   - Every claim links: According to [[01_Source/fedvt/...]], X is true
   - Cross-references: See [[02_Analyst/related_file.md]]
   - Frameworks: Related: [[03_References/theory.md]]

4. **History Moves, Not Deletes**
   - Active: File body contains current state
   - Stale: Move to `## History [YYYY-MM-DD]` section
   - Very old (>6 months): Move to `/04_Archive/`

5. **Memory Index (<200 lines)**
   - Load only one-liners in MEMORY.md
   - Keywords enable grep searches
   - Old entries archived when list grows long

## Token Efficiency Checklist

- [ ] `/save-audit [topic]` runs after major work (section done, research finished)
- [ ] `/save-audit` runs weekly to catch bloat
- [ ] MEMORY.md stays <200 lines (old entries archived)
- [ ] All frontmatter is current (last_updated recent)
- [ ] No orphaned folders (every folder has files + index)
- [ ] No broken wikilinks (audit catches these)
- [ ] History >6 months is archived (not in active files)
- [ ] Source files never edited (immutable guarantee)

## When to Run

**`/save-audit [topic]`** after:
- Adding new Source files to that project
- Major section/feature completion
- Multiple dumps uploaded at once

**`/save-audit`** periodically:
- Weekly if high-volume work
- After large refactors
- Before running important analysis

## Example: Lifecycle of FEDVT Research

**Day 1: Initial Research**
- Upload 5 Source files
- Run `/save-audit FEDVT`
- Creates Analyst files with links
- Memory created: project_fedvt.md

**Week 1: Progress**
- Add Methods section to Source
- Run `/save-audit FEDVT`
- Synthesizes new content
- History preserves old decisions
- Memory updated: status = in_progress

**Month 1: Phase Complete**
- Run `/save-audit FEDVT`
- Archives old History to `/04_Archive/`
- Memory updated: status = methods_complete

**Later: Paper Ready**
- All History archived
- Active files lean
- MEMORY.md references current state
- Context stays clean for new work

---

**Philosophy:** Optimization is automatic. You work; `/save-audit` maintains the vault. No manual cleanup needed.
