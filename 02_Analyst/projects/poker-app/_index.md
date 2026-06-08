---
description: "Navigation hub for poker app"
title: Poker App - Project Index
project: poker-app
scope: projects/poker-app
status: active
agent_context: true
surface_in_root: true
current_focus:
  - plan phase-2 multiplayer without breaking the existing poker training foundation
  - keep poker-specific work aligned to Felt as the parent brand
active_tasks:
  - make the phase-2 multiplayer scope concrete enough to build
  - preserve the poker-specific UX principles that should survive the Felt merge
prompt_context:
  - "[[02_Analyst/projects/poker-app/phase-2-multiplayer]]"
  - "[[02_Analyst/projects/poker-app/felt-ui-feedback-2026-05-03]]"
  - "[[02_Analyst/projects/felt/_index]]"
definition_of_done:
  - multiplayer scope, risks, and dependencies are explicit
  - poker-specific decisions stay consistent with the Felt umbrella
blocked_by:
  - cross-game merger work can blur poker-specific requirements if the Felt umbrella note is not loaded
last_updated: 2026-05-21
---

# Poker App

Browser-based poker application. Phase 1 already exists. Phase 2 adds real-time multiplayer and stronger training architecture.

This folder is now the poker-specific subproject under the broader [[02_Analyst/projects/felt/_index|Felt]] umbrella. New cross-game strategy, campaign, and brand work should land in `projects/felt/`.

## Phases

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1 | Poker UI (single-player) | Existing |
| Phase 2 | Multiplayer: tables, real-time sync, chip tracking | Planning |

## Files

- [[phase-2-multiplayer]] - PRD synthesis: table management, gameplay rules, chip tracking, auth
- [[felt-ui-feedback-2026-05-03]] - Felt UI session distilled into a training-mode audit and implementation workflow
- [[felt-poker-marketing-plan-2026-05-07]] - TikTok slideshow-first marketing strategy grounded in the current product state
