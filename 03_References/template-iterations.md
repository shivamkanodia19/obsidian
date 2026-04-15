---
name: "Reference File Iterations Template"
description: "Template showing the standard Iterations section format for all Reference files"
type: "template"
created: "2026-04-15"
---

# Iterations Section Template

This file documents the standard format for tracking iterations, versions, and test results in all Reference files across the vault.

## Template Structure

Every Reference file should have an `## Iterations` section that follows this format:

```markdown
## Iterations

### v1.0 — Initial Version
**Test Date:** YYYY-MM-DD  
**Result:** [Success/Failed/Partial/Learning]  
**Key Metrics:** [What was measured]  
- Metric 1: Value
- Metric 2: Value

**Changes Made:** [What was tried]
**Next Steps:** [What to test next]

---

### v1.1 — [Specific Improvement]
**Test Date:** YYYY-MM-DD  
**Result:** [Success/Failed/Partial/Learning]  
**Key Metrics:** [What was measured]  
- Metric 1: Value
- Metric 2: Value

**Changes Made:** [What was tried]
**Next Steps:** [What to test next]

---

### v1.2 — [Another Specific Improvement]
**Test Date:** YYYY-MM-DD  
**Result:** [Success/Failed/Partial/Learning]  
**Key Metrics:** [What was measured]  
- Metric 1: Value
- Metric 2: Value

**Changes Made:** [What was tried]
**Next Steps:** [What to test next]
```

## Concrete Example (Copy-Paste Ready)

Below is a filled example for a cold email CTA variation test:

```markdown
## Iterations

### v1.0 — Vague Open-Ended CTA
**Test Date:** 2026-03-01  
**Result:** Failed  
**Key Metrics:**  
- Open Rate: 23%
- Click Rate: 2%
- Meeting Booked: 0

**Changes Made:** Used generic CTA: "Let me know what you think"  
**Next Steps:** Test specific binary choice

---

### v1.1 — Binary Choice CTA
**Test Date:** 2026-03-15  
**Result:** Success  
**Key Metrics:**  
- Open Rate: 25%
- Click Rate: 8%
- Meeting Booked: 3

**Changes Made:** Changed to: "Prefer Tuesday at 2pm or Thursday at 3pm?"  
**Next Steps:** Add scarcity element to increase urgency

---

### v1.2 — Binary Choice + Scarcity
**Test Date:** 2026-04-01  
**Result:** Success (13% improvement over v1.1)  
**Key Metrics:**  
- Open Rate: 27%
- Click Rate: 15%
- Meeting Booked: 6

**Changes Made:** Added: "I have 2 slots left this week for 30-min calls"  
**Next Steps:** Test personalization trigger
```

## Version Numbering Convention

- **v1.0** = Initial version tested
- **v1.1, v1.2, etc.** = Minor improvements within the same core idea
- **v2.0** = Major pivot or fundamental strategy change
- **v2.1, v2.2, etc.** = Improvements on the v2 approach

## Key Fields Explained

| Field | Purpose | Example |
|-------|---------|---------|
| **Test Date** | When this version was tested | 2026-03-15 |
| **Result** | Outcome category | Success/Failed/Partial/Learning |
| **Key Metrics** | What was tracked | Open Rate, Click Rate, etc. |
| **Changes Made** | Exact diff from previous version | "Added 'I have 2 slots left this week'" |
| **Next Steps** | What to test next based on learnings | "Test personalization trigger" |

## When to Create a New Iteration

- After each test cycle completes
- When you try a different approach
- When metrics change noticeably (>5% swing)
- When you learn something that affects future versions

## Integration with Agent Discovery

When agents load a Reference file, they should:
1. Read the Iterations section first
2. Identify the most successful version (highest metric in "Result" column)
3. Understand what failed before (learn from "Changes Made" in failed versions)
4. Check "Next Steps" in the latest version to find the recommended next test

---

**Last Updated:** 2026-04-15  
**Template Version:** 1.0
