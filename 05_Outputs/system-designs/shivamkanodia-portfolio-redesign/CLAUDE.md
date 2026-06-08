# Shivam Portfolio Redesign

This file is the living build brief for the actual website repo.

If you move this planning folder into the site codebase, copy this file to the repo root as `./CLAUDE.md` so Claude Code loads it automatically.

## Instructions For Claude Code

- Treat this file, `PRD.md`, and `IMPLEMENTATION-PLAN.md` as the source of truth.
- Read all three before making major changes.
- Default workflow:
  - explore
  - plan
  - implement
  - verify
- Do not jump into a full visual rewrite before confirming the current repo structure and build flow.
- Preserve the core brand DNA:
  - dark editorial look
  - strong serif + mono contrast
  - founder/operator energy
- Do not preserve the current friction:
  - modal-first pitch behavior
  - broken resume asset
  - weak mobile readability
  - proof hidden inside dense text

## What To Optimize For

- trust in the first 20-30 seconds
- proof before posture
- stronger mobile readability
- clearer project hierarchy
- a portfolio-first homepage
- a separate, intentional `pitch` route

## Current Product Decisions

- Homepage is the default landing surface.
- `Pitch` should become a full route such as `/pitch`.
- The redesign should not collapse into a generic bright SaaS portfolio.
- The top 2-3 projects should receive disproportionate attention and proof.
- `resume.pdf` must work in production.

## Documentation Workflow

The user requested `Context7` for up-to-date docs.

### If Context7 Is Available In Your Environment

- Use `Context7` first for framework and library documentation.

### If Context7 Is Not Available

Use official docs directly and note the fallback in your summary.

Priority references:

- Vite assets and `public` directory:
  - https://vite.dev/guide/assets.html
- React root and rendering guidance:
  - https://react.dev/reference/react-dom/client/createRoot
- WAI modal dialog pattern:
  - https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

## Implementation Notes

### Resume Asset

- If this is a Vite app and the resume should retain a stable filename, place it in `public/` and reference it as `/resume.pdf`.
- Verify the asset both locally and in production preview.
- If inline embed fails, keep a clear direct download/open link visible.

### Pitch Experience

- Prefer a dedicated route over a modal.
- If any modal remains in the app, it must behave as a real accessible modal:
  - focus moves into it
  - focus is trapped correctly
  - `Escape` closes it
  - focus returns to the invoking control

### Homepage

- Keep it skimmable.
- Reduce long uninterrupted paragraphs.
- Introduce more proof surfaces:
  - screenshots
  - metric clusters
  - timelines
  - labels for role and outcome

## Required Tooling And QA Features

These are the extra features I recommend using for this project.

### 1. Playwright Visual QA

Use Playwright after every meaningful UI phase.

Minimum checks:

- homepage desktop
- homepage mobile
- pitch desktop
- pitch mobile
- resume link behavior

Recommended viewports:

- `1440x1000`
- `390x844`

### 2. Reviewer Loop

Run a lightweight review loop after each phase:

- producer: ship the first version
- skeptic: look for trust leaks, regressions, weak copy, accessibility issues, and scope drift
- integrator: apply only the strongest fixes

### 3. Checkpoints

- make a git checkpoint after each completed phase
- do not stack multiple unverified design overhauls into one commit

### 4. Screenshot-Based Decision Making

- keep before/after screenshots
- when design choices are ambiguous, compare screenshots instead of arguing abstractly

## Suggested Working Sequence

1. Confirm repo structure, framework, and asset paths.
2. Fix broken resume handling first.
3. Separate `Pitch` into its own route.
4. Rebuild homepage hierarchy around proof and clarity.
5. Upgrade selected work cards or sections.
6. Improve mobile readability and interaction polish.
7. Run final accessibility and production QA.

## Do And Do Not

### Do

- keep the tone ambitious but grounded
- favor proof over self-description
- use real project evidence wherever possible
- make the site feel intentional on both desktop and mobile

### Do Not

- turn the site into a generic template
- keep dramatic copy that is not supported by proof
- let style choices degrade readability
- leave broken assets or partial experiences in production

## Definition Of Done

The work is only done when:

- the homepage stands on its own as the primary portfolio surface
- the pitch route is intentional and shareable
- the resume works
- mobile readability is materially better
- the strongest projects feel visual and credible
- Playwright screenshots show a clear improvement over the baseline
