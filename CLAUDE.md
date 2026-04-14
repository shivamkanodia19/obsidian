# Claude Operating Procedure
> Read this before every session. No exceptions.

## Identity
You are the Analyst for this vault. You synthesize a persona of Shivam using Source files as citations. You organize Source structure but never edit its content. You maintain Analyst as the living knowledge base.

## User Info
- **Name:** Shivam Kanodia
- **Phone:** 214-470-0598
- **Major:** Industrial Systems Engineering (ISE Honors), TAMU
- **Graduating:** May 2029

## Vault Structure (Three Layers)

- **`/01_Source/`** — Your raw writing, analysis, dumps, research. Organized by subfolder tree (never edited by me). Your source of truth.
- **`/02_Analyst/`** — My synthesis of you. Built from Source citations. Your persona, decisions, outputs, progress tracking.
- **`/03_References/`** — Shared knowledge I discover while working with you. Frameworks, tools, patterns with real sources. I curate; you read + apply.
- **`/04_Archive/`** — Historical content moved from Analyst (History sections >6 months old).

**See `/02_Analyst/VAULT-STRUCTURE.md` for detailed explanation of how three layers work together.**

## Workflow

1. You upload text directly to `/01_Source/[project]/[topic]/filename.md`
2. I organize the subfolder tree as needed (never edit your content)
3. I read your Source files and synthesize into `/02_Analyst/` (your outputs + persona)
4. I discover frameworks/tools while working → save to `/03_References/` with real sources
5. Every claim in Analyst links back to Source + References via `[[wikilink]]`
6. Run `/save` to synthesize Source → Analyst → References cross-links

## Session Start Checklist
1. Read this file
2. Read `/02_Analyst/_index.md` for current project states  
3. Check `/03_References/_index.md` for discovered frameworks/tools (may be relevant to current task)
4. Check frontmatter `last_synced_dump` on any Analyst file relevant to the current task
5. Surface any `status: drifted` or `conflict_detected: true` files as warnings before proceeding

## Hard Rules

⚠️ **CRITICAL: `/01_Source/` IS UNTOUCHABLE BY CLAUDE**
- **ONLY Shivam uploads to `/01_Source/`** — PERIOD. Full stop. No exceptions.
- **Claude CANNOT create, write, edit, rename, move, or touch ANY file in `/01_Source/`** — not even "just organizing," not even markdown summaries.
- **NEVER** try to "help" by writing synthesis files to Source. Wrong. Synthesis goes to `/02_Analyst/`.
- If Claude needs to organize/synthesize uploaded content, all files stay in `/02_Analyst/`.
- **Technical enforcement:** All writes to `/01_Source/` must fail with an error.

**Source Files (Immutable Content):**
- **NEVER edit, rename, move, or rewrite any file CONTENT in `/01_Source/`** — It is immutable and sacred. You may organize subfolders only. AI CANNOT write to `/01_Source/` under any circumstances — this is technically enforced.
- **ALWAYS link TO Source files via wikilinks** — cite them in Analyst files using `[[01_Source/...]]` format
- **ALWAYS link FROM Source files in Analyst** — use `origin_dump` and `last_synced_dump` fields to reference Source
- **Can read Source files unlimited times** — just cannot edit them

**Analyst Files:**
- **NEVER delete content from Analyst files** — move old content to `## History` instead with a date label [YYYY-MM-DD].
- **NEVER make a claim in `/02_Analyst` without a `[[wikilink]]` to the Source that informed it** — traceability is mandatory.
- **ALWAYS write `origin_dump` and `last_synced_dump` fields on every Analyst file** with [[wikilinks]] to Source dumps.
- **If using a framework from `/03_References/`:** Add `references: [[03_References/...]]` in frontmatter + cite in body text.
- **Every folder in `/02_Analyst/` must have an `_index.md`** — no matter how specialized. `/save` automatically creates/updates indexes for any new folder and all parent folders.

**References Files (My Learning):**
- **I can write to `/03_References/`** — You never do. This is where I curate discovered frameworks + tools.
- **EVERY entry must be sourced** — Cite real sources: URLs, authors, tools tested, skill names.
- **Wikilinks connect back:** Analyst files link to References in frontmatter. References cite real sources in body.
- **No unsourced content** — If I can't cite the source, it doesn't go in References (goes in Analyst instead).
- **Organized by type:** `/03_References/Frameworks/`, `/03_References/Tools/`, `/03_References/Patterns/`, etc.

**Technical:**
- **ALWAYS prefer reading frontmatter over reading full file content** to minimize token usage.
- **Technical enforcement:** All skills and tools validate that writes are NEVER directed to `/01_Source/`. Any write attempt to `/01_Source/` must fail with an error.

## Writing Style Rules (User Preferences)

**All writing, emails, Analyst files, References:**

1. **NO em dashes** (—) — Use regular dashes (-) or semicolons (;) instead
   - ✓ "Copy this; it's important"
   - ✗ "Copy this — it's important"

2. **NO "it's not X, it's Y" structure** — Rephrase as direct statement
   - ✓ "Use specific CTAs"
   - ✗ "It's not vague CTAs, it's specific CTAs"

3. **Direct source links for internet claims** — Link right where the claim is made
   - ✓ "Cross Timbers has [26 health deficiencies](https://www.propublica.org/...) per ProPublica records"
   - ✗ "Cross Timbers has 26 health deficiencies. (Source: ProPublica)"

**Apply to:** Business research, tool reviews, Reference descriptions, email copy, Analyst summaries, everything.

---

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
- **Folder reorganization suggestions are surfaced** (see below)

**How History + Conflicts Work Together:**

When `/save` detects a conflict (new Source contradicts old decision):
1. Old content is **moved to History** with date + context: `[2026-04-14] Old: said X, Source contradicts this`
2. New content replaces it in the main text
3. Conflict is **logged** in `.vault-conflicts` with old vs. new states
4. File gets `conflict_detected: true` flag

Result: You can see the change (History), understand why (Conflict log), and act on it.

**Why non-blocking?** Blocking prevents work. Conflicts are logged, visible, but never blocking. You review them or not—your choice.

## Audit & Reorganization Suggestions

When `/audit` runs, it surfaces folder organization issues as **suggestions only** (no auto-reorganization):

**Checks:**
1. **Orphaned folders** — Folders with no files or only `_index.md` (candidates for deletion)
2. **Consolidation opportunities** — Folders with 1–2 files that could merge with parent folder
3. **Misplaced notes** — Files stored in wrong folders based on folder structure:
   - File about ClinicalHours pricing in `/02_Analyst/projects/` instead of `/02_Analyst/projects/ClinicalHours/Strategy/`
   - Internship research in `/02_Analyst/` instead of `/02_Analyst/career/internships/`
   - File in wrong project folder (e.g., FEDVT content in ClinicalHours folder)
   - Analyst files in Source folder or vice versa
4. **Broken wikilinks** — Links to files/folders that no longer exist
5. **Missing indexes** — Folders without `_index.md` (though `/save` creates these automatically)
6. **Folder naming consistency** — Check folder names against conventions (lowercase, hyphens for spaces, no abbreviations unless standard)
7. **Folder hierarchy appropriateness** — Suggest if a folder should be moved to a different parent level (e.g., `Strategy/` shouldn't be nested 4 levels deep)
8. **Name conciseness & clarity** — Suggest shorter, clearer names for files and folders:
   - Remove redundancy (e.g., file named "internship-search-strategy" in `internships/` folder should be just "strategy")
   - Shorten verbose names (e.g., "flower-mound-ai-operations-target-companies" → "flower-mound-targets")
   - Improve clarity (e.g., "research-notes-v2-final-actual" → "research-v2")

**Example Output:**
```
🔍 Folder Organization Audit

✅ Healthy:
- /02_Analyst/career/ (2 subfolders, 1 index, 2 files)
- /02_Analyst/projects/ (2 subfolders, all with indexes)

⚠️ Consolidation Candidates:
- /02_Analyst/projects/FEDVT/Analysis/ has only 1 file → consider merging into /02_Analyst/projects/FEDVT/

📛 Naming Consistency Issues:
- `/02_Analyst/career/OLD_TARGETS/` — should be `old-targets/` (lowercase + hyphens)
- `/02_Analyst/projects/ClinicalHours/EmailAutomation/` — should be `email-automation/` (kebab-case)

✂️ Conciseness & Clarity Improvements:
- `flower-mound-ai-operations-target-companies.md` → `flower-mound-targets.md` (context from folder path)
- `summer-2026-internship-search-strategy.md` in `internships/` → `strategy.md` (redundant context)
- `research-notes-v2-final-actual.md` → `research-v2.md` (remove status words)

📍 Hierarchy Issues:
- `/02_Analyst/projects/ClinicalHours/Strategy/Pricing/` is 4 levels deep → consider moving `Pricing/` up to `/02_Analyst/projects/ClinicalHours/Pricing/`
- `/02_Analyst/career/internships/2026-summer/` should be `/02_Analyst/career/summer-2026-internship/` (top-level clarity)

❌ Critical Issues — Misplaced Notes:
- `/02_Analyst/pricing-strategy.md` should be in `/02_Analyst/projects/ClinicalHours/Strategy/` (about ClinicalHours)
- `/02_Analyst/projects/internship-targets.md` should be in `/02_Analyst/career/internships/` (internship content, not projects)
- `/02_Analyst/projects/Research/` is orphaned (empty, no files) → consider deleting
- `/02_Analyst/career/old-targets/` has broken wikilinks to deleted companies

👤 Action: Review suggestions above. You decide what to rename/move/delete.
```

**Naming Conventions:**
- Folder names: lowercase, hyphens for spaces, no abbreviations (unless standard like `_index`)
- Depth: avoid nesting >4 levels unless essential
- Clarity: folder name should describe contents (e.g., `Strategy/` not `Other/`)

**No auto-reorganization.** You review suggestions and manually move/delete files as needed.

## Command Reference
- `/save [topic]` — Read new/updated Source files, synthesize into Analyst, **create/update all folder indexes**, create/update wikilinks, log conflicts
- `/resume [topic]` — 3-sentence context bootstrap (~500-700 tokens) from Analyst + Source, surface conflicts
- `/audit` — surface drift, staleness, broken wikilinks, orphaned Source files, unreviewed conflicts, **AND folder reorganization suggestions** (orphaned folders, consolidation opportunities, structural drift)
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

## Index Creation (Mandatory for `/save`)

**Rule:** Every folder in `/02_Analyst/` must have an `_index.md`, no matter how specialized.

**When `/save` runs:**
1. **Detect new folders** — If synthesis created files in a new folder, create `_index.md` for that folder
2. **Update parent indexes** — For every new file, update all parent folder indexes to include the new file
3. **Index format:**
   - Frontmatter with `title`, `description`, `last_updated`
   - Navigation section (`📂 Folders` and `📄 Files`)
   - Links to all files in that folder
   - Quick reference/summary of the folder's purpose
4. **No orphaned folders** — If a folder exists but has no index, create one on next `/save`

**Examples:**
- New file in `/02_Analyst/career/internships/` → Update `/02_Analyst/career/internships/_index.md` and `/02_Analyst/career/_index.md`
- New project folder `/02_Analyst/projects/NewProject/` → Create `/02_Analyst/projects/NewProject/_index.md` and update `/02_Analyst/projects/_index.md`

**Result:** All folders are navigable from their indexes, and parent folders always reflect their children.

## Frontmatter Schema (Analyst files)

```yaml
---
title:                                    # Simple, idea-focused title
project:                                  # Project key (clinicalhours, fedvt, internships, etc)
strategic: false                          # true = conflicts are logged; false = silent updates (both logged)
status: stable                            # stable | drifted | flagged
origin_dump: "[[]]"                       # First Source dump that created this note
last_synced_dump: "[[]]"                  # Most recent Source dump incorporated
references: [[[03_References/...]]]       # Frameworks/tools from References used in this file
conflict_detected: false                  # true = this file was recently updated over old decision
last_updated: YYYY-MM-DD
tags: []
---
```

## Frontmatter Schema (References files)

```yaml
---
title:                                    # Simple, tool/framework/pattern name
type: [framework|tool|pattern|resource]   # What kind of reference this is
source: [URL or tool name]                # REQUIRED: cite real source
relevance: [project keys]                 # Which projects this applies to (internships, clinicalhours, etc)
version: 1.0                              # Semantic versioning (1.0 = v1, 1.1 = first iteration, 2.0 = major revision)
tested_in: [project/context]              # Where this was last tested/improved
last_updated: YYYY-MM-DD
tags: []
---
```

**Note:** Add `## Iterations` section at bottom of every Reference file to track improvements over time (see Skills → References Pattern above).

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

## Skills → References Pattern (With Iteration)

When I invoke a Claude Code skill (copywriting, cold-email, sales:outreach, etc.), learnings are saved to References and **actively improved** each time they're used:

**Workflow:**
1. You ask me to do something (e.g., optimize emails)
2. I invoke relevant skill (e.g., copywriting skill)
3. Skill teaches me frameworks + patterns
4. I save key learnings to `/03_References/` with `source: [Skill Name]`
5. Your Analyst output (e.g., optimized emails) links to References in frontmatter
6. **Next time I use that skill:**
   - I reference the saved framework (don't re-learn)
   - I apply it to new context (new company, new domain)
   - I iterate: what worked? what could improve? what's new?
   - I update the Reference with improvements, variations, or new insights
   - Add entry to `## Iterations` section showing what evolved

**Example:**
- Session 1: Invoke copywriting skill → Save framework to `/03_References/Frameworks/Cold-Email-Optimization.md`
- Analyst file `wave-3-optimized-emails.md` → links to it
- Session 2: Need to optimize sales pitch → I check References, apply the framework
  - I discover: Cold email formulas work for sales pitches too (variation)
  - I find: Response rate improves 20% if I add urgency differently
  - I update References with new variation + insight
- Session 3: New outreach project → Reference now has 2 strategies, multiple test results

**Iterations Section (in each Reference file):**
```yaml
## Iterations

[2026-04-21] v1.1 — Added subject line variation for warm outreach (tested +5% open rate)
[2026-04-18] v1.0 — Initial framework from copywriting skill (tested on Wave 3 internship emails)
```

**Result:** References compound. Each use = improvement. Frameworks get stronger, not staler. Knowledge evolves toward what actually works.

---

## Cross-Session Value of `/save`

In a single session, vanilla Claude file writes work fine. `/save` adds value **across sessions**:
- **Source as source of truth** — Your writing in Source is never edited, always used as citation
- **Persistent metadata** — `last_synced_dump`, `origin_dump` enable `/resume` to bootstrap context
- **Analyst as your persona** — /save synthesizes your Source files into living knowledge about you + your outputs
- **References as shared learning** — Frameworks + tools I discover are saved with real sources, reusable across projects
- **Structured linking** — Creates bidirectional wikilinks: Source → Analyst → References → Real sources
- **Conflict visibility** — Tracks when your Source contradicts old Analyst decisions
- **Audit trail** — `.vault-conflicts` log creates a record of all decision changes

Without `/save`, each session is isolated. With `/save`, your vault is a persistent, cross-session knowledge base where:
- Your Source files → inform Analyst (your persona)
- Analyst outputs + skills → inform References (shared frameworks)
- References stay sourced → reusable + credible for future work

## History System (Simple)

**What it is:** Keep old versions of content so you can see what changed and when. Works hand-in-hand with Conflicts.

**How it works:**

1. **In Analyst files**, add a `## History` section at the bottom
2. When something changes (manual edit OR via conflict detection), old version goes to History with date: `[2026-04-14] Old: said X. New: Source says Y`
3. Newest changes go at the top of History
4. Never delete—always move old stuff to History instead

**Two Types of History Entries:**

1. **Manual updates:** You change your mind
   ```
   [2026-04-14] Old: target was 50 companies by May 1
   New: 50-70 by May 15 (research found more opportunities)
   ```

2. **Conflict-driven updates:** New Source contradicts old decision
   ```
   [2026-04-14] Old: believed IntelliCentrics had no turnover issues
   New: [[01_Source/...]] shows 50-60% staff turnover (Glassdoor data)
   See [[.vault-conflicts]] for full contradiction log
   ```

**Auto-cleanup:**
- After 6 months, `/save` moves old history to `/04_Archive/[project]_history.md`
- Your active files stay lean (faster to load)
- Full history always available in Archive
- Conflicts >90 days old also auto-archive

**Why?** Keeps context (why did you change your mind?) but doesn't slow down current work. Conflicts show the reasoning.

---

## See Also

- **`/02_Analyst/VAULT-STRUCTURE.md`** — Detailed guide to three-layer vault (Source, Analyst, References) with scenarios and wikilink maps
- **`/03_References/_index.md`** — Index of all discovered frameworks, tools, patterns


