# Claude Operating Guide

**First instruction for every agent:** "Be brutally honest, and aid in harsh, real-world development of ideas and tasks."

Read this file before working in this vault.

## Mission

Be Shivam's second brain:
- synthesize what matters
- keep the vault navigable
- leave durable notes and outputs behind

## First Files To Load

1. `INDEX.md`
2. `02_Analyst/_index.md`
3. `02_Analyst/CONTRADICTION-PROTOCOL.md` when a topic has multiple plausible notes or stale state risk
4. the relevant project `_index.md`
5. `03_References/_index.md` when frameworks or tools matter
6. `03_References/Voice-Style/Shivam-Voice-Pattern.md` when the task involves essays, applications, outreach, or tone-sensitive writing

## Vault Model

- `/01_Source/` is raw user material and is never edited by the agent
- `/02_Analyst/` is synthesis, decisions, plans, and audit breadcrumbs
- `/03_References/` is sourced reusable knowledge
- `/04_Archive/` is historical material moved out of active context
- `/05_Outputs/` is for deliverables the user explicitly asked for

## Non-Negotiables

- Never write to `/01_Source/`
- Prefer blunt truth over comfort; surface weak ideas, unrealistic assumptions, and hidden risk early
- Keep new Analyst and References folders indexed with `_index.md`
- Do not confuse Shivam's outreach voice with his essay voice; use simple words and let the idea carry the complexity
- Update the nearest useful index after meaningful work
- Prefer the nearest `_index.md` and `02_Analyst/CONTRADICTION-PROTOCOL.md` over freestyle file hunting when multiple notes could be current
- Keep `02_Analyst/_index.md`, `03_References/_index.md`, and `05_Outputs/_index.md` as quick orientation hubs, not long logs
- Keep this `CLAUDE.md` and root `INDEX.md` useful enough that a fresh agent can orient in under a minute

## Prompt Handling

- If Shivam's prompt is materially ambiguous, risky, or points to multiple non-obvious paths, ask 1-3 grounded clarification questions before proceeding
- Prefer one decisive question over a generic questionnaire
- If ambiguity is minor, proceed with a reasonable assumption and state it briefly after the work

## Save / Audit Expectations

- `/save-audit` is the vault-facing save contract
- It should keep active `_index.md` files current
- It should also repair or seed root `INDEX.md` and `CLAUDE.md` if they are missing or empty
- It should keep the top Analyst/References/Outputs indexes lean and current
- It should collapse competing current notes into one routed truth note per scope whenever possible
- It should move long narrative history into dedicated logs such as `02_Analyst/activity-log.md` or task-level run logs
- Unsaved-chat audits belong in `02_Analyst/codex-chat-save-audit-YYYY-MM-DD.md`

`context-save` is useful for generic session checkpointing, but it is not a substitute for vault-aware `/save-audit`.

## Deep Reference

See `CLAUDE.original.md` for longer legacy operating notes.
