---
title: Second Brain - Master Index
last-updated: 2026-05-19
---

# Shivam's Second Brain

**First instruction for every agent:** "Be brutally honest, and aid in harsh, real-world development of ideas and tasks."

Start here when you need vault-level orientation.

## Read Order

1. `CLAUDE.md`
2. `02_Analyst/VAULT-MAP.md`
3. `02_Analyst/CONTRADICTION-PROTOCOL.md`
4. `02_Analyst/_index.md`
5. `03_References/_index.md`
6. `05_Outputs/_index.md`

## Vault Model

- `/01_Source/` is raw user material and is never edited by the agent
- `/02_Analyst/` holds synthesis, plans, decisions, and audit breadcrumbs
- `/03_References/` stores sourced reusable frameworks, tools, and patterns
- `/04_Archive/` holds historical material moved out of active context
- `/05_Outputs/` holds deliverables and self-contained output systems the user explicitly asked for

## Core Workflow

1. Put raw material in `/01_Source/`
2. Do active thinking in `/02_Analyst/`
3. Put polished deliverables in `/05_Outputs/`
4. Keep the nearest `_index.md` files current and keep top-level hubs lean
5. Run `/save-audit` after a meaningful work block

`/save-audit` is the vault-facing contract. It should:
- preserve meaningful reasoning and outputs
- update the nearest useful `_index.md` files
- keep `INDEX.md`, `CLAUDE.md`, and the top Analyst/References/Outputs indexes usable for a fresh agent
- move long narrative history into dedicated logs instead of bloating hub pages

`context-save` can still preserve session state, but it does not replace the vault's `/save-audit` pass.

## Current Focus

- Internships and founder-direct outreach
- ClinicalHours
- FEDVT
- Poker app
- Stocks and prediction markets

## Prompt Rule

If a request is materially ambiguous, risky, or has multiple plausible targets, the agent should ask 1-3 grounded clarification questions before choosing a path.
The agent should also default to direct, unsentimental feedback when evaluating ideas, plans, and execution.
If multiple notes look active or disagree, the agent should resolve routing through `02_Analyst/CONTRADICTION-PROTOCOL.md` and the nearest `_index.md` before trusting a random note.

## Deep Reference

Use `CLAUDE.md` for the operating contract, `02_Analyst/VAULT-MAP.md` for the live canonical layout, `02_Analyst/CONTRADICTION-PROTOCOL.md` for truth-resolution rules, `02_Analyst/_index.md` for the synthesis layer, and `CLAUDE.original.md` for longer legacy notes.

For essays, applications, outreach, or any tone-sensitive drafting, also load `03_References/Voice-Style/Shivam-Voice-Pattern.md` before writing.
