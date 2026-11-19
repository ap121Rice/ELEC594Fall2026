"""Regenerates figures/latency.pdf (Fig. 3). Numbers are the measurements reported in Tables I and II."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, ORANGE, INK, MUTED, GRID = "#2a78d6", "#eb6834", "#1f1f1e", "#6b6a64", "#e6e5e0"
plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "Nimbus Roman", "DejaVu Serif"],
                     "font.size": 8, "axes.edgecolor": MUTED, "text.color": INK, "pdf.fonttype": 42})

rows = [  # label, ms per 1920x1440 frame
    ("Server GPU (FP16)", 5.2),
    ("iPhone Neural Engine", 23.5),
    ("Colab T4 (original, FP32)", 43.1),
    ("iPhone GPU", 119.4),
    ("iPhone CPU", 145.7),
    ("Server CPU (FP32)", 205.0),
]
fig, ax = plt.subplots(figsize=(3.45, 1.85))
labels, ms = [r[0] for r in rows][::-1], [r[1] for r in rows][::-1]
bars = ax.barh(labels, ms, height=0.62, color=[ORANGE if "Neural" in l else BLUE for l in labels], edgecolor="white", linewidth=1)
for b, v in zip(bars, ms):
    ax.text(v + 4, b.get_y() + b.get_height() / 2, f"{v:g} ms ({1000 / v:.0f} fps)", va="center", fontsize=6.5)
ax.set_xlim(0, 330)
ax.set_xticks([0, 50, 100, 150, 200, 250])
ax.set_xlabel("Time per 1920×1440 frame (ms)")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.xaxis.grid(True, color=GRID, lw=0.6); ax.set_axisbelow(True)
ax.tick_params(axis="y", length=0)
fig.tight_layout(pad=0.2)
fig.savefig("latency.pdf", bbox_inches="tight", pad_inches=0.02)
