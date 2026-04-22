---
title: Clara — AI Pre-Visit Intake System
project: ideathon26
strategic: false
status: stable
origin_dump: [[01_Source/ideathon26/CLARA_RUBRIC_RESPONSES.md]]
last_synced_dump: [[01_Source/ideathon26/CLARA_RUBRIC_RESPONSES.md]]
conflict_detected: false
last_updated: 2026-04-18
tags: [ideathon, healthcare, AI, intake, physician-workflow, product-tamu]
---

# Clara — AI Pre-Visit Intake System

**Product@TAMU Ideathon — General Track Submission**

## Core Insight

Physicians spend ~30% of each appointment on intake paperwork instead of actual care. Everyone optimizes the during-visit experience. Nobody's optimized pre-visit. Clara moves intake upstream via AI, giving doctors back their time for patients.

From [[01_Source/ideathon26/CLARA_RUBRIC_RESPONSES.md]]:
> Clinicians interrupt patients every 18 seconds during visits because they're drowning in intake paperwork. Aryan saw his own family doctor working through lunch just to keep up.

---

## What It Does

**24-hour pre-visit call** → **AI asks targeted questions** → **structured SOAP note** → **physician dashboard**

### The Flow:
1. **Patient receives automated call** (via Twilio) 24 hours before appointment
2. **Conversational AI engine** adapts questions based on chief complaint (uses Claude + GPT-4o Mini)
3. **System extracts structured data:** symptoms, duration, severity, medications, red flags
4. **Physician dashboard** surfaces clean SOAP note + clinical brief + alerts 5 min before patient arrives
5. **Result:** Doctor has full attention for the patient, not typing notes

### Key Outcomes:
- 4.5 minutes saved per visit
- Targeted questions (no generic checklists)
- Reduced missed diagnoses (red flag detection + case matching)
- 100 minutes saved daily per clinic
- Reduced no-shows
- Increased EOC scores & patient satisfaction

---

## How We Built It

### Design Process (Figma)
- **Patient intake flow:** Designed conversation path with branching logic for different chief complaints
- **Physician dashboard:** Dashboard wireframe showing SOAP note, alerts, patient context
- **Integration design:** API flow between Twilio → LLM → Epic FHIR endpoint
- **Iterated with physician feedback** from Dr. Haroon Hyder (pulmonologist); refined based on real workflow constraints

### Technical Stack:
- **Voice calls:** Twilio for outbound pre-visit calls
- **Conversation engine:** Claude API + GPT-4o Mini for adaptive clinical Q&A
- **Data extraction:** LLM-powered structured note generation (SOAP format)
- **Red flags:** Hybrid rules + AI detection (e.g., chest pain + SOB = cardiac risk)
- **EHR sync:** FHIR API integration to Epic (no manual data entry)
- **Physician UI:** React dashboard displaying intake summary

**No manual entry. No paperwork. Just structured data flowing into the existing system.**

---

## Challenges We Ran Into

1. **Medical speech-to-text errors** — "Lasix" transcribed as "lasics." Fixed via post-processing transcripts with medical LLM.

2. **Conversation flow tuning** — System was asking too many follow-ups. Refined to ask only what matters based on pilot feedback.

3. **Epic FHIR integration** — Had to build secure data push into Epic without manual entry. Standard FHIR patterns solved this.

4. **Red flag false positives** — System over-alerting. Tuned thresholds with physician feedback to catch real risks.

5. **Regulatory clarity** — Clara is not a medical device (supports physician judgment, doesn't diagnose). Removes deployment barriers.

---

## Accomplishments We're Proud Of

✅ **Working prototype** — Already deployed with real physicians; not just a demo

✅ **Real clinical outcomes** — Saves time, reduces no-shows, higher patient satisfaction

✅ **Epic integration working** — Data flows seamlessly into hospital's existing system

✅ **Doctors actually trust it** — Built explainability so physicians understand why Clara flags alerts

✅ **Regulatory sorted** — Confirmed as non-device; removes barriers to deployment

---

## What We Learned

1. **Pre-visit is the uncontested gap** — Everyone optimizes during-visit. Nobody's optimizing the 30% of time lost to intake. That's where the opportunity lives.

2. **Doctors want to see the reasoning** — Built a black-box AI model that was accurate. Doctors ignored it. But when we showed *why* Clara flagged something, they trusted it.

3. **Real user feedback matters way more than hypothetical research** — Feedback from actual physicians validated more than any market study.

4. **Integration with existing systems is key** — Epic FHIR integration makes this deployable *tomorrow*. We're not asking hospitals to rip out workflows; we're plugging into what they already use.

---

## Market & Strategy

**Healthcare intake market is underserved:**
- 42% of hospitals use Epic (largest EHR market)
- Current competitors focus on during-visit optimization
- Pre-visit intake is completely uncontested
- Physician burnout from administrative tasks is acute and measurable

**Clara positions as:**
- Not a competitor to Epic, but an extension that plugs into it
- Solves a specific, measurable pain (intake time + physician attention)
- Deployable with minimal workflow disruption (integrates with existing systems)

---

## Implementation Roadmap

### Phase 1: Prototype Validation (Months 1–3)
- Expand physician pilot from current cohort
- Measure: call completion rate, transcription accuracy, SOAP note quality
- Deliverable: Validated prototype with real clinical outcomes

### Phase 2: Production Hardening (Months 4–6)
- Improve transcription accuracy (medical vocabulary expansion)
- Implement HIPAA-compliant storage + encryption
- Build robust error handling for voice call failures
- Deliverable: Production-ready system

### Phase 3: Scaling Foundation (Months 7–9)
- Deploy to 2–3 additional hospital systems
- Optimize FHIR integration for different Epic configurations
- Build admin dashboard (hospital staff management)
- Deliverable: Multi-site deployment capability

### Phase 4: Multi-EHR Support (Months 10+)
- Add integration for Cerner, Epic Ambulatory variants
- Standardize FHIR implementation for broader compatibility
- Deliverable: Support for 70%+ of EHR market

---

## Success Metrics

- **Physician adoption:** % of eligible clinicians using Clara for pre-visit intake
- **Time saved:** Minutes saved per appointment (target: 4.5+ min)
- **Patient completion:** % of patients completing pre-visit calls
- **Transcription accuracy:** Word error rate for medical terminology
- **FHIR integration stability:** % of successful note pushes to Epic (target: 99%+)
- **Reduced no-shows:** % decrease in patient no-shows after Clara deployment
- **Patient satisfaction:** NPS/EOC scores for practices using Clara vs. control

---

## Why Clara Matters

Pre-visit intake is a systemic problem in healthcare:
- Physicians spend 1/3 of visit time on paperwork instead of care
- Patients wait longer in clinics because doctors are behind schedule
- Important details get missed because physicians are rushing
- Physician burnout is partly driven by administrative overload

Clara solves this by moving the administrative work upstream to a time when it doesn't compete with patient care. The insight isn't complex—it's just that nobody's tried it yet.

---

## Team

**Aryan Shah** (Computer Science) — Backend, LLM integration, FHIR API

**Dhir Parekh** (Biomedical Engineering) — Clinical requirements, FDA/regulatory strategy
