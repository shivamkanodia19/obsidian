---
title: Felt TikTok Codex Image Prompt System v6 - 2026-05-16
description: First-pass prompt system for refining Felt TikTok slideshow images without losing product truth or compliance
last_updated: 2026-05-16
---

# Felt TikTok Codex Image Prompt System v6

## Purpose

This playbook is the first-pass prompt system for refining Felt TikTok slideshow images and slide compositions.

It is based on the current Felt strategy and slideshow working set:

- `02_Analyst/projects/felt/strategy/felt-simple-plan-2026-05-14.md`
- `02_Analyst/projects/felt/strategy/felt-marketing-plan-2026-05-14.md`
- `02_Analyst/projects/felt/campaigns/tiktok-slideshow/felt-tiktok-slideshow-retention-strategy-2026-05-15.md`
- `02_Analyst/projects/felt/campaigns/tiktok-slideshow/felt-tiktok-slideshow-research-master-brief-2026-05-15.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/handoff/felt_tiktok_handoff_v5_2026-05-16.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/felt_tiktok_iteration_notes_v5.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/docs/qa/felt_tiktok_compliance_qa_checklist.md`
- `05_Outputs/images/felt_tiktok_2026-05-14/composition/felt_tiktok_carousel.html`

## Strategic Ground Truth

All refinement prompts should preserve these truths:

- Felt is a `play-money` card app, not a casino product.
- The brand is `poker-first`, with training, private tables, and friend-group organization as the cleanest marketing wedge.
- The slideshow narrative should stay `friction -> simplification -> operational proof -> mastery -> return`.
- The creative should feel `premium, calm, product-led, and credible`, not loud, scammy, or gambling-coded.
- Real product proof matters more than decorative polish.

## Reusable System Prompt

Use this as the base system prompt for any model or agent refining a single Felt slideshow slide, a slide image comp, or a related proof asset.

```text
You are refining a single image or slide composition for Felt's TikTok slideshow.

Your job is to improve clarity, hierarchy, emotional pull, and swipe momentum without breaking product truth.

Brand and product context:
- Felt is a play-money card app with private tables, training, practice, review, and friend-group organization.
- Do not make Felt look like a real-money casino, gambling app, or hype-driven betting product.
- Felt should feel premium, restrained, modern, legible, and product-led.

Non-negotiable rules:
- Treat real Felt screenshots as the primary proof whenever the slide makes a product claim.
- Do not fabricate UI states, buttons, chips, players, metrics, or social proof that the product cannot currently show.
- Do not introduce browser chrome, error states, signed-out states, fake notifications, or broken flows.
- Do not use casino-coded language or imagery: jackpots, neon slot vibes, lucky streaks, cash, winnings, payouts, or "go all in" energy.
- Keep essential text inside conservative TikTok-safe zones.
- Optimize for under-2-second readability.
- One slide = one dominant message, one dominant proof asset, and at most one useful support asset.

Refinement priorities in order:
1. Stronger proof
2. Faster comprehension
3. Better composition and spacing
4. Better visual rhythm and premium tone
5. Stronger swipe curiosity into the next slide

Visual direction:
- Dark neutral stage
- Real cream product surfaces
- Felt green for continuity
- Warm gold used sparingly as an attention accent
- Controlled contrast, not loud contrast

Output standard:
- Make the screenshot prove the copy faster.
- Remove decorative elements that do not add evidence.
- Preserve truthful UI details.
- Keep the slide emotionally clear: tension, relief, proof, mastery, or return depending on slide role.

If forced to choose, prefer truth and legibility over spectacle.
```

## Prompt Input Template

Use this template when sending a refinement brief to a model, designer, or future agent.

```text
Project: Felt TikTok slideshow
Slide number: {{slide_number}}
Slide role: {{slide_role}}
Primary message: {{primary_message}}
Viewer question to answer: {{viewer_question}}
Primary proof asset: {{primary_proof_asset}}
Support proof asset: {{support_proof_asset_or_none}}
Truth boundary: {{what_must_not_be_fabricated}}
Composition direction: {{composition_direction}}
Spacing direction: {{spacing_direction}}
Headline direction: {{headline_direction}}
Subtext direction: {{subtext_direction}}
Proof intent: {{proof_intent}}
Negative prompts: {{negative_prompts}}
Compliance guardrails: {{compliance_guardrails}}
Output goal: {{what_success_looks_like}}
```

## Prompt Fields Reference

### Composition

Use this field to define the eye path and proof hierarchy.

- `Goal`: establish the first glance, second glance, and support glance.
- `Default`: headline first, hero screenshot second, support detail third.
- `Preferred language`: "one dominant screenshot", "clear left-to-right or top-to-bottom reading path", "support crop only if it adds proof".
- `Avoid`: mirrored clutter, sticker-like crops, tiny proof panels, busy overlaps, centered everything.

Example:

```text
Composition direction: Large desktop hero anchored low in frame, headline block high-left, one small mobile support crop overlapping the lower-right edge only if it adds specificity.
```

### Spacing

Use this field to protect readability and premium tone.

- `Goal`: make the slide breathe without creating dead space.
- `Default`: generous outer margins, visible separation between copy and proof, no text sitting on busy UI.
- `Safe-zone bias`: keep essential copy comfortably inside conservative TikTok-safe bounds.
- `Avoid`: edge collisions, cramped gutters, floating micro-elements, text grazing image corners.

Example:

```text
Spacing direction: Maintain generous top breathing room above the headline, at least one clean gutter between text and proof, and enough negative space around the CTA or support crop so the frame feels calm rather than packed.
```

### Negative Prompts

Use this field to block the most common failure modes.

- `Goal`: prevent drift into fake UI, casino energy, and generic AI styling.
- `Default`: no fabricated UI, no cash language, no neon glow overload, no floating chips, no extra people, no fake device chrome, no lorem ipsum, no distorted text.
- `Avoid`: "make it exciting" without constraints. That almost always causes bad output.

Example:

```text
Negative prompts: No casino cues, no money imagery, no fake player avatars, no invented analytics, no browser chrome, no unreadable tiny labels, no oversaturated gold, no generic fintech dashboard styling.
```

### Proof Intent

Use this field to state what the screenshot must prove emotionally and functionally.

- `Goal`: connect the message to visible product truth.
- `Default`: every claim should map to a visible UI state.
- `Questions to answer`: What should the viewer believe after one glance? Which exact UI region proves it?
- `Avoid`: vague benefit language with no visible evidence.

Example:

```text
Proof intent: The viewer should instantly understand that Felt gives one place to host, join, and rejoin private games. The visible join-code and lobby structure should do most of the persuasion.
```

### Compliance

Use this field to keep the slide inside the current Felt marketing lane.

- `Goal`: product-led, play-money, training-oriented, private-table oriented.
- `Default`: no real-money or profit framing, no hype gambling verbs, no misleading social proof.
- `Required bias`: the slide should feel like a smart card product, not a gambling ad.

Example:

```text
Compliance guardrails: Keep copy anchored in private tables, practice, review, and group organization. No winnings, payouts, jackpots, lucky streaks, or cash-out implications. If chips appear, they must read as truthful in-product play chips only.
```

## Slide-By-Slide Prompt Brief

These briefs align to the current `v5` narrative and proof inventory.

### Slide 1: Friction

- `Role`: tension hook
- `Viewer question`: Is there a cleaner way to run game night?
- `Current best proof assets`:
  - `captures/home/felt_home_desktop_clean_1440x1400_v5.png`
  - `captures/home/felt_home_mobile_clean_430x932_v5.png`
- `Current copy lane`: `Game night needs one home.`
- `Prompt brief`:

```text
Refine slide 1 as the tension hook. Make the frame feel like organized relief is possible, not like chaos is already happening. Use the clean home desktop screenshot as the hero proof and the mobile home screenshot only if it adds real specificity. Keep the message structural and plain: one home for private tables, join codes, and practice. Build a premium dark stage with restrained gold and Felt green accents. The screenshot should read fast and feel truthful, calm, and useful.

Composition direction: Large wide hero near the lower half, copy block high-left, optional small mobile support crop angled or nested only if it earns its space.
Spacing direction: Strong top margin, generous gap between headline and subtext, no collisions between the support crop and the main reading path.
Proof intent: Show that Felt consolidates the messy logistics of private card sessions into one clean home surface.
Negative prompts: No fake social activity, no fake active room counts, no busy collage treatment, no casino-neon atmosphere, no decorative chip explosions.
Compliance guardrails: Keep the slide about organization and private play, not winning or betting.
```

### Slide 2: Simplification

- `Role`: fast payoff
- `Viewer question`: How quickly can people get into a game?
- `Current best proof assets`:
  - `captures/lobby/felt_lobby_mobile_430x932_v5.png`
  - `captures/lobby/felt_lobby_desktop_1440x1200_v5.png`
- `Current copy lane`: `One code. Whole crew in.`
- `Prompt brief`:

```text
Refine slide 2 as the immediate payoff to slide 1. The viewer should feel that hosting, joining, and rejoining are simple enough to understand in one glance. Use the mobile lobby screenshot as the hero if it clearly shows the join path; use the desktop lobby crop as support only if it strengthens the host or rejoin story. Emphasize flow clarity, not quantity of UI.

Composition direction: One strong phone hero with the text block opposite it; support crop can sit lower and flatter to reinforce the system rather than compete with it.
Spacing direction: Keep the phone hero large enough to read the main interface zones, with breathing room around the copy and any host/join/rejoin label element.
Proof intent: Prove that Felt reduces social friction by making the invite and join flow feel lightweight.
Negative prompts: No fake invite notifications, no added avatars, no fake chat bubbles, no tiny unreadable code labels, no hard-sell CTA energy.
Compliance guardrails: Language should stay on access and coordination, not gambling action.
```

### Slide 3: Operational Proof

- `Role`: credibility
- `Viewer question`: Does the product stay clear during real play?
- `Current best proof asset`:
  - `captures/guided/felt_guided_live_desktop_1440x1400_v5.png`
- `Current copy lane`: `You can read the room.`
- `Prompt brief`:

```text
Refine slide 3 as the strongest proof slide in the deck. Let the live guided table desktop state do most of the work. The key emotional outcome is trust: the table should look readable, intentional, and under control mid-hand. Avoid over-framing it with decorative copy blocks or extra crops unless a crop adds a new layer of evidence.

Composition direction: Oversized panoramic hero that owns most of the slide, with a compact headline area that does not compete with the table.
Spacing direction: Preserve a clean runway from headline to screenshot. Keep margins wide enough that the hero still feels elevated rather than cramped.
Proof intent: Show visible turn state, stacks, and action clarity so the product feels like a real system, not a mockup.
Negative prompts: No added cards, no invented opponents, no fake chip balances, no motion-blur gimmicks, no UI redraws that alter actual product structure.
Compliance guardrails: This is operational clarity, not gambling hype. The frame should communicate control and legibility.
```

### Slide 4: Mastery

- `Role`: differentiation and improvement
- `Viewer question`: Does Felt help me get sharper, not just get seated?
- `Current best proof assets`:
  - `captures/training/felt_training_desktop_1440x1400_v5.png`
  - `captures/guided/felt_guided_table_feedback.png`
- `Current copy lane`: `Train spots. Review leaks.`
- `Prompt brief`:

```text
Refine slide 4 as the mastery proof. The hero should be the training desktop capture, with the feedback crop only if it makes the coaching value more concrete. This slide should feel more specific and more skill-oriented than the earlier slides. Make improvement visible, not abstract.

Composition direction: One strong desktop training hero with one optional feedback detail inset placed where it reinforces, not interrupts, the reading path.
Spacing direction: Keep the support crop from sitting too close to the headline. Give the hero enough scale that the training context reads immediately.
Proof intent: Prove that Felt offers decision practice, review, and progress visibility rather than just table logistics.
Negative prompts: No fake solver outputs, no invented coaching text, no pseudo-analytics, no generic edtech visual tropes, no excessive glow around the inset.
Compliance guardrails: Keep the language around training, review, and decision quality. No "win more" framing.
```

### Slide 5: Return

- `Role`: social continuity and CTA
- `Viewer question`: Why would people come back?
- `Current best proof asset`:
  - `captures/home/felt_home_mobile_clean_430x932_v5.png`
- `Current copy lane`: `Your crew gets a home base.`
- `Prompt brief`:

```text
Refine slide 5 as the calm close. The viewer should leave feeling that Felt gives a group a place to return to, not just a one-time utility. Use the clean mobile home surface as the main proof. The CTA should feel credible and product-led, with minimal pressure.

Composition direction: One clean phone hero paired with a grounded CTA card or footer block. The frame should feel quieter and more resolved than the earlier slides.
Spacing direction: Preserve a clear separation between the CTA block and the phone proof so the close feels composed, not crowded.
Proof intent: Show repeat-use logic through private tables, home re-entry, and practice adjacency.
Negative prompts: No fake badges, no fake retention numbers, no urgency banners, no "download now" ad cliches, no cash or reward imagery.
Compliance guardrails: Close on private tables and play chips only. Do not imply money, prizes, or earnings.
```

## Recommended Defaults By Field

Use these defaults unless a slide clearly needs an exception.

| Field | Default |
| --- | --- |
| `Narrative role` | Match the fixed 5-slide sequence already used in `v5` |
| `Proof hierarchy` | 1 hero screenshot, max 1 support crop |
| `Headline length` | 4-7 words when possible |
| `Subtext length` | 1 short sentence |
| `Background` | dark neutral with subtle gold and green atmosphere |
| `Color ratio` | mostly dark neutrals, some Felt green, sparse warm gold |
| `Text placement` | inside safe zones, never on busy UI |
| `Proof source` | real Felt screenshots first |
| `Refinement bias` | truth and legibility over novelty |

## When To Use Real Screenshots vs Image Generation

### Use Real Screenshots When

- the slide is making a direct product claim
- the UI itself is the evidence
- the viewer needs to trust that the feature, state, or flow is real
- the slide is about hosting, joining, rejoining, training, review, or table readability

For this Felt deck, that means the core proof on all 5 slides should remain real screenshots unless a better truthful capture is unavailable and the generated asset is purely atmospheric.

### Use Image Generation Only When

- you are creating non-product atmospheric support such as background texture, subtle lighting mood, abstract shape layers, or framing elements
- you are mocking a visual direction before replacing it with truthful screenshot proof
- you need a decorative support element that does not imply any product capability, metric, player count, or UI state

### Do Not Use Image Generation For

- fake screenshots
- invented interface states
- fabricated player tables or join flows
- fake coaching outputs
- fake proof of social activity
- any product evidence that the viewer could mistake as real Felt UI

## Practical Approval Test

Before accepting any refined slide, ask:

1. Is the main claim proven by the visible asset in under 2 seconds?
2. Does the slide make Felt feel cleaner and smarter, not more casino-like?
3. Is every support element earning its space?
4. Would a skeptical viewer still believe the product promise after seeing the screenshot?
5. If I removed one decorative element, would the slide get better? If yes, remove it.

## First-Pass Conclusion

This prompt system should keep future Felt slideshow refinements inside the right lane:

- truthful proof
- stronger hierarchy
- calmer premium staging
- clearer slide-specific emotional jobs
- no drift into fake UI or gambling-coded creative

Use it as the default prompt framework for the next round of slide image refinement, then tighten per-slide wording after new proof captures are reviewed.
