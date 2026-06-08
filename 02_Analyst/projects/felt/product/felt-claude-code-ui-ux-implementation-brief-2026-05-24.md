# Claude Code Implementation Brief: Felt UI/UX Upgrade

Use this file as the working prompt and operating brief for ongoing UI/UX improvements to `felt.bet`.

## Role

You are Claude Code working on the local Felt codebase. Your job is to make `felt.bet` more beautiful, premium, and attractive without sacrificing clarity, speed, or usability.

You must implement improvements in phases and run regression checks after every phase. Do not make the site flashy for its own sake. The right feel is premium, strategic, tactile, and controlled.

## Current Context

### Live-site review date

- Reviewed against the live public site on `May 24, 2026`.

### Live routes reviewed

- `https://felt.bet/`
- `https://felt.bet/poker`
- `https://felt.bet/poker/play`
- `https://felt.bet/poker/multiplayer`
- `https://felt.bet/blackjack`
- `https://felt.bet/blackjack/solo`
- `https://felt.bet/blackjack/training`

### Source UI references

- Felt: `https://felt.bet/`
- Cult UI: `https://www.cult-ui.com/`
- Cult UI components index: `https://www.cult-ui.com/docs/components`
- Skiper UI: `https://skiper-ui.com/`
- Skiper UI components index: `https://skiper-ui.com/components`

### Important live findings

- `felt.bet` already has a strong base palette: dark felt greens, gold/ivory accents, serif hero typography.
- The site is clean and legible, but many surfaces still feel static and text-heavy.
- `Blackjack` currently feels more complete than `Poker`.
- The `poker` and `blackjack` setup/config pages are clear, but they feel more like internal tools than premium product surfaces.
- `https://felt.bet/lobby` returned a `404` during review on `May 24, 2026`.
- The multiplayer poker setup uses engineering-facing copy about the framework/server state; this should be reframed as a polished beta/limited-access product state.

## Local Codebase Map

The local Felt work appears to be split across two apps:

- `blackjack/`
  - stack: `Next.js 15`, `React 19`, `Tailwind`, `Radix`, `Supabase`
- `poker/`
  - stack: `Vite`, `React 18`, custom CSS, `motion`, `vitest`

Do not assume the exact file structure beyond that. During Phase 0, discover the real entry points and edited surfaces directly from the repo before making changes.

### Source mismatch note

The live public site appears to be ahead of or somewhat different from the local source snapshots. Before making changes, audit the current local routes and map each live surface to the best local implementation target. Do not assume exact one-to-one parity.

## Design Direction

Keep and strengthen these qualities:

- Dark felt atmosphere
- Gold/ivory accents
- Confident spacing
- Strategic, skill-first tone
- Clean information hierarchy

Do not drift into:

- Generic startup gradients
- Purple-heavy default AI styling
- Over-animated novelty UI
- Casino-noise visual clutter
- Low-contrast microtext

## Component Inspirations To Implement

These are the best ideas to adapt from `Cult UI` and `Skiper UI` into Felt.

### 1. Shift Lobby Cards

Inspiration:

- `Cult UI` card interactions and richer hover/lift surfaces

Implement as:

- Stronger `Poker` and `Blackjack` destination cards on the home page
- Richer CTA treatment
- Deeper visual hierarchy
- Hover/tap reveal behavior that shows extra detail without making the cards noisy

Requirements:

- Mobile cannot depend on hover
- Cards must remain readable at a glance
- Disabled or unavailable states must look clearly different from live states

### 2. Hero Feature Selector

Inspiration:

- `Skiper UI` Apple Feature Block

Implement as:

- A homepage feature showcase where a vertical stack or segmented list drives one large central visual
- Candidate topics: `AI Coach`, `Hand Replayer`, `Blackjack Drills`, `Leak Finder`, `Progress Tracking`

Requirements:

- The visual panel must feel product-real, not like fake marketing art
- Each state should communicate one major product value
- Transition motion should be smooth and restrained

### 3. Dynamic Status Island / Live Hand Capsule

Inspiration:

- `Cult UI` Dynamic Island
- `Skiper UI` Dynamic Island

Implement as:

- A compact, premium status capsule for gameplay/training surfaces
- Use it for streaks, coach state, hint readiness, turn status, bankroll deltas, or drill-complete states

Requirements:

- It must never distract from primary game controls
- It should expand only when useful
- One primary status at a time

### 4. Expandable Hand Card

Inspiration:

- `Cult UI` Expandable Card

Implement as:

- Expandable study surfaces for hand review, coach notes, guide sections, decision explanations, and post-hand summaries

Requirements:

- The collapsed state must still carry the key takeaway
- Expansions should feel smooth and deliberate
- Avoid modal overload where inline expansion will do

### 5. Full-Screen Scenario Morph

Inspiration:

- `Cult UI` ExpandableScreen

Implement as:

- Smooth morphing transition from a compact lesson/drill tile into a full-screen study or training workspace

Requirements:

- Use this selectively for premium transitions
- Back/close behavior must be obvious and instant
- Do not trap mobile users in an awkward overlay flow

### 6. Floating Table Dock

Inspiration:

- `Skiper UI` Expandable Tabs Navigation

Implement as:

- A floating pill-style dock for high-value navigation or utility controls
- Best fit: table tools, training controls, notes, coach, sound, replay, settings

Requirements:

- Labels or discoverable states must remain clear
- Do not replace essential controls with mystery icons
- Keep the action set small

### 7. Animated Stats Rail

Inspiration:

- `Skiper UI` animated number patterns

Implement as:

- Higher-quality stat presentation for recaps, streaks, EV gain, bankroll swing, accuracy, and challenge progress

Requirements:

- Motion must be quick and informative
- Never create doubt about the underlying numbers

### 8. Morphing Coach Surface

Inspiration:

- `Cult UI` morphing panels and expandable toolbars

Implement as:

- A compact-to-expanded coach/help panel for hints, explanations, strategic notes, or decision analysis

Requirements:

- It should feel integrated, not bolted on
- The gameplay surface must stay primary

## Source Links And Prompt Material

Important note:

- On `May 24, 2026`, these component pages did not consistently expose a dedicated AI-generation prompt block.
- Where a page exposed only a description, usage scaffold, or source-access note, use that as the authoritative source material.
- The prompt seeds below are intentionally source-aligned and should be treated as closer to the component authors' intent than a fresh guess.

### 1. Shift Lobby Cards

- Source page: `https://www.cult-ui.com/docs/components/shift-card`
- Source-exposed description: "A card that shows more detail on hover."
- Source access: Cult exposes this as a source-distributed component through its registry/docs flow.
- Source-aligned prompt seed:

Build a premium destination card for Felt that starts compact and readable, then reveals richer detail on hover or tap. Preserve fast scanning, but add a stronger sense of depth, hierarchy, CTA intent, and tactile lift. Use the effect to make `Poker` and `Blackjack` cards feel collectible and productized rather than flat feature boxes.

### 2. Dynamic Status Island

- Source page: `https://www.cult-ui.com/docs/components/dynamic-island`
- Source-exposed description: "Composable, animated Dynamic Island primitives for building adaptive notification, status, and action surfaces."
- Source access: Cult exposes this as a registry/docs component.
- Source-aligned prompt seed:

Build a composable Felt status capsule that can stay compact by default and expand when state changes matter. It should support training feedback, streaks, hint readiness, turn state, bankroll delta, and coach alerts. Keep the motion smooth and springy, but never let it overpower primary gameplay.

### 3. Expandable Hand Card

- Source page: `https://www.cult-ui.com/docs/components/expandable`
- Source-exposed description: "Expandable Card primitive to easily condense and expand details"
- Source access: Cult exposes this as a registry/docs component.
- Source-aligned prompt seed:

Build an expandable card system for Felt study surfaces so hand history, coach notes, strategy notes, and post-hand summaries can stay condensed until needed. The collapsed state must still communicate the key takeaway. Expansion should feel polished, spatial, and low-friction, not like a heavy modal.

### 4. Full-Screen Scenario Morph

- Source page: `https://www.cult-ui.com/docs/components/expandable-screen`
- Source-exposed description: "A full-screen expandable component with morphing animations using shared layout IDs for smooth transitions"
- Source access: Cult exposes this as a registry/docs component.
- Source-aligned prompt seed:

Build a morphing transition in Felt where a drill tile, lesson tile, or review tile can expand into a full-screen training workspace using shared layout motion. The change should feel premium and continuous, not like an abrupt route jump. Closing the surface must be instant and obvious on desktop and mobile.

### 5. Expandable Action Toolbar

- Source page: `https://www.cult-ui.com/docs/components/toolbar-expandable`
- Source-exposed description: "Expandable toolbar component with step-based navigation, smooth animations, and enhanced scrolling"
- Source access: Cult exposes this as a registry/docs component.
- Source-aligned prompt seed:

Build a compact Felt action dock that can expand into a small, guided utility toolbar for table and training actions such as `Hint`, `Why`, `Replay`, `Compare Lines`, `Notes`, and `Settings`. Keep the action set intentionally small, the hierarchy obvious, and the expanded state lightweight.

### 6. Morphing Coach Surface

- Source page: `https://www.cult-ui.com/docs/components/morph-surface`
- Source-exposed description: "A morphing surface component with smooth animations, customizable dimensions, and configurable content"
- Source access: Cult exposes this as a registry/docs component.
- Source-aligned prompt seed:

Build a morphing coach/help surface for Felt that grows from a compact assistant affordance into a richer panel for hints, ranges, strategic explanation, and quick review controls. The coach surface should feel like part of the product shell, not a bolted-on drawer.

### 7. Floating Table Dock

- Source page: `https://skiper-ui.com/v1/skiper96`
- Source-exposed description: "An expandable tabs component with smooth content transitions, direction-aware animations, and dynamic height adjustments."
- Source access note: Skiper marks this one as paid-only source access rather than open CLI install.
- Source-aligned prompt seed:

Build a floating pill-style dock for Felt that can switch between compact icon mode and expanded labeled mode with direction-aware transitions. Use it for top-level table or training utilities. It should feel elegant and light, but remain explicit enough that players never have to guess what a control does.

### 8. Hero Feature Selector

- Source page: `https://skiper-ui.com/v1/skiper76`
- Source-exposed description: "Apple-style feature block for latest iphone 17 pro with glassmorphism effects and smooth transitions"
- Source guidance exposed by page: the example renders the component as a full-screen showcase block; attribution notes it is inspired by Apple product pages.
- Source access note: Skiper marks this one as paid-only source access rather than open CLI install.
- Source-aligned prompt seed:

Build a Felt homepage feature showcase with Apple-style product-storytelling structure: a stack of selectable feature pills on one side and a large hero visual on the other. Each selection should reveal one major capability such as `AI Coach`, `Hand Replayer`, `Blackjack Drills`, `Leak Finder`, or `Progress Tracking`. Keep the transitions smooth, premium, and restrained.

### 9. Live Hand Capsule

- Source page: `https://skiper-ui.com/v1/skiper2`
- Source-exposed description: "Interactive Dynamic Island with multiple app states and smooth transitions, inspired by iOS"
- Source access note: Skiper marks this one as paid-only source access rather than open CLI install.
- Source-aligned prompt seed:

Build an interactive, stateful live-hand capsule for Felt that can switch between multiple compact states such as idle, coach active, streak gained, recommended sizing, spot loaded, and review ready. It should feel crisp and intentional, with smooth transitions between states and zero interference with gameplay.

### 10. Animated Stats Rail

- Source page: `https://skiper-ui.com/v1/skiper37`
- Source-exposed description: "Number counter with smooth counting animations and easing effects"
- Source access note: this page exposes a direct CLI install path for the free component.
- Source-aligned prompt seed:

Build an animated stats rail for Felt that upgrades key numbers like EV gained, accuracy, bankroll swing, streaks, and session totals with smooth counting motion and easing. The animation must feel precise and trustworthy rather than flashy.

### 11. Strategy Canvas

- Source page: `https://skiper-ui.com/v1/skiper73`
- Source-exposed description: "Infinite canvas with smooth transitions and content reveal"
- Source guidance exposed by page: the example uses a full-screen container with configurable image density and spacing.
- Source access note: Skiper marks this one as paid-only source access rather than open CLI install.
- Source-aligned prompt seed:

Build a high-end study canvas for Felt that supports spatial exploration of ranges, study paths, hand clusters, or collaborative notes. It should feel like a tactical workspace, not a generic settings page. Treat this as a secondary advanced surface, not the default interaction pattern.

## Additional UI/UX Improvements From The Live Audit

Implement these in addition to the borrowed component ideas:

### Home and hub improvements

- Add a faint felt texture and slow spotlight drift to hero backgrounds
- Improve suit-mark glow and overall atmosphere without making the page busy
- Standardize home-to-hub spacing and CTA hierarchy

### Poker improvements

- Upgrade the AI setup screen from a plain form into a premium session configurator
- Show a more vivid relationship between buy-in, opponent count, and play mode
- Replace engineering-facing multiplayer placeholder language with polished beta language
- Make `Coming Soon` and disabled states clearly subordinate to live options

### Blackjack improvements

- Upgrade `solo` and `training` configuration panels so they feel like curated mode selectors, not raw forms
- Convert strategy/help content into better drawers, expandable cards, or study panels
- Strengthen the hierarchy between primary mode cards and the lower `Extended Modes` area

### Shared improvements

- Standardize header/breadcrumb/auth styling across surfaces
- Improve contrast of muted copy and legal/supportive text
- Add ambient motion: subtle reveal, lift, glow, and transitions
- Make empty, disabled, beta, and unavailable states feel intentional
- Preserve fast scanning on mobile and desktop

## Implementation Order

Work in phases. Complete one phase, validate it, then continue.

### Phase 0: Audit and Baseline

1. Inspect both codebases and map live surfaces to local components/routes.
2. Identify exactly which files control:
   - home pages
   - poker setup surfaces
   - blackjack setup surfaces
   - table headers / action surfaces
   - guide/help surfaces
3. Save a short implementation plan in the repo before major edits.
4. If browser tooling is available, capture baseline screenshots for comparison.

### Phase 1: Shared Visual System

Implement:

- stronger background atmosphere
- felt texture treatment
- controlled glow/shadow system
- motion primitives
- clearer live/disabled/beta state hierarchy
- Let Claude identify the actual shared style entry points during Phase 0 instead of assuming exact file paths.

### Phase 2: Home and Hub Upgrade

Implement:

- Shift Lobby Cards
- Hero Feature Selector
- better CTA hierarchy
- stronger hover/tap interactions
- Let Claude identify the actual home and hub entry points during Phase 0 instead of assuming exact file paths.

### Phase 3: Session Configurator Upgrade

Implement:

- premium setup panels for poker AI / multiplayer
- premium setup panels for blackjack solo / training
- stronger segmented controls
- cleaner choice grouping
- session summary or preview where it helps
- Let Claude locate the real setup/configurator surfaces during the repo audit.

### Phase 4: Gameplay and Training Surfaces

Implement:

- Dynamic Status Island / Live Hand Capsule
- Floating Table Dock
- Morphing Coach Surface
- Expandable Hand Cards
- Animated Stats Rail
- Let Claude identify the real gameplay, table, coach, and guide surfaces during the repo audit.

### Phase 5: Polish and Cleanup

Implement:

- copy cleanup
- consistent headers
- responsive fixes
- contrast fixes
- removal of placeholder/engineering-facing product text

## Regression Loop

After every phase:

1. Run the relevant local validation commands.
2. Manually smoke-test the affected flows.
3. If browser tooling exists, capture updated screenshots and compare to baseline.
4. Fix regressions before moving on.

### Poker validation

From the `poker` app directory run:

```bash
npm run lint
npm run typecheck
npm run test
npm run build:app
```

If any UI logic changes touch engine-linked behavior, also run:

```bash
npm run verify
```

### Blackjack validation

From the `blackjack` app directory run:

```bash
npm run build
```

Also run:

```bash
npm run lint
```

If `lint` is not configured or fails due to missing setup, do not ignore that silently. Either fix the setup or explain the limitation and add the smallest useful regression safety net for the edited surfaces.

## Testing Expectations

You are expected to improve regression coverage while implementing.

### Poker

- Extend existing test coverage where appropriate
- Add focused tests for changed UI logic if the current suite does not already protect it

### Blackjack

- If there is no meaningful automated UI coverage for the touched surfaces, add lightweight regression coverage for the highest-risk flows
- Prefer small, focused tests over broad snapshot spam
- Good targets:
  - home mode selection
  - setup form defaults
  - disabled/live state rendering
  - expandable guide behavior

## Acceptance Criteria

The work is successful only if:

- Felt looks more premium and attractive immediately
- The UI still scans fast and feels trustworthy
- Home/hub cards are more magnetic, not just more decorated
- Setup flows feel curated and productized
- Gameplay/training surfaces gain better status and support UI without clutter
- Disabled/beta/unavailable states are visually obvious
- Mobile remains strong
- Regression checks pass or any gaps are clearly documented

## Working Style

- Do not dump a giant rewrite if phased improvements will get there more safely.
- Prefer evolving the existing visual language over replacing it.
- Reuse existing patterns where sensible, but do not stay trapped in bland defaults.
- Make the site feel more like a serious modern game-training product and less like a raw tool.
- Keep notes brief and practical after each phase: what changed, what was tested, what still needs work.

## First Task

Start by auditing the local source, mapping the live reviewed surfaces to actual files, and proposing a short phase-by-phase execution plan before editing. Then begin with Phase 1 and Phase 2 unless the audit shows a better order.
