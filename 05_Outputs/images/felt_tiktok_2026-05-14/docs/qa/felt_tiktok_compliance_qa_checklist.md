# felt.bet TikTok Carousel Compliance + QA Checklist

Reviewed against:
- `felt_tiktok_handoff.md`
- `felt_tiktok_carousel.html`
- existing exports `felt_tiktok_slide_1.png` through `felt_tiktok_slide_5.png`

Current export status:
- Existing `v1` PNGs in this folder are all `1080 x 1920`

## 1. Compliant Messaging Checklist

Use this as a pass/fail list before approving any `v2` slide.

### Positioning

- Keep the story anchored in `private games`, `invite-only tables`, `group organization`, `session tracking`, `training`, `review`, `decision practice`, and `coach feedback`.
- Make Felt feel like a `productivity + training tool for poker groups`, not a gambling promotion.
- Prefer language about `running a smoother game` over language about `winning`, `beating`, or `profiting`.

### Must Avoid

- No `real money` framing in headlines, subheads, CTAs, captions, or callouts.
- No `casino` tropes: jackpots, roulette, slot-machine cues, flying chips, neon gambling clichés, lucky-streak framing, or “big win” energy.
- No cheesy gambling copy such as `go all in`, `print money`, `stack cash`, `clean up`, `crush the table`, `run it up`, or similar hype language.
- No implication that Felt helps users `win money`, `gamble smarter`, or `make better bets`.

### Safer Copy Patterns

- Good: `host a private table`
- Good: `track the session`
- Good: `practice tough spots`
- Good: `review decisions`
- Good: `keep your game organized`
- Good: `play chips only`
- Good: `invite-only`
- Good: `training mode`

### Higher-Risk Terms Requiring Care

- `poker`: allowed, but should stay category-descriptive rather than hype-driven.
- `buy-ins`: allowed only when clearly framed as organization or tracking, not winnings or profit.
- `chips`: acceptable if clearly `play chips only` and presented as part of the real UI.
- `table`: acceptable if clearly private, friend-group, or training oriented.

### Screenshot Truthfulness

- Use only real Felt UI states already captured in this folder.
- Do not fabricate flows or overstate capabilities that were not accessible in capture.
- Remove or crop out any broken, signed-out, or error-state messaging unless the slide is explicitly about a limitation.

## 2. Likely Risk Areas In Current v1

These are the biggest compliance and QA watch-outs from the current set.

### Text Risks

- Slide 1 headline: `Poker night gets messy fast.`
  Risk: category-accurate, but it leads with poker culture instead of product utility. Better if paired with logistics pain, not gambling excitement.
- Slide 3 headline: `Track buy-ins without the chaos.`
  Risk: acceptable, but `buy-ins` needs supporting context that keeps it in the lane of session organization and play-chip tracking.
- Slide 5 footer: `Private poker tools + training.`
  Risk: usable, but `private game tools + training` is a safer alternative if we want less gambling-coded language.

### Imagery Risks

- The `Create a table` screenshot used in current slides shows an error state (`Could not create table...`).
  Risk: this weakens credibility and should not survive into final exports.
- Any crop that emphasizes cards/chips more than interface controls can drift toward gambling vibes instead of product utility.
- Strong gold CTA treatments are fine, but if paired with overly aggressive verbs they can feel salesy or casino-adjacent.

## 3. Final Export QA Rubric

Score each slide `Pass / Needs revision / Fail`.

### A. Compliance

- `Pass`: product-led, no real-money framing, no casino tropes, no cheesy gambling copy, screenshots remain truthful.
- `Needs revision`: one risky phrase or one crop that over-indexes on gambling-coded imagery, but easy to correct.
- `Fail`: money/profit/winning language, glamorized gambling framing, or misleading UI representation.

### B. Message Clarity

- `Pass`: slide meaning is obvious in under 2 seconds; one main idea only.
- `Needs revision`: readable, but competing focal points or copy is slightly too long.
- `Fail`: unclear hook, crowded layout, or headline/subhead compete with screenshot details.

### C. Product-Led Proof

- `Pass`: real UI is the hero, and the screenshot clearly supports the claim on the slide.
- `Needs revision`: real UI is present, but the crop does not strongly reinforce the message.
- `Fail`: screenshot feels decorative, confusing, or contradicts the copy.

### D. Visual Restraint

- `Pass`: premium dark-mode feel, tasteful gold/green accents, no tacky glow overload, no casino energy.
- `Needs revision`: mostly premium, but one or two effects feel noisy or too ad-like.
- `Fail`: effects, color, or composition feel gimmicky, loud, or cliché.

### E. Technical Export

- `Pass`: exact file names, exact pixel dimensions, PNG format, sharp text, no clipping, no accidental browser chrome.
- `Needs revision`: technically usable but has soft text, inconsistent margins, or export artifacts.
- `Fail`: wrong dimensions, wrong naming, clipped copy, or visible broken UI/error state.

## 4. File + Export Verification Guidance

Required `v2` outputs:
- `felt_tiktok_slide_1_v2.png`
- `felt_tiktok_slide_2_v2.png`
- `felt_tiktok_slide_3_v2.png`
- `felt_tiktok_slide_4_v2.png`
- `felt_tiktok_slide_5_v2.png`

Required dimensions:
- `1080 x 1920` for every final PNG

PowerShell check:

```powershell
Add-Type -AssemblyName System.Drawing
Get-ChildItem "05_Outputs/images/felt_tiktok_2026-05-14/exports/v2/felt_tiktok_slide_*_v2.png" |
  ForEach-Object {
    $img = [System.Drawing.Image]::FromFile($_.FullName)
    [PSCustomObject]@{
      Name = $_.Name
      Width = $img.Width
      Height = $img.Height
    }
    $img.Dispose()
  }
```

Expected result:
- every file reports `Width = 1080`
- every file reports `Height = 1920`

## 5. Final Pre-Ship Checklist

- Every slide is understandable in under 2 seconds.
- No critical copy sits in likely TikTok UI overlap zones near the edges.
- No slide includes the table-creation error state.
- No headline, CTA, or footer implies money, winnings, or gambling performance.
- Any use of `buy-ins`, `chips`, or `poker` is grounded by private-game, play-chip, or training context.
- The CTA slide feels credible and product-led, not pushy.
- All five `v2` PNGs export cleanly at `1080 x 1920`.

