"""Simulate uniform motion step by step: x = x + v * dt.

Prints the steps for a coarse dt and plots the simulated points against the
exact solution x(t) = x0 + v * t.

Run from the repo root:  .venv/bin/python p01-uniform_motion/simulate.py
"""

from pathlib import Path

import matplotlib.pyplot as plt

OUT = Path(__file__).parent

# Same car as the worked example
X0 = 4  # m
V = 3  # m/s
T_END = 5  # s

LINE = "#2563eb"
RED = "#dc2626"
INK = "#1f2937"
MUTED = "#6b7280"
GRID = "#e5e7eb"

plt.rcParams.update({
    "font.size": 11,
    "text.color": INK,
    "axes.labelcolor": INK,
    "axes.edgecolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.grid": True,
    "grid.color": GRID,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.facecolor": "white",  # stays readable in GitHub dark mode
})


def simulate(x0, v, dt, t_end):
    """Step the motion forward from t = 0 to t_end and return the times and positions."""
    t = 0
    x = x0
    ts, xs = [t], [x]
    # Count the steps instead of testing t < t_end: after adding 0.1 a hundred times,
    # t is 9.99999999999998, so a while loop would run one extra step.
    for _ in range(round(t_end / dt)):
        x = x + v * dt
        t = t + dt
        ts.append(t)
        xs.append(x)
    return ts, xs


def print_table(ts, xs, dt):
    print(f"dt = {dt} s")
    print(f"{'step':>4}  {'t (s)':>6}  {'x (m)':>7}  {'exact (m)':>9}")
    for n, (t, x) in enumerate(zip(ts, xs)):
        print(f"{n:>4}  {t:>6.2f}  {x:>7.2f}  {X0 + V * t:>9.2f}")


def simulation_graph():
    fig, ax = plt.subplots(figsize=(6.4, 4))
    ax.plot([0, T_END], [X0, X0 + V * T_END], color=RED, lw=1.5,
            label=r"exact: $x = x_0 + v\,t$")

    ts, xs = simulate(X0, V, dt=0.1, t_end=T_END)
    ax.plot(ts, xs, "o", color=LINE, ms=3.5, label=r"$\Delta t = 0.1$ s")

    ax.set_yticks(range(0, 21, 4))
    ax.set(xlim=(0, T_END), ylim=(0, 22),
           xlabel="time $t$ (s)", ylabel="position $x$ (m)",
           title=r"Simulation: $x \leftarrow x + v\,\Delta t$")
    ax.legend(loc="upper left", frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / "simulation.svg")


if __name__ == "__main__":
    ts, xs = simulate(X0, V, dt=0.1, t_end=T_END)
    print_table(ts, xs, dt=0.1)
    simulation_graph()
