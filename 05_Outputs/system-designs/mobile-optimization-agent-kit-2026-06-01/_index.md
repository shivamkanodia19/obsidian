---
title: Mobile Optimization Agent Kit
description: Claude-facing playbook and local tooling for mobile web optimization
last_updated: 2026-06-07
---

# Mobile Optimization Agent Kit

This folder is a self-contained handoff pack for mobile-view optimization work.

## Files

- [[mobile-optimization-claude-brief-2026-06-01]] - main Claude-facing playbook
- [[toolkit/_index|toolkit/]] - navigation hub for the local Playwright and Lighthouse toolkit
- [[toolkit/playwright.config.ts]] - Playwright mobile-project config
- [[toolkit/tests/mobile-smoke.spec.ts]] - baseline mobile smoke tests
- [[toolkit/lighthouserc.cjs]] - Lighthouse CI starter config
- [[toolkit/package.json]] - local tool manifest

## Notes

- The `toolkit/` folder is meant to be copied or adapted into the real site repo.
- The brief tells Claude how to use the toolkit and what "good" mobile work looks like.
