---
title: Keeper Clash Product Brief
project: keeper-clash
strategic: true
status: stable
origin_dump: [[01_Source/projects/keeper-clash/goalie-duel-brainstorm-2026-04-21]]
last_synced_dump: [[01_Source/projects/keeper-clash/goalie-duel-brainstorm-2026-04-21]]
conflict_detected: false
last_updated: 2026-04-21
tags:
  - product
  - mvp
  - computer-vision
  - game
---

# Keeper Clash Product Brief

Source: [[01_Source/projects/keeper-clash/goalie-duel-brainstorm-2026-04-21]]

## Product Thesis

Keeper Clash is a browser-based camera game where the user's hands become the goalie and an AI striker tries to score. The core bet is that computer vision is strongest here as a live controller, not as a post-hoc video analysis wrapper.

The product should feel fun within 30 seconds. The immediate test is not whether the AI is sophisticated; it is whether the physical input loop makes people replay.

## Why This Is Stronger Than The Pushup Idea

The pushup leaderboard idea was too narrow as a standalone product. It risks becoming a rep counter with a novelty leaderboard, and the social loop may not survive after the first few tries.

Keeper Clash has a stronger loop:
- It is live, not retrospective.
- The body is the controller.
- The AI opponent creates tension.
- The user can improve through timing, positioning, and reaction.
- It can expand into friend challenges and multiplayer without changing the core mechanic.

## MVP

Build one mode first: **Penalty Rush**.

Core flow:
1. User opens the browser app.
2. App requests camera access.
3. Hand tracking activates.
4. A goal appears on screen.
5. AI striker shoots balls at different target zones.
6. User blocks shots with hands.
7. Match lasts 60 seconds.
8. Final screen shows saves, goals allowed, streak, reaction time, and rank.
9. User can replay immediately.

Do not start with accounts, complex onboarding, live multiplayer, full-body tracking, or advanced AI. The first prototype should answer whether the game loop is addictive.

## Technical Direction

Use a browser-first stack:
- MediaPipe or TensorFlow.js for hand tracking.
- Canvas for game rendering.
- Simple 2D ball physics and collision detection.
- Procedural shot generator for the AI striker.
- Difficulty ramp based on saves, misses, and reaction time.

The "AI striker" can initially be procedural:
- Pick target zones.
- Vary shot speed.
- Add fake-outs.
- Target user weak zones after observing missed saves.
- Increase difficulty during streaks.

This is enough to feel intelligent before adding any real model complexity.

## Validation

The first real validation metric:

Can 10 friends play it and each replay at least 3 times?

If yes, the next feature should be challenge links or daily seeded runs. If not, fix the feel of the core interaction before adding social features.

## Risks

- Hand tracking may feel laggy or unreliable on lower-end devices.
- If collision feedback is not satisfying, the game will feel like a tech demo.
- The game could be fun once but not retain users.
- Multiplayer is expensive in complexity and should wait until the single-player loop is clearly replayable.
- The product may need a sharper audience later: schools, streamers, sports teams, PE classes, or friend groups.

## Next Build Prompt

Build a browser game called Keeper Clash. Use webcam hand tracking so the user's hands act as blockers in front of a virtual soccer goal. Create one 60-second mode called Penalty Rush where a procedural AI striker shoots balls at different speeds and target zones. Track saves, goals allowed, streak, and reaction time. End with a score screen and replay button. Prioritize low latency, responsive collision feedback, and immediate replayability.
