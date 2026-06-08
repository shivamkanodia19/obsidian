---
title: Vault Audit - 2026-06-07
description: Full-vault routing audit focused on June chat coverage, missing human-facing indexes, and current health logs
last_updated: 2026-06-07
status: historical
note_role: audit
audit_family: vault-audit
audit_role: latest
tags:
  - vault
  - audit
  - routing
  - health
---

# Vault Audit - 2026-06-07

Scope: root guidance, active Analyst and Output hubs, June 2026 Codex chat coverage, `.vault-conflicts`, `.vault-broken-links.md`, `.vault-contradictions.md`, and current human-facing index coverage.

## Highest-Risk Findings

### 1. June chat coverage had no umbrella audit note after 2026-05-31

- Meaningful June sessions already produced real artifacts, but the save trail stopped at `2026-05-31`.
- Risk: future agents could assume June work was unsaved simply because the audit breadcrumb was missing.
- Fix applied: added [[codex-chat-save-audit-2026-06-07]] and updated the main Analyst hub plus activity log.

### 2. New summer 2026 ClinicalHours export folders were half-routed

- The parent slide and image hubs pointed toward the newer summer 2026 ClinicalHours branches, but the image-export folders themselves had no `_index.md`.
- Risk: the actual final PNG outputs were discoverable only if an agent already knew to jump through the slide-strategy layer.
- Fix applied: added `_index.md` files for:
  - `05_Outputs/images/clinicalhours_summer2026_faceless_slideshow/`
  - `05_Outputs/images/clinicalhours_summer2026_high_impact_slideshow/`
  - `05_Outputs/images/clinicalhours_summer2026_premium_problem_first_slideshow/`
  - `05_Outputs/images/clinicalhours_summer2026_playful_animated_slideshow/`

### 3. The mobile optimization toolkit lacked its own local router

- `05_Outputs/system-designs/mobile-optimization-agent-kit-2026-06-01/` was indexed, but `toolkit/` itself was not.
- Risk: future agents could see the high-level brief but still have to file-hunt the actual Playwright, Lighthouse, and smoke-test files.
- Fix applied: added [[05_Outputs/system-designs/mobile-optimization-agent-kit-2026-06-01/toolkit/_index]] and surfaced it from the parent kit index.

### 4. A finished academic deliverable was sitting loose at vault root

- `Sunrise Bakery Capstone Answers.md` was a finished answer sheet, not a root-level workspace file.
- Risk: root clutter makes the vault look less trustworthy and makes future routing noisier.
- Fix applied: moved it into [[05_Outputs/academics/sunrise-bakery-capstone-answers-2026-06-04]] and updated the Academic Outputs hub.

## Current Health Snapshot

- Broken wikilinks: `0`
- Open conflicts in `.vault-conflicts`: `1`
- Pending-validation conflicts in `.vault-conflicts`: `1`
- Closed conflicts in `.vault-conflicts`: `1`
- Current-truth collisions surfaced by `.vault-contradictions.md`: `0`
- Duplicate note stems requiring review in `.vault-contradictions.md`: `0`
- Intentional duplicate stems recognized by `.vault-contradictions.md`: `1`
- Scoped duplicate stems recognized by `.vault-contradictions.md`: `5`
- Agent-context indexes missing task fields: `0`

## Structural Findings Left Intentionally Alone

- Generated run folders under `05_Outputs/automation-code/mindchuk-obsidian-bridge/agent-inbox/runs/` remain intentionally unindexed.
- Empty `agent-inbox/pending/` and `agent-inbox/processing/` queue folders in the MindChuk bridge are runtime placeholders, not vault clutter, and are now treated as machine state by the audit rules.
- Generated pipeline run folders under `05_Outputs/images/felt_tiktok_2026-05-14/pipeline/runs/` remain intentionally unindexed.
- `node_modules/` trees under output systems remain intentionally unindexed.
- Those are machine internals, not human navigation hubs, so treating them as missing-index problems would create audit noise instead of clarity.

## Deferred Cleanup

- The vault root still contains a large set of image captures and scratch artifacts.
- I did not move them in this pass because the git worktree is already heavily dirty and I could not prove every root artifact was safe to relocate without stepping on in-progress user work.
- That remains a real cleanup candidate, but it is a separate relocation pass, not a safe audit-side tweak.

## Result

This pass fixed the human-facing routing gaps, refreshed the June chat breadcrumb trail, kept the current contradiction picture visible, and avoided polluting the vault with generated-folder indexes that would make navigation worse instead of better.
