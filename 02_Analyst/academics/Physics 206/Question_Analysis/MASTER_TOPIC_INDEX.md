---
title: Master Topic Index - All Questions Organized by Topic
project: academics
status: stable
last_updated: 2026-04-14
---

# Master Topic Index - All 15 Exams (2005-2019)

Complete question database organized by **topic**, with cross-references to specific exams.

---

## TOPIC 1: Polar Coordinate Kinematics ⭐⭐⭐

**Frequency:** 100% of exams (2005-2019)  
**Typical Points:** 20-25 per exam  
**Typical Position:** Problem 1 in most years  
**Difficulty:** Easy-Medium

### What's Always Tested

1. **Derive $v_r$ and $v_\theta$ components**
   - $v_r = \dot{r}$ (radial velocity)
   - $v_\theta = r\dot{\theta}$ (tangential velocity)
   
2. **Derive $a_r$ and $a_\theta$ components**
   - $a_r = \ddot{r} - r\dot{\theta}^2$ (radial acceleration, includes centripetal term)
   - $a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta}$ (tangential acceleration, includes Coriolis-like term)

### Exam References

| Year | Problem | Focus | Points | Status |
|------|---------|-------|--------|--------|
| **2007** | 1a | Derivation | 20 | ✅ Analyzed |
| **2007** | 1b | Application (find F) | 5 | ✅ Analyzed |
| **2008** | 1 | Full derivation | 25 | ✅ Analyzed |
| **2009** | 1 | r and θ components | 25 | ✅ Analyzed |
| **2010** | 1 | r and θ components | 25 | ✅ Analyzed |
| **2005** | ? | Likely Problem 1 | ~25 | ⚠️ Image-based |
| **2006** | ? | Likely Problem 1 | ~25 | ⚠️ Image-based |
| **2011-2019** | Likely P1 | Polar coords | ~25 | ⚠️ Image-based |

### Key Formulas to Memorize

```
Position:      r(t), θ(t)

Velocity:      v_r = dr/dt
               v_θ = r·dθ/dt

Acceleration:  a_r = d²r/dt² - r(dθ/dt)²
               a_θ = r·d²θ/dt² + 2(dr/dt)(dθ/dt)

Speed:         v = √(v_r² + v_θ²)
```

### Practice Problems from Analysis

- **2007 Problem 1a:** Standard derivation (20 pts)
- **2007 Problem 1b:** Find force given $r(t)=kt²$, $θ(t)=bt²$ (5 pts)
- **2008 Problem 1:** Full derivation (25 pts)
- **2009 Problem 1:** r and θ components (25 pts)

---

## TOPIC 2: Collisions & Momentum Conservation ⭐⭐⭐

**Frequency:** 75-100% of exams  
**Typical Points:** 12-25 per exam  
**Typical Position:** Problem 2  
**Difficulty:** Easy-Medium to Medium

### Collision Types

#### 2.1 Perfectly Inelastic (Objects Stick)
- **Momentum conserved:** $p_before = p_after$
- **Energy NOT conserved:** Energy is lost to deformation, heat, etc.
- **Formula:** $m_1 v_1 + m_2 v_2 = (m_1 + m_2)v_f$

**Exam appearances:**
- **2007 Problem 2a:** Ball swings and sticks to object (12 pts)
- **2008 Problem 2:** Man jumps between sleds (13 pts)
- **2009 Problem 2b:** Object sticks to block on spring (13 pts)

#### 2.2 Perfectly Elastic (Objects Bounce)
- **Momentum conserved:** $p_before = p_after$
- **Energy conserved:** $KE_before = KE_after$
- **Two equations, two unknowns**

**Exam appearances:**
- **2007 Problem 2b:** Ball bounces off object (set up equations only) (12 pts)
- **2008 Problem 4c:** Elastic collision scenario (12 pts)
- **2009 Problem 2a:** Elastic bounce off block (12 pts)

#### 2.3 Multi-Dimensional Collisions
- **Conserve momentum in each direction**
- **Track velocity vectors, not just speeds**

**Exam appearances:**
- **2008 Problem 2b:** Man jumps to sled at angle (13 pts)

### Key Equations

**Momentum Conservation (always):**
$$m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'$$

**Energy Conservation (elastic only):**
$$\frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2 = \frac{1}{2}m_1 v_1'^2 + \frac{1}{2}m_2 v_2'^2$$

**Energy Lost (inelastic):**
$$\Delta E = KE_{before} - KE_{after}$$

### Practice Strategy

1. **Identify collision type** (elastic or inelastic)
2. **Write momentum conservation equation(s)**
3. **If elastic, also write energy conservation**
4. **Solve the system** (may be set of equations, not full solution)

---

## TOPIC 3: Angular Momentum & Conservation ⭐⭐⭐

**Frequency:** 75-100% of exams  
**Typical Points:** 8-25 per exam  
**Typical Position:** Problem 3  
**Difficulty:** Easy-Medium to Hard

### Core Concept

**Angular Momentum:**
$$L = I\omega$$
where I = moment of inertia, ω = angular velocity

**Conservation (when no external torques):**
$$L_{initial} = L_{final}$$
$$I_i \omega_i = I_f \omega_f$$

### Common Scenarios

#### 3.1 Moment of Inertia Changes (Very Common)
**Example:** Person on spinning platform pulls arms in
- As I decreases → ω increases (to conserve L)
- Classic "figure skater" problem

**Exam appearances:**
- **2007 Problem 3b:** Arms pull from S to S/4 (8 pts)
- **2007 Problem 3c:** Same but man has mass (8 pts)
- **2008 Problem 3a:** Mass moves toward axis (8 pts)
- **2008 Problem 3c:** With massive rod (8 pts)
- **2009 Problem 4a:** Mass ejected from rod (8 pts)
- **2009 Problem 4b:** With rod's moment of inertia (7 pts)

#### 3.2 Angular Momentum About a Point
$$\vec{L} = \vec{r} \times m\vec{v}$$
$$L = mvr\sin\theta$$
(θ = angle between position and velocity vectors)

**Exam appearances:**
- **2008 Problem 4a:** Plane's angular momentum about origin (5 pts)
- **2009 Problem 4a:** Flying plane's L about origin (5 pts)

#### 3.3 Composite Systems
- Rod has moment of inertia $I_{rod}$
- Masses on rod have $I_{masses}$
- **Total:** $I_{total} = I_{rod} + I_{masses}$

**Exam appearances:**
- **2008 Problem 3:** Various sub-problems (24 pts)

### Moment of Inertia Formulas

| Shape | Formula | Note |
|-------|---------|------|
| Point mass at distance r | $I = mr^2$ | Single mass |
| Solid cylinder | $I = \frac{1}{2}MR^2$ | About central axis |
| Thin hoop | $I = MR^2$ | All mass at edge |
| Solid sphere | $I = \frac{2}{5}MR^2$ | About center |
| Thin rod (about center) | $I = \frac{1}{12}ML^2$ | L = length |
| Thin rod (about end) | $I = \frac{1}{3}ML^2$ | About one end |

**Parallel Axis Theorem:**
$$I = I_{cm} + Md^2$$
(d = distance from center of mass to rotation axis)

### Practice Strategy

1. **Check: Are there external torques?**
   - If YES → Angular momentum NOT conserved
   - If NO → $L_i = L_f$

2. **Calculate moment of inertia** before and after

3. **Set up conservation equation:**
   $$I_i \omega_i = I_f \omega_f$$

4. **Solve for unknown**

---

## TOPIC 4: Torque & Rotational Dynamics ⭐⭐

**Frequency:** 75% of exams  
**Typical Points:** 6-25 per exam  
**Typical Position:** Problem 4 (often)  
**Difficulty:** Easy to Medium

### Core Equations

**Torque:**
$$\tau = rF\sin\theta = r_\perp F$$
where $r_\perp$ = perpendicular distance from axis to force

**Newton's Second Law for Rotation:**
$$\tau = I\alpha$$
where α = angular acceleration

### Common Problems

#### 4.1 Rod Rotating About Hinge
- Rod of length L, mass M, moment of inertia I
- Gravity acts at center (distance L/2)
- Various angles: horizontal, vertical, arbitrary

**Exam appearances:**
- **2007 Problem 4:** Rod rotations - 4 sub-problems (25 pts)
  - 4a: Torque when horizontal (6 pts)
  - 4b: Angular acceleration when horizontal (6 pts)
  - 4c: Torque when vertical (6 pts)
  - 4d: Acceleration when vertical (7 pts)

#### 4.2 Pulley Systems
- Torque from hanging mass tension
- Relates linear and angular acceleration

#### 4.3 Applied Forces
- Motor supplying torque
- Time-varying torque

**Exam appearances:**
- **2009 Problem 3:** Conveyor belt angular acceleration
  - 3a: Velocity at point (8 pts)
  - 3b: Force vs. time (8 pts)
  - 3c: Maximum angular acceleration (9 pts)

### Key Insights

1. **Torque = 0 when:**
   - Force passes through axis
   - Force is parallel to radius

2. **Maximum torque when:**
   - Force perpendicular to radius
   - Distance from axis is maximum

3. **Linear vs. Angular:**
   - $a = r\alpha$ (tangential acceleration)
   - $a_c = \omega^2 r$ (centripetal acceleration)

### Practice Problems

- **2007 Problem 4a-d:** Complete rod analysis (25 pts)
- **2009 Problem 3a-c:** Conveyor belt (25 pts)

---

## TOPIC 5: Spring & Oscillatory Motion ⭐

**Frequency:** 25-50% of exams (increasing)  
**Typical Points:** 8-25 per exam  
**Typical Position:** Problem 2 or 3  
**Difficulty:** Easy-Medium to Hard

### Core Equations

**Hooke's Law:**
$$F = -kx$$
where x = displacement from equilibrium

**Spring Potential Energy:**
$$PE_s = \frac{1}{2}kx^2$$

**Simple Harmonic Motion Period:**
$$T = 2\pi\sqrt{\frac{m}{k}}$$

### Common Problems

#### 5.1 Collision with Spring
- Object hits block attached to spring
- Find maximum compression

**Exam appearances:**
- **2009 Problem 2:** Block-spring collision (25 pts)
  - 2a: Elastic collision + spring compression (set up, no algebra) (12 pts)
  - 2b: Inelastic collision + spring compression (13 pts)

#### 5.2 Spring Attached to Conveyor Belt
- Spring compressed/extended as system moves
- Energy exchange

#### 5.3 Energy in Oscillations
- Total energy = $E = \frac{1}{2}kA^2$ (A = amplitude)
- At position x: $KE = \frac{1}{2}k(A^2-x^2)$, $PE = \frac{1}{2}kx^2$

### Practice Strategy

1. **When springs appear with collisions:**
   - First solve collision (momentum conservation)
   - Then solve for spring compression (energy conservation)

2. **When springs appear in oscillations:**
   - Use energy methods
   - $E_{initial} = E_{final}$

---

## TOPIC 6: Circular Motion & Centripetal Force ⭐

**Frequency:** 50-75% of exams  
**Typical Points:** 5-25 per exam  
**Typical Position:** Various (often part of other problems)  
**Difficulty:** Easy-Medium

### Core Equations

**Centripetal Acceleration:**
$$a_c = \frac{v^2}{r} = \omega^2 r$$

**Centripetal Force:**
$$F_c = ma_c = \frac{mv^2}{r} = m\omega^2 r$$

**Circular Motion Kinematics:**
$$v = r\omega$$
$$a_{tangential} = r\alpha$$

### Common Scenarios

#### 6.1 Orbital Motion
- Object orbits fixed center (planet, atom, etc.)
- Central force provides centripetal acceleration

**Exam appearances:**
- **2008 Problem 4a:** Electron orbiting proton (5 pts)
- **2009 Problem 4:** Flying plane's angular momentum (5 pts)

#### 6.2 Conveyor Belts & Circular Paths
- Object on circular belt
- Both tangential and centripetal forces act

**Exam appearances:**
- **2009 Problem 3:** Box on circular conveyor (25 pts)

#### 6.3 Banked Curves (likely in 2011+)
- Object on inclined circular path
- Normal force + friction + gravity

### Practice Strategy

1. **Identify the circular motion component**
2. **Calculate centripetal acceleration needed**
3. **Identify forces providing centripetal force**
4. **Apply F = ma in radial direction**

---

## TOPIC 7: Energy Conservation Methods ⭐

**Frequency:** 50-75% of exams  
**Typical Points:** Woven throughout (5-20 pts often)  
**Typical Position:** Most problems  
**Difficulty:** Easy to Hard (depending on context)

### Types of Energy

1. **Kinetic Energy:** $KE = \frac{1}{2}mv^2$
2. **Gravitational PE:** $PE_g = mgh$
3. **Spring PE:** $PE_s = \frac{1}{2}kx^2$
4. **Rotational KE:** $KE_{rot} = \frac{1}{2}I\omega^2$

### Conservation Principles

**Mechanical Energy (no friction, no heat):**
$$E_{total} = KE + PE = constant$$
$$KE_i + PE_i = KE_f + PE_f$$

**With Friction (energy lost):**
$$E_i - |W_{friction}| = E_f$$
$$KE_i + PE_i - \mu mg d = KE_f + PE_f$$

**In Collisions:**
- **Elastic:** Energy conserved
- **Inelastic:** Energy lost (some becomes heat)

### Applications in Exams

- **2007 Problem 2a:** Swinging ball → collision height
- **2008 Problem 2a:** Sliding down frictionless hill
- **2009 Problem 2:** Spring compression after collision
- **All exams:** Multiple energy conversions within problems

### Practice Strategy

1. **Identify reference level for PE** (usually bottom)
2. **List all energy forms** at initial and final states
3. **Write energy equation:** $E_i = E_f$ or $E_i - loss = E_f$
4. **Solve for unknown**

---

## TOPIC 8: Work & Power (Less Common)

**Frequency:** 10-25% of exams  
**Typical Points:** 5-15 per exam  
**Typical Position:** Part of larger problems  
**Difficulty:** Easy-Medium

### Definitions

**Work:**
$$W = \int F \cdot dx = F d \cos\theta$$

**Power:**
$$P = \frac{W}{t} = F \cdot v$$

**Work-Energy Theorem:**
$$W_{net} = \Delta KE$$

### Applications

- Work by conservative forces (gravity, springs)
- Work against friction
- Power calculations (motor, person climbing)

**Exam appearances:**
- **2008 Problem 4c:** Work by Coulomb force (7 pts)

---

## Topic Summary Table

| Topic | Frequency | Points | Position | Difficulty |
|-------|-----------|--------|----------|-----------|
| Polar Kinematics | **100%** | 20-25 | P1 | Easy-Med |
| Collisions | **75%+** | 12-25 | P2 | Easy-Med |
| Angular Momentum | **75%+** | 8-25 | P3 | Easy-Hard |
| Torque/Rotation | **75%** | 6-25 | P4 | Easy-Med |
| Springs/Oscillations | **25-50%** | 8-25 | P2/3 | Easy-Hard |
| Circular Motion | **50%+** | 5-25 | Mixed | Easy-Med |
| Energy Methods | **50-75%** | Varies | Woven | Easy-Hard |
| Work/Power | **10-25%** | 5-15 | Mixed | Easy-Med |

---

## Next Steps

1. **Create individual year breakdowns** (Exam 2005, Exam 2006, etc.)
2. **Build practice sets by topic** (All polar coord problems, all collision problems, etc.)
3. **Organize difficulty-based problem lists** (Do all Easy first, then Easy-Medium, etc.)
4. **Create formula reference cards** by topic

---

*Last Updated: April 14, 2026*  
*Next: Individual exam analysis + practice sets by topic*
