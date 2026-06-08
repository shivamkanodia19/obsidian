---
title: Vault Audit - 2026-05-20
description: Full-vault contradiction audit with routing fixes for active agent workflows
last_updated: 2026-05-20
status: historical
note_role: audit
audit_family: vault-audit
audit_role: archived
tags:
  - vault
  - audit
  - contradictions
  - routing
---

# Vault Audit - 2026-05-20

Scope: full scan of root guidance, active Analyst/References/Outputs notes, `.vault-conflicts`, and the current save/audit skill stack.

## Highest-Risk Contradiction Clusters

### 1. Conflict Queue Protocol Drift

- `.vault-conflicts` documented `awaiting_review` and `resolved`, but live entries also used `pending_validation` and `supported_by_example`.
- Risk: agents cannot reliably tell what is still open vs already settled.
- Fix applied: normalized the queue model so open states are `awaiting_review` and `pending_validation`, and closed states are `resolved` and `archived`.

### 2. Stocks Had Competing Current-State Notes

- `02_Analyst/stocks/_index.md` routed several portfolio notes as if they were all part of the current source of truth.
- `PORTFOLIO-SNAPSHOT-2026-04-21.md` and `PORTFOLIO-REFRESH-2026-04-29.md` both looked current enough to confuse a fresh agent.
- Fix applied: `PORTFOLIO-REFRESH-2026-04-29.md` is now the latest known portfolio-state note, the screenshot note is marked `snapshot`, and the index separates canonical vs historical notes.

### 3. ClinicalHours Mixed Current Product Direction With Older Outreach Execution

- The main ClinicalHours index mixed current wedge-selection notes with older clinic-outreach execution notes.
- Risk: agents can overfit to the earlier outreach wave instead of the current workflow wedge.
- Fix applied: the main project index now separates `Current Canonical Notes` from `Historical Execution Notes`, and the Outreach index points agents back to Strategy for current product direction.

### 4. Internship Outreach Routing Drift

- The outreach hub kept growing while leaving Wave 4 and the later founder batches visually similar in priority.
- Risk: agents may enter the older Wave 4 cluster instead of the May 2026 founder-direct work.
- Fix applied: the outreach hub now names the current canonical notes, and the Wave 4 index explicitly marks itself as historical campaign context.

### 5. Sibling Alias Folder Collision

- `02_Analyst/research/dairy farms/` and `02_Analyst/research/dairy-farms/` coexist under the same parent.
- Risk: agents can save new dairy notes into the legacy alias folder.
- Fix applied: both indexes now state that `dairy farms/` is canonical and `dairy-farms/` is historical only.

## Additional Structural Findings

- Exact basename duplicates found in active markdown:
  - `email-optimization-strategy`
  - `draft-emails`
  - `narrative_plan`
- `email-optimization-strategy.md` under `career/internships/` is a deliberate redirect stub and should remain.
- Duplicate section headers were present in `02_Analyst/career/internships/outreach/_index.md`; that routing noise has been cleaned.
- Three folders with markdown content but no `_index.md` remain in generated-output areas:
  - `05_Outputs/slides/clinicalhours_marketing_slideshow_2026-05-19/`
  - `05_Outputs/slides/clinicalhours_summer2026_faceless_slideshow/`
  - `05_Outputs/research-analysis/legends-merch-assessment-2026-05-07/node_modules/@oai/artifact-tool/`
- Those were left alone because they are output artifacts or vendor trees, not human navigation hubs.

## Protocol Added

- Added [[CONTRADICTION-PROTOCOL]] as the vault-level rulebook for:
  - one canonical note per scope
  - status normalization
  - stale-routing vs true contradiction handling
  - `.vault-conflicts` queue-state normalization
- Root guidance and top Analyst rules now point agents to that protocol earlier.

## Save-Audit Follow-Through

The current `save`, `audit`, and `save-audit` skills now need to do more than link cleanup.

They should also:

- detect competing current notes
- normalize contradiction queue states
- surface alias-folder collisions
- keep `_index.md` files explicit about current vs historical vs draft notes

That skill-level work is being updated alongside this audit so the fix becomes part of normal vault maintenance, not a one-off cleanup.
