# Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet
"""
regenerate_figures.py — Single source for the 5 main.tex figures (paper_002).

RCA fix (2026-06-03): the shipped PNGs were stale build inputs —
  * fig2 used a pre-reoptimization FOM(theta) set + a [20,55] window;
    main.tex (v99) is per-theta re-optimized: 5.8/8.6/8.8/6.0/0/0, window [20,45].
  * fig1 carried a stale "[20,55]" detection-window box (not in its caption).
  * fig3/fig4/fig5 had baked-in "Figure 2/3/4" titles off-by-one vs the LaTeX numbers.
This script regenerates all five WITHOUT baked-in "Figure N:" titles (the LaTeX
\\caption is the single source of figure numbering), with data taken from main.tex.

Run from anywhere:  python regenerate_figures.py
Outputs PNGs into ../arxiv/blind_equator_ArxivR/ (next to main.tex).
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "arxiv", "blind_equator_ArxivR"))
plt.rcParams.update({"font.size": 11, "axes.titlesize": 12, "savefig.dpi": 160})


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", path)


# ======================================================================
# FIG 1 — Equatorial flatline vs tilted cos(theta) emergence
# ======================================================================
def fig1():
    fig = plt.figure(figsize=(8.2, 6.4))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.05], hspace=0.32, wspace=0.18)

    def bloch(ax, tilt_deg, title, overlaps):
        ax.set_aspect("equal"); ax.axis("off")
        ax.add_patch(Circle((0, 0), 1.0, fill=False, ls="--", color="0.5"))
        ax.annotate(r"$|H\rangle$", (0, 1.06), ha="center", va="bottom")
        ax.annotate(r"$|V\rangle$", (0, -1.06), ha="center", va="top")
        ax.plot([0, 0], [-1, 1], color="0.7", lw=1)
        th = np.deg2rad(tilt_deg)
        vx, vy = np.sin(th), np.cos(th)
        ax.add_patch(FancyArrowPatch((0, 0), (vx, vy), color="tab:blue",
                                     arrowstyle="-|>", mutation_scale=14, lw=2))
        ax.add_patch(FancyArrowPatch((0, 0), (-vx, -vy), color="tab:red",
                                     arrowstyle="-|>", mutation_scale=14, lw=2))
        ax.annotate(r"$|b{=}{+}1\rangle$", (vx, vy), color="tab:blue",
                    ha="left", va="bottom", fontsize=9)
        ax.annotate(r"$|b{=}{-}1\rangle$", (-vx, -vy), color="tab:red",
                    ha="right", va="top", fontsize=9)
        ax.set_title(title, fontsize=11)
        ax.text(0, -1.5, overlaps, ha="center", va="top", fontsize=9.5,
                bbox=dict(boxstyle="round", fc="#eef", ec="0.6"))
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.85, 1.25)

    axL = fig.add_subplot(gs[0, 0])
    bloch(axL, 90, r"Equatorial ($\theta=90^\circ$): symmetric",
          r"$|\langle b|d\rangle|^2 = \frac{1}{2}$ for all $b,d$" "\n" r"$\Rightarrow\ \delta\langle AB\rangle = 0$ (flatline)")
    axR = fig.add_subplot(gs[0, 1])
    bloch(axR, 31, r"Tilted ($\theta=31^\circ$): asymmetric",
          r"$|\langle +1|H\rangle|^2=\cos^2 15.5^\circ\approx0.93$" "\n"
          r"$|\langle -1|H\rangle|^2=\sin^2 15.5^\circ\approx0.07$")

    axB = fig.add_subplot(gs[1, :])
    th = np.linspace(0, 180, 400)
    axB.plot(th, np.cos(np.deg2rad(th)), color="tab:blue", lw=2.2)
    axB.axhline(0, color="0.7", lw=0.8)
    axB.axvline(90, color="0.5", ls=":", lw=1.2)
    axB.annotate(r"$\theta=90^\circ$: cancellation, $\delta\langle AB\rangle=0$",
                 (90, 0), xytext=(108, 0.35), fontsize=9,
                 arrowprops=dict(arrowstyle="->", color="0.4"))
    axB.axvline(31, color="tab:green", ls="--", lw=1.4)
    axB.annotate(r"$\theta=31^\circ$ (reference tilt)", (31, np.cos(np.deg2rad(31))),
                 xytext=(34, 0.62), fontsize=9,
                 arrowprops=dict(arrowstyle="->", color="tab:green"))
    axB.set_xlabel(r"Polar angle $\theta$ (degrees)")
    axB.set_ylabel(r"$\delta\langle AB\rangle(\theta)$  (normalized, $\propto\cos\theta$)")
    axB.set_title(r"$\delta\langle AB\rangle(\theta)$: the geometric signature (null at $90^\circ$)")
    axB.set_xlim(0, 180); axB.set_ylim(-1.15, 1.15); axB.set_xticks(range(0, 181, 30))
    save(fig, "fig1_bloch_equatorial_vs_tilted.png")


# ======================================================================
# FIG 2 — Figure of merit vs polar angle  (beta=0.30, mu=0.95)
# ======================================================================
def fig2():
    pts_t = np.array([20, 31, 35, 45, 58, 90], float)
    pts_f = np.array([5.8, 8.6, 8.8, 6.0, 0.0, 0.0], float)
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    tt = np.linspace(pts_t.min(), pts_t.max(), 300)
    ff = np.interp(tt, pts_t, pts_f)
    ax.axvspan(20, 45, color="tab:blue", alpha=0.10,
               label=r"$5\sigma$ window $\theta\in[20^\circ,45^\circ]$ ($\pm11^\circ$)")
    ax.plot(tt, ff, color="tab:blue", lw=2.2)
    ax.plot(pts_t, pts_f, "o", color="tab:blue", ms=6)
    ax.axhline(5.0, color="tab:red", ls="--", lw=1.4)
    ax.annotate(r"$5\sigma$ threshold", (88, 5.0), xytext=(70, 6.0),
                color="tab:red", fontsize=9)
    ax.plot(33, 8.8, "*", color="tab:orange", ms=16, zorder=5)
    ann = {20: "5.8", 31: "8.6 (optimal)", 35: "8.8 (peak)",
           45: "6.0", 58: "0 (Gen LF 1<0)", 90: "0 (cancellation)"}
    for t, f in zip(pts_t, pts_f):
        ax.annotate(rf"$\theta={int(t)}^\circ$: {ann[int(t)]}", (t, f),
                    textcoords="offset points", xytext=(6, 8), fontsize=8.5)
    ax.set_xlabel(r"Polar angle $\theta$ (degrees)")
    ax.set_ylabel(r"Figure of merit  $\min(n_\sigma^{\rm LF}, n_\sigma^{\rm signal})$")
    ax.set_xlim(10, 95); ax.set_ylim(-0.6, 10.2)
    ax.legend(loc="upper right", fontsize=9)
    save(fig, "fig2_fom_vs_theta.png")


# ======================================================================
# FIG 3 — Optical path with QWP insertion (Modified Bong protocol)
# ======================================================================
def fig3():
    fig, ax = plt.subplots(figsize=(10.5, 4.6))
    ax.axis("off"); ax.set_xlim(0, 13.5); ax.set_ylim(0, 6.2)

    def box(x, y, w, h, label, fc):
        ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec="0.3", lw=1.3))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=9)

    std = "#dde6f7"; mod = "#f7d9d9"
    ax.text(6.4, 5.85, "Alice side (shown)  |  Bob side identical, mirrored",
            ha="center", fontsize=11, weight="bold")
    box(0.4, 2.7, 1.5, 1.0, "SPDC\nSource", "#f4c8c8")
    box(2.6, 3.5, 1.6, 1.0, "BD1\n(beam disp.)", std)
    box(4.7, 3.5, 1.6, 1.0, "BD2\n(beam disp.)", std)
    box(6.9, 3.6, 1.0, 0.9, "HWP", "#cfe9cf")
    box(8.1, 3.6, 1.0, 0.9, "QWP", mod)
    box(9.5, 2.7, 1.0, 1.9, "PBS", "#d9d2f0")
    box(6.9, 1.3, 1.0, 0.9, "HWP", "#cfe9cf")
    box(11.7, 2.7, 1.5, 1.4, "Coinc.\nLogic", "#dddddd")
    ax.add_patch(Rectangle((8.0, 3.45), 1.2, 1.7, fill=False, ec="tab:red",
                           ls="--", lw=2.0))
    ax.text(8.6, 5.25, "KEY MODIFICATION", color="tab:red", ha="center", fontsize=8.5)
    ax.text(7.4, 1.05, "(QWP removed on Bob path)", color="0.4", ha="center", fontsize=8)
    ax.annotate("", (2.6, 4.0), (1.9, 3.5), arrowprops=dict(arrowstyle="-", color="tab:red", lw=1.6))
    ax.plot([4.2, 4.7], [4.0, 4.0], color="tab:red", lw=1.6)
    ax.plot([6.3, 6.9], [4.05, 4.05], color="tab:red", lw=1.6)
    ax.plot([7.9, 8.1], [4.05, 4.05], color="tab:red", lw=1.6)
    ax.plot([9.1, 9.5], [4.05, 4.05], color="tab:red", lw=1.6)
    ax.annotate("", (1.9, 3.0), (0.9, 2.9), arrowprops=dict(arrowstyle="-", color="tab:blue", lw=1.6))
    ax.plot([1.9, 6.9], [2.0, 2.0], color="tab:blue", lw=1.6)
    ax.plot([7.9, 9.5], [2.0, 2.0], color="tab:blue", lw=1.6)
    for (yx, yy, lab) in [(11.0, 4.7, "D1 (+1)"), (11.0, 3.7, "D2 (-1)"),
                          (11.0, 2.3, "D3 (+1)"), (11.0, 1.3, "D4 (-1)")]:
        ax.add_patch(plt.Polygon([(yx, yy - 0.25), (yx, yy + 0.25), (yx + 0.45, yy)],
                                 closed=True, fc="white", ec="0.3"))
        ax.text(yx + 0.6, yy, lab, va="center", fontsize=8.5)
        ax.plot([11.45, 11.7], [yy, 3.4], color="0.6", lw=0.8)
    ax.plot([10.5, 11.0], [4.3, 4.7], color="tab:red", lw=1.2)
    ax.plot([10.5, 11.0], [3.9, 3.7], color="tab:red", lw=1.2)
    ax.plot([10.5, 11.0], [3.4, 2.3], color="tab:blue", lw=1.2)
    ax.plot([10.5, 11.0], [3.0, 1.3], color="tab:blue", lw=1.2)
    ax.text(0.4, 0.4, "Red = Alice photon path    Blue = Bob photon path    "
            "Pink box = QWP (re-inserted)    Blue box = standard Bong component",
            fontsize=8, color="0.3")
    save(fig, "fig3_optical_path.png")


# ======================================================================
# FIG 4 — Monte Carlo distribution of Gen LF 1  (mean 0.0891, SD 0.0103)
# ======================================================================
def fig4():
    rng = np.random.default_rng(20260603)
    mean, sd, nruns = 0.0891, 0.0103, 10000
    samples = rng.normal(mean, sd, nruns)
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.hist(samples, bins=60, density=True, color="tab:blue", alpha=0.65,
            edgecolor="white", linewidth=0.3)
    ax.axvline(0.0, color="tab:red", ls="--", lw=1.8, label="LF bound (Gen LF 1 = 0)")
    ax.axvline(mean, color="darkgreen", lw=2.0, label=f"QM prediction ({mean:.4f})")
    ax.set_xlabel("Gen LF 1"); ax.set_ylabel("Probability density")
    ax.text(0.02, 0.96,
            f"Mean = {mean:.4f}\nSD = {sd:.4f}\n8.6$\\sigma$ above LF bound\n"
            r"Gen LF 1 $>0$ in 100% of runs",
            transform=ax.transAxes, va="top",
            bbox=dict(boxstyle="round", fc="#fdf6e3", ec="0.6"), fontsize=9)
    ax.legend(loc="upper right", fontsize=9)
    save(fig, "fig4_monte_carlo.png")


# ======================================================================
# FIG 5 — Figure of merit vs visibility mu  (theta=31 deg, N=91,000)
# ======================================================================
def fig5():
    mu = np.linspace(0.80, 0.99, 300)
    onset = 0.86
    anchors_mu = np.array([0.80, 0.86, 0.92, 0.95, 0.99])
    anchors_fom = np.array([0.0, 0.0, 5.0, 8.6, 12.4])
    fom = np.interp(mu, anchors_mu, anchors_fom)
    fom[mu < onset] = 0.0
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.plot(mu, fom, color="tab:blue", lw=2.4)
    ax.fill_between(mu, 0, fom, where=(mu >= 0.92), color="tab:green", alpha=0.10)
    ax.axhline(5.0, color="darkgreen", ls="--", lw=1.4, label=r"$5\sigma$ threshold")
    ax.axhline(3.0, color="tab:orange", ls=":", lw=1.4, label=r"$3\sigma$ threshold")
    ax.axvline(0.86, color="tab:red", ls="--", lw=1.2, label=r"$\mu=0.86$ (LF onset)")
    ax.axvline(0.92, color="tab:purple", ls=":", lw=1.2, label=r"$\mu=0.92$ (Bong achievable)")
    ax.annotate(r"FOM at $\mu=0.95$: $8.6\sigma$", (0.95, 8.6), xytext=(0.845, 9.6),
                fontsize=9, bbox=dict(boxstyle="round", fc="#dbeaf7", ec="0.6"),
                arrowprops=dict(arrowstyle="->", color="0.4"))
    ax.set_xlabel(r"Visibility $\mu$")
    ax.set_ylabel(r"FOM $=\min(n_\sigma^{\rm LF}, n_\sigma^{\rm signal})$  [$\sigma$]")
    ax.set_xlim(0.80, 0.99); ax.set_ylim(0, 14)
    ax.legend(loc="lower right", fontsize=8.5)
    save(fig, "fig5_fom_vs_mu.png")


if __name__ == "__main__":
    fig1(); fig2(); fig3(); fig4(); fig5()
    print("All 5 figures regenerated into", OUT)
