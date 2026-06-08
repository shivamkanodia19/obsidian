# felt.bet TikTok Slideshow Skill / MCP Guardrails - 2026-05-15

## Purpose

This is not literal model training. It is the **operating spec** future agents, skills, and MCP-assisted workflows should follow so we stop shipping:

- bad crops
- duplicated screenshots with no new meaning
- text cut off by TikTok UI
- proof assets overlapping copy
- generic ad layouts that do not match Felt

## Non-Negotiables

- Final PNGs must be exactly `1080 x 1920`.
- All essential text must remain inside the conservative safe area already encoded in `felt_tiktok_carousel.html`.
- Every slide needs one dominant message and one dominant proof asset.
- Use real felt.bet UI only. Do not invent fake interface states.
- Never use red error states, signed-out states, or broken-flow captures unless the assignment explicitly requires them.
- No casino-coded language or real-money framing.
- If a screenshot crop is too small to explain the point in under 2 seconds, it is decorative and should be replaced or enlarged.

## Role Assignments By Skill

### `content-strategy`

Owns:

- the emotional job of each slide
- the sequence logic across all 5 slides
- headline and subtext brevity

Must enforce:

- `slide 1 = tension`
- `slide 2 = relief`
- `slide 3 = proof`
- `slide 4 = mastery`
- `slide 5 = return / CTA`

Prompt rule:

`Do not write more than one promise per slide. If two claims appear in one slide, delete one.`

### `content-research-writer`

Owns:

- evidence behind strategic claims
- platform best-practice sourcing
- compliance phrasing

Must enforce:

- every psychological hook maps to a real Felt product truth
- every external best-practice claim has a credible source
- all copy avoids manipulative gambling language

Prompt rule:

`If the claim cannot be shown in a real screenshot, weaken the claim or remove it.`

### `canvas-design`

Owns:

- composition
- focal hierarchy
- color restraint
- screenshot legibility

Must enforce:

- one hero screenshot per slide
- max two support crops
- text cannot sit on top of busy UI
- gold is accent, not wallpaper
- support crops must add proof, not clutter

Prompt rule:

`Treat the screenshot as the hero object. Design around it; do not bury it under styling.`

### `audit`

Owns:

- final structural QA
- detection of collisions, unsafe text, and export mistakes

Must enforce:

- no text overflow
- no text-safe-zone violations
- no proof-asset overlap with essential text
- exact export dimensions

## Role Assignments By Tool / Workflow

### Browser capture / MCP screenshot tools

Before saving any source screenshot:

- capture the full truthful state first
- save the uncropped original
- only then create derived crops in composition
- reject captures with browser chrome, partial panels, or clipped CTA controls

### Figma or design-surface MCPs

If used:

- treat them as ideation or layout helpers, not as the source of truth
- always bring the final proof back to local HTML export if the local pipeline is more reliable
- do not trust a frame until local export confirms the crop and safe zone

### Local HTML composition

The canonical composition source is:

- `05_Outputs/images/felt_tiktok_2026-05-14/composition/felt_tiktok_carousel.html`

Rules:

- any screenshot layer must get `data-proof="true"` and a readable `data-name`
- any essential text element must keep `data-essential="true"` and `data-text="true"`
- never add a new proof asset without QA afterward

### Local render script

The canonical export command is:

```powershell
.\render_felt_tiktok_carousel.ps1 -VersionSuffix v4 -RunQa -GenerateQaShots
```

What the script now enforces:

- renders each slide individually
- runs QA DOM inspection for each slide
- throws an error if any slide reports `QA WARN`
- can generate visual QA screenshots with overlays
- verifies every export is `1080 x 1920`

## What QA Now Catches Automatically

From `felt_tiktok_carousel.html`:

- text overflow
- text-safe-zone violations
- text-on-text overlap
- proof-asset overlap against essential text

## What Still Requires Human Review

Automation is not enough for these:

- whether the crop shows the right product state
- whether a support crop is meaningful or just decorative
- whether two slides feel too visually repetitive
- whether the slide reads emotionally in under 2 seconds
- whether the sequence feels premium instead of template-like

## Human Review Rubric

Ask these questions in order:

1. `Can I understand the slide in under 2 seconds?`
2. `Does the screenshot prove the copy, or merely accompany it?`
3. `Is the proof asset large enough to matter?`
4. `Is any important text near TikTok UI danger zones?`
5. `Is the gold/green contrast helping hierarchy, or just adding noise?`
6. `Would this still feel credible if the brand name were removed?`

If the answer to any question is no, revise before export.

## Screenshot Crop Rules

- Crop to reveal a concrete affordance: button, code field, table state, feedback, or trainer surface.
- Avoid crops that show mostly blank whitespace.
- Avoid crops that rely on tiny unreadable text.
- Do not crop so aggressively that the UI loses context.
- Do not repeat the same crop shape and scale across all 5 slides.

## Copy Rules

- Headlines should usually be `4-7` words total.
- Subtext should usually be one short sentence.
- Fine print is allowed only when it clarifies the CTA or compliance posture.
- Never let subtext carry the main idea the headline failed to communicate.

## Default Handoff Prompt For Future Agents

Use this verbatim if a future agent takes over:

`Work from the existing felt_tiktok_carousel.html and latest PNG exports. Keep real felt.bet screenshots as the hero. Before export, run the local render script with QA enabled and fix every warning. Do not ship any slide with cropped-off text, proof assets touching essential text, or screenshots that fail to visually support the headline in under 2 seconds.`

## Related Files

- `05_Outputs/images/felt_tiktok_2026-05-14/composition/felt_tiktok_carousel.html`
- `05_Outputs/images/felt_tiktok_2026-05-14/composition/render_felt_tiktok_carousel.ps1`
- `02_Analyst/projects/felt/campaigns/tiktok-slideshow/felt-tiktok-slideshow-retention-strategy-2026-05-15.md`

