---
title: Obsidian Vault - Token Usage Optimization Audit
date: 2026-04-15
total_vault_size: 72M
active_files: 120
trash_files: 17
---

# Token Usage Optimization Audit

## Executive Summary

**Current State:**
- **Active Content:** 958 KB (~240,000 tokens)
- **Trash:** 1.9M (~475,000 tokens) — 33% of vault size is deleted content
- **Config Files:** .obsidian/ + plugins
- **Total Vault:** 72M (mostly binary plugin/media data)

**Key Finding:** Your vault has **low redundancy but HIGH wasted space in trash + one 34KB global config file.**

---

## 1. Token Distribution (Active Files)

| Category | Files | Tokens | % of Total | Issue? |
|----------|-------|--------|-----------|--------|
| Career (internships, research) | ~25 | 134,790 | 56% | Largest category; well-managed |
| CLAUDE.md (global config) | 1 | ~8,600 | 3.6% | See below |
| Academics (Physics, ETAM) | ~15 | 47,093 | 20% | Contains some redundancy |
| Research (FEDVT) | ~8 | 12,127 | 5% | Appropriately scoped |
| Projects (ClinicalHours) | ~5 | 20,180 | 8% | Well-organized |
| Other (_index files, etc) | ~66 | ~38,000 | 16% | Navigation + metadata |

**Total Active:** ~240,000 tokens

---

## 2. Top Token Consumers (Detailed)

| File | Tokens | Category | Status |
|------|--------|----------|--------|
| CLAUDE.md | 8,600 | Config | ⚠️ LARGE |
| READY-TO-SEND-TIER-1.md | 6,100 | Internship emails | ✅ Active |
| Exam3_Deep_Analysis.md | 6,200 | Physics study | ✅ Active |
| EVERY_PROBLEM_EXTRACTED.md | 4,450 | Physics study | 🔍 Redundant? |
| ALL_EXAMS_COMPREHENSIVE_ANALYSIS.md | 3,560 | Physics study | 🔍 Redundant? |
| industry-frameworks.md | 4,770 | Internship strategy | ✅ Active |
| Question_by_Question_Analysis.md | 4,450 | Physics study | 🔍 Redundant? |
| paper-draft-v1.md | 3,780 | FEDVT research | ✅ Active |

---

## 3. Redundancy & Waste Analysis

### Issue #1: Physics 206 - Multiple Comprehensive Analysis Files

**Problem:** The Physics 206 folder contains multiple "complete" analysis files with overlapping scope:

- `EVERY_PROBLEM_EXTRACTED.md` (4,450 tokens)
- `ALL_EXAMS_COMPREHENSIVE_ANALYSIS.md` (3,560 tokens)
- `COMPLETE_15_EXAM_ANALYSIS.md` (similar scope)
- `Question_by_Question_Analysis.md` (4,450 tokens)
- `MASTER_TOPIC_INDEX.md` (3,310 tokens)

**Assessment:** These are **likely partial duplicates** — different formats of the same exam data. At least 2-3 files appear to be summaries of overlapping content.

**Token Cost:** ~15,000 tokens tied up in redundant formats

**Recommendation:** 
- Keep ONE master file (`COMPLETE_15_EXAM_ANALYSIS.md` or rename to `Physics-206-Complete-Analysis.md`)
- Convert others to `.md.bak` or move to `.trash` if not actively used
- If multiple formats are needed, merge into a single file with multiple sections (by problem, by topic, by year)
- **Estimated Recovery:** 8,000-10,000 tokens

---

### Issue #2: CLAUDE.md Size (34 KB / 8,600 tokens)

**Problem:** Your global operating procedure is extremely comprehensive (which is good) but is read on every session.

**Content Breakdown:**
- 150+ lines of operational rules
- 200+ lines of memory system documentation
- 100+ lines of history + conflict management
- Folder organization rules, frontmatter schemas, command reference

**Assessment:** ✅ **This is appropriate.** Your vault has complex architecture; the config file justifies its size. BUT:

**Token Optimization Options (Low Priority):**

1. **Move to separate files** (would add reading overhead instead of saving):
   - Memory system → `/02_Analyst/VAULT-MEMORY-SYSTEM.md`
   - Folder rules → `/02_Analyst/VAULT-FOLDER-ORGANIZATION.md`
   - Status: ❌ **Not recommended** — splitting adds more reads at session start

2. **Compress rules** (minor savings, ~5%):
   - Collapse redundant examples
   - Move "See Also" links to `_index.md` instead
   - Estimated savings: 400 tokens

3. **Keep as-is** (recommended):
   - One read per session is efficient
   - Content is essential for vault operation
   - No token loss over time

**Decision:** Leave CLAUDE.md alone. It's a configuration investment that pays for itself.

---

### Issue #3: Trash Folder (1.9 MB / 475,000 tokens)

**Problem:** Your `.trash/` contains deleted content taking up 33% of total vault size.

**Contents:**
- Old strategy files (Dumps from April 14)
- Deprecated notes (2026-04-14 baselines)
- 17 markdown files with full content intact

**Assessment:** Trash is operational; Obsidian keeps deleted content for recovery. But check if any should be **permanently deleted:**

**Inspection Needed:**
- `2026-04-14.md` (likely daily note)
- `Dumps/` subfolder (old versions of current files?)
- `clinicalhours.md`, `csce120.md` (archived projects?)

**If permanently deleting:**
- Empty trash in Obsidian app (Ctrl+Shift+Delete or Settings → About → Empty Trash)
- **Estimated Recovery:** 475,000 tokens (~1.9 MB disk space)
- **Recommendation:** Keep trash for now (recovery safety). Delete when confident you don't need April 14 dumps.

---

## 4. Efficiency Metrics

| Metric | Status | Notes |
|--------|--------|-------|
| **Active file bloat** | ✅ Low | Most files 10-30KB; appropriately sized |
| **Index coverage** | ✅ High | Every folder has `_index.md`; good navigation |
| **Wikilink density** | ✅ Good | Files are cross-linked; easy to navigate |
| **Metadata overhead** | ✅ Minimal | Frontmatter is standard + concise |
| **Duplicate content** | ⚠️ Medium | Physics folder has 3+ versions of similar analyses |
| **Trash accumulation** | ⚠️ Medium | 1.9M of deleted content (but Obsidian norms) |
| **Plugin overhead** | ⚠️ Medium | .obsidian folder is heavy (binary plugin data) |

---

## 5. Token Usage by Time

**Active working memory (files you read in a session):**
- Typical session reads: CLAUDE.md (8.6K) + 3-5 Analyst files (5-15K each) + Memory index
- **Per-session cost:** ~30-50K tokens for navigation + context setup
- This is **normal and acceptable** for a complex vault

**Annual cost** (rough estimate, 100 sessions/year):
- Session overhead: 3-5M tokens/year
- This is < 1% of annual Claude usage if you're a regular user

---

## 6. Optimization Roadmap

### Quick Wins (30 minutes, save 8-10K tokens)

1. **Physics folder cleanup:**
   - [ ] Open `/02_Analyst/academics/Physics 206/Question_Analysis/`
   - [ ] Compare `EVERY_PROBLEM_EXTRACTED.md` vs `COMPLETE_15_EXAM_ANALYSIS.md` (are they the same?)
   - [ ] Keep one, `.trash` the redundant version
   - [ ] Merge `ALL_EXAMS_COMPREHENSIVE_ANALYSIS.md` into master file if scope overlaps

2. **Review trash:**
   - [ ] Check if `Dumps/` folder has any files you want to permanently delete
   - [ ] Empty Obsidian trash (safe once you confirm)

### Long-term (Post-exam)

3. **Physics archive:**
   - Once Physics 206 exam is done, move entire folder to `/04_Archive/` (frees 47K tokens from active memory)
   - Obsidian can still search archived content; just not loaded on session start

4. **Intern Wave history:**
   - Once Wave 4 closes, archive wave-3 and earlier
   - Keeps current-term work in active memory

---

## 7. Does Token Usage Matter?

**Short answer:** Not really, unless you're:
- ✅ Paying per-token at scale
- ✅ Reading your entire vault into Claude on every request
- ✅ Using `/resume` or `/save` frequently

**Token usage is optimized IF:**
- Active files are < 1M tokens → **✅ You're at 240K** (well within)
- Config file isn't reloaded repeatedly → **✅ Loaded once per session**
- Navigation is fast (wikilinks work, indexes are current) → **✅ Your structure is solid**

**Verdict:** Your vault is **token-efficient for its complexity.** The improvements above save ~10K tokens, which is ~2% of active content. Nice to have, not critical.

---

## 8. Recommendations Summary

| Priority | Action | Token Savings | Effort | Deadline |
|----------|--------|----------------|--------|----------|
| **High** | De-duplicate Physics 206 analyses | 8-10K | 30 min | Post-exam cleanup |
| **Medium** | Empty trash (after confirming) | 475K disk space | 5 min | When confident |
| **Low** | Archive completed projects to /04_Archive | Session load improvement | Ongoing | Post-project |
| **Ignore** | Split CLAUDE.md | 400 tokens | 1+ hr | Not worth it |

---

## Key Insight: Your Vault is Well-Designed

Most optimization gains come from **removing redundant analysis files** (Physics), not from architectural changes. Your three-layer system (Source, Analyst, References) is token-efficient by design:
- Source files are write-protected (no duplication)
- Analyst is synthesized (not raw dumps)
- References are curated (not duplicated)

**Do the Physics cleanup. Otherwise, you're in good shape.**

