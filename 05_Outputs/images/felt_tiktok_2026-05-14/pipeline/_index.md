---
title: Felt TikTok Pipeline
description: Automation files, JSON schemas, deck specs, and run artifacts for Felt TikTok slideshow grading
last_updated: 2026-05-21
---

# Felt TikTok Pipeline

This folder holds the first-pass automation layer for rendering, grading, assembling, and preparing Felt TikTok slideshow decks for email.

## Files

- `felt_tiktok_pipeline_config.json` - shared campaign config, recipient, rubric path, and required strategy context files
- `run_felt_tiktok_pipeline.ps1` - render, manifest, grading, deck assembly, and email-payload staging script
- `schemas/` - JSON schemas for slide manifests, grades, deck manifests, grades, email payloads, and deck specs
- `specs/` - candidate deck input specs that define slide roles, copy, and proof sources for a render/grading run
- `runs/` - generated run artifacts, including approved and rejected slides and decks

## Future-Agent Note

- Treat this Felt slideshow pipeline as a reusable reference architecture, not necessarily the long-term primary marketing automation target.
- Shivam may want a similar grading, deck-assembly, and email-release system adapted for `ClinicalHours` marketing later.
- Unless explicitly told otherwise, preserve the reusable schemas and flow here, but do not assume Felt is the only or final destination for this pattern.

## Navigation

- Parent: [[05_Outputs/images/felt_tiktok_2026-05-14/_index|felt_tiktok_2026-05-14]]
- Related rubric: [[02_Analyst/projects/felt/campaigns/tiktok-slideshow/social_media_expert/_index|social_media_expert]]

## New Files

- [[schemas/_index|schemas/]] - Navigation hub for schemas
- [[specs/_index|specs/]] - Navigation hub for specs
