---
title: Contradiction Protocol
description: How the vault marks canonical notes, stale notes, and unresolved contradictions
last_updated: 2026-05-21
status: current
tags:
  - vault
  - contradictions
  - canonical
---

# Contradiction Protocol

Use this note when two files on the same topic disagree, when multiple notes look active, or when an index does not make the winner obvious.

## Core Rule

One scope gets one canonical truth note at a time.

- The nearest useful `_index.md` decides which note is canonical for that scope.
- Only one note in a scope should use `status: current`.
- Older useful notes should be marked `snapshot`, `historical`, `draft`, `template`, or `superseded`.
- Durable frameworks can stay `active`, but they should not pretend to be the latest state snapshot.

## Recommended Frontmatter

Use these fields on stateful Analyst notes whenever a topic can drift:

```yaml
status: current
project: stocks
scope: stocks/portfolio-state
as_of: 2026-04-29
canonical: true
supersedes:
  - [[PORTFOLIO-SNAPSHOT-2026-04-21]]
```

Minimum expectation:

- `status`
- `project`
- `last_updated`

Strongly preferred when the note can conflict with siblings:

- `scope`
- `as_of`
- `canonical`
- `supersedes` or `superseded_by`

## Status Vocabulary

- `current`: the one note that should be trusted first for that exact scope
- `active`: a reusable framework or durable operating note still in force
- `snapshot`: point-in-time state capture
- `historical`: useful context, not the default truth
- `draft`: working note, not trusted by default
- `template`: reusable scaffold
- `superseded`: explicitly replaced by a newer note
- `archived`: no longer part of active routing

Legacy custom body labels are fine, but frontmatter should normalize to this smaller set.

## What Counts As A Contradiction

- `replacement`: a newer decision or measurement should replace the old one
- `augmentation`: the new note adds detail without invalidating the old note
- `support`: the new note reinforces the old note
- `pending-validation`: the new evidence is real but not strong enough to replace the old note yet
- `stale-routing`: the notes may be fine individually, but the index leaves multiple candidates looking current

## Conflict Queue Rules

Use `.vault-conflicts` only for unresolved or decision-relevant disagreements.
Use `.vault-contradictions.md` as the save-audit generated scan of likely contradiction clusters and routing drift.
Inside `.vault-contradictions.md`, only duplicate stems labeled as review candidates should be treated as cleanup debt; intentional redirects and scoped duplicates are informational.

Allowed queue statuses:

- `awaiting_review`: a human decision is needed
- `pending_validation`: more evidence is needed before choosing a winner
- `resolved`: decision made, or the contradiction was downgraded to support/augmentation
- `archived`: historical queue item moved out of active review

Treat `awaiting_review` and `pending_validation` as open.
Treat `resolved` and `archived` as closed.

## Resolution Workflow

1. Identify the exact scope that is in conflict.
2. Decide whether this is replacement, augmentation, support, or pending validation.
3. Update the nearest `_index.md` so one note is clearly routed as current.
4. Downgrade losing notes from `current` to `snapshot`, `historical`, or `superseded`.
5. Add `supersedes` or `superseded_by` when the replacement is explicit.
6. Log only unresolved or high-stakes disagreements to `.vault-conflicts`.

## Index Rules

When a folder has more than one meaningful note on the same topic, its `_index.md` should prefer sections like:

- `Current Canonical Notes`
- `Historical Notes`
- `Drafts and Queues`

Do not dump all related files into one flat list if that would make multiple truths look equally live.

For indexes with `agent_context: true`, stale or conflicting task frontmatter also counts as routing drift. If `active_tasks` points one way and the canonical note points another, update the index first.

## Save-Audit Contract

`save-audit` should not stop at link hygiene.

It should also:

- detect competing `current` notes and source-of-truth claims
- surface sibling alias folders like `dairy farms/` vs `dairy-farms/`
- surface duplicate note stems that may represent split truth
- normalize `.vault-conflicts` into open vs closed queue states
- push agents to fix routing in `_index.md` before leaving the vault
