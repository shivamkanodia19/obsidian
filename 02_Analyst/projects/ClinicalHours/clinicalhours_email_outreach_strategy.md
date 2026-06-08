---
title: ClinicalHours Email Outreach Strategy
project: clinicalhours
status: execution-ready
origin_dump: [[01_Source/projects/ClinicalHours/clinic outreach.md]]
last_synced_dump: [[01_Source/projects/ClinicalHours/clinic outreach.md]]
last_updated: 2026-04-19
tags: [clinicalhours, sales, outreach, strategy]
---

# ClinicalHours Email Outreach Strategy (2026-04)

**Status:** Execution ready (60 drafts created, ready to send)  
**Focus:** Systematic, data-driven clinic outreach using agentic systems  
**Metrics:** Response rate, meeting booking rate, conversion to pilot  

---

## Current State (Session 2026-04-19)

### Positioning (Per Source)
- **Target:** Small clinics without volunteer infrastructure in place
- **Channels:** Email + phone outreach
- **Competition:** Volgistics, VSys (enterprise systems) — we differentiate on affordability + clinic-specific features
- **Key requirement:** Ensure features truly benefit clinics (not feature bloat)

### Outreach Progress (Session 2026-04-19)
- **Drafts created:** 60 Gmail drafts across Texas
  - **Batch 1:** 20 drafts (DFW + major cities: Dallas, Houston, Austin, San Antonio, Fort Worth, Lubbock, Tyler, Waco, Corpus Christi, El Paso)
  - **Batch 2:** 25 drafts (expansion: Beaumont, Galveston, Port Arthur, Rio Grande Valley, secondary markets)
  - **Batch 3:** 15 drafts (secondary markets: Abilene, Amarillo, Longview, Texarkana, Sherman, Denison, Denton, Frisco, Irving, Carrollton, Plano, Killeen, Temple, Waxahachie, Midland)
- **Duplication check:** Cross-verified against 11 clinics already contacted (Apr 17); no duplicates
- **Template:** Simple, consistent (clinic name personalization only; no complex psychology hooks)
- **Readiness:** Drafts in Gmail; ready to review + send

### Known Targets (Tier 1 DFW)
1. **Mercy Clinic Friends** — 140+ volunteers, largest DFW opportunity
2. **Julia's Center** — 60+ volunteers  
3. **Community Health** — 60+ volunteers
4. **EPIC Medical** — 62+ volunteers

### Current Pain Points in Process
- **Contact finding:** Manual Google search, inconsistent quality
- **Email personalization:** Generic template, limited clinic-specific customization
- **Research bottleneck:** Limited understanding of clinic pain points, decision-making process
- **Follow-up:** No systematic follow-up sequence
- **Validation:** No A/B testing or metrics on what works

---

## Optimization Strategy (To Be Refined by Research)

### Phase 1: Deep Contact Finding
**Goal:** Find decision-makers (Executive Director, Volunteer Coordinator, Operations Manager)

**Techniques:**
- [ ] LinkedIn search filters (non-profit + clinic title searches)
- [ ] Form 990 database search (GuideStar/ProPublica) to find leadership
- [ ] Clinic website staff directory scraping
- [ ] NPI registry lookup (CMS database)
- [ ] Phone-based title validation (call clinic, ask "who manages volunteers?")
- [ ] Email validation APIs (RocketReach, Hunter, Clearout)
- [ ] Fuzzy matching on clinic directors across multiple databases

**Output:** Structured contact database
```
clinic_name | city | website | director_name | director_title | director_email | director_phone | 
volunteer_coordinator_name | vc_email | vc_phone | volunteer_count | clinic_type
```

### Phase 2: Clinic Intelligence & Segmentation
**Goal:** Customize outreach by clinic size, type, and pain points

**Segmentation dimensions:**
- **Size:** 10-30 volunteers vs 30-75 vs 75-150+
- **Type:** Religious/faith-based vs community health center vs standalone clinic
- **Geography:** Urban vs suburban
- **Operations:** Hospital-network affiliated vs independent nonprofit
- **Signals:** Website quality, recent hiring activity, social media presence

**Intelligence to gather:**
- Volunteer count (from clinic websites, LinkedIn, HRSA data)
- Current tools they mention (VSys, Volgistics, Google Forms, etc.)
- Recent news/funding (non-profit news sites, Twitter)
- Pain points visible in job postings (volunteer coordinator recruiting?)
- Decision-making timeline (fiscal year cycles, grant cycles)

### Phase 3: Email Optimization
**Goal:** Higher response rate through research-backed messaging

**Elements to optimize (based on research findings):**
1. **Subject lines:** Problem-focused vs curiosity vs relationship
2. **Opening:** Personalization depth (specific volunteer count? recent news? mutual connection?)
3. **Problem statement:** Which pain point resonates? (recruitment, retention, compliance, cost savings?)
4. **Social proof:** Case study from BCS FHC (results: X more efficient, Y higher retention, Z cost savings)
5. **CTA:** Specificity (15-min call vs demo vs office visit?)
6. **Tone:** Professional vs conversational vs urgent

**A/B Test Framework:**
- Subject line variants (3-4 versions)
- Opening variants (personalization depth)
- Pain point emphasis (volunteer recruiting vs retention vs compliance)
- CTA variants (meeting type, timing, specificity)

### Phase 4: Follow-Up Sequences
**Goal:** Maximize meeting booking without being annoying

**Sequence logic:**
- Email 1 (Day 0): Initial outreach
- Email 2 (Day 5-7): If no response, re-emphasize value + new angle
- Email 3 (Day 12-14): If no response, add social proof (case study)
- Email 4 (Day 19-21): If no response, lower-friction ask (5-min call?)
- Phone call (Day 21+): If email sequence exhausted
- LinkedIn follow-up (Day 28+): If still no response

**Cadence variants by clinic type:**
- Hospital networks: Longer sales cycle (60+ days)
- Independent clinics: Faster decision (30-45 days)

### Phase 5: Agentic System Architecture
**Goal:** Systematize the entire process with minimal manual work

**Components:**
1. **Contact Finder Agent** — searches LinkedIn, Form 990, clinic websites, validates emails
2. **Intelligence Gatherer Agent** — clinic size, tools, recent news, pain points
3. **Email Generator Agent** — personalized subject + body based on clinic segment
4. **Follow-Up Manager Agent** — tracks responses, schedules follow-ups, escalates to phone
5. **Metrics Agent** — calculates response rates, conversion funnels, optimization insights

**Data Flow:**
```
Target City/Region
  ↓
Contact Finder (LinkedIn + Form 990 + websites)
  ↓
Intelligence Gatherer (clinic data, tools, pain points)
  ↓
Segmentation (size, type, urgency score)
  ↓
Email Generator (personalized outreach)
  ↓
Gmail Draft Creation (human review before sending)
  ↓
Follow-Up Manager (tracks responses, sequences follow-ups)
  ↓
Metrics Dashboard (response rates, conversion, optimization insights)
```

---

## Success Metrics

### Immediate (First 30 Days)
- [ ] Contact database: 50+ clinic directors identified + validated
- [ ] Email send volume: 30-50 personalized outreach emails
- [ ] Response rate: Target 20%+ (benchmark: cold email to nonprofits ~5-10%)

### Short-term (60 Days)
- [ ] Meetings booked: 5-10 from initial outreach
- [ ] Pilot conversions: 1-2 new clinics in trial (beyond BCS FHC)
- [ ] A/B testing: Identify top-performing subject line + pain point combo

### Long-term (6 Months)
- [ ] Customer pipeline: 10+ clinics in discussion, 3-5 paying customers
- [ ] Revenue: $3,600-6,000 MRR from DFW clinics
- [ ] Repeatable playbook: Documented process for expanding to new regions

---

## Research Inputs Needed (From Parallel Agents)

- [ ] **Clinic decision-making process:** Who decides? Timeline? Budget approval?
- [ ] **Volunteer management pain points:** Top 3-5 ranked by urgency
- [ ] **Pricing sensitivity:** Can free clinics afford $1,200/year? What's price threshold?
- [ ] **Competitive positioning:** What alternatives are they considering?
- [ ] **Cold email best practices:** Subject line patterns, open/reply benchmarks, follow-up cadence
- [ ] **Student volunteer motivations:** Secondary but important for positioning

---

## Next Steps (After Research Completes)

1. **Consolidate research findings** → Create clinic persona template
2. **Design email variants** → 3-4 subject lines × 2 pain points × 2 CTAs
3. **Build contact database** → LinkedIn + Form 990 + validation
4. **Set up A/B testing** → Track responses, optimize
5. **Deploy agentic system** → Contact finder + intelligence gatherer + email generator
6. **Monitor & iterate** → Weekly metrics review, rapid optimization

---

## Budget & Resource Plan

- **Tools:** LinkedIn (existing), Form 990 database (free), email validators (RocketReach/Hunter)
- **Time:** 2-4 weeks to build systematic outreach, then 1-2 hours/week to manage
- **Automation:** Leverage existing agent infrastructure + new agentic components
- **Manual effort:** Email review before sending, meeting scheduling, initial calls
