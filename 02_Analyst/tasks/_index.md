---
title: Task System
description: Structured task specs for agent work across research, writing, reasoning, outreach, and operations
last_audited: 2026-05-10
last_updated: 2026-05-10
---

# Task System

This folder holds reusable task scaffolding for agent work that needs a clear scope, a clean definition of done, and a repeatable execution path.

It is an overlay for active cross-project work, not a replacement for the existing project folders. If a topic can be owned cleanly by one project or research hub, the default task brief should now live in that folder's `_index.md` frontmatter via [[02_Analyst/TASK-CONTEXT-PROTOCOL]].

## What Belongs Here

- Task specs for non-trivial agent work
- Reusable templates for defining goals, constraints, and success criteria
- Cross-project task cards when the work is not owned by a single project folder
- Reviewer-loop or run-log-worthy tasks that need a durable standalone spec

## What Does Not Belong Here

- Raw notes or dumps from you
- Final outputs ready to share
- Full session transcripts
- Every single project-local TODO when the project `_index.md` can hold that context directly

## Core Files

- [[task-template]] - Copy-ready task card template with a hard definition of done

## New Files

- [[clinicalhours-next-wedge-priority-2026-05-10]] - Real strategy task card for deciding the next ClinicalHours workflow wedge

## Active Work by Type

- Research
- Writing
- Reasoning and decisions
- Outreach
- Operations

Create type subfolders only when one of these areas becomes crowded enough to justify a dedicated index.

## By Project

- Use this folder for cross-project tasks or shared execution scaffolding.
- Keep deep project detail in the canonical project folder whenever a single project clearly owns the work.

## Waiting / Blocked

- Add task cards here only when the blocker itself is important context for future agent runs.

## Recently Completed

- Close the loop by linking the durable artifact or the run log instead of leaving a stale task card behind.

## Recommended Workflow

1. Start with [[task-template]] and define the objective before the agent starts working.
   Use project `_index.md` frontmatter instead when the work is contained to one topic and does not need a standalone card.
2. Route the task using [[03_References/Frameworks/task-routing-policy]].
3. If the work is high-stakes or externally facing, apply [[03_References/Frameworks/reviewer-loop-policy]].
4. Record the execution summary in [[02_Analyst/run-logs/_index]] when the run materially changes a project, output, or decision.

## Common Task Types

- Research synthesis
- Writing or revision
- Reasoning and decision support
- Outreach generation or evaluation
- Operations and workflow design
- Mixed multi-step tasks that cross projects

## Navigation

- **Parent:** [[02_Analyst/_index]]
- **Related:** [[02_Analyst/run-logs/_index]]
