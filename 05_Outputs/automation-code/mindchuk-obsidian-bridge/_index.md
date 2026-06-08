---
title: MindChuk Obsidian Bridge
description: Two-way bridge between MindChuk and this vault
last_updated: 2026-06-02
---

# MindChuk Obsidian Bridge

This bridge gives MindChuk a real place inside the vault:

- `pull` mirrors MindChuk messages and reminders into markdown files
- `push` sends markdown notes from the local outbox into MindChuk
- `sync` does both
- agent-like phone prompts get copied into `agent-inbox/` when they use tag `AGENT` or start with `/agent` or `/codex`
- `mindchuk_agent_runner.mjs` can turn `agent-inbox/pending` notes into real `codex exec` runs
- the runner first refines raw phone-captured prompts, then executes them, and saves both stages in `agent-inbox/runs/`
- completed or failed runs can publish a result note back into MindChuk automatically
- stale tasks left in `processing/` are recovered automatically on the next runner cycle
- on this Windows machine, the runner can fall back from `workspace-write` to `danger-full-access` when Codex hits the known sandbox refresh issue

## Files

- `mindchuk_bridge.mjs` - main bridge script
- `run_mindchuk_bridge.ps1` - Windows-friendly wrapper
- `mindchuk_agent_runner.mjs` - queue runner that launches `codex exec`
- `run_mindchuk_agent_runner.ps1` - Windows-friendly runner wrapper
- `start_mindchuk_agent_runner.ps1` - starts the watcher in the background with logs and a pid file
- `stop_mindchuk_agent_runner.ps1` - stops the background watcher
- `mirror/_index.md` - generated mirror hub after the first pull
- `agent-inbox/_index.md` - generated agent-style prompt queue after the first pull
- `outbox/_template.md` - starter note format for pushing from the vault back into MindChuk

## Setup

Set these environment variables before running it:

- `MINDCHUK_EMAIL`
- `MINDCHUK_PASSWORD`

Optional overrides:

- `MINDCHUK_TARGET_DIR`
- `MINDCHUK_OUTBOX_DIR`
- `MINDCHUK_AGENT_DIR`
- `MINDCHUK_AGENT_REPORT_RESULTS`

## Commands

```powershell
powershell -File .\run_mindchuk_bridge.ps1 pull
powershell -File .\run_mindchuk_bridge.ps1 push
powershell -File .\run_mindchuk_bridge.ps1 sync
powershell -File .\run_mindchuk_agent_runner.ps1 once
powershell -File .\run_mindchuk_agent_runner.ps1 watch
powershell -File .\start_mindchuk_agent_runner.ps1 -Email "you@example.com" -Password "your-password"
powershell -File .\stop_mindchuk_agent_runner.ps1
powershell -File .\watch_mindchuk_agent_live.ps1
```

## Live Monitoring

Run this in a separate terminal before you text an agent task:

```powershell
powershell -File .\watch_mindchuk_agent_live.ps1
```

It gives you a live dashboard for:

- queue counts across `pending`, `processing`, `completed`, and `failed`
- the current task file and prompt preview
- the latest run directory
- the refine and execute stdout tails
- the final model message
- the success or blocker note
- the background runner log

## Reality Check

This gets phone-captured notes into the vault cleanly, can push selected vault notes back into MindChuk, and now has a separate local runner that can launch `codex exec` for queue items.

The realistic version of "start agents from my phone" is now:

1. text or save a prompt into MindChuk
2. sync it into `agent-inbox/pending`
3. run `mindchuk_agent_runner.mjs` in `watch` mode
4. let the runner move jobs through `processing`, `completed`, or `failed` while saving logs in `agent-inbox/runs`
5. receive a result note back in MindChuk when the run finishes

The runner now refines the raw phone-captured task into a cleaner execution prompt before it launches the execution pass.

The background starter also pins absolute `node` and `codex` paths and verifies that the hidden watcher stayed alive before writing `runner.pid`.

Result notes are tagged `CODEXRESULT`, and the bridge ignores them as new agent tasks even if MindChuk also auto-applies `AGENT`.

This is still local automation, not a hosted remote agent service. Your machine has to be on for jobs to run.
