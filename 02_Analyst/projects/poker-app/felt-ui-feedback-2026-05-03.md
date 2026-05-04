---
title: Felt UI Feedback and Training-Mode Prompting - 2026-05-03
project: poker-app
strategic: true
status: stable
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-05-03
tags: [poker-app, product, training-mode, cursor, ui]
---

# Felt UI Feedback and Training-Mode Prompting - 2026-05-03

Status: backfilled memo from the session that started as Felt UI/product feedback and ended with a stronger training-mode architecture workflow.

## What Happened

The original ask was product/design feedback for Felt. The most durable output was not a visual critique on its own. It was a better implementation workflow:

1. audit the current poker and training architecture first
2. separate shared poker-engine logic from coaching or training overlays
3. scope training mode honestly before adding product polish

## Durable Product Principle

Training mode should not pretend to be broader or smarter than the underlying logic can support.

That led to a strong product/engineering stance:

- shared poker rules engine for both gameplay and training
- no duplicate action-legality or stack-math logic
- narrow V1 scope if needed
- explicit data-backed coaching instead of vague AI claims

## Cursor Workflow Produced

The session produced a two-step workflow for Cursor:

- `TRAINING_MODE_AUDIT.md`
- `TRAINING_MODE_PRD.md` plus a migration plan

## Why This Matters

The important idea was not "make the UI prettier." It was "do not ship a polished training experience on top of structurally weak poker logic." That makes this session more useful as a product-architecture note than as a one-off design critique.
