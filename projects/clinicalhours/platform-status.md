---
title: ClinicalHours — Volunteer Management Platform for Free Clinics
type: project
status: active
stage: early-traction
last-updated: 2026-04-13
tech: React, TypeScript, Supabase, Vite, Tailwind, Stripe, Capacitor
users: 200+
clinic-partners: BCS Free Health Clinic
advisors: Baylor Scott & White, St. Joseph Health, Ascension
tags: [startup, healthtech, volunteer-management, saas]
---

# ClinicalHours — Project Overview

## What It Is

ClinicalHours is a two-sided volunteer management platform for the free and charitable clinic ecosystem. Clinics get a full volunteer operations backend (applications, interviews, scheduling, onboarding, email comms, analytics). Students get a searchable directory of clinical volunteer opportunities with a streamlined apply flow.

The core thesis: free clinics are massively underserved on operations software. They run on spreadsheets and email. ClinicalHours replaces that stack entirely and uses the student demand side as the growth engine.

## Business Overview

ClinicalHours builds volunteer management infrastructure for small free and charitable clinics, with a student-facing platform as the demand side.

The platform has 200+ organic users with zero paid marketing.

Only confirmed clinic partner is BCS Free Health Clinic, where we manage their entire volunteer infrastructure end to end.

Baylor Scott & White, St. Joseph Health, and Ascension have been consulted as advisors only, not as partners or customers.

Student acquisition uses faceless TikTok slideshows and organic content targeting pre-meds. Clinic acquisition uses direct email and phone outreach, with a domino network effect as clinics refer other clinics.

## Tech Stack

**Frontend**
- React 18 + TypeScript + Vite (SPA)
- React Router v6
- Tailwind CSS + Radix UI + shadcn/ui components
- TanStack Query (server state)
- React Hook Form + Zod (forms and validation)
- Recharts (analytics dashboards)
- Mapbox GL (clinic map/globe view)
- Capacitor (iOS wrapper, in progress)

**Backend**
- Supabase (Postgres + Auth + Storage + Realtime)
- 50+ Supabase Edge Functions (Deno/TypeScript) covering:
  - Auth: cookie management, CSRF, session restore, email verification, password reset
  - Applications: submit, status updates, interview invites, resume scoring
  - Clinic ops: hospital signup, position management, bulk email, onboarding
  - Payments: Stripe checkout, subscription cancel, webhooks
  - Integrations: Gmail OAuth, Calendly webhook, logo fetching
  - Data: CSV import, geocoding, deduplication, Texas hospital import
  - Analytics: event tracking

**Infrastructure**
- Deployed on Vercel (SPA with rewrites)
- Supabase hosted Postgres with row-level security
- Cloudflare R2 (assets/logos)
- Stripe (subscriptions)

## Current Status

- **Live and in production** at clinicalhours.org
- 200+ registered student users, zero paid acquisition
- One fully onboarded clinic (BCS Free Health Clinic) — end-to-end volunteer infrastructure
- Advisor relationships with BSW, St. Joseph Health, Ascension (not paying customers)
- Active feature development; codebase is ~1,200 nodes across src + supabase

## Active Partnerships

| Partner | Status | Relationship |
|---------|--------|--------------|
| BCS Free Health Clinic | Active | Full volunteer management, end-to-end |
| Baylor Scott & White | Advisor | Consulted only, not a customer |
| St. Joseph Health | Advisor | Consulted only, not a customer |
| Ascension | Advisor | Consulted only, not a customer |

## Immediate Priorities

- Expand clinic partnerships beyond BCS (direct outreach pipeline)
- Build out TikTok content flywheel for continued organic student growth
- Harden onboarding flow for new clinics (self-serve signup)
- Improve resume scoring / application matching features
- iOS app via Capacitor

## Codebase Navigation

Knowledge graph at: `C:\Users\shiva\ClinicalHours\graphify-out\`  ✓ (correct location)
- `graph.html` — interactive visualization
- `GRAPH_REPORT.md` — god nodes, surprising connections, suggested questions

Key god nodes: `handler()` (72 edges), `escapeHtml()` (15), `trackEvent()` (9)
Key insight: email verification flow directly manages the entire cookie lifecycle (`createSessionCookie`, `createCSRFCookie`, `createRefreshTokenCookie`, `clearRefreshTokenCookie`)

## Links
- [[pitch-deck]] — ClinicalHours pitch deck
- [[resume-current]] — Shivam's resume (ClinicalHours co-founder section)
