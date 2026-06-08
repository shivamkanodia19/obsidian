---
title: ClinicalHours TikTok Future Agent Prompt - MCP Auth And Iteration Build - 2026-05-31
description: Paste-ready prompt for the next refreshed Codex agent to capture truthful ClinicalHours proof, use the right MCP stack, and iterate until a deck is actually strong
last_updated: 2026-05-31
---

# ClinicalHours TikTok Future Agent Prompt - MCP Auth And Iteration Build - 2026-05-31

## Why This Prompt Exists

The ClinicalHours visual system is already strong on:

- lane discipline
- truthful proof
- local render QA
- documented deck branches

The next agent should not restart from vague "make slides" instincts.

It should:

- use the right tool order
- use the available ClinicalHours auth when needed
- prefer first-party product visuals over searched screenshots
- use generated imagery only in a secondary role
- run fresh-context judging until the branch is genuinely good or explicitly retired

## Operational Reality

The refreshed agent should assume this environment may expose more MCPs than the previous session did.

Priority tool routing:

1. `Playwright` or `Chrome` for truthful product capture and auth flows
2. direct first-party ClinicalHours screenshot assets when they already exist
3. `open-websearch` for route and asset discovery only
4. `Figma` or local HTML composition for layout exploration and deck building
5. `Higgsfield` for generated support imagery if callable
6. fallback image generation only if needed, and only after proof is locked

Do not use generated imagery as claim-bearing proof.

## Known First-Party ClinicalHours Visual Sources

Use these before searching the web for screenshots:

- `https://clinicalhours.org/screenshots/opportunities.png`
- `https://clinicalhours.org/screenshots/map.png`
- `https://clinicalhours.org/screenshots/profile.png`

These are official site-hosted visuals and are better than search results, thumbnails, reposts, or manual screen snips.

Treat source order as:

1. official site-hosted screenshot assets
2. fresh direct public-page capture
3. fresh authenticated demo capture
4. websearch only for discovery or reference

## Auth Credential For Approved Test Capture

If the agent needs authenticated student-product proof, it may use this ClinicalHours test login through the product auth flow:

- email: `codextest@gmail.com`
- password: `codex123`

Rules:

- use these credentials only for ClinicalHours capture work
- do not use them outside ClinicalHours
- do not change account settings unless the task specifically requires it
- do not publish or surface private-looking profile details without redaction review

## Paste-Ready Prompt

```text
You are the next refreshed Codex agent working in:

c:\Users\shiva\obsidian

Assignment:
Create or improve a ClinicalHours TikTok-style slide deck using the vault's existing truthful-proof system, the best available MCPs in the refreshed session, and repeated fresh-context judging until the deck is actually good.

Mission:
Do not stop at the first valid render.
Do not stop at "layout passed."
Do not stop at "the screenshot is real."

The deck is only ready when:
- the lane is clear
- the proof is the right proof for the claim
- the screenshot text helps the headline
- the slide sequence gets more specific as it progresses
- at least two fresh-context judges independently pass it

Before doing serious work:
1. Check which MCPs are actually callable in this refreshed session.
2. Prefer this tool order:
   - Playwright or Chrome for truthful capture and login
   - direct ClinicalHours first-party screenshot assets
   - open-websearch for discovery only
   - Figma or local HTML composition for layout
   - Higgsfield for secondary support imagery if callable
3. If subagents are available, use them:
   - one explorer for proof inventory and capture opportunities
   - one explorer for branch audit and strongest reusable starting point
   - one explorer for fresh-context critique or rubric extraction
4. While those run, read the required files and inspect the current branches locally.

Interactive rule:
If Shivam has not specified the deck topic yet, ask one short question:
"What topic should this ClinicalHours deck cover?"

If the task is automated or no answer is available, default to:
- lane: clinic_ops_primary
- target branch: v1 or a new clinic-ops issue branch if clearly justified

Required read order:
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/_index.md
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18.md
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_system_handoff_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_iteration_loop_v1_2026-05-31.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_playwright_future_agent_playbook_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_codex_image_prompt_system_v1_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_skill_mcp_guardrails_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_compliance_qa_checklist.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/pipeline/clinicalhours_tiktok_pipeline_config.json

Auth note:
If authenticated student surfaces are needed, use the ClinicalHours test credentials through the actual product auth flow:
- email: codextest@gmail.com
- password: codex123

Use auth only when it materially improves proof.
Public or first-party hosted proof is preferred whenever it supports the topic well enough.

Source-order rule for ClinicalHours visuals:
1. Use official site-hosted screenshots first when they fit the slide topic:
   - https://clinicalhours.org/screenshots/opportunities.png
   - https://clinicalhours.org/screenshots/map.png
   - https://clinicalhours.org/screenshots/profile.png
2. If those are not the right proof, capture fresh public states with Playwright or Chrome.
3. If the needed proof is auth-only, log in with the approved test account and capture carefully.
4. Use websearch only to discover routes or references, not as the final source of slide pixels.

Proof rules:
- screenshot first, copy second
- one dominant hero proof asset per slide
- if the screenshot does not prove the claim in about 2 seconds, replace it, crop it tighter, or weaken the claim
- generated support visuals may support atmosphere, rhythm, or framing only
- do not invent product proof with image generation, Figma redraws, or cleaned-up UI

Image-generation rules:
- If Higgsfield is callable, use it as the primary support-imagery MCP
- If Higgsfield is unavailable, use the best available image-generation MCP in the refreshed session
- Keep all generated assets secondary to real ClinicalHours proof
- Run an image-only fresh-context review before placing any generated still into a slide
- Reject generated stills with fake text, fake UI, anatomy issues, ambiguous workflow claims, or over-polished product mimicry

Recommended starting points by lane:
- clinic_ops_primary: start from v1 unless the topic clearly matches v4onboard or v4expiry
- student_discovery_secondary: compare v3bright7, v4impact, v4memory, v5firstpath, v6guestfirst, and v6realleads before choosing

Known branch caution:
- v6realleads is currently the weakest durable student branch for topic-to-proof fit and should not be reused casually

Known proof cautions:
- avoid the lower student homepage placeholder metric cards
- treat profile-style authenticated screens as sensitive and check visible personal details before reuse
- preserve or account for map attribution when using map visuals
- do not imply partnerships or endorsements from visible institution names unless verified

Working sequence:
1. Declare:
   - deck topic
   - lane
   - evidence_tier
   - proof_access
   - target branch or new branch
2. Audit current proof inventory before writing copy.
3. Choose the strongest truthful hero proof for each slide.
4. Decide whether support imagery is even needed.
5. Build or revise the deck in the right composition source.
6. Render with QA enabled.
7. Use the review bundle as the cold-review packet.
8. Run Judge A from a fresh context.
9. Run Judge B from a separate fresh context.
10. Synthesize findings, repair the branch, and repeat until pass or explicit retirement.

Render command:
.\render_clinicalhours_tiktok_carousel.ps1 -VersionSuffix <suffix> -RunQa -GenerateQaShots

If an alternate HTML file is the source, pass -HtmlFile explicitly.

Hard requirements:
- do not ship on the first clean render
- run at least two independent fresh-context judges
- treat repeated semantic weakness across two rounds as a signal to reframe or retire the branch
- save durable outputs: updated iteration note, updated spec if reproducible, latest review bundle, and any judgment artifacts

Deliverables:
- one improved or newly built ClinicalHours deck branch
- exports at 1080 x 1920
- passing render QA and copy audit
- a review bundle for the current suffix
- at least two independent fresh-context judge verdicts
- updated iteration note and relevant indexes if the branch becomes durable

Final response requirements:
- start with findings or the main outcome, not process recap
- say which branch was used or replaced and why
- link the composition, exports, QA, review bundle, and iteration note
- say whether the deck passed or still needs another round
- call out remaining proof limitations honestly
```

## Related Notes

- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_system_handoff_2026-05-19]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_iteration_loop_v1_2026-05-31]]
