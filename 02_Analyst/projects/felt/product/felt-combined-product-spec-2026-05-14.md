---
title: Felt Combined Product Spec - 2026-05-14
project: felt
strategic: true
status: draft
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-05-14
tags: [felt, product, poker, blackjack, strategy, spec]
---

# Felt Combined Product Spec - 2026-05-14

**Status:** Strategic spec for the merged product  
**Product:** `Felt`  
**Scope:** One app, one account, poker plus blackjack, play-money only for now, web plus mobile view priority

## User-Confirmed Inputs

- Blackjack "real play" means solo play against a dealer simulation, not real-money or human dealer play.
- The product should be one app with one account.
- Poker and blackjack should stay separate inside the app.
- Poker chips are handled by table/session.
- Blackjack currency is lower priority and does not need poker-style table tracking.
- The product is play-money only for now.
- Poker AI play means AI opponents.
- Training means AI coaching.
- Assume the modes already exist and this doc is deciding how the merged product should be structured.

## Brutal Executive Decision

Felt should be **one brand with two clean game lanes**, not one blended "casino app" with mixed modes, mixed chips, and fake synergy.

That means:

- shared shell, shared account, shared friend layer
- separate game hubs for poker and blackjack
- separate gameplay engines and separate coaching logic
- separate economies
- shared brand identity and shared profile only where it actually helps

If you try to over-unify this, the product gets blurrier, the engineering gets worse, and the app starts feeling more like a sketchy social casino than a sharp card product.

## Product Thesis

Felt should position itself as a **play-money card app for social play and skill improvement**, not as a generic casino app.

The clean product promise is:

- **Poker:** play AI opponents, train decisions, and play live with friends
- **Blackjack:** play fast solo sessions against the dealer, train basic strategy with coaching, and run private friend tables

## Brand Architecture

### Product Name

- Use `Felt` as the product name.
- Keep `Poker` and `Blackjack` as first-class game hubs inside Felt.
- Do not create separate in-app mini-brands unless one game later becomes large enough to deserve its own product line.

### What Felt Is

- A card-games app with poker and blackjack
- Play-money only
- Social plus training oriented

### What Felt Is Not

- A real-money gambling app
- A blended chip-wallet casino product
- A fake "AI casino" brand

## Core Product Structure

### Top-Level Navigation

Use a **game-first** information architecture, not a mode-first architecture.

Recommended nav:

- `Home`
- `Poker`
- `Blackjack`
- `Profile`

Persistent global actions:

- notifications/invites
- account/settings
- quick resume

### Why Game-First Is Correct

Do **not** use top-level tabs like `Play`, `Train`, and `Friends`.

That sounds neat, but it is the wrong abstraction because:

- poker play and blackjack play are fundamentally different
- poker training and blackjack training are fundamentally different
- poker friend mode and blackjack friend mode have different table logic

Mode-first navigation makes the app feel like a stitched-together menu. Game-first navigation makes it feel intentional.

## Home Surface

The home screen should be a routing layer, not a dumping ground.

### Home Priorities

- continue last session
- quick launch into favorite game/mode
- recent stats
- current streak or daily challenge
- friend invite/rejoin card
- soft cross-promotion from one game to the other

### First-Time Onboarding

New users should choose a **primary game** first:

- `Poker`
- `Blackjack`

Then choose an initial intent:

- `Play`
- `Train`
- `Play with Friends`

This reduces cognitive load immediately. Throwing six modes at a new user on first launch is bad product design.

## Shared Systems

These systems should be shared across the whole app:

- authentication and account management
- friend graph and invite system
- notifications and rejoin prompts
- responsive design system for web and mobile view
- profile shell
- session history shell
- analytics and event instrumentation
- age gate / disclaimer layer
- support and feedback tools

These systems should **not** be forced into one abstraction too early:

- core gameplay logic
- AI opponent logic
- coaching logic
- chip/bankroll systems

## Poker Hub

Poker remains the more strategically differentiated part of Felt.

### Poker Hub Primary Actions

- `Train`
- `Play with Friends`
- `Play AI`

This order is intentional.

Brutal truth:

- Poker friend play is socially powerful.
- Poker training is content-rich and marketable.
- Poker AI play is useful, but it is not the main public wedge.

### Poker Mode 1: AI Play

Purpose:

- entertainment
- practice through repeated hands
- low-friction solo play

Requirements:

- AI opponents with distinct styles
- stable hand history
- clean action feedback after hands
- fast restarts and session flow

Do not oversell this as "superhuman AI poker." If the opponents are not genuinely strong and varied, that claim will age badly.

### Poker Mode 2: Training

Purpose:

- decision coaching
- repeated spot reps
- habit correction

Requirements:

- shared poker rules engine with gameplay
- post-action feedback tied to actual game state
- optional explanation depth
- spot drills plus full-session coaching

Strategic rule:

Poker training should inherit the product principle from [[02_Analyst/projects/poker-app/felt-ui-feedback-2026-05-03]]:

- no duplicate action logic
- no coaching layer that invents authority the engine does not have

### Poker Mode 3: Play with Friends

Purpose:

- private social play
- repeat sessions
- identity and retention

Requirements:

- private tables
- invite codes/links
- rejoinable seats
- session-scoped chips
- clear turn-state sync
- max six players from the current poker PRD

Keep poker chips table-scoped and session-scoped. That is still the right decision.

## Blackjack Hub

Blackjack should be faster, simpler, and more approachable than poker.

### Blackjack Hub Primary Actions

- `Play Solo`
- `Train`
- `Play with Friends`

This order is also intentional.

Brutal truth:

- Blackjack is a quicker-entry game than poker.
- Its strongest early UX is fast solo repetition.
- The training loop can be excellent, but the first promise is still quick play.

### Blackjack Mode 1: Solo Play

Purpose:

- fast sessions
- low-friction play
- repeatable reps

Requirements:

- dealer simulation
- quick table start
- rules presets where relevant
- fast rebuy/reset
- clean session summary

Important wording decision:

Do **not** market this as an `AI dealer`.

Why:

- a blackjack dealer mostly follows fixed rules
- calling that "AI" is fake sophistication
- users will eventually smell the nonsense

Internally you can still treat the table as simulated play. Publicly, this should be framed as:

- solo blackjack
- dealer play
- quick blackjack sessions

### Blackjack Mode 2: Training

Purpose:

- basic strategy improvement
- fast error correction
- confidence building

Requirements:

- immediate action feedback
- explanation for hit/stand/double/split/surrender decisions where applicable
- optional test mode with coaching hidden until after the hand
- accuracy tracking over time

This is where AI language can actually help:

- AI coaching
- explanation layer
- mistake review

### Blackjack Mode 3: Play with Friends

Purpose:

- social sessions
- private group tables
- shared experience without poker complexity

Recommended structure:

- multiple players seated at one table
- each player plays independently against the same dealer
- host controls rules and table settings
- session results shown per player

Do not force blackjack friend mode into a poker-like multiplayer model. That would be the wrong social experience.

## Economy and Progression

### Hard Decision

**Do not create a shared global chip wallet across poker and blackjack.**

That is the cleanest choice for product clarity and risk control.

### Poker Economy

- chips are session-scoped and table-scoped
- buy-in happens per table
- no cross-table poker wallet in V1

### Blackjack Economy

- use a session bankroll, not a permanent cross-game wallet
- let users choose a quick starting stack or reset easily
- track stats, not chip identity

This matches your instinct that blackjack tracking is less important.

### Shared Progression

Share only what actually makes sense:

- profile
- streaks
- achievements
- unlockable cosmetics
- friend identity

Keep performance stats separate:

- poker stats
- blackjack stats

Do not create one fake "Felt skill score." Poker and blackjack skill are different.

## AI and Logic Architecture

### Shared Infrastructure

Can be shared:

- prompt orchestration patterns
- explanation card UI
- analytics
- user settings

### Separate Game Systems

Must stay separate:

- poker engine
- blackjack rules engine
- poker AI opponents
- blackjack decision coaching model
- poker training logic

### Brutal Engineering Call

Do **not** over-generalize into one giant multi-game rules engine unless there is already a clean abstraction that proves itself.

What you can share safely:

- card rendering
- deck/shoe primitives
- RNG utilities
- table UI primitives
- session services

What you should not force together:

- betting logic
- decision trees
- coaching systems
- win-resolution logic

Premature engine unification is where good product teams waste months pretending to be elegant.

## UX Rules

### Rule 1

The user should always know:

- which game they are in
- whether they are playing or training
- whether the session is solo or social

### Rule 2

Training overlays must be clearly optional.

Do not contaminate normal play with unwanted coaching noise.

### Rule 3

Responsive design is a real requirement, not a post-launch polish item.

Since web plus mobile view are both priority:

- mobile must have thumb-friendly actions
- table layouts must survive narrow screens
- training explanations must collapse well on mobile
- web must still feel dense and intentional, not like stretched mobile

### Rule 4

Home should route. Hubs should focus. Sessions should stay clean.

## Product Sequencing Priorities

If everything is assumed built, the post-build priority is not "add more features." It is:

1. clean up the shared shell
2. make mode boundaries obvious
3. instrument retention by game and mode
4. polish poker training and friend play
5. polish blackjack solo speed and training clarity
6. cross-sell users from one game to the other without making the app feel muddled

## Cross-Sell Strategy Inside the App

Cross-sell should be contextual, not loud.

Examples:

- Poker user finishes training session -> "Want faster reps? Try blackjack training."
- Blackjack user finishes 5 solo sessions -> "Want deeper social play? Try private poker tables."

Do not force aggressive cross-sell popups everywhere. That makes the app feel like two products stapled together.

## Main Product Risks

### Risk 1: Brand dilution

If the app tries to be equally poker-first and blackjack-first everywhere, it loses sharpness.

### Risk 2: Economy confusion

A shared chip wallet would create unnecessary complexity and more casino-like optics with little upside.

### Risk 3: Fake AI positioning

Calling ordinary rules-based behavior "AI" is short-term marketing sugar and long-term trust damage.

### Risk 4: Overbuilt shared engine

If the team tries to make poker and blackjack live inside one over-abstracted game core, progress will slow down for the wrong reason.

### Risk 5: Weak onboarding

If users land in a mixed menu without a clear first action, conversion will suffer.

## Final Product Call

Felt should ship and operate as:

- **one brand**
- **one account**
- **two distinct game hubs**
- **separate economies**
- **shared shell**
- **poker-first public identity**
- **blackjack as a fast, strong second lane**

That is the cleanest version of the merged product.
