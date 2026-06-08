---
title: Prompt For The Next Codex Agent - 2026-05-16
description: Ready-to-paste prompt for the next major Felt TikTok slideshow iteration after v5
last_updated: 2026-05-16
---

# Prompt For The Next Codex Agent

You are taking over the next major iteration of the felt.bet TikTok slideshow after the current `v5` rebuild.

Your job is to inspect the actual `v5` deck, use the browser tooling available in this session, capture better real screenshots only where they genuinely improve the story, and build a materially stronger `v6`.

This is not a maintenance pass. The current work is solid, but it is not the last word.

## Read These Files Before Doing Anything

Strategy and psychology:

- `02_Analyst/projects/felt/strategy/felt-attraction-retention-strategy-2026-05-14.md`
- `02_Analyst/projects/felt/campaigns/tiktok-slideshow/felt-tiktok-slideshow-research-master-brief-2026-05-15.md`
- `02_Analyst/projects/felt/campaigns/tiktok-slideshow/felt-tiktok-slideshow-retention-strategy-2026-05-15.md`

Execution and current-state context:

- `05_Outputs/images/felt_tiktok_2026-05-14/docs/handoff/felt_tiktok_handoff_v5_2026-05-16.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/felt_tiktok_iteration_notes_v5.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/playbooks/felt_tiktok_playwright_future_agent_playbook_2026-05-15.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/qa/felt_tiktok_skill_mcp_guardrails_2026-05-15.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/qa/felt_tiktok_compliance_qa_checklist.md`

Current artifacts:

- inspect `felt_tiktok_slide_1_v5.png` through `felt_tiktok_slide_5_v5.png`
- inspect `composition/felt_tiktok_carousel.html`
- inspect `composition/render_felt_tiktok_carousel.ps1`

## Your Mission

Create a new slideshow version that feels:

- more premium
- more product-legible
- more psychologically sticky
- more swipe-inducing
- more grounded in real felt.bet UI

while staying:

- truthful
- compliant
- restrained
- non-gambling-coded

## Required Workflow

### 1. Critique `v5` First

Before capturing anything, write a findings-first critique of the current `v5` deck.

Look specifically for:

- repetitive or predictable layout rhythm
- screenshots that still feel too zoomed, too clipped, or too distant
- support proof that is still optional rather than necessary
- weak slide-to-slide momentum
- places where the screenshot proves the copy only partially
- anything premium-but-flat rather than premium-and-sticky

### 2. Capture Better Real Product States Only When Worth It

Use Playwright MCP if available.

Capture new real screenshots only if they materially beat the current proof.

Priority targets:

- cleaner home return state
- stronger lobby / invite / rejoin proof
- stronger live table state with readable stacks, blinds, and turn flow
- stronger coaching / review / feedback state
- stronger social continuity or return state if newly accessible

Do not use:

- broken flows
- signed-out states
- error states
- browser chrome
- fabricated UI

### 3. Keep The Narrative Spine

Use this sequence unless a clearly stronger version emerges:

1. friction
2. simplification
3. operational proof
4. mastery
5. return

Each slide should answer one question and open the next.

### 4. Screenshot Rules

- Capture the full truthful state first.
- Save the clean source capture.
- Only then make crops for slide composition.
- Prefer the screenshot that proves the claim faster, not the one that is merely prettier.

Reject any proof asset that:

- relies on tiny unreadable text
- duplicates a previous message without new value
- feels decorative instead of evidentiary
- weakens the slide by creating clutter

### 5. Copy Rules

- one promise per slide
- headline usually `4-7` words
- subtext usually one short sentence
- plain language beats cleverness
- the screenshot must prove the line quickly

Avoid:

- money or winnings framing
- casino tropes
- cheesy gambling language
- vague superiority claims

### 6. Visual System Rules

Aim for:

- premium dark-mode staging
- stronger hierarchy
- more intentional contrast
- more varied pacing across slides

Use:

- dark neutrals as stage
- Felt green as product continuity
- warm gold as sparse attention accent
- real cream UI surfaces as proof contrast

Rules:

- one dominant proof asset per slide
- maximum one support proof crop
- headline wins first glance
- hero proof wins second glance
- support proof stays only if it adds meaning

### 7. Export Requirements

Create `v6` outputs in:

- `05_Outputs/images/felt_tiktok_2026-05-14`

Use these names:

- `felt_tiktok_slide_1_v6.png`
- `felt_tiktok_slide_2_v6.png`
- `felt_tiktok_slide_3_v6.png`
- `felt_tiktok_slide_4_v6.png`
- `felt_tiktok_slide_5_v6.png`

Also create:

- `felt_tiktok_iteration_notes_v6.md`

### 8. QA Requirements

If the existing local HTML/render path remains the best path, keep using it:

- `composition/felt_tiktok_carousel.html`
- `composition/render_felt_tiktok_carousel.ps1`

Before finalizing, verify:

- every slide reads in under 2 seconds
- every slide has a reason to swipe to the next one
- every slide uses real product proof
- nothing feels casino-coded, broken, or untrustworthy
- every export is exactly `1080 x 1920`

### 9. Working Style

- findings first
- then plan
- then capture
- then design
- then QA
- then export

Do not just describe improvements. Make them.

Do not start from scratch unless the current composition file is clearly slowing you down more than helping.

Do not keep weak proof just because it already exists.

## Final Instruction

The next deck should outperform `v5`, not just differ from it.

Be highly taste-driven, but only make claims and design decisions that the actual screenshots can support.
