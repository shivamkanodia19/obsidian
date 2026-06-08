---
title: Task Context Protocol
description: How project and topic indexes should carry prompt-ready task context
last_updated: 2026-05-21
status: current
tags:
  - vault
  - tasks
  - routing
  - prompts
---

# Task Context Protocol

You do not need a single top-3-goals list for the whole vault.

The better pattern for this system is local ownership: each active project or topic can carry its own prompt-ready task state in its nearest `_index.md`.

## Core Rule

If a project or topic index should directly shape agent prompts, mark it with:

```yaml
agent_context: true
```

When that flag is present, agents should load that frontmatter before they start deeper project work.

## Required Fields

Use these scalar fields:

```yaml
project: clinicalhours
scope: projects/clinicalhours
status: active
agent_context: true
```

Use these short list fields:

```yaml
current_focus:
  - [1-3 live focus statements]
active_tasks:
  - [1-3 concrete tasks]
prompt_context:
  - "[[02_Analyst/...]]"
definition_of_done:
  - [observable completion condition]
```

Optional but useful:

```yaml
blocked_by:
  - [current constraint]
task_cards:
  - "[[02_Analyst/tasks/...]]"
surface_in_root: true
```

## What Goes In The Index

- `current_focus` = what matters now
- `active_tasks` = what an agent should try to advance
- `prompt_context` = the smallest useful set of canonical notes
- `definition_of_done` = what good output must achieve
- `blocked_by` = the constraint most likely to cause bad output

Keep these short. If the frontmatter turns into a long memo, it stops helping.

## When To Make A Separate Task Card

Use a standalone note in `02_Analyst/tasks/` only when the task is:

- cross-project
- high-stakes
- reusable as a spec
- likely to need a run log or reviewer loop

Otherwise, the project index frontmatter should be enough.

## Root Visibility

Use:

```yaml
surface_in_root: true
```

only on primary hubs that should appear in the root Analyst frontmatter as active projects.

Do not set it on every supporting topic or research subtrack, or the root router gets noisy again.

## Why This Helps

This avoids two common failures:

- the whole vault pretending one global priority list can cover everything
- agents having to infer current task state from scattered prose and historical notes

## Save-Audit Contract

`save-audit` should treat stale task frontmatter as routing drift.

If an index says one thing, but the canonical notes clearly say something else, update the index first.
