# Felt Claude Code Execution Prompt

You are Claude Code working on the local Felt codebase.

Your goal is to make `felt.bet` materially more beautiful, premium, and attractive while preserving clarity, usability, trust, and performance.

Do not redesign Felt into a generic startup site or flashy casino site. Keep the tone premium, strategic, tactile, and controlled.

## What You Should Know

- Live site reviewed on `May 24, 2026`
- Public routes reviewed:
  - `https://felt.bet/`
  - `https://felt.bet/poker`
  - `https://felt.bet/poker/play`
  - `https://felt.bet/poker/multiplayer`
  - `https://felt.bet/blackjack`
  - `https://felt.bet/blackjack/solo`
  - `https://felt.bet/blackjack/training`
- Important live findings:
  - Felt already has a strong palette: dark felt greens, gold/ivory accents, serif hero typography
  - The site is clean, but many surfaces still feel static and text-heavy
  - `Blackjack` currently feels more complete than `Poker`
  - Setup/config flows are clear but feel too much like internal tools rather than premium product surfaces
  - `https://felt.bet/lobby` returned a `404` on `May 24, 2026`
  - Multiplayer poker uses engineering-facing placeholder language that should be reframed as polished beta or limited-access product language

## Local Repo Reality

The local work appears split across:

- `blackjack/`
- `poker/`

Do not assume exact file ownership beyond that. Start by auditing the repo and mapping live surfaces to actual local implementation targets.

The live public site may be ahead of the local source snapshots. Verify before changing anything.

## Source References

- Felt: `https://felt.bet/`
- Cult UI: `https://www.cult-ui.com/`
- Cult UI components: `https://www.cult-ui.com/docs/components`
- Skiper UI: `https://skiper-ui.com/`
- Skiper UI components: `https://skiper-ui.com/components`

## Design Guardrails

Preserve and strengthen:

- dark felt atmosphere
- gold/ivory accents
- serif-led premium hierarchy
- confident spacing
- skill-first tone
- quick scanning and obvious interaction states

Avoid:

- generic startup gradients
- purple-heavy AI styling
- novelty-first motion
- casino-noise clutter
- low-contrast microtext
- icon-only ambiguity for important actions

## Components To Adapt

Use these as source inspirations. If a page exposes only description, usage scaffolding, or source-access notes, treat that as the authoritative reference rather than inventing a fake prompt.

### Shift Lobby Cards

- Source: `https://www.cult-ui.com/docs/components/shift-card`
- Source description: "A card that shows more detail on hover."
- Intent:
  - Upgrade Felt destination cards so they start compact and readable, then reveal richer detail on hover or tap
  - Make `Poker` and `Blackjack` cards feel collectible and productized rather than flat feature boxes

### Dynamic Status Island

- Source: `https://www.cult-ui.com/docs/components/dynamic-island`
- Source description: "Composable, animated Dynamic Island primitives for building adaptive notification, status, and action surfaces."
- Intent:
  - Build a compact Felt status capsule for streaks, hint readiness, turn state, bankroll delta, coach alerts, and drill-complete states
  - Keep it smooth and premium, never distracting

### Expandable Hand Card

- Source: `https://www.cult-ui.com/docs/components/expandable`
- Source description: "Expandable Card primitive to easily condense and expand details"
- Intent:
  - Build expandable study surfaces for hand history, coach notes, strategy notes, post-hand summaries, and guide content
  - Keep collapsed states meaningful

### Full-Screen Scenario Morph

- Source: `https://www.cult-ui.com/docs/components/expandable-screen`
- Source description: "A full-screen expandable component with morphing animations using shared layout IDs for smooth transitions"
- Intent:
  - Let a drill tile, lesson tile, or review tile expand into a full-screen training workspace with a premium, continuous transition

### Expandable Action Toolbar

- Source: `https://www.cult-ui.com/docs/components/toolbar-expandable`
- Source description: "Expandable toolbar component with step-based navigation, smooth animations, and enhanced scrolling"
- Intent:
  - Build a compact utility dock for table/training actions like `Hint`, `Why`, `Replay`, `Compare Lines`, `Notes`, and `Settings`

### Morphing Coach Surface

- Source: `https://www.cult-ui.com/docs/components/morph-surface`
- Source description: "A morphing surface component with smooth animations, customizable dimensions, and configurable content"
- Intent:
  - Build an integrated coach/help surface that can grow from compact to rich without crowding gameplay

### Floating Table Dock

- Source: `https://skiper-ui.com/v1/skiper96`
- Source description: "An expandable tabs component with smooth content transitions, direction-aware animations, and dynamic height adjustments."
- Source-access note: paid/source-copy style component
- Intent:
  - Build a pill-style floating dock for high-value table/training utilities with explicit states and labels

### Hero Feature Selector

- Source: `https://skiper-ui.com/v1/skiper76`
- Source description: "Apple-style feature block for latest iphone 17 pro with glassmorphism effects and smooth transitions"
- Source-access note: paid/source-copy style component
- Intent:
  - Build a homepage showcase where a selectable feature stack drives one large visual for `AI Coach`, `Hand Replayer`, `Blackjack Drills`, `Leak Finder`, and `Progress Tracking`

### Live Hand Capsule

- Source: `https://skiper-ui.com/v1/skiper2`
- Source description: "Interactive Dynamic Island with multiple app states and smooth transitions, inspired by iOS"
- Source-access note: paid/source-copy style component
- Intent:
  - Build a compact live-hand capsule that can shift between states like idle, coach active, streak gained, recommended sizing, and review-ready

### Animated Stats Rail

- Source: `https://skiper-ui.com/v1/skiper37`
- Source description: "Number counter with smooth counting animations and easing effects"
- Intent:
  - Upgrade session recap, EV, accuracy, streak, bankroll swing, and progress numbers with precise, trustworthy animated counting

### Strategy Canvas

- Source: `https://skiper-ui.com/v1/skiper73`
- Source description: "Infinite canvas with smooth transitions and content reveal"
- Source-access note: paid/source-copy style component
- Intent:
  - Build an advanced study workspace for spatial review, range exploration, study boards, or collaborative notes
  - Treat this as a secondary advanced surface, not a default interaction

## Extra UI/UX Improvements

Implement these in addition to the component inspirations:

- Add subtle felt texture and slow spotlight drift to hero backgrounds
- Improve suit-mark glow and atmospheric depth without noise
- Strengthen CTA hierarchy on home and hub surfaces
- Upgrade poker setup flows into premium session configurators
- Upgrade blackjack solo/training setup flows into curated mode selectors
- Replace engineering-facing multiplayer placeholder language with polished beta copy
- Make disabled, beta, and coming-soon states clearly subordinate to live actions
- Standardize headers, breadcrumbs, and auth treatment
- Improve contrast of muted/supporting text
- Use ambient motion only: subtle reveal, lift, glow, and transitions

## Build Order

Work in phases. Complete each phase and regress-test before moving on.

### Phase 0

- Audit the repo
- Map live surfaces to real local implementation targets
- Identify the actual style entry points, home surfaces, configurators, gameplay surfaces, and guide/help surfaces
- Write a short execution plan before major edits

### Phase 1

- Shared visual system
- felt texture
- better background atmosphere
- glow/shadow system
- motion primitives
- clearer live/disabled/beta hierarchy

### Phase 2

- Home and hub upgrade
- Shift Lobby Cards
- Hero Feature Selector
- stronger CTA hierarchy
- better hover/tap behaviors

### Phase 3

- Session configurator upgrade
- poker AI setup
- poker multiplayer setup
- blackjack solo setup
- blackjack training setup
- stronger segmented controls
- clearer grouping
- optional session preview/summary if it helps

### Phase 4

- Gameplay and training surfaces
- Dynamic Status Island
- Floating Table Dock
- Morphing Coach Surface
- Expandable Hand Cards
- Animated Stats Rail

### Phase 5

- Polish
- responsive cleanup
- contrast cleanup
- copy cleanup
- remove placeholder engineering language

## Regression Requirements

After every phase:

1. run validation for the affected app
2. manually smoke-test the touched flows
3. capture comparison screenshots if browser tooling is available
4. fix regressions before continuing

### Poker app validation

Run from the `poker` app directory:

```bash
npm run lint
npm run typecheck
npm run test
npm run build:app
```

If UI changes touch engine-linked behavior, also run:

```bash
npm run verify
```

### Blackjack app validation

Run from the `blackjack` app directory:

```bash
npm run build
npm run lint
```

If lint or coverage setup is missing or weak, do not ignore that silently. Add the smallest useful regression protection for the edited surfaces.

## Testing Expectations

- Extend existing tests where useful
- Add focused regression coverage for new UI logic
- Prefer small meaningful tests over broad snapshot spam
- Good targets:
  - mode selection
  - setup defaults
  - disabled/live state rendering
  - expandable guide/help behavior
  - training utility state changes

## Definition Of Done

The work is only done if:

- Felt looks noticeably more premium and attractive
- the UI still scans fast
- the product feels more alive without becoming noisy
- setup flows feel curated and intentional
- gameplay/training surfaces gain higher-quality support UI without clutter
- disabled/beta/unavailable states are obvious
- mobile remains strong
- regression checks pass or gaps are clearly documented

## First Step

Start by auditing the local source, mapping the live reviewed surfaces to actual implementation targets, and writing a short execution plan. Then begin with Phase 1 and Phase 2 unless the audit shows a better order.
