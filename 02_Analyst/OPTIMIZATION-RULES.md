# Vault Optimization Rules

How `/save-audit` keeps context lean, navigable, and useful for future agents.

## Core Principle

Atomic synthesis, not incremental bloat.

The vault exists to improve agent reasoning, writing, research, outreach, planning, and decision support. Save behavior should preserve that value without turning hub pages into logs.

## Public Contract

Use `/save-audit` as the vault-facing command.

- `context-save` can preserve session state.
- `/save-audit` is what updates the vault itself.

Think of `/save-audit` as two internal phases:

1. Save phase: preserve durable reasoning, outputs, and project state.
2. Audit phase: keep structure, links, and `_index.md` files healthy.

## Save Phase

The save phase should:

1. Read only the relevant new source or working context.
2. Update the canonical Analyst or Output note instead of duplicating it.
3. Update the nearest useful `_index.md` files.
4. If the nearest relevant index has `agent_context: true`, treat its frontmatter as the default prompt brief and keep `current_focus`, `active_tasks`, `prompt_context`, and `definition_of_done` current.
   Use `surface_in_root: true` only on primary hubs that belong in the root Analyst router.
5. Record a standalone task card or run log only when the work is substantial, high-stakes, reusable, or cross-project.
6. Add a vault-level save note only when the work really changes navigation or closes a chat-coverage gap.

## Audit Phase

The audit phase should:

1. Check `INDEX.md` and `CLAUDE.md` for clarity and freshness.
2. Check the top hubs:
   - `02_Analyst/_index.md`
   - `03_References/_index.md`
   - `05_Outputs/_index.md`
3. Check active child indexes in Analyst, References, and Outputs.
4. Surface broken links and stale aliases.
5. Create missing `_index.md` files when a folder is active enough to need navigation.
6. Avoid noisy archive-only findings unless they affect active wayfinding.

## Contradiction Hygiene

- Do not leave two notes looking equally current for the same scope.
- Update the canonical note first; downgrade the losing note to `snapshot`, `historical`, or `superseded`.
- If the winner is unclear, log the disagreement in `.vault-conflicts` with `awaiting_review` or `pending_validation`.
- Keep the nearest `_index.md` explicit about which notes are current, historical, or draft.
- Use [[CONTRADICTION-PROTOCOL.md]] when a folder has multiple plausible state notes.
- Use [[TASK-CONTEXT-PROTOCOL.md]] when a topic needs prompt-ready task state without spawning a separate task card.
- Keep audit notes historical. Use audit-specific metadata instead of letting them masquerade as current project truth.

## Index Rules

### Main Hubs Stay Lean

- `02_Analyst/_index.md` is a hub, not a diary.
- `03_References/_index.md` is a map of reusable knowledge, not a running discovery log.
- `05_Outputs/_index.md` is a router to deliverables, not an inventory of every artifact.

### Put History Elsewhere

- Long narrative history goes in `02_Analyst/activity-log.md`, task-level run logs, or project notes.
- Save-audit notes belong in `02_Analyst/codex-chat-save-audit-YYYY-MM-DD.md` when they represent real vault-wide audit coverage.

### Child Index Standard

Each useful `_index.md` should answer three questions fast:

1. What is this folder for?
2. Which files matter first?
3. What is the next layer down?

If an index cannot answer those questions in under a minute, it needs cleanup.

## Link Hygiene

- Prefer vault-root-relative wikilinks like `[[02_Analyst/projects/ClinicalHours/_index]]`.
- Avoid leading-slash links like `[[/02_Analyst/...]]`.
- Avoid fragile relative traversal like `[[../...]]` when a stable root-relative link is clearer.

## Context Hygiene

- Load indexes before deep files.
- Load only the smallest sufficient context first.
- Pull deeper files on demand.
- Do not copy entire conversation history into hub pages.
- If an index has `agent_context: true`, load its frontmatter before digging into deeper notes.

## Operational Heuristics

- If work changes a single project, update that project index first.
- If work changes a whole domain, update the domain index.
- If work changes vault-wide navigation or policy, update the root files and top hubs.
- If an index starts turning into a log, split the log out immediately.

## What Success Looks Like

A fresh agent should be able to:

- orient from `INDEX.md` and `CLAUDE.md`
- enter the right domain from the top Analyst, References, or Outputs hub
- find the right subfolder from its `_index.md`
- understand the current task state without rereading unrelated history
