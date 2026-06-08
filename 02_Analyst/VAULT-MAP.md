---
title: Vault Map
description: Live canonical layout and routing rules for the Obsidian vault
last_updated: 2026-05-19
status: current
tags:
  - vault
  - navigation
  - map
---

# Vault Map

Use this note when you need the real working layout of the vault, not just the abstract three-layer model.

## Root Rules

- Keep vault-wide guidance at root: `INDEX.md`, `CLAUDE.md`, `CLAUDE.original.md`, and a small set of system notes.
- Project-specific captures, session summaries, and source packets should not live at root.
- The numbered folders are the canonical navigation spine.

## Canonical Zones

### `01_Source/`

Raw user material and source bundles.

- `academics/` - class packets, essay sources, and the TAMU mechanics-finals corpus
- `career/internships/` - raw internship goals, resumes, and outreach research inputs
- `projects/ClinicalHours/`, `projects/ideathon26/`, `projects/keeper-clash/`, `projects/poker-app/` - raw project-specific inputs
- `research/fedvt/` and `research/dairy farms/` - raw research packets and external files

### `02_Analyst/`

Synthesis, command centers, decisions, and durable agent breadcrumbs.

- Root meta/governance: `_index.md`, `VAULT-STRUCTURE.md`, `WORKFLOW.md`, `MEMORY-SYSTEM.md`, `OPTIMIZATION-RULES.md`, audits, and logs
- `career/internships/` - canonical recruiting hub
- `projects/ClinicalHours/` - canonical ClinicalHours project home
- `projects/felt/` - canonical umbrella for Felt strategy, product, and campaigns
- `projects/poker-app/` - poker-specific supporting subproject under Felt
- `research/FEDVT/` - canonical FEDVT synthesis layer
- `research/ClinicalHours/` - deck/design critique only
- `research/clinicalhours_market_research/` - supporting ClinicalHours market dossier
- `prediction-markets/`, `stocks/`, `tasks/`, `run-logs/` - decision systems and agent execution overlays

### `03_References/`

Reusable cross-project knowledge.

- `Best-Practices/`
- `Frameworks/`
- `Patterns/`
- `Tools/`
- `Voice-Style/`

### `04_Archive/`

Historical material that should no longer compete with active navigation.

- old project packs
- superseded academic material
- future home for trimmed history snapshots when active notes get too long

### `05_Outputs/`

User-requested deliverables and self-contained output systems.

- top level stays type-based: `academics/`, `email-campaigns/`, `images/`, `research-analysis/`, `resumes/`, `system-designs/`, `automation-code/`
- inside complex project folders, prefer explicit subareas like `docs/`, `captures/`, `exports/`, `artifacts/`, and `pipeline/`

## Current Canonical Homes

- ClinicalHours:
  - raw inputs: `01_Source/projects/ClinicalHours/`
  - main analyst hub: `02_Analyst/projects/ClinicalHours/`
  - supporting market research: `02_Analyst/research/clinicalhours_market_research/`
  - image/output systems: `05_Outputs/images/clinicalhours_*`
- Internships:
  - raw inputs: `01_Source/career/internships/`
  - main analyst hub: `02_Analyst/career/internships/`
  - deliverables: `05_Outputs/email-campaigns/` and `05_Outputs/resumes/`
- Felt:
  - main analyst hub: `02_Analyst/projects/felt/`
  - poker-specific supporting notes: `02_Analyst/projects/poker-app/`
  - image/output system: `05_Outputs/images/felt_tiktok_2026-05-14/`
- FEDVT:
  - raw inputs: `01_Source/research/fedvt/`
  - main analyst hub: `02_Analyst/research/FEDVT/`
  - deliverables: `05_Outputs/research-analysis/`
- TAMU mechanics finals:
  - source bundle: `01_Source/academics/tamu_mech_finals/`
  - analyst summary: `02_Analyst/academics/mechanics-final-patterns-2026-04-30.md`

## Fast Routing Rules

- New raw material belongs in `01_Source/`.
- Decisions, plans, and durable reasoning belong in `02_Analyst/`.
- Reusable frameworks belong in `03_References/`.
- Shareable deliverables, screenshot packs, and reproduction systems belong in `05_Outputs/`.
- Historical material belongs in `04_Archive/` or a project `history/` folder when that project still has an active home.

## Retrieval Rules

- Start with the deepest relevant `_index.md`, not a random file search.
- Keep one canonical home per project family.
- Use supporting satellites only when their role is explicit.
- Do not create new parent-level duplicate notes when a child folder already owns the topic.
- For new notes and folders, prefer lowercase kebab-case unless the project already has an established canonical name.
