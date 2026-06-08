---
title: ClinicalHours TikTok Composition
description: Local composition source and rendering script for the ClinicalHours TikTok slideshow
last_updated: 2026-06-07
---

# ClinicalHours TikTok Composition

Files used to compose, QA, and export the slideshow locally.

## Files

- `clinicalhours_tiktok_carousel.html` - canonical `clinic_ops_primary` composition source for `v1`
- `clinicalhours_tiktok_clinic_onboarding_visibility.html` - light-only issue-specific `clinic_ops_primary` composition for the onboarding-visibility `v4onboard` branch
- `clinicalhours_tiktok_clinic_expiring_clearances.html` - light-only issue-specific `clinic_ops_primary` composition for the expiring-clearances `v4expiry` branch
- `clinicalhours_tiktok_clinic_ops_concise.html` - light general `clinic_ops_primary` composition for the concise `v8conciseops` branch
- `clinicalhours_tiktok_clinic_ops_impact.html` - impact-led concise `clinic_ops_primary` composition for the corrected `v9impactops` branch
- `clinicalhours_tiktok_student_auth_v2.html` - authenticated student-lane composition for `v2auth`
- `clinicalhours_tiktok_student_auth_v3bright.html` - brighter student-facing composition aligned with the `2026-05-19` visual strategy note and the current `v3bright7` export set
- `clinicalhours_tiktok_student_impact_story.html` - issue-specific student-facing composition for the `v4impact` branch focused on reflections, recall, and showing impact later
- `clinicalhours_tiktok_student_search_memory.html` - issue-specific bright student composition for the `v4memory` branch centered on losing track after discovery
- `clinicalhours_tiktok_student_first_path.html` - issue-specific student-facing composition for the `v5firstpath` branch centered on the first click through the first logged shift
- `clinicalhours_tiktok_student_real_leads.html` - issue-specific student-facing composition for the `v6realleads` branch focused on stale lists, trust, and proving a clinic is worth the click
- `clinicalhours_tiktok_student_guest_first.html` - issue-specific student-facing composition for the `v6guestfirst` branch focused on reducing signup friction with a guest-first entry story
- `clinicalhours_tiktok_student_semester_start.html` - issue-specific student-facing composition for the `v7semesterstart` branch focused on semester-time search, preview, save/app-link follow-through, and a guest-first closing CTA
- `clinicalhours_tiktok_student_fall_high_impact.html` - high-impact student-facing composition for the `v10fallimpact` branch that ports the cleaner summer editorial styling into the durable proof-first student system
- `build_clinicalhours_tiktok_crop_derivatives.ps1` - canonical crop-builder for reusable screenshot derivatives
- `audit_clinicalhours_tiktok_copy.ps1` - pre-render copy and proof-asset audit for student-facing variants
- `render_clinicalhours_tiktok_carousel.ps1` - render and QA export script

## Operating Notes

- The machine-readable pipeline currently covers the `v1` clinic-ops deck, the issue-specific onboarding `v4onboard` branch, the expiring-clearances `v4expiry` branch, the `v3bright7` bright student deck, the `v4impact` student impact-story branch, the `v4memory` student search-memory branch, the `v5firstpath` student first-path branch, and the `v6realleads` plus `v6guestfirst` student trust/activation branches.
- `clinicalhours_tiktok_clinic_ops_concise.html` keeps the default clinic-ops lane, but compresses the copy and removes extra slide clutter for the `2026-06-02` queue-driven `v8conciseops` branch.
- `clinicalhours_tiktok_clinic_ops_impact.html` is the current concise clinic-ops correction branch. It keeps the shorter-copy goal, but rebuilds the proof framing and slide-role variation after the `v8conciseops` failure modes were documented.
- `clinicalhours_tiktok_student_first_path.html` was proof-alignment repaired on `2026-05-30` so the clinic-preview slide now leads with the featured clinic card and the first-log slide now leads with the visible journal CTA.
- `clinicalhours_tiktok_student_semester_start.html` passed a fresh two-judge review loop on `2026-06-01` after replacing the weak New York row crop with a Houston Methodist proof chain across slide `3` and slide `4`.
- `clinicalhours_tiktok_student_fall_high_impact.html` keeps the same trusted student proof chain as `v7semesterstart`, but uses shorter headlines, fewer overlays, and a cleaner high-impact editorial shell.
- `render_clinicalhours_tiktok_carousel.ps1` now auto-routes any `clinicalhours_tiktok_student_*` composition into the `bright_student` audit profile instead of relying on a hardcoded student-file allowlist.
- If a future agent creates a new HTML variant, the corresponding export version, handoff note, and replication docs should be updated in the same pass.

## Navigation

- Parent: [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/_index|clinicalhours_tiktok_2026-05-18]]
- Related source captures: [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/captures/_index|captures]]
- Related replication guide: [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19]]
