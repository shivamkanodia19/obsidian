# Prompt For The Next Codex Agent

You are taking over the next major iteration of the felt.bet TikTok slideshow build.

Your job is to go to `felt.bet`, use the available browser tooling in this session, capture **real, clean, high-quality screenshots**, and build a materially stronger 5-slide TikTok slideshow than the current local set.

This is not a light polish pass. The current slides still have meaningful weaknesses. Your goal is to improve the **actual screenshot quality, crop quality, pacing, hierarchy, and swipe-through psychology** while staying truthful to the real product.

## Your Mission

Create a new slideshow version that feels:

- more premium
- more psychologically sticky
- more swipe-inducing
- more product-legible
- more grounded in real felt.bet UI

while staying:

- compliant
- tasteful
- non-gambling-coded
- truthful

## First: Read These Files Before Doing Anything

Strategy and psychology:

- `02_Analyst/projects/felt/strategy/felt-attraction-retention-strategy-2026-05-14.md`
- `02_Analyst/projects/felt/campaigns/tiktok-slideshow/felt-tiktok-slideshow-research-master-brief-2026-05-15.md`
- `02_Analyst/projects/felt/campaigns/tiktok-slideshow/felt-tiktok-slideshow-retention-strategy-2026-05-15.md`

Execution and QA:

- `05_Outputs/images/felt_tiktok_2026-05-14/docs/playbooks/felt_tiktok_playwright_future_agent_playbook_2026-05-15.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/qa/felt_tiktok_skill_mcp_guardrails_2026-05-15.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/qa/felt_tiktok_compliance_qa_checklist.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/handoff/felt_tiktok_handoff.md`

Current artifacts:

- inspect `felt_tiktok_slide_1_v4.png` through `felt_tiktok_slide_5_v4.png`
- inspect `felt_tiktok_carousel.html`
- inspect `render_felt_tiktok_carousel.ps1`

## Required Workflow

### 1. Critique the current slideshow first

Before capturing new screenshots, write a short findings-first critique of the current `v4` set.

Specifically look for:

- weak or repetitive layout rhythm
- screenshots that are too zoomed out, too cropped, or not proving the copy strongly enough
- dead space that does not increase focus
- support crops that feel decorative
- weak slide 1 to slide 2 swipe momentum
- anything that feels too dark, too flat, or not premium enough

### 2. Use real website captures

Go to `felt.bet` and use the browser tooling available in the session. If Playwright MCP is surfaced, use it. If not, use the best equivalent browser tool available and say so.

Capture **new real screenshots** where better ones are available.

Priority capture targets:

- clean home screen with strong `private tables`, `play with friends`, or `join with a code` proof
- clean lobby / host / join flow
- strongest live table state where stacks, blinds, turn state, and seats are readable
- strongest training entry state
- strongest feedback / coaching / review state
- if accessible, a clean successful table-creation or rejoin state

Do not use:

- signed-out states
- error states
- broken flows
- browser chrome
- misleading mock UI

### 3. Screenshot standards

For every useful state:

- capture the full truthful screen first
- save the best clean source capture
- only then create derived crops for slide composition

Choose screenshots based on:

- legibility in under 2 seconds
- how well they prove the copy
- how visually distinctive they are from one another

Reject captures that:

- are too busy
- hide the important proof
- rely on tiny unreadable text
- feel like decorative filler rather than evidence

### 4. Narrative structure

Build the slideshow around this sequence:

1. friction
2. simplification
3. operational proof
4. mastery
5. return

Each slide should answer one question and open the next:

1. what is the mess?
2. how does Felt simplify it?
3. does it actually hold up in real use?
4. does it help me get better?
5. why would I come back or bring my group here?

### 5. Psychological goals

Use the research already documented. The final slideshow should create retention and swipe-through through:

- curiosity gap with fast payoff
- tension then relief
- progressively stronger specificity
- clear product-proof anchoring
- social return logic
- mastery / improvement framing
- identity / taste signaling

Do not chase retention through:

- fake hype
- casino energy
- money language
- unresolved mystery
- decorative excess

### 6. Visual system goals

The slides should feel:

- premium dark-mode
- sharper in contrast
- more intentional in hierarchy
- more varied from slide to slide

Color logic:

- dark neutrals as the stage
- Felt green as product continuity
- warm gold as sparse attention accent
- real cream product surfaces as proof contrast

Rules:

- one dominant proof asset per slide
- maximum one or two support proof crops
- headline must win first glance
- hero screenshot must win second glance
- support proof only stays if it adds meaning

### 7. Copy rules

Write copy only after choosing screenshots.

Rules:

- one promise per slide
- headline usually `4-7` words
- subtext usually one short sentence
- plain language beats cleverness
- screenshot must prove the claim quickly

Avoid:

- money / winnings framing
- casino tropes
- cheesy gambling language
- vague superiority claims

Safe positioning:

- private games
- invite-only tables
- organization
- session clarity
- decision practice
- training
- review

### 8. Output requirements

Create a distinct new version in:

- `05_Outputs/images/felt_tiktok_2026-05-14`

Use these names:

- `felt_tiktok_slide_1_v5.png`
- `felt_tiktok_slide_2_v5.png`
- `felt_tiktok_slide_3_v5.png`
- `felt_tiktok_slide_4_v5.png`
- `felt_tiktok_slide_5_v5.png`

Also create:

- `felt_tiktok_iteration_notes_v5.md`

That note should include:

- findings on what was wrong with the previous version
- what you changed and why
- what screenshots you captured and used
- which research conclusions you actually applied
- any remaining limitations
- confirmation that every final PNG is exactly `1080 x 1920`

### 9. QA requirements

If the local HTML/render path remains the best export path, use it and preserve the QA system already built into:

- `felt_tiktok_carousel.html`
- `render_felt_tiktok_carousel.ps1`

If you use another composition path, you still must enforce the same standards:

- safe text areas
- no text clipping
- no proof asset collisions with essential text
- exact `1080 x 1920` PNGs

Before finalizing, verify:

- every slide is understandable in under 2 seconds
- every slide has a clear reason to swipe to the next one
- every slide uses real product proof
- nothing looks casino-coded, broken, or untrustworthy
- every final PNG is exactly `1080 x 1920`

### 10. Working style

- findings first
- then plan
- then capture
- then design
- then QA
- then export

Do not just talk about improvements. Make them.

Do not start from scratch unless the existing source files are clearly slowing you down more than helping.

Do not keep weak screenshots just because they already exist.

Do not confuse safe-zone compliance with actual design quality.

The best result should feel like:

- a real product story
- built from real felt.bet UI
- optimized for TikTok swipe momentum
- premium enough to stop scroll
- restrained enough to stay credible

## Final instruction

Be highly taste-driven, but make decisions that the research and the screenshots can justify.

The final slideshow should outperform `v4`, not just differ from it.

