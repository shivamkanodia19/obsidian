---
title: Felt Simple Plan - 2026-05-14
project: felt
strategic: true
status: active
last_updated: 2026-05-14
tags: [felt, plan, poker, blackjack, product, business]
---

# Felt Simple Plan - 2026-05-14

**Product:** `Felt`  
**Scope:** one app, one account, two separate game hubs, play-money only, web and mobile priority

## Core Idea

Felt should be a **sharp card app**, not a generic casino app.

- `Poker` is the stronger brand and product wedge.
- `Blackjack` is the simpler, faster second lane.
- The app should share shell, account, friends, and design system.
- The games should stay structurally separate inside the product.

## Brutal Product Rule

If combining the apps makes poker worse, the merger failed.

That means:

- poker UI/UX is the source of truth
- blackjack should adapt to the shared shell
- the final app should feel intentional, not stitched together

## What The App Needs To Be

### Poker

- AI play
- training with AI coaching
- real friend play

### Blackjack

- solo play against dealer simulation
- training with AI coaching
- friend mode

### Shared Layer

- one account
- one home screen
- one profile
- one friend/invite system
- one responsive design system

## Product Structure

Use game-first navigation:

- `Home`
- `Poker`
- `Blackjack`
- `Profile`

Do not use top-level mode-first navigation like `Play`, `Train`, and `Friends`. That would make the product feel messy.

## Development Plan

### Phase 1: Merge Foundation

- choose one host repo
- move to one shared app shell
- unify auth, profile, and navigation
- preserve the best poker UX patterns

### Phase 2: Functional Merge

- integrate blackjack into the shared shell
- keep poker and blackjack engines separate
- keep poker chips table-based
- keep blackjack currency lightweight
- make all major flows work on web and mobile

### Phase 3: Quality And Regression

- run repeated Playwright testing
- test auth, home, poker, blackjack, and friend flows
- verify Supabase schema, policies, storage, and edge functions
- remove rough edges until the app feels like one product

### Phase 4: Launch Readiness

- tighten onboarding
- improve screenshots, landing pages, and store copy
- test with real users
- fix retention and clarity issues before spending on growth

## Marketing Plan

### Positioning

Felt should be marketed as a **play-money card app for sharper decisions and better social sessions**.

### Primary Marketing Angle

- lead with `Poker`
- use `Blackjack` as the easy secondary lane

### Content Focus

- poker decision clips
- blackjack decision clips
- AI coaching moments
- friend table moments
- build-in-public product clips

### Channel Focus

- TikTok
- Instagram Reels
- YouTube Shorts
- landing pages on `felt.bet`

### Marketing Rule

Do not market this like gambling.

Use:

- play money
- training
- coaching
- friends
- better decisions

Avoid:

- win money
- cash out
- casino vibes
- fake AI claims

## Business Plan

### Near-Term Goal

Get a product people actually want to come back to.

Success matters more than premature monetization.

### Early Business Focus

- retention
- session frequency
- friend invites
- cross-play from poker to blackjack
- proof that users understand the product quickly

### Likely Monetization Later

- premium features
- cosmetics/themes
- advanced training tools
- clubs, leagues, or hosted social features

Do not rush into ads or monetization that cheapens the product.

## Key Metrics

- account signup conversion
- day 1 / day 7 retention
- poker session starts
- blackjack session starts
- friend invite rate
- training mode usage
- cross-over rate between poker and blackjack

## End Goal

Build a **credible, clean, marketable card-games product** where:

- poker is the main identity
- blackjack broadens usage without weakening the brand
- the app looks and feels like one polished system
- users come for play and stay for training, friends, and repeat sessions
- the product is strong enough to support real growth and later monetization

## Immediate Working Goal

Combine the two apps into one Felt product that is:

- visually poker-first
- functionally complete
- regression-tested
- responsive on web and mobile
- good enough to ship without embarrassment

## Related Notes

- [[felt-combined-product-spec-2026-05-14]]
- [[felt-marketing-plan-2026-05-14]]
