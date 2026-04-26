---
title: Poker App — Phase 2 Multiplayer PRD
project: poker-app
strategic: false
status: stable
origin_dump: "[[01_Source/projects/poker-app/prd-phase-2-multiplayer]]"
last_synced_dump: "[[01_Source/projects/poker-app/prd-phase-2-multiplayer]]"
conflict_detected: false
last_updated: 2026-04-24
tags: [poker, multiplayer, real-time, PRD]
---

# Phase 2: Multiplayer

Source: [[01_Source/projects/poker-app/prd-phase-2-multiplayer]]

## Goal

Turn existing poker UI into a functional real-time multiplayer experience with persistent tables and chip tracking.

---

## Core Requirements

### Authentication
- Account required to play; login gates all table access

### Table Management
- Create a table with name + buy-in amount
- Join via lobby or invite code
- Tables persist after players disconnect
- Disconnected player can rejoin same seat with chip count intact
- Lobby shows who is seated and current game status

### Gameplay
- Up to 6 players per table
- Game state synchronized in real time across all clients
- All players see same board, pot, and action simultaneously
- Turn timer with auto-fold on timeout
- Authoritative server-side chip math — clients cannot manipulate results (side pots included)

### Chip Tracking
- Buy-in defined at session start (per table, not global)
- Net gain/loss tracked per hand across the session
- End-of-session summary for all players

---

## Out of Scope
- Real money / payments
- Tournaments
- Global chip wallet across tables
- Mobile app

---

## Key Architectural Constraints

1. **Authoritative server** — all pot/winner calculations happen server-side to prevent client manipulation
2. **Session-scoped chips** — no cross-table ledger (simplifies MVP significantly)
3. **Persistent seats** — reconnection must restore seat + chip state; requires durable session storage

---

## Next Steps

- Decide tech stack for real-time sync (WebSockets via Socket.io, Supabase Realtime, Liveblocks, etc.)
- Define state machine for game phases (waiting → dealing → betting → showdown → payout)
- Determine reconnection window (how long is a seat held?)
