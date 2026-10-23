# Uniform motion in one dimension

"Uniform" motion means the **velocity is constant**: the same speed, always in the same direction. Because nothing about the motion changes over time, people sometimes also call it "steady." The object covers equal distances in equal time intervals.

## The setup

- Motion happens along a single axis, which we call $x$.
- $x(t)$ is the position at time $t$, measured from some chosen origin.
- $v$ is the velocity. It is a signed number: positive means moving toward +x, negative means moving toward −x.
- $a$ is the acceleration.

## The equations

### 1. Velocity is constant

$$v(t) = v = \text{const}$$

This is the definition of uniform motion.

### 2. Acceleration is zero

$$a = \frac{dv}{dt} = 0$$

The velocity never changes, so its rate of change is zero. By Newton's 2nd law ($F_\text{net} = ma$), this means the **net force on the object is zero**. Uniform motion is Newton's 1st law in action.

### 3. Position is a linear function of time

$$x(t) = x_0 + v t$$

- $x_0$ is the position at $t = 0$, the starting point.
- $v t$ is how far the object has moved since then.

This comes from integrating $\dfrac{dx}{dt} = v$:

$$\int_{x_0}^{x} dx' = \int_0^t v dt' \quad\Rightarrow\quad x - x_0 = v t$$

If the clock starts at some time $t_0$ instead of 0:

$$x(t) = x_0 + v (t - t_0)$$

### 4. Displacement and velocity

$$\Delta x = v \Delta t \qquad\Longleftrightarrow\qquad v = \frac{\Delta x}{\Delta t}$$

When velocity is constant, the **average velocity equals the instantaneous velocity** at every moment. That is why the simple "distance ÷ time" formula is exact here. For non-uniform motion it only gives an average.

## Graphs

| Graph | Shape | What it tells you |
|---|---|---|
| $x$ vs $t$ | Straight line | The slope is *v*, and the intercept is $x_0$. A steeper line means faster motion. A downward slope means *v* < 0. |
| $v$ vs $t$ | Horizontal line at height *v* | The **area under it**, $v \Delta t$, is the displacement Δx. |
| $a$ vs $t$ | Flat line at 0 | No acceleration. |

## Worked example

A car is at $x_0 = 20\text{ m}$ at $t = 0$ and moves at $v = -5\text{ m/s}$ (toward −x).

- Position: $x(t) = 20 - 5t$
- At $t = 3\text{ s}$: $x = 20 - 15 = 5\text{ m}$
- It reaches the origin when $0 = 20 - 5t$, so $t = 4\text{ s}$.

## Common pitfalls

- **Distance vs. displacement:** Δx can be negative, but distance traveled is $|v| \Delta t$. In uniform motion the direction never reverses, so distance $= |\Delta x|$.
- **Speed vs. velocity:** speed is $|v|$, and velocity carries a sign.
- **Uniform vs. uniformly accelerated:** in uniformly accelerated motion it's the *acceleration* that stays constant, not the velocity. That case uses $x = x_0 + v_0 t + \tfrac12 a t^2$. Uniform motion is the special case where $a = 0$.
