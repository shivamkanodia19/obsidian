# /history Skill

## Purpose
Trace the evolution of a concept or decision across time. Show how something has changed, what prompted the changes, and current state.

## Token Budget
Load Analyst file first. Only load Source dumps if user requests primary evidence.

## Steps

1. **READ `claude.md`** (vault root).

2. **LOAD the relevant Analyst file**. Look for the `## History` section and current state.

3. **BUILD a chronological timeline** from:
   - History entries (with dates)
   - Current state
   - Linked Source dumps (if needed)

4. **FOR EACH entry, label clearly:**
   ```
   [CURRENT] — present state
   [2026-04-14] — past milestone
   [2026-04-10] — earlier milestone
   ```

5. **If user says "show me the source,"** THEN load the linked Source dump(s). Otherwise, do not load sources.

6. **OUTPUT the timeline** chronologically. No editorializing. Facts and dates only.

## Example Output
```
## ClinicalHours — Evolution

[CURRENT] B2C freemium $4.99/mo, B2B clinic portal $750-1000/yr. BCS Free Health Clinic confirmed partner (200+ users). Executing Meloy accelerator roadmap.
→ [[01_Source/Dumps/2026-04-14_clinicalhours-status]]

[2026-04-10] Aggie Pitch not yet submitted. Email automation strategy designed. TikTok content agent v4 complete.
→ [[01_Source/Dumps/2026-04-10_clinicalhours-update]]

[2026-03-20] Zero marketing, 200 users. First revenue: BCS partnership. Product: Next.js + Supabase.
```
