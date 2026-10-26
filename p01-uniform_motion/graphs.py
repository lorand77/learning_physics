"""Generate the graphs for uniform_motion_1d.md.

Run from the repo root:  .venv/bin/python p01-uniform_motion/graphs.py
"""

from pathlib import Path

import matplotlib.pyplot as plt

OUT = Path(__file__).parent

# Worked example: the car starts at x0 = 4 m and moves at v = 3 m/s
X0 = 4  # m
V = 3  # m/s
T_END = 5  # s

LINE = "#2563eb"
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


def x_of_t(t):
    return X0 + V * t


def position_graph():
    fig, ax = plt.subplots(figsize=(6.4, 4))
    ax.plot([0, T_END], [x_of_t(0), x_of_t(T_END)], color=LINE, lw=2)
    ax.axhline(0, color=MUTED, lw=1)

    # Intercept: starting position
    ax.plot(0, X0, "o", color=LINE, ms=8, clip_on=False)
    ax.annotate(r"$x_0 = 4$ m", (0, X0), xytext=(10, -4), textcoords="offset points",
                va="top")

    # Slope triangle between t = 2 s and t = 3 s
    t1, t2 = 2, 3
    ax.plot([t1, t2], [x_of_t(t1)] * 2, color=INK, lw=1, ls="--")
    ax.plot([t2, t2], [x_of_t(t1), x_of_t(t2)], color=INK, lw=1, ls="--")
    ax.text((t1 + t2) / 2, x_of_t(t1) - 0.8, r"$\Delta t = 1$ s", ha="center", va="top")
    ax.text(t2 + 0.1, (x_of_t(t1) + x_of_t(t2)) / 2, r"$\Delta x = 3$ m", va="center")
    ax.text(2.8, 3, r"slope $= \dfrac{\Delta x}{\Delta t} = v = 3$ m/s")

    # Reaching x = 16 m
    t_16 = (16 - X0) / V
    ax.plot(t_16, 16, "o", color=LINE, ms=8)
    ax.annotate(r"$x = 16$ m when $t = 4$ s", (t_16, 16),
                xytext=(-12, 6), textcoords="offset points", ha="right", va="bottom")

    ax.set_yticks(range(0, 21, 4))
    ax.set(xlim=(0, T_END), ylim=(0, 22),
           xlabel="time $t$ (s)", ylabel="position $x$ (m)",
           title=r"Position vs time: $x(t) = 4 + 3\,t$")
    fig.tight_layout()
    fig.savefig(OUT / "x_vs_t.svg")


def velocity_graph():
    fig, ax = plt.subplots(figsize=(6.4, 4))
    ax.plot([0, T_END], [V, V], color=LINE, lw=2)
    ax.axhline(0, color=MUTED, lw=1)
    ax.text(T_END - 0.1, V + 0.2, r"$v = 3$ m/s", ha="right", va="bottom")

    # Area between the line and the t-axis from t = 0 to t = 2 s is the displacement
    t_a = 2
    ax.fill_between([0, t_a], [V, V], 0, color=LINE, alpha=0.15, lw=0)
    ax.text(t_a / 2, V / 2, "area $= v\\,\\Delta t = (3)(2)$\n$= 6$ m $= \\Delta x$",
            ha="center", va="center")

    ax.set(xlim=(0, T_END), ylim=(-1, 5),
           xlabel="time $t$ (s)", ylabel="velocity $v$ (m/s)",
           title="Velocity vs time: a horizontal line")
    fig.tight_layout()
    fig.savefig(OUT / "v_vs_t.svg")


if __name__ == "__main__":
    position_graph()
    velocity_graph()
