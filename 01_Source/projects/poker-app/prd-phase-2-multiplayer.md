# PRD: Poker App — Phase 2 (Multiplayer)

**Date:** 2026-04-23
**Scope:** Real-time multiplayer, table management, chip tracking

---

## Overview

Phase 2 turns the existing poker UI into a functional multiplayer experience. Players can create or join persistent tables, play live games with other users, and track chips won and lost over time.

---

## Authentication

- Users must have an account to play
- Login is required before accessing any table

---

## Table Management

- A player can **create a table** with a name and buy-in amount
- A player can **join an existing table** from a lobby or via a code
- Tables **persist** — they are not destroyed when players leave
- A player who disconnects can **rejoin their seat** with their chip count intact
- Tables display who is seated and the current game status

---

## Gameplay

- Up to 6 players per table
- Game state is **synchronized across all players in real time**
- All players see the same board, pot, and action as it happens
- A player's turn has a **time limit**; inaction results in an auto-fold
- Chip math (pots, winners, side pots) is **authoritative** — clients cannot manipulate results

---

## Chip Tracking

- Each player starts a table session with a defined buy-in
- Chips are tracked **per table**, not globally
- The table records each player's **net gain/loss** across hands
- An end-of-session summary shows each player's result

---

## Out of Scope

- Real money
- Tournaments
- Global chip wallet across tables
- Mobile app
