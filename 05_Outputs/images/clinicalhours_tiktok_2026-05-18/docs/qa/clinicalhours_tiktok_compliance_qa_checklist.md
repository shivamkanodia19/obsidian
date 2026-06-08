---
title: ClinicalHours TikTok Compliance QA Checklist
description: Messaging, truthfulness, and export checklist for ClinicalHours TikTok slideshow approval
last_updated: 2026-05-29
---

# ClinicalHours TikTok Compliance + QA Checklist

Reviewed against:

- the ClinicalHours strategy notes
- the live public site captured on `2026-05-18`
- the ClinicalHours TikTok render system

Read with:

- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_skill_mcp_guardrails_2026-05-18]]

## 1. Messaging Checklist

### User Intent

- If Shivam is asking for a new ClinicalHours deck directly, confirm what content or topic the slides should cover before generating.
- If needed, ask one short follow-up about audience or CTA.

### Positioning

- Keep each deck inside one audience lane unless explicitly asked otherwise.
- Default lane is `clinic_ops_primary`.
- Make ClinicalHours feel like workflow infrastructure, not vague startup inspiration.
- Prefer language about workflow relief, visibility, status, onboarding, credentialing, and coordination.

### Must Avoid

- No guaranteed admissions or "get into med school" framing.
- No guaranteed staffing, compliance, or credential outcomes.
- No fake hospital partnerships or fake enterprise adoption.
- No stronger medical-compliance claims than the visible or documented evidence supports.
- No placeholder metrics from the current homepage.
- No internal strategy language in audience-facing copy.
- No screenshot proof whose biggest readable text is generic filler, empty-state text, or off-lane boilerplate.

### Safer Copy Patterns

- Good: `one platform`
- Good: `workflow relief`
- Good: `status in one place`
- Good: `request a demo`
- Good: `find clinical opportunities`
- Good: `browse as guest`

### Higher-Risk Terms Requiring Care

- `HIPAA`: only when clearly supported and not overstated
- `compliance`: acceptable when tied to status, audit trail, or visible workflow
- `AI`: acceptable only when framed conservatively and operationally
- `clinical future`: acceptable for student-facing lane

## 2. Truthfulness Checklist

- Use only real ClinicalHours captures already saved in this folder unless a new truthful capture is taken.
- Do not fabricate queues, records, dashboards, or clinician supply.
- Do not show PHI.
- Do not use home-page placeholder `0+` metrics as proof.
- Generated support imagery is allowed only when it stays atmospheric, non-claim, and secondary to live proof.
- Fail any slide where generated imagery implies product capability, resembles fabricated UI, or does the persuasion the proof asset should do.
- If a claim is only a market hypothesis, label it or weaken it.
- Repeated quantitative claims inside one deck must match exactly.
- Store claim strength in `evidence_tier` and screenshot visibility in `proof_access`.

## 3. Final Export Rubric

### A. Truth And Compliance

- `Pass`: truthful asset, correct evidence tier, no PHI, no fake claims
- `Needs revision`: one risky phrase or weakly supported claim
- `Fail`: fabricated proof, PHI, or strong unsupported outcome claim

### B. Message Clarity

- `Pass`: slide meaning is obvious in under 2 seconds
- `Needs revision`: idea is readable but diffuse
- `Fail`: unclear lane, crowded copy, or confusing proof

### B1. Copy And Screenshot Text Gate

- `Pass`: overlay copy is audience-facing and the dominant screenshot text reinforces the claim
- `Needs revision`: copy is mostly clear but one support label or screenshot string still feels generic
- `Fail`: visible copy sounds like a strategy note, or the hero screenshot is dominated by empty-state or boilerplate text

### C. Product-Led Proof

- `Pass`: hero proof visibly supports the claim
- `Needs revision`: screenshot is real but weak
- `Fail`: proof feels decorative or contradictory, or generated support art is functioning like fake proof

### D. Visual Restraint

- `Pass`: calm, sharp, healthcare-infrastructure tone
- `Needs revision`: mostly clean but slightly noisy
- `Fail`: gimmicky, salesy, or generic startup-ad tone

### E. Technical Export

- `Pass`: exact filenames, exact dimensions, no clipping, no browser chrome
- `Needs revision`: usable but soft or uneven
- `Fail`: wrong dimensions, overflow, or visible export artifacts

## 4. File Verification

Required dimensions:

- `1080 x 1920`

PowerShell check:

```powershell
Add-Type -AssemblyName System.Drawing
Get-ChildItem "05_Outputs/images/clinicalhours_tiktok_2026-05-18/exports/v1/clinicalhours_tiktok_slide_*_v1.png" |
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

- The requested slide topic is explicit.
- Every slide is understandable in under 2 seconds.
- The lane is obvious.
- `evidence_tier` and `proof_access` use canonical values.
- Overlay copy speaks to the viewer, not to the creator.
- No overlay line contains `proof`, `story`, `close`, `cold traffic`, `in-feed`, or similar meta-marketing language.
- The biggest readable screenshot text supports the headline.
- Empty-state text is not the main proof unless the slide is explicitly about setup.
- No critical copy sits in TikTok UI overlap zones.
- No slide uses homepage placeholder metrics as proof.
- Generated support imagery, if any, stays subordinate to the live proof and does not mimic product UI.
- No repeated metric conflicts appear across slides.
- No slide contains PHI or fake partner/adoption proof.
- The CTA slide feels credible and calm.
- All five PNGs export cleanly at `1080 x 1920`.
