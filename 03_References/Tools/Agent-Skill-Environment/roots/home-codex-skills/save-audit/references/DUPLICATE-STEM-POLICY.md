# Duplicate Stem Policy

This file explains how `save-audit` classifies duplicate markdown stems.

The machine-readable source of truth is `DUPLICATE-STEM-POLICY.json`.

## Goal

Not every duplicate stem is a contradiction.

The policy separates:

- `intentional_redirect` - a short legacy redirect note kept for old links
- `scoped_duplicate` - same stem reused inside clearly separate campaign or output folders
- `review_candidate` - duplicate stem still needs human cleanup or routing work

## How To Extend It

Add a rule in `DUPLICATE-STEM-POLICY.json` with:

- `stem` - lowercase note stem
- `classification` - `intentional_redirect` or `scoped_duplicate`
- `reason` - short explanation written into `.vault-contradictions.md`

Optional matchers:

- `required_paths` - exact relative paths that must be present
- `path_globs` - glob patterns every duplicate path must match
- `required_markers` - body markers that should exist in one of the matched files
- `exact_count` - exact number of duplicate files expected for the rule

## Current Rules

- `email-optimization-strategy` - intentional redirect stub for older internship links
- `draft-emails` - valid reuse across internship outreach waves
- `narrative_plan` - valid reuse across separate slideshow output folders
- `claude` - valid reuse across separate system-design output folders
- `prd` - valid reuse across separate system-design output folders

## Heuristic Fallback

If no rule matches, `save-audit` still tries one safe heuristic:

- a very short note with redirect markers like `Canonical note:` or `stable redirect` can be treated as an intentional redirect stub

Everything else stays a `review_candidate`.
