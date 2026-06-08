---
title: Mobile Optimization Toolkit
description: Playwright, Lighthouse, and smoke-test files for the mobile optimization handoff pack
last_updated: 2026-06-07
---

# Mobile Optimization Toolkit

Local QA toolkit files for the mobile optimization handoff pack.

## Files

- [[package.json]] - toolkit manifest
- [[package-lock.json]] - locked dependency tree
- [[playwright.config.ts]] - mobile-oriented Playwright config
- [[lighthouserc.cjs]] - Lighthouse CI starter config
- [[tests/mobile-smoke.spec.ts]] - baseline mobile smoke tests

## Notes

- `node_modules/` is a local vendor tree and is intentionally not treated as a navigation surface.

## Navigation

- [[05_Outputs/system-designs/mobile-optimization-agent-kit-2026-06-01/_index|Mobile optimization agent kit]]
- [[05_Outputs/system-designs/_index|System designs]]
