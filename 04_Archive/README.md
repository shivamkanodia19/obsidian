---
name: "Archive Directory Guide"
description: "Documentation for the Archive system organizing old memory, history, and reference materials"
type: "guide"
created: "2026-04-15"
---

# Archive Directory Structure

This directory contains materials moved from active vault folders when they exceed age thresholds or are superseded. The Archive is organized into three sections for rapid discovery.

## Directory Layout

```
04_Archive/
├── README.md                    # This file
├── memory-archive/              # Old memory files (>6 months)
│   └── [year-month]/
│       └── *.md                 # Archived memory entries
├── history/                     # History sections moved from active files
│   └── [original-filename]/
│       └── history-YYYY-MM-DD.md
└── reference-archive/           # Superseded reference materials (optional)
    └── [topic]/
        └── *.md
```

## Subdirectories

### memory-archive/
**Purpose:** Stores memory files older than 6 months.  
**Organization:** Sorted by year-month folder (e.g., `2025-10/`, `2025-11/`)  
**Contents:** Complete archived memory entries that are no longer active but may be needed for historical context.  
**Access Pattern:** Agents rarely need these unless researching historical decisions.

**Example:**
```
memory-archive/
├── 2025-09/
│   ├── project_old_campaign_v1.md
│   ├── feedback_archived_writing_style.md
│   └── system_deprecated_email_framework.md
├── 2025-10/
│   └── project_internship_2025.md
```

### history/
**Purpose:** Stores history sections moved out of active files to keep them focused.  
**Organization:** Subfolder per original file, dated history snapshots inside.  
**Contents:** Historical changes, iterations, or context that once lived in active files.  
**Access Pattern:** Used when you need to understand how something evolved.

**Example:**
```
history/
├── project_clinicalhours_strategy/
│   ├── history-2026-01-15.md    # Historical market research
│   ├── history-2026-02-01.md    # Earlier pricing iterations
│   └── history-2026-03-20.md    # Team structure changes
├── project_fedvt_paper/
│   ├── history-2026-02-10.md    # Introduction drafts v1-v2
│   └── history-2026-03-01.md    # Rejected methodology notes
```

### reference-archive/ (Optional)
**Purpose:** For superseded or outdated reference materials.  
**Organization:** By topic (CTA variants, email templates, etc.)  
**Contents:** Old versions that may be useful for learning patterns but aren't active.  
**Access Pattern:** Rarely accessed, mainly for pattern research.

## When to Archive

### Move to memory-archive/ when:
- A memory entry hasn't been updated in 6+ months
- The project/feedback is complete or on indefinite hold
- You need to declutter MEMORY.md but preserve the context

### Move to history/ when:
- An active file has accumulated >20 lines of historical notes
- You want to keep file focus on current state, not evolution
- Multiple dated sections make active file hard to scan

### Move to reference-archive/ when:
- A Reference file's iteration chain is superseded by newer work
- Old testing variants are no longer relevant but worth keeping

## Archiving Procedure

**Step 1: Identify candidates**
```bash
# Find memory files older than 6 months
find .claude/projects/C--Users-shiva/memory -name "*.md" -mtime +180
```

**Step 2: Create dated snapshot**
```
# In archive folder, create: history-YYYY-MM-DD.md
# Copy the history section or entire old file content
# Add timestamp in frontmatter
```

**Step 3: Remove from active location**
- Delete or archive the original memory entry
- Update MEMORY.md index if entry was listed

**Step 3: Link from active file**
- If keeping the active file, add a link: "See: `/04_Archive/history/[original-name]/history-YYYY-MM-DD.md` for history"

## Finding Archived Materials

### By Recency
```bash
ls -lt memory-archive/2026-*/  # Most recent archives first
```

### By Topic
Archive directory structure mirrors vault structure, so:
- `memory-archive/` mirrors `/memory/`
- `history/` preserves original filenames

### Searching Content
```bash
grep -r "search-term" /04_Archive/
```

## Guidelines for Archiving Agents

1. **Preserve Frontmatter:** Always keep YAML frontmatter when moving files.
2. **Add Archive Timestamp:** Include a line in frontmatter: `archived: "2026-04-15"`
3. **Link from Original:** If keeping an active version, add reference link at bottom.
4. **Never Delete:** Archive, don't destroy. Old context has value.
5. **Update Index:** If the archived item was in MEMORY.md, update that index.

## Archive Cleanup Schedule

- **Quarterly Review:** Check for orphaned or forgotten archived items
- **Annual Consolidation:** Move older monthly archives into year folders
- **Permanence Threshold:** Items >2 years old can be considered for permanent deep archive

---

**Last Updated:** 2026-04-15  
**Archive Version:** 1.0  
**Next Review:** 2026-07-15 (quarterly)
