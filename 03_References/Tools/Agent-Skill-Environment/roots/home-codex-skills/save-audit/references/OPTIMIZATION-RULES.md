# Save-Audit Optimization Rules

How the `save-audit` skill should behave in this vault.

## Purpose

This vault is for context management and better non-development agent output:
- reasoning
- writing
- research
- outreach
- planning
- decision support

`save-audit` should preserve that value and keep the navigation layer healthy.

## Core Contract

`save-audit` means:

1. Save phase
   - preserve durable reasoning in the canonical note
   - update the nearest useful `_index.md`
   - keep project-local task frontmatter current when an index declares `agent_context: true`
   - create standalone task cards or run logs only when the work is substantial, reusable, or cross-project

2. Audit phase
   - refresh active indexes in `02_Analyst`, `03_References`, and `05_Outputs`
   - ensure active indexes have frontmatter
   - keep root guidance and top hubs usable
   - surface broken links and brittle index-link styles
   - surface contradiction clusters, not just structural drift

## Index Rules

- Main hubs should stay short.
- `_index.md` files should answer:
  - what is this folder for
  - which files matter first
  - where should the next agent go next
- Long narrative history belongs in activity logs, run logs, or project notes, not hub pages.

## Link Rules

- Prefer vault-root-relative wikilinks like `[[02_Analyst/projects/ClinicalHours/_index]]`
- Avoid rooted links like `[[/02_Analyst/...]]`
- Avoid fragile `[[../...]]` traversal when a root-relative link is clearer

## Contradiction Rules

- One scope should have one canonical current note.
- If a newer note replaces an older one, downrank the older note to `snapshot`, `historical`, or `superseded`.
- If the winner is unclear, log it to `.vault-conflicts` as `awaiting_review` or `pending_validation`.
- `_index.md` files should separate current notes from historical notes when a folder has multiple plausible candidates.
- The audit backend should write contradiction findings to `.vault-contradictions.md`.
- Duplicate-stem exceptions should live in `DUPLICATE-STEM-POLICY.json`, not as hidden one-off heuristics.

## Commit Rule

Do not auto-commit by default.

Use a git commit only when the user explicitly wants it.

## Honest Boundary

The audit backend can maintain structure and indexes.

It cannot replace the agent's reasoning step for synthesis, decision quality, or writing quality.
