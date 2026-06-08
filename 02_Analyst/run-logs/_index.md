---
title: Run Logs
description: Structured execution breadcrumbs for major agent runs across research, writing, reasoning, outreach, and operations
last_updated: 2026-05-10
---

# Run Logs

This folder is for concise execution traces when an agent run materially changes a project, output, or decision. It is not a transcript store.

## Purpose

- Preserve how a result was produced
- Record what context was loaded and what review loop was used
- Make future resume, critique, and re-run steps faster

## Core Files

- [[run-log-template]] - Copy-ready template for future agent runs

## Recent Runs

- [[agent-run-2026-05-10-clinicalhours-next-wedge-priority]] - High-stakes ClinicalHours reasoning run using the new task-routing and reviewer-loop layer

## Naming Convention

- `agent-run-YYYY-MM-DD-short-topic.md`

Examples:
- `agent-run-2026-05-10-clinicalhours-evaluation-pass.md`
- `agent-run-2026-05-10-founder-research-synthesis.md`

## What To Record

- Linked task card
- Route used
- Context loaded first versus pulled later
- Agent roles or review loop used
- Artifacts produced
- Remaining risks or unresolved questions

## Relationship To Existing Save Notes

- Keep `codex-chat-save-audit-*` notes as human-readable vault audit breadcrumbs.
- Use this folder for task-level execution traces going forward.
- Migrate older log-like files only if consistency becomes worth the effort later.

## Navigation

- **Parent:** [[02_Analyst/_index]]
- **Related:** [[02_Analyst/tasks/_index]]
