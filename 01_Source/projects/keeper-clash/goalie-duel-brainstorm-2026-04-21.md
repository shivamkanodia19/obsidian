# Goalie Duel Product Brainstorm - 2026-04-21

Captured from a Codex brainstorming session.

## Starting Context

I have roughly 100 Lovable credits, Codex, and Claude Code when available. I want to build a useful project that has potential to become a product. The starting principle was that the strongest startup ideas usually solve a real problem I understand personally.

Initial idea: a computer vision weightlifting form tracker or grader. Concern: if the product is only "upload video, AI analyzes it, and gives advice," it becomes a thin AI wrapper instead of a differentiated product.

Friend reference point: friends recently made a computer vision pickleball app where an AI plays against the user using CV to track the pickleball stroke. I liked the concept of physical movement as the input to a game, with low latency and possible multiplayer.

## Ideas Explored

### Pushup Competition

One idea was a live pushup competition using CV to track the number of pushups daily and rank people on a leaderboard.

Brutal assessment:
- "Pushup counter plus daily leaderboard" is probably too weak as a standalone startup.
- It is more of a feature than a product.
- Novelty may wear off quickly.
- Cheating and partial reps become a major issue if rankings matter.
- Pushups alone are too narrow.

Better version:
- Camera-verified fitness competition platform.
- Daily 60-second verified challenges.
- Groups, gyms, teams, ROTC, fraternities, dorms, companies, or fitness creators.
- Example challenges: pushups, planks, squats, burpees, wall sits, shadowboxing, mobility challenges.

Validation test:
- Before building, run a manual 7-day challenge in a group chat.
- Have people submit videos.
- Manually count reps.
- Post the leaderboard.
- If people do not engage when it is manual and social, CV will not save it.

## Pivot Away From Exercise

The more interesting pattern from the pickleball example is not "fitness," but:

Use computer vision to turn a real physical action into a live game input, then make the AI bot feel like an opponent.

Important constraint:
- CV should be simple, fast, and reliable.
- The product should not require the model to understand too much.
- Pick one clear movement or object and build the game around it.

Ideas considered:
- Webcam Goalie Duel
- Shadowboxing Boss Fight
- AR Pong / Hand Paddle
- Tabletop Flick Battle
- Reaction Duel

Best-ranked option: Webcam Goalie Duel.

## Goalie Duel / Keeper Clash

Core concept:

A webcam game where your hands or body become the goalie, and an AI striker tries to score on you.

Why it seems strong:
- Low latency matters.
- CV is simpler than full sports technique analysis.
- It is fun almost immediately.
- It can work single-player first and multiplayer later.
- It can become penalty shootout battles with friends.
- It has more "wait, let me try again" energy than a pushup leaderboard.

MVP loop:
- User opens browser.
- Camera detects hands.
- Goal appears on screen.
- AI striker shoots balls at different angles and speeds.
- User blocks with hands.
- Match lasts 60 seconds.
- Score includes saves, goals allowed, streak, and reaction time.
- End screen gives rank and challenge link.

What makes it fun:
- Ball curves and fake-outs.
- Streak multiplier.
- Slow-motion "insane save" moments.
- Trash-talk style AI opponent.
- Daily challenge seed so everyone faces the same shots.
- Shareable scorecard: "I saved 17/25 vs Robo Striker."

Product expansion:
- Friend challenges.
- Live 1v1 penalty shootouts.
- Custom rooms.
- School or team leaderboards.
- Twitch or streamer challenge mode.
- Physical education or gym-class mode.
- Branded sports club challenges.

Technical MVP:
- Browser app.
- MediaPipe or TensorFlow.js hand/body tracking.
- Canvas game layer.
- Simple procedural AI shot generator.
- Lovable can help with the app shell and UI.
- Codex and Claude Code can help with implementation.

Important design decision:
- Start with hand tracking as blockers.
- Do not require full-body tracking at first.
- Reason: hand tracking is more precise, easier to explain, less fragile, and works at a desk.

MVP scope:
- One mode: "Penalty Rush: save as many shots as possible in 60 seconds."
- Camera permission.
- Hand tracking.
- Ball physics.
- Collision detection.
- Score.
- Timer.
- AI difficulty ramp.
- Final score screen.
- Replay button.

Validation milestone:

Can 10 friends play it and each replay at least 3 times?

If yes, add challenge links and leaderboard.

Potential names:
- Keeper Clash
- Goalie Rush
- Save Streak
- ShotStop
- NetGuard
- Penalty Panic

Current favorite names: Keeper Clash or Goalie Rush.

User reaction: "i really like the goalie idea. that sounds genuinely fun."
