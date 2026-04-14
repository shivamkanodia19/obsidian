---
title: Exam 3 Deep Analysis & Question Mapping
project: academics
status: stable
origin_dump: "Interview with Shivam - April 14, 2026"
last_synced_dump: "April 14, 2026"
last_updated: 2026-04-14
---

# Exam 3 - Complete Question Analysis & Study Strategy

## Study Timeline

**Exam Date:** May 2026 (3-4 weeks away)  
**Available Resources:** 15 past exams (2005-2019)  
**Strategy:** Deep pattern analysis + concept mastery

---

## Part 1: Exam Format & Structure

### General Exam Characteristics

| Aspect | Details |
|--------|---------|
| Duration | 50 minutes (typically) |
| Total Questions | 10-12 problems |
| Point Distribution | Usually 100 points total |
| Allowed Tools | Calculator (scientific), no graphing |
| Format | Free-response (show all work) |

### Typical Score Breakdown

| Points | Percentage | Questions |
|--------|-----------|-----------|
| 70+ | 70%+ | Passing (usually C or better) |
| 80+ | 80%+ | Strong understanding |
| 90+ | 90%+ | Mastery level |

### Partial Credit System

- **Full credit:** Correct answer with clear methodology
- **Partial credit:** Right method, computational error (usually 80-90% credit)
- **Partial credit:** Right answer, unclear work (variable, but 50-70%)
- **No credit:** Completely wrong approach

**Strategy:** Always show work. Partial credit can make the difference between C and B.

---

## Part 2: Question Type Deep Dive

### Category 1: Circular Motion & Centripetal Force (15-20% of exam)

#### Type 1.1: Basic Centripetal Acceleration
**Frequency:** 1-2 per exam | **Difficulty:** Easy | **Time:** 3-4 min

**Pattern:**
- Object moving in circular path (horizontal or on banked surface)
- Find centripetal acceleration, velocity, or force

**Key Formulas:**
```
a_c = v²/r = ω²r
F_c = ma_c = mv²/r
```

**Common Traps:**
- Confusing centripetal vs. tangential acceleration
- Forgetting that centripetal force is NET force directed toward center
- Unit errors (convert rpm to rad/s: ω = 2πf)

**Preparation Strategy:**
- Draw force diagrams showing ALL forces
- Identify which force provides centripetal force
- Check: Centripetal force is perpendicular to velocity

**Sample Problem Structure:**
```
Given: radius R, speed v, mass m
Find: centripetal acceleration (a_c)
Solution: Use a_c = v²/r directly
```

#### Type 1.2: Banked Curves & Friction
**Frequency:** 1 per exam | **Difficulty:** Medium | **Time:** 5-7 min

**Pattern:**
- Road/track banked at angle θ
- Find minimum/maximum speed before slipping
- Friction may or may not be involved

**Key Analysis:**
- Component of normal force provides centripetal force
- Friction acts up or down the slope depending on speed

**Critical Angles:**
- If v < v_min: friction acts UP the slope
- If v > v_max: friction acts DOWN the slope
- At critical speed: no friction needed (N alone provides centripetal)

**Force Diagram Setup:**
```
                N
               /|
              / |
             /  |θ
            /   |
           /    |---- F_friction
          /     |
         /------|
              mg
```

**Preparation Strategy:**
- Practice free body diagrams at different speeds
- Master the two-equation system (vertical equilibrium + horizontal = centripetal)
- Know when friction helps vs. opposes circular motion

#### Type 1.3: Vertical Circular Motion (Loop-the-Loop)
**Frequency:** 1 per exam | **Difficulty:** Hard | **Time:** 6-9 min

**Pattern:**
- Object moving in vertical circle
- Find normal force at specific point or minimum speed to complete loop
- Common: car on circular track, ball on string, loop-de-loop

**Critical Points to Analyze:**
1. **Top of loop:** N = 0 when at critical speed
   - mg + N = mv²/r  → At critical: N = 0, so v_min = √(gr)
2. **Bottom of loop:** N is maximum
   - N - mg = mv²/r  → N = mg + mv²/r
3. **Side of loop (90°):** 
   - N = mv²/r (only force providing centripetal)

**Common Question Variations:**
- Find minimum speed to complete full loop
- Find speed at specific point given initial height
- Find normal force at given point
- Track leaves the surface when N = 0

**Preparation Strategy:**
- Always identify the critical point (usually top of loop)
- Use energy conservation from entry to critical point
- Check if object completes loop: is N ≥ 0 at all points?
- Practice identifying when object "loses contact"

---

### Category 2: Work & Energy (20-25% of exam)

#### Type 2.1: Work-Energy Theorem
**Frequency:** 1-2 per exam | **Difficulty:** Easy-Medium | **Time:** 4-6 min

**Fundamental Equation:**
```
W_net = ΔKE = ½m(v_f² - v_i²)
```

**Or broken down by forces:**
```
W_tension + W_gravity + W_friction = ΔKE
```

**Pattern Recognition:**
- Multiple forces acting on object
- Path from point A to point B
- Find final velocity or force

**Component Work:**
```
W = F·d·cos(θ)  [where θ is angle between F and displacement]
```

**Common Scenarios:**
1. **Object pulled up incline with friction**
   - W_applied = F·d
   - W_gravity = -mg(h) = -mgd·sin(θ)
   - W_friction = -μmg·cos(θ)·d
   - Sum all, set equal to ΔKE

2. **Object moving along curved path**
   - Gravity: only height change matters W_g = -mg·Δh
   - Friction: full path length matters W_f = -μN·d_total
   - Applied force: depends on path

3. **Work by varying force**
   - Given F(x) = kx or similar
   - Calculate work using graph (area under curve) or integration

**Preparation Strategy:**
- Identify all forces doing work
- For each force: calculate work carefully (watch angles!)
- Sum all work = change in KE
- Check signs: negative work removes KE

#### Type 2.2: Power Problems
**Frequency:** 1 per exam | **Difficulty:** Easy-Medium | **Time:** 3-5 min

**Definitions:**
```
P_avg = W / Δt  [average power]
P_inst = F·v·cos(θ)  [instantaneous power]
```

**Common Scenarios:**
1. **Constant force, constant velocity:** P = Fv
2. **Varying force or velocity:** Use calculus or graph
3. **Climbing grade:** P = Fv = (mg·sin(θ))·v when moving up slope at constant speed

**Quick Recognition:**
- If steady speed → Power = (Force needed for steady motion) × (velocity)
- If changing speed → Power varies with velocity

#### Type 2.3: Work with Graphs
**Frequency:** 0-1 per exam | **Difficulty:** Medium | **Time:** 4-6 min

**Pattern:**
- Force vs. position graph provided
- Work = area under F-x curve

**Calculation Method:**
```
W = ∫F dx = area under curve
```

**Common Shapes:**
- **Linear (triangle):** W = ½ × base × height
- **Rectangular:** W = width × height
- **Composite:** Break into regions, sum areas

**Watch out:**
- Negative work (force opposite to displacement) = below x-axis
- Piecewise linear graphs = multiple regions to sum

---

### Category 3: Potential Energy & Conservation (20-25% of exam)

#### Type 3.1: Gravitational PE
**Frequency:** 1-2 per exam | **Difficulty:** Easy | **Time:** 2-3 min

**Equation:**
```
PE = mgh  [where h is height above reference level]
ΔPE = mgΔh
```

**Key Insight:**
- Only height change matters, not path
- Choose convenient reference level (usually PE = 0 at lowest point)

#### Type 3.2: Spring PE & Elastic Forces
**Frequency:** 1 per exam | **Difficulty:** Easy-Medium | **Time:** 3-5 min

**Spring Force:**
```
F = -kx  [Hooke's Law, x = displacement from equilibrium]
```

**Spring Potential Energy:**
```
PE_spring = ½kx²  [always positive!]
```

**Common Scenarios:**
1. **Compressed spring releases object:** PE_spring converts to KE
2. **Object lands on spring:** Combines gravity PE + spring PE
3. **Oscillating spring-mass:** Exchanges PE ↔ KE

**Preparation Strategy:**
- Remember: x is displacement FROM equilibrium, not from natural length
- Spring PE is always positive (it's about stored energy)
- At maximum compression, all energy is PE_spring

#### Type 3.3: Energy Conservation (No Friction)
**Frequency:** 2-3 per exam | **Difficulty:** Medium-Hard | **Time:** 6-9 min

**Fundamental Equation:**
```
E_initial = E_final
KE_i + PE_grav_i + PE_spring_i = KE_f + PE_grav_f + PE_spring_f
```

**General Strategy:**
1. Identify reference level for gravitational PE
2. Identify all forms of energy present
3. Write energy equation for initial and final states
4. Solve for unknown (velocity, height, spring compression, etc.)

**Common Scenarios:**
1. **Pendulum at different heights:**
   - ½mv_bottom² = mgh (where h = height difference)
   - v_bottom = √(2gh)

2. **Block on spring:**
   - At maximum compression: all energy is spring PE
   - ½mv² = ½kx² (if starting from equilibrium)

3. **Object down frictionless incline:**
   - mgh = ½mv² (where h = vertical drop)
   - v = √(2gh) independent of slope!

**Critical Mistakes to Avoid:**
- Forgetting potential energy terms
- Wrong reference level for PE
- Confusing initial and final states
- Not accounting for all energy forms

#### Type 3.4: Energy with Friction (Non-Conservative)
**Frequency:** 1-2 per exam | **Difficulty:** Hard | **Time:** 7-10 min

**Key Concept:**
```
W_friction = -μmg·d_path  [always negative, always opposes motion]
```

**Energy Equation with Friction:**
```
KE_i + PE_i - |W_friction| = KE_f + PE_f
[or: E_i - |W_friction| = E_f]
```

**Friction Work Depends On:**
- Coefficient of friction μ (given)
- Normal force N (which depends on incline/surface)
- Path length traveled d (full path, not displacement!)

**Common Scenarios:**
1. **Block sliding down incline with friction:**
   - Initial PE = final KE + work done by friction
   - mgh = ½mv_f² + μmg·cos(θ)·d

2. **Horizontal surface with friction:**
   - Initial KE = work done by friction
   - ½mv_i² = μmg·d
   - d = v_i² / (2μg)

3. **Spring with friction:**
   - Initial spring PE = final KE + work by friction
   - ½kx² = ½mv² + μmg·d

**Preparation Strategy:**
- Always calculate friction force correctly (depends on surface)
- Use path length, not displacement
- Track all three energy types: KE, gravitational PE, spring PE
- Friction always dissipates energy (never creates it)

---

### Category 4: Rotational Motion (15-20% of exam)

#### Type 4.1: Angular Kinematics
**Frequency:** 1 per exam | **Difficulty:** Easy-Medium | **Time:** 3-5 min

**Equations:**
```
θ = ω_i·t + ½α·t²  [angular displacement]
ω_f = ω_i + α·t  [angular velocity]
ω_f² = ω_i² + 2α·θ  [useful when time unknown]
```

**Linear-Angular Relationships:**
```
v = rω  [linear velocity = radius × angular velocity]
a_tangential = rα  [tangential acceleration]
a_centripetal = ω²r  [centripetal acceleration]
```

**Unit Conversions:**
- RPM to rad/s: ω = (RPM) × 2π / 60
- Revolutions to radians: θ = (revolutions) × 2π

**Common Problem:** 
Wheel spinning at constant RPM → Find # of revolutions in time t
- Convert RPM to rad/s
- Use θ = ω·t
- Convert back to revolutions

#### Type 4.2: Moment of Inertia & Torque
**Frequency:** 1-2 per exam | **Difficulty:** Medium | **Time:** 4-7 min

**Definition:**
```
I = Σ m_i r_i²  [for discrete masses]
I = ∫ r² dm  [for continuous bodies]
```

**Standard Shapes:**
```
Solid cylinder/disk:  I = ½MR²
Thin hoop:           I = MR²
Solid sphere:        I = ⅖MR²
Thin rod (about center): I = 1/12 ML²
Thin rod (about end):    I = ⅓ML²
```

**Parallel Axis Theorem:**
```
I_arbitrary = I_cm + Md²
[where d = distance from center of mass to rotation axis]
```

**Torque:**
```
τ = rF·sin(θ)  [where θ = angle between r and F]
τ = I·α  [rotational Newton's second law]
```

**Problem Identification:**
- If asked for I of standard shape → Use formula
- If asked for I of composite → Break into parts, use parallel axis theorem
- If asked for angular acceleration → Use τ = I·α

**Preparation Strategy:**
- Memorize the standard moment of inertia formulas
- Practice applying parallel axis theorem
- Draw torque diagrams (force perpendicular distance from pivot)
- Remember: only component of F perpendicular to r contributes to torque

#### Type 4.3: Rotational Energy & Power
**Frequency:** 1 per exam | **Difficulty:** Medium | **Time:** 4-6 min

**Rotational KE:**
```
KE_rot = ½I·ω²  [analogous to ½mv²]
```

**Rolling Without Slipping:**
```
v_cm = rω  [center of mass velocity = radius × angular velocity]
```

**Total KE (rolling object):**
```
KE_total = ½m·v_cm² + ½I·ω²
         = ½m·v_cm² + ½I·(v_cm/r)²
```

**For different rolling shapes:**
```
Solid cylinder: KE = ½mv² + ½(½mr²)(v/r)² = ¾mv²
Solid sphere:   KE = ½mv² + ½(⅖mr²)(v/r)² = 0.7mv²
Thin hoop:      KE = ½mv² + ½(mr²)(v/r)² = mv²
```

**Key Insight:** Only fraction of gravitational PE converts to translational KE when rolling. Rest goes to rotational KE!

**Energy Conservation for Rolling:**
```
mgh = ½m·v² + ½I·ω²  [no friction doing work - rolling constraint]
```

**Problem Recognition:**
- "Ball rolls down incline" → Both translational and rotational KE
- Speed at bottom < √(2gh) because energy split between translation & rotation
- Order: solid sphere < solid cylinder < thin hoop (less energy in rotation)

---

### Category 5: Angular Momentum & Rotation (10-15% of exam)

#### Type 5.1: Angular Momentum
**Frequency:** 1 per exam | **Difficulty:** Medium | **Time:** 5-7 min

**Definition:**
```
L = I·ω  [angular momentum = moment of inertia × angular velocity]
```

**Conservation of Angular Momentum:**
```
L_initial = L_final (if no external torques)
I_i·ω_i = I_f·ω_f
```

**Classic Problem: Spinning Skater**
```
Initial: I_i (arms out), ω_i
Final: I_f (arms in, smaller I), ω_f = ?

I_i·ω_i = I_f·ω_f
ω_f = (I_i/I_f)·ω_i  [smaller I → higher ω]
```

**Common Scenarios:**
1. **Person on spinning stool picks up weights**
   - Initial: person + stool spinning
   - Final: person picks up objects (I increases)
   - Result: ω decreases to conserve L

2. **Collision adding/removing mass**
   - Object lands on spinning wheel
   - Angular momentum exchanged
   - Final angular velocity lower

3. **Explosion or separation**
   - Object breaks apart
   - Angular momentum conserves
   - Parts move in opposite directions

**Preparation Strategy:**
- Always check if there are external torques (usually there aren't)
- Calculate I before and after carefully (use parallel axis if needed)
- Remember: L is conserved if τ_external = 0

#### Type 5.2: Rotational Dynamics with Torque
**Frequency:** 1 per exam | **Difficulty:** Medium-Hard | **Time:** 6-8 min

**Pattern:**
- Pulley system with hanging mass
- Forces applied at radius creating torque
- Find angular acceleration, tension, or motion

**System Analysis:**
1. **Draw free body diagrams:** Both rotating object AND any linear masses
2. **Write equations:** 
   - For rotational part: Στ = I·α
   - For linear parts: ΣF = m·a
3. **Connect with constraints:** If string doesn't slip, a_linear = r·α

**Example: Pulley with hanging mass**
```
Pulley: I, R, rotating
Mass: m, falling

For mass: mg - T = m·a (down positive)
For pulley: T·R = I·α

Constraint: a = R·α (string doesn't slip)

Substitute: mg - T = m·R·α
           T·R = I·α → T = I·α/R
           
mg - (I·α/R) = m·R·α
mg = m·R·α + I·α/R
mg = α(m·R + I/R)
α = mg / (m·R + I/R)
```

---

### Category 6: Oscillations & Simple Harmonic Motion (15-20% of exam)

#### Type 6.1: Spring-Mass Systems
**Frequency:** 2 per exam | **Difficulty:** Easy-Medium | **Time:** 4-6 min

**Period:**
```
T = 2π√(m/k)  [in seconds]
f = 1/T = (1/2π)√(k/m)  [frequency in Hz]
ω = 2πf = √(k/m)  [angular frequency in rad/s]
```

**Key Properties:**
- Period depends ONLY on m and k, NOT on amplitude
- Stiffer spring (larger k) → shorter period
- More mass (larger m) → longer period

**Displacement in SHM:**
```
x(t) = A·cos(ωt + φ)
v(t) = -Aω·sin(ωt + φ) = -A·ω·cos(ωt + φ + π/2)
a(t) = -Aω²·cos(ωt + φ) = -ω²·x(t)
```

**Energy in SHM:**
```
E_total = ½kA²  [constant, independent of position]
At position x: KE = ½k(A² - x²), PE = ½kx²
```

**Key Points:**
- Maximum speed at equilibrium: v_max = Aω = A√(k/m)
- Maximum acceleration at extremes: a_max = Aω²
- Speed at position x: v = ω√(A² - x²)

#### Type 6.2: Pendulum Problems
**Frequency:** 1-2 per exam | **Difficulty:** Medium | **Time:** 5-7 min

**Simple Pendulum (small angles):**
```
T = 2π√(L/g)  [length L, gravity g]
Period independent of mass!
Period independent of amplitude (if small angle)
```

**Physical Pendulum:**
```
T = 2π√(I/(mgd))
[I = moment of inertia about pivot, d = distance to center of mass]
```

**Common Problem Type:**
- Find period of pendulum with given length
- Find length needed for specific period
- Compare periods of different pendulums

**Energy in Pendulum:**
```
E = ½mv² + mgh  [h measured from lowest point]
At angle θ: h = L(1 - cos θ)
At bottom: E = ½mv_max² = mgL(1 - cos θ_max)
```

**Preparation Strategy:**
- Remember T = 2π√(L/g) for simple pendulum
- For physical pendulum, must calculate I correctly
- Most exam problems use small angle approximation
- Energy methods often simpler than force analysis

#### Type 6.3: Energy & Oscillations
**Frequency:** 1 per exam | **Difficulty:** Medium | **Time:** 5-7 min

**Total Mechanical Energy:**
```
E = ½kA² = constant throughout oscillation
```

**At Any Position x:**
```
½mv² + ½kx² = ½kA²
v² = (k/m)(A² - x²)
v = ω√(A² - x²)
```

**From v and x, find A:**
```
A² = x² + (v/ω)² = x² + v²/(k/m)
```

**Problems:**
1. **Find amplitude given initial conditions**
   - Given x₀ and v₀ → Find A
   - Use: A = √(x₀² + (v₀/ω)²)

2. **Find speed at specific position**
   - Given A and x → Find v
   - Use: v = ω√(A² - x²)

3. **Find total energy**
   - E = ½kA²

#### Type 6.4: Damped Oscillations (Less Common)
**Frequency:** 0-1 per exam | **Difficulty:** Hard | **Time:** 8-10 min

**Damped oscillation:**
```
x(t) = A₀·e^(-t/τ)·cos(ωt + φ)
[amplitude decays exponentially with time constant τ]
```

**Energy decay:**
```
E(t) = E₀·e^(-2t/τ)  [energy decays twice as fast]
```

**Usually not heavily tested** but good to understand concept.

---

## Part 3: Problem-Solving Strategy

### Step-by-Step Framework

**1. Identify the Problem Type (2 min)**
- What physics concept is tested? (Circular motion? Energy? Rotation?)
- What quantity is unknown?
- What are the given quantities?

**2. Choose Solution Method (2 min)**
- **Force approach:** Draw FBD, apply Newton's laws
- **Energy approach:** Use conservation if possible (often simpler!)
- **Kinematics approach:** Direct use of equations

**Rule of thumb:** 
- Energy is usually fastest for problems involving different heights or speeds
- Forces needed for problems asking about specific forces (tension, normal, etc.)

**3. Set Up Equations (3-5 min)**
- Write all relevant equations
- Define variables and reference frames clearly
- Check dimensions

**4. Solve Algebraically (2-4 min)**
- Solve symbolically first (not numbers)
- Substitute numbers only at end
- This catches errors and makes partial credit clearer

**5. Check Answer (1-2 min)**
- Does magnitude make sense?
- Are units correct?
- Do limiting cases work? (e.g., if friction → 0, does answer approach frictionless case?)

### Common Mistakes & How to Avoid

| Mistake | Solution |
|---------|----------|
| Wrong sign on work/PE | Carefully identify direction of force vs. displacement |
| Forgetting a force | Draw complete FBD before writing equations |
| Confusion about "center" | Clarify: center of mass? center of rotation? center of circle? |
| Unit inconsistency | Convert all units to SI (m, kg, s) at beginning |
| Mixing rotational/linear | Keep ω separate from v; use v = rω to connect |
| Forgetting friction work depends on distance | Friction work = μmg × (full path length, not displacement) |
| Wrong PE reference | Choose zero PE early and state it clearly |
| Energy conservation when friction present | Energy isn't conserved; use W = ΔE instead |

---

## Part 4: Practice Strategy for May Exam

### Week-by-Week Schedule

**Week 1 (April 14-20): Foundation**
- [ ] Review Exam 3 Question Types Guide (1 hr)
- [ ] Work 2-3 problems of each type from easiest exams (2015-2019)
- [ ] Time yourself: aim to beat the "time to solve" estimates
- [ ] Review any weak areas

**Week 2 (April 21-27): Application**
- [ ] Work 10-12 problems selecting different years randomly
- [ ] Practice full "exam conditions": 50 min, no interruptions
- [ ] Review mistakes deeply (don't just correct, understand why)
- [ ] Focus on medium-difficulty problems

**Week 3 (April 28-May 4): Mastery**
- [ ] Take 2-3 full practice exams under timed conditions
- [ ] Mix in hard problems
- [ ] Identify remaining weak topics
- [ ] Deep practice on weak areas

**Week 4 (May 5-10): Final Polish**
- [ ] Quick review of key formulas
- [ ] Light practice on mixed problems
- [ ] Confidence-building with some easier problems
- [ ] Rest and test day

### Practice Selection Strategy

**Day 1-2: Easy Foundation**
- Exams: 2018, 2019 (usually a bit easier)
- Problems: Type 1A, 2A, 3A, 4A, 5A, 6A only
- Goal: Build confidence, lock down basics

**Day 3-4: Medium Problems**
- Exams: 2015, 2016, 2017
- Problems: Add Type 1B, 2B, 3B, 4B, 5B, 6B
- Goal: Develop problem-solving stamina

**Day 5-6: Hard Problems**
- Exams: 2010, 2013, 2014
- Problems: Add Type 1C, 4D, 6C
- Goal: Push limits of understanding

**Day 7+: Mixed & Timed**
- Select problems randomly from all years
- Take full 50-minute exams
- Simulate actual test conditions

### Self-Assessment Checklist

**After Each Problem, Ask:**
- [ ] Did I identify the question type correctly?
- [ ] Did I choose an efficient solution method?
- [ ] Did I set up equations correctly?
- [ ] Did my algebra flow logically?
- [ ] Did I check my answer for reasonableness?
- [ ] How long did it take vs. the estimate?

**After Each Topic Block:**
- [ ] Can I identify these questions in an exam?
- [ ] Can I solve them in under the time limit?
- [ ] Do I feel confident explaining the concepts?
- [ ] Which sub-types still trip me up?

**After Each Full Practice Exam:**
- [ ] What types did I miss?
- [ ] Which mistakes were careless vs. conceptual?
- [ ] Did time management work?
- [ ] What's my likely score?

---

## Part 5: Concept Summary (Quick Reference)

### Top 10 Must-Know Equations

```
1. Centripetal Acceleration:    a_c = v²/r
2. Work-Energy:                 W = ½m(v_f² - v_i²)
3. Gravitational PE:            PE = mgh
4. Spring PE:                   PE = ½kx²
5. Period of spring:            T = 2π√(m/k)
6. Rotational KE:               KE = ½Iω²
7. Angular momentum:            L = Iω
8. Torque:                      τ = I·α
9. Period of pendulum:          T = 2π√(L/g)
10. Rolling constraint:          v = rω
```

### Top 5 Problem-Solving Insights

1. **Energy > Forces:** When possible, use energy conservation (often one equation instead of three)
2. **Draw Pictures:** FBDs, energy diagrams, geometry sketches save time and prevent errors
3. **Symbol First:** Solve algebraically before plugging in numbers; easier to check and get partial credit
4. **Check Limiting Cases:** Does answer go to zero when force → 0? Does it match expected behavior?
5. **Partial Credit:** Show work clearly. Methodology matters even if final answer is wrong.

---

## Part 6: Resources

### For This Exam

**Past Exams Available:** 15 exams (2005-2019)
- Location: `/02_Analyst/academics/Mechanics/Exam3/`
- Recommendation: Don't just work problems; analyze them for patterns

**Key Concepts to Revisit:**
- Distinguishing between centripetal and tangential acceleration
- Work done by friction (always depends on path length)
- Energy conservation only valid when no non-conservative forces present
- Moment of inertia differences between shapes
- Rolling motion combines translation and rotation

### During Exam Strategy

**First 5 min (Read all problems):**
- [ ] Skim all 10-12 problems
- [ ] Identify which are easy, medium, hard
- [ ] Plan attack order (do easy first for quick points)

**Next 40 min (Solve problems):**
- [ ] Start with 2-3 easiest problems (quick wins, confidence)
- [ ] Move to medium problems (bread and butter)
- [ ] Attempt hard problems if time allows (partial credit possible)
- [ ] Show all work (even if unsure of final answer)

**Last 5 min (Check if time):**
- [ ] Review solutions for obvious errors
- [ ] Check dimensions and reasonableness
- [ ] Make sure all work is legible

---

## Summary

You have 15 past exams covering 15 years of patterns. This guide maps the question types, provides deep conceptual understanding, and gives you a structured study plan. The key is deliberate practice: understand each question type, solve many examples, and identify your weak areas early.

**Your advantage:** With 4 weeks and 15 exams (150+ practice problems), you have excellent material for mastery. Focus on depth over breadth: better to deeply understand 5 question types than superficially know all 25.

**Target:** 85%+ (85+ points) by May

---

*Last Updated: April 14, 2026*  
*Prepared for: Shivam Kanodia - TAMU Physics Mechanics Exam 3*
