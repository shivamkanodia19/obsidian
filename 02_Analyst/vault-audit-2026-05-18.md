---
title: Vault Audit - 2026-05-18
description: Whole-vault structural audit with safe navigation fixes and review findings
last_updated: 2026-05-18
status: historical
note_role: audit
audit_family: vault-audit
audit_role: archived
tags:
  - vault
  - audit
  - save
---

# Vault Audit - 2026-05-18

Scope: full scan of `02_Analyst/`, `03_References/`, `04_Archive/`, and `05_Outputs/`, plus root vault hubs, `.vault-conflicts`, and the external Claude memory directory.

## Auto-Fixed

- Seeded 8 high-signal `_index.md` files for active ClinicalHours campaign and output folders:
  - `02_Analyst/projects/ClinicalHours/campaigns/_index.md`
  - `02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/social_media_expert/_index.md`
  - `05_Outputs/images/clinicalhours_tiktok_2026-05-18/captures/_index.md`
  - `05_Outputs/images/clinicalhours_tiktok_2026-05-18/composition/_index.md`
  - `05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/_index.md`
  - `05_Outputs/images/clinicalhours_tiktok_2026-05-18/exports/_index.md`
  - `05_Outputs/images/clinicalhours_tiktok_2026-05-18/pipeline/_index.md`
  - `05_Outputs/images/clinicalhours_tiktok_2026-05-18/qa/_index.md`
- Refreshed the main navigation hubs most affected by this work:
  - `02_Analyst/_index.md`
  - `02_Analyst/projects/ClinicalHours/_index.md`
  - `05_Outputs/_index.md`
  - `05_Outputs/images/_index.md`
  - `05_Outputs/images/clinicalhours_tiktok_2026-05-18/_index.md`

## Structure Findings

- Meaningful missing indexes were concentrated in the new ClinicalHours campaign and output system, and those are now covered.
- Empty structural placeholders remain in `04_Archive/history/` and `04_Archive/memory-archive/`; they were intentionally preserved.
- Additional missing `_index.md` hits mostly live in generated artifact trees under `05_Outputs/images/` and were intentionally left alone to avoid polluting pipeline folders with low-value hubs.

## Link and Naming Findings

- Broken frontmatter wikilinks in `02_Analyst/`: none found.
- Brittle rooted wikilinks using `[[/...]]`: 12 occurrences, all in older save-audit notes or guidance examples.
- Brittle traversal wikilinks using `[[../...]]`: 4 occurrences, all in templates or guidance examples.
- Naming-style drift remains in several legacy folders, including:
  - `02_Analyst/academics/ETAM`
  - `02_Analyst/career/internships/outreach/wave-4/ACTION-ITEMS`
  - `02_Analyst/projects/ClinicalHours`
  - `02_Analyst/projects/ClinicalHours/Market`
  - `02_Analyst/projects/ClinicalHours/Outreach`
  - `02_Analyst/projects/ClinicalHours/Strategy`
  - `02_Analyst/research/FEDVT`
  - `02_Analyst/research/dairy farms`
  - `03_References/Best-Practices`
  - `03_References/Voice-Style`
- These were surfaced only; no folder renames were attempted because that would create wide wikilink churn.

## Duplicate and Cleanup Findings

- `02_Analyst/career/internships/email-optimization-strategy.md` duplicates the name of `02_Analyst/career/internships/strategy/email-optimization-strategy.md`, but the root file is a deliberate redirect stub and should stay.
- No safe duplicate consolidations were performed.
- No deletions were performed in this pass because the worktree already contains substantial in-flight changes and several empty folders appear to be pipeline placeholders.

## Root and Hub Review

- `INDEX.md` and `CLAUDE.md` are still lean enough to orient a fresh agent quickly.
- `02_Analyst/_index.md` remains usable as a hub, though it is carrying a growing historical tail in `Recent Durable Changes` and `New Files`.
- `03_References/_index.md` is clean and current enough for navigation.
- `05_Outputs/_index.md` had duplicate `New Files` headings; this audit collapsed that into a single cleaner section and restored `images/` as a first-class output hub.

## Conflicts and Memory

- `.vault-conflicts` entries with `awaiting_review`: 5
- `.vault-conflicts` entries with `resolved`: 5
- No stale external memory files met the archive rule. The files found were still active, in progress, pending clarification, or permanent guidance.

## Result

This pass completed the high-signal navigation work for the active ClinicalHours campaign/output cluster, preserved the state of the rest of the vault without risky deletions, and saved the findings as a durable whole-vault audit.
