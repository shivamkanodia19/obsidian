# /resume Skill

## Purpose
Give a fast, current-state briefing on a topic. Surface any strategic conflicts logged since last review. Token-efficient bootstrap (<1000 tokens).

## Token Budget
Maximum files loaded: _index.md + 1 target Analyst file + `.vault-conflicts` (if conflicts exist). Never load Source dumps unless /history is explicitly called.

## Steps

1. **READ `claude.md`** (vault root).

2. **READ `_index.md` frontmatter only**. Identify target file from `active_projects` using user intent.

3. **CHECK FOR STRATEGIC CONFLICTS**:
   - If target file has `strategic: true` AND `conflict_detected: true` in frontmatter:
     - Read `.vault-conflicts` file to surface unreviewed conflicts
     - Display conflict summary prominently at top of output

4. **LOAD the target Analyst file**. Read frontmatter first:
   - If `status: drifted` → prepend warning: "⚠️ This file has unsynced dumps in 03_Inbox."
   - If `last_updated` > 30 days ago → label as [HISTORICAL CONTEXT — last update YYYY-MM-DD]
   - If `conflict_detected: true` → note this was recently updated over an older decision

5. **OUTPUT exactly this structure:**
   ```
   ## [Project Title] — Current State
   [3 sentences max. Present tense. Specific numbers/dates from frontmatter.]
   
   ## Key Facts
   - [Primary direction/focus]
   - [Latest milestone or blocker]
   - [Next immediate action]
   
   ## Conflicts (if any)
   [IF strategic: true AND conflict_detected: true]
   ⚠️ This file was updated [date] over an earlier decision.
   Old: [what was recorded before]
   New: [what changed]
   Review in .vault-conflicts if needed.
   
   ## Sources
   [[last_synced_dump]]
   ```

6. **DO NOT summarize History sections** unless user explicitly asks for timeline.

7. **DO NOT load Source dumps** unless user says "show me the source" or "/history [topic]".

## Example Output
```
## ClinicalHours — Current State
B2C freemium $4.99/mo, B2B clinic portal $750-1000/yr. BCS Free Health Clinic is only confirmed partner (200+ users). Executing Meloy accelerator roadmap.

## Key Facts
- Stack: Next.js, Supabase, Vercel
- Strategic: true (major pivots tracked)
- Last update: 2026-04-14

## Conflicts
None.

## Sources
[[01_Source/Dumps/2026-04-14_clinicalhours-init]]
```
