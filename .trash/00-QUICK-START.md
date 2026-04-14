# Quick Start: Image Generation Setup

**Time required:** 25 minutes  
**Difficulty:** Easy (copy-paste mostly)

---

## Overview

You now have a self-improving image generation system. Here's what it does:

**Week 1:** You set it up (today)  
**Week 2+:** Claude reads vault → generates smart images → learns what works → improves

---

## Setup Checklist (Do These Now)

### ✅ Step 1: Configure MCP in Obsidian (5 min)

1. Open **Obsidian Settings** (bottom left gear icon)
2. Scroll down left sidebar → find **"MCP Tools"**
3. Click it to expand settings
4. Set these values:
   - **Vault path:** `C:\Users\shiva\Obsidian`
   - **Enable Read files:** Toggle ON ✅
   - **Enable Write files:** Toggle ON ✅
5. Click **"Test Connection"** button → should show ✅ connected
6. **Restart Obsidian** (close and reopen completely)

**Troubleshoot:** If connection fails, restart again. Local REST API plugin needs to be enabled.

---

### ✅ Step 2: Configure Claude Code (5 min)

1. **Open Claude Code**
2. Go to **Settings** (gear icon, top right)
3. Look for **"System Instructions"** or **"Custom Instructions"**
4. In this vault, open note: **[[CLAUDE-SYSTEM-INSTRUCTIONS]]**
5. **Copy the entire system prompt** (the big code block starting with "You are a vault-aware creative director...")
6. **Paste it into Claude's system instructions** area
7. **Save**

**Done!** Claude now knows how to read your vault and generate images.

---

### ✅ Step 3: Set Environment Variables (5 min)

You need to tell your system where your API keys are.

**Windows:**
1. Right-click **This PC** (or My Computer) on desktop
2. Click **Properties**
3. On left sidebar, click **"Advanced system settings"**
4. Click **"Environment Variables"** button (bottom right)
5. Under **"User variables for [your name]"**, click **New**
6. Fill in:
   - **Variable name:** `GEMINI_API_KEY`
   - **Variable value:** `AIzaSy...` (paste your Gemini API key from ai.google.dev)
7. Click **OK**
8. Repeat step 5-7 for another new variable:
   - **Variable name:** `ANTHROPIC_API_KEY`
   - **Variable value:** `sk-ant-...` (paste your Claude API key from console.anthropic.com)
9. Click **OK** to close everything
10. **Restart Claude Code** completely (close all windows)

**Mac/Linux:**
```bash
# Open terminal and edit your shell config:
nano ~/.zshrc

# Add these lines at the bottom:
export ANTHROPIC_API_KEY="sk-ant-..."
export GEMINI_API_KEY="AIzaSy..."

# Save (Ctrl+X, then Y, then Enter)
# Reload:
source ~/.zshrc
```

**Verify it worked:**
- Open terminal
- Type: `echo $GEMINI_API_KEY`
- Should show your key (not blank)

---

### ✅ Step 4: Test the Connection (5 min)

1. **Open Claude Code**
2. Create a new chat/note
3. **Type this exactly:**
   ```
   @mcp Read the file 00-Strategy-Overview.md from my vault
   ```
4. **Press Enter**
5. **Claude should respond** with your strategy overview content

**If it works:** ✅ You're connected!  
**If it fails:** "MCP not found" → Go back to Step 1, restart Obsidian

---

### ✅ Step 5: Generate Your First Images (30 min)

Now let's generate actual images!

1. **Open Claude Code** (fresh chat)
2. **Copy-paste this entire prompt:**

```
I need you to generate images for this week's ClinicalHours marketing.

STEP 1: Use @mcp to read my vault context files first.

STEP 2: Generate 5 image prompts for this week's #ClinicMindset post:
Topic: "Why clinical hours are your unfair advantage"

Use my vault context to ensure:
- Brand alignment (from 20-Content-Templates)
- Strategic alignment (from 00-Strategy-Overview)
- Learning from past performance (from 62-Visual-Performance-Tracker)

STEP 3: Call Gemini API to generate 2 images per prompt (10 total)
Save to: /images/hook/2026-04-14/, /images/problem/2026-04-14/, etc.

STEP 4: Analyze each image against my brand guidelines
Score 1-10 and provide strengths/weaknesses/suggestions

STEP 5: Append all critiques to 51-Image-Critiques.md

STEP 6: Show me a summary:
- Top 3 images (ready to post)
- Bottom 3 images (needs rework)
- Overall insights

Let me know when you're ready to start!
```

3. **Press Enter**
4. **Wait 2-3 minutes** while Claude:
   - Reads your entire vault
   - Generates 5 smart image prompts
   - Calls Gemini API to create 10 images
   - Analyzes and scores each one
   - Updates your vault

5. **Check your vault** → Go to `/images/hook/` folder, you should see images! 🎉

---

## What Happens Next

**Claude's output will show:**
```
✓ Connected to vault
✓ Read your strategy (brand guidelines, past performance)
✓ Generated 5 image prompts aligned with your brand
✓ Created 10 images via Gemini
✓ Scored each image 1-10

TOP PERFORMERS:
1. clinicmindset-hook-v2.png - 9/10 ✅
2. clinicmindset-problem-v1.png - 8/10 ✅
3. clinicmindset-solution-v1.png - 9/10 ✅

NEEDS REWORK:
1. clinicmindset-story-v1.png - 5/10 ❌
```

**In your vault:**
- **`51-Image-Critiques.md`** → Auto-updated with all critiques
- **`/images/hook/2026-04-14/`** → Your 10 generated images

---

## Troubleshooting

### "MCP connection failed"
- Restart Obsidian completely
- Check: Settings → MCP Tools → "Test Connection"
- Make sure Local REST API plugin is enabled

### "Claude can't read vault / @mcp not working"
- In Claude, test: `@mcp List files in my vault`
- If that works, vault is connected
- If not, restart Obsidian

### "API key not found" error
- Check environment variables are set correctly
- Verify: Open terminal, type `echo $GEMINI_API_KEY` (should show key, not blank)
- Restart Claude Code after setting variables

### "Gemini API error"
- Double-check your Gemini API key is correct (from ai.google.dev)
- Make sure you have a valid Gemini API project

### Images not saving to vault
- Check `/images` folder exists in your vault
- Verify write permissions (MCP Tools → Enable Write files ✅)
- Check file paths are correct

---

## Next Steps (After First Generation)

**Tuesday:**
- Review the images Claude created
- Check `[[51-Image-Critiques]]` for scores
- Regenerate any images <7/10 if you want

**Tue-Sun:**
- Post your best images (1 per day)
- Track engagement (views, saves, comments)

**Next Monday:**
- Do the same workflow
- Claude will be SMARTER (learns from engagement data)
- Images will be better quality

---

## Key Files to Know

- **[[00-Strategy-Overview]]** → Claude reads this to understand your brand
- **[[20-Content-Templates]]** → Claude uses this for visual style
- **[[CLAUDE-SYSTEM-INSTRUCTIONS]]** → Paste this into Claude settings
- **[[51-Image-Critiques]]** → Claude auto-updates with all scores + feedback
- **[[62-Visual-Performance-Tracker]]** → You update this weekly with engagement data

---

## Quick Reference

**Setup time:** 25 minutes (one-time)  
**Weekly generation:** 15 minutes (Monday)  
**Weekly review:** 20 minutes (Tuesday)  
**Daily posting:** 5 minutes (Tue-Sun)  

**Total weekly time:** ~1 hour (mostly automated)

---

## You're Ready! 🚀

Start with **Step 1** now. Let me know if you get stuck on any step!

After you're done with everything, remember to run `/save` to save progress to memory.
