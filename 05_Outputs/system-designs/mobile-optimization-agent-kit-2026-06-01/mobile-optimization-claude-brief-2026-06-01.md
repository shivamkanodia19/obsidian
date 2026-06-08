# Claude Brief: Agentic Mobile Optimization Playbook

Use this file as the operating brief when improving any website for mobile view.

## Mission

Make the site genuinely good on mobile, not just "technically responsive."

That means:

- no horizontal scrolling at common phone widths
- content remains legible and tappable
- navigation, forms, and CTAs work comfortably with thumbs
- above-the-fold content loads quickly
- layout remains stable while assets load
- fixes are verified with tooling, not guessed

## Core Rule

Do not freehand mobile work.

Use a loop:

1. measure real problems
2. inspect layout and interaction failures
3. make small targeted fixes
4. verify with automated checks
5. verify on a real or emulated mobile device
6. report what changed and what still looks risky

## Success Criteria

Treat these as the default acceptance criteria unless the project already has stricter ones.

### Layout

- Works at `320`, `375`, `390`, `414`, `430`, and `768` CSS px widths
- No accidental horizontal overflow
- No clipped text, cut-off buttons, or broken cards
- No unusable fixed headers, drawers, or modals

### Readability

- Body text is readable without zoom
- Headings do not wrap into ugly stacks unless intentional
- Line length stays comfortable
- Key content is visible before heavy scrolling

### Touch and Input

- Primary controls are easy to tap
- Form inputs have the right keyboard types
- Menus and drawers are scroll-safe and dismissible
- Sticky UI does not cover critical content or submit buttons

### Performance

- Mobile LCP target: `<= 2.5s`
- Mobile INP target: `<= 200ms`
- Mobile CLS target: `< 0.1`

If those exact targets are not reachable immediately, still improve them and state the gap clearly.

## Non-Negotiable Technical Checks

- Confirm the page uses a viewport tag like:

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

- Prefer the same URL and responsive layout rather than separate mobile pages
- Keep primary mobile content equivalent to desktop content
- Reserve image and media space with `width` and `height` or `aspect-ratio`
- Do not lazy-load the hero or likely LCP asset
- Use responsive images with `srcset` and `sizes` where appropriate
- Avoid heavy client-side rendering for above-the-fold content when it delays the hero

## Default Workflow

### 1. Measure first

Start with:

- PageSpeed Insights for mobile
- Search Console Core Web Vitals if available
- local runtime checks in Chrome DevTools

If the site has analytics or RUM, prefer that over lab-only assumptions.

### 2. Reproduce the breakage

Check:

- Chrome DevTools Device Mode
- Playwright mobile emulation
- at least one physical device or BrowserStack if available

### 3. Audit the page in this order

1. viewport setup
2. global overflow sources
3. header / nav behavior
4. hero section and first screen
5. cards, grids, and carousels
6. forms and keyboard behavior
7. footer and sticky UI collisions
8. image loading and font loading
9. interactive delays from JavaScript

### 4. Fix small, high-confidence issues first

Typical order:

- remove horizontal overflow
- repair broken stacking and spacing
- fix nav and CTA usability
- reduce hero image and font bottlenecks
- reduce layout shifts
- then optimize slower interactions

### 5. Verify

Run:

- Playwright smoke tests
- Lighthouse or Lighthouse CI
- manual mobile pass

Do not claim "done" from CSS changes alone.

## Local Toolkit

The local toolkit for this pack lives in `toolkit/`.

Installed local packages:

- `@playwright/test`
- `lighthouse`
- `@lhci/cli`
- `web-vitals`

### Toolkit Commands

Run these from `toolkit/`:

```bash
npm install
npm run install:browsers
npm run test:mobile
npm run test:mobile:headed
npm run audit:lhci
```

### What each tool is for

- `@playwright/test`: mobile viewport tests, screenshots, nav/form interaction checks
- `lighthouse`: mobile performance, accessibility, SEO, best-practices auditing
- `@lhci/cli`: repeatable Lighthouse runs in CI to catch regressions
- `web-vitals`: field instrumentation for LCP, INP, and CLS

## External Tools Worth Using

Use these when available:

- PageSpeed Insights: field + lab overview
- Search Console Core Web Vitals: mobile URL-group issues from real users
- Chrome DevTools: device mode, performance traces, layout shifts, network inspection
- BrowserStack: real-device validation across iPhone/Android combinations
- WebPageTest: deeper performance forensics, filmstrips, waterfall, repeat runs

## What to look for during mobile audits

### Layout failures

- elements wider than viewport
- fixed-width cards or tables
- `100vw` causing overflow with scrollbars or padding
- large negative margins
- images without `max-width: 100%`
- code blocks, chips, tabs, or carousels forcing width

### Navigation failures

- menus that open off-screen
- drawers that trap scroll badly
- sticky headers hiding anchor targets
- top bars consuming too much first-screen space

### Typography failures

- font sizes too small on actual phones
- headings with bad wrapping
- excessive `letter-spacing`
- line-height too tight on dense layouts

### Interaction failures

- tiny tap targets
- buttons too close together
- hover-only interactions
- forms with wrong keyboard type
- submit buttons hidden behind the software keyboard

### Performance failures

- hero image discovered late by JS or CSS
- too much lazy loading near the top of the page
- render-blocking fonts or CSS
- excessive JS on load
- long tasks that delay taps
- layout shifts from images, ads, embeds, or font swaps

## Default Fix Patterns

### Layout

- switch fixed widths to fluid widths
- use `minmax()`, Flexbox, Grid, and container queries
- add `max-width: 100%` to media
- use `overflow-wrap: anywhere` for long strings when needed
- replace brittle breakpoint hacks with component-aware sizing

### Images

- add `srcset` and `sizes`
- compress oversized hero assets
- preload or prioritize the true hero asset if it is the LCP element
- lazy-load only below-the-fold images

### Typography

- use fluid sizing carefully
- keep mobile reading size practical
- reduce heading extremes
- prefer stable fallback fonts or good font-display strategy

### Forms

- use correct input types such as `email`, `tel`, `url`
- add `inputmode` where useful
- ensure labels remain visible
- test keyboard overlap on mobile

### Performance

- reduce unnecessary JavaScript
- split or defer non-critical work
- keep the hero discoverable in initial HTML
- reserve space for dynamic content
- avoid layout-affecting animations when possible

## Guardrails for Claude

When doing this work:

- prefer targeted edits over broad redesigns unless asked
- preserve the established visual language unless the page is already broken
- verify every claim with a test, trace, screenshot, or metric
- do not optimize only for emulation if a physical-device check is possible
- do not use desktop-only behavior as proof of success

## Required Deliverables

At the end of a mobile optimization pass, produce:

1. a short summary of the highest-impact issues found
2. the specific fixes made
3. the widths and devices tested
4. Lighthouse or comparable findings before and after, if available
5. remaining risks or follow-up items

## Suggested Working Prompt

Use a prompt like this to start:

```text
Audit and improve this site for mobile view. Start with the highest-impact mobile issues first. Test at 320, 375, 390, 430, and 768 widths. Eliminate horizontal overflow, fix broken layouts, improve tap targets, and improve mobile LCP/INP/CLS where practical. Use the local Playwright and Lighthouse toolkit, verify the changes, and report what changed plus any remaining mobile risks.
```

## Repo Adaptation Instructions

If this toolkit is being moved into a real app repo:

1. copy `toolkit/` into the repo root or a `qa/mobile/` folder
2. set `BASE_URL` to the local preview URL
3. adjust the Playwright test selectors to the actual nav, hero, and CTA structure
4. update Lighthouse CI URLs to real routes
5. add RUM instrumentation with `web-vitals` if the site does not already have it

## Sources and Reference Links

- MDN responsive design: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
- MDN viewport meta: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport
- MDN container queries: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_container_queries
- web.dev responsive design course: https://web.dev/learn/design/
- web.dev Core Web Vitals priorities: https://web.dev/articles/top-cwv
- web.dev optimize LCP: https://web.dev/articles/optimize-lcp
- web.dev optimize INP: https://web.dev/articles/optimize-inp
- web.dev responsive images: https://web.dev/learn/design/responsive-images/
- web.dev font best practices: https://web.dev/articles/font-best-practices
- Chrome DevTools device mode: https://developer.chrome.com/docs/devtools/device-mode
- Chrome DevTools performance panel: https://developer.chrome.com/docs/devtools/performance/overview
- Playwright emulation: https://playwright.dev/docs/emulation
- Lighthouse overview: https://developer.chrome.com/docs/lighthouse/overview/
- Lighthouse CI: https://web.dev/articles/lighthouse-ci
- Google mobile-first indexing: https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing
- Google Core Web Vitals and search: https://developers.google.com/search/docs/appearance/core-web-vitals
