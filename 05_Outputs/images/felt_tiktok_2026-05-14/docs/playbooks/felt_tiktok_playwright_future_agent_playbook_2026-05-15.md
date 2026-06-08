# felt.bet TikTok Slideshow Playwright Future-Agent Playbook - 2026-05-15

## Purpose

This is the end-to-end execution playbook for the next agent who will use the Playwright MCP and local assets to rebuild the Felt TikTok slideshow properly.

Use this document as the main workflow guide.

Read alongside:

- `02_Analyst/projects/felt/campaigns/tiktok-slideshow/felt-tiktok-slideshow-research-master-brief-2026-05-15.md`
- `02_Analyst/projects/felt/strategy/felt-attraction-retention-strategy-2026-05-14.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/qa/felt_tiktok_skill_mcp_guardrails_2026-05-15.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/qa/felt_tiktok_compliance_qa_checklist.md`

## Mission

Do not treat the current slides as final-quality creative.

Use them only for:

- narrative pacing reference
- screenshot inventory reference
- QA guardrail reference

The next version should outperform the current set on:

- screenshot quality
- crop quality
- visual hierarchy
- slide-to-slide pacing
- swipe curiosity
- premium restraint

## Output Folder

Work in:

- `05_Outputs/images/felt_tiktok_2026-05-14`

Existing relevant assets in that folder:

- real screenshots already captured from felt.bet
- `felt_tiktok_carousel.html`
- `render_felt_tiktok_carousel.ps1`
- existing PNG exports from `v1` through `v4`

## Available Playwright-MCP-Relevant Tools

At minimum, the surfaced Playwright MCP tools in this environment include:

- `mcp__playwright__browser_snapshot`
- `mcp__playwright__browser_take_screenshot`
- `mcp__playwright__browser_hover`
- `mcp__playwright__browser_network_requests`
- `mcp__playwright__browser_navigate_back`
- `mcp__playwright__browser_close`

Practical use:

- use `browser_snapshot` with boxes when you need DOM structure or element coordinates
- use `browser_take_screenshot` for truthful captures
- use `browser_hover` to reveal hidden states only when those states are part of the real product
- use `browser_network_requests` when a broken state might be caused by auth or data issues

## End-To-End Workflow

### 1. Read Before Touching Anything

Read these first:

- the research master brief
- the original attraction/retention strategy note
- the compliance checklist
- the current guardrail file
- the current handoff note

Then inspect:

- `felt_tiktok_slide_1_v4.png` through `felt_tiktok_slide_5_v4.png`

Do not assume the current composition is the right final layout. Its main value is the QA system and some sequencing logic.

### 2. Decide What Needs Replacement

Before capturing anything new, write a short critique of the current slide set.

At minimum, look for:

- repeated layout rhythm
- screenshots that are too zoomed out or too cropped
- text that is technically safe but visually weak
- support crops that feel decorative
- dead space that is not helping focus
- weak slide 1 to slide 2 curiosity handoff

### 3. Capture Better Screenshots With Playwright

The goal is not "more screenshots." The goal is better proof states.

#### Capture rules

- always capture the full truthful screen before making derived crops
- prefer stable logged-in states
- do not use broken, signed-out, or error states unless the brief explicitly requires them
- avoid browser chrome
- avoid partial modals cut off by viewport edges unless that cut-off is intentional and still legible

#### Suggested naming pattern

- `felt_<surface>_<device>_<dimensions>.png`
- `felt_<surface>_snapshot.md` for notes if needed

#### Priority states to capture

Highest priority:

- clean home screen with `private tables`, `play with friends`, or `join with a code`
- clean lobby screen showing `start a new table` and `join` behavior
- best available live table state where stacks, blinds, seats, and turn state are readable
- clean training screen with obvious practice entry points
- clean feedback / coaching state with explanation visible

If newly accessible:

- successful host / table-creation state
- successful table-share or rejoin state
- stronger social return surface than the current home capture

#### Capture strategy by slide intent

For slide 1:

- capture the cleanest "organized home for games" state

For slide 2:

- capture the clearest host/join/code flow

For slide 3:

- capture the most legible room-state / table-state proof

For slide 4:

- capture the clearest training + feedback pairing

For slide 5:

- capture the best return surface showing social continuity and practice adjacency

#### When to use `browser_snapshot`

Use it when:

- you need element boxes to understand crop opportunities
- you want to identify exact UI blocks worth centering in the final composition
- you need to make sure the useful proof is not hidden below the fold

#### When to use `browser_take_screenshot`

Use it when:

- the UI state is clean and stable
- you have decided it is worth preserving as a master source image

Take:

- one full truthful source capture
- optional tighter alternate captures if they reveal a materially better proof moment

### 4. Choose The Narrative Before Designing

Do not start composing slides before locking the 5-slide logic.

Recommended sequence:

1. friction
2. simplification
3. operational proof
4. mastery
5. return

Each slide must answer one question and open the next:

1. what is the mess?
2. how does Felt simplify it?
3. does it hold up in actual use?
4. does it make me better?
5. why would I come back?

### 5. Write Copy Only After Screenshot Selection

Rule:

- screenshot first
- copy second

Why:

- the claim should be constrained by what the UI can actually prove

Copy rules:

- headline usually `4-7` words
- subtext usually one short sentence
- one promise per slide
- plain language beats clever language

Avoid:

- casino-coded language
- money / winnings framing
- vague superiority claims
- hype with no proof

### 6. Build The Slides

Preferred composition priorities:

- one dominant proof asset per slide
- one support proof asset only if it adds meaning
- strong headline-to-proof eye path
- high contrast typography
- restrained use of gold as attention accent
- Felt green as continuity color, not the only color event

What must vary across slides:

- crop scale
- object weighting
- focal rhythm
- emotional tone

What must stay consistent:

- brand tone
- premium restraint
- truthful UI
- compliance lane

### 7. Use Existing Local Infrastructure Where Helpful

Existing local assets that may help:

- `felt_tiktok_carousel.html`
- `render_felt_tiktok_carousel.ps1`

If the local HTML path remains the fastest reliable export path, update it.

If another local path is clearly better, use it, but preserve the same QA standards:

- safe zones
- overlap checks
- exact `1080 x 1920`
- clean PNG export

### 8. QA Before Final Export

The future agent must do both machine QA and human QA.

#### Machine QA

If using the existing HTML/render path:

- tag proof assets
- keep essential text tagged
- run the render script with QA enabled

Command:

```powershell
.\render_felt_tiktok_carousel.ps1 -VersionSuffix <new_version> -RunQa -GenerateQaShots
```

Required outcome:

- all slides return `QA PASS`
- all exports verify as `1080 x 1920`

#### Human QA

Ask:

1. can I understand the slide in under 2 seconds?
2. does the screenshot prove the copy?
3. is the hero screenshot large enough to matter?
4. is the slide visually distinct from the previous slide?
5. does the slide feel premium rather than loud?
6. does anything feel casino-coded, error-prone, or untrustworthy?

### 9. Compliance Check

The slideshow must stay framed around:

- private games
- invite-only tables
- organization
- session clarity
- training
- review
- decision practice

It must avoid:

- real money framing
- winning / profit language
- big-win energy
- gambling cliches
- misleading claims

### 10. Export And Document

Required deliverables:

- 5 final PNGs
- short iteration notes
- exact screenshot-to-slide mapping
- any remaining limitations

Required file dimensions:

- `1080 x 1920` for every final PNG

## What To Keep Vs What To Replace

Keep:

- the best truthful screenshots if no better ones are captured
- the existing QA logic
- the compliance lane
- the narrative idea of `friction -> return`

Replace aggressively if a better option exists:

- weak hero crops
- repetitive layout rhythm
- support crops that do not add proof
- decorative darkness with too little color energy
- any slide whose proof is not readable at first glance

## Fast Decision Rules

If choosing between two screenshot states:

- choose the one with the clearer proof, not the prettier background

If choosing between two layouts:

- choose the one that makes the next swipe feel more necessary

If choosing between two copy options:

- choose the one the screenshot can prove immediately

If a support crop is tiny:

- enlarge it or delete it

If a slide is technically clean but emotionally flat:

- it still needs revision

## Suggested Task Framing For The Next Agent

Use this internal brief:

`Rebuild the Felt TikTok slideshow from the strongest truthful felt.bet screenshots you can capture with Playwright. Use the research master brief for retention psychology and the local QA guardrails for export safety. The final deck should feel more premium, more swipe-inducing, and more product-legible than the current v4 set.`

## Sources And Local References

Research:

- `02_Analyst/projects/felt/campaigns/tiktok-slideshow/felt-tiktok-slideshow-research-master-brief-2026-05-15.md`
- `02_Analyst/projects/felt/strategy/felt-attraction-retention-strategy-2026-05-14.md`

Execution references:

- `05_Outputs/images/felt_tiktok_2026-05-14/docs/handoff/felt_tiktok_handoff.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/qa/felt_tiktok_skill_mcp_guardrails_2026-05-15.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/qa/felt_tiktok_compliance_qa_checklist.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/composition/felt_tiktok_carousel.html`
- `05_Outputs/images/felt_tiktok_2026-05-14/composition/render_felt_tiktok_carousel.ps1`

