"""Resting heart rate distributions for men and women measured from Quer et al. 2020, Fig 2.

Usage:
    python pipelines/digitise/quer_2020_fig2.py

Reads raw/figures/quer_2020_fig2.png (the publisher's 2180 x 1512 image of
Fig 2, CC BY) and writes
metrics/resting_heart_rate/sources/quer_2020_fitbit_fig2_digitised/data.csv.

The figure plots, for each sex, the fraction of individuals at each whole
beat per minute from 40 to 90, with a dashed line at the mean. The curve
height is read at each whole value from 41 to 89, and the mean, SD, and
percentiles are computed from those fractions.
"""

from __future__ import annotations

import numpy as np
from figure import ROOT, load_rgb, near, runs

OUT = ROOT / "metrics" / "resting_heart_rate" / "sources" / "quer_2020_fitbit_fig2_digitised" / "data.csv"
N = {"Male": 34621, "Female": 57836}  # stated in the Fig 2 caption
X_RANGE = (40, 90)  # beats/min at the left and right of the plot frame
Y_TOP = 0.06  # fraction of individuals at the top of the plot frame
PERCENTILES = (2.5, 5, 10, 25, 50, 75, 90, 95, 97.5)
# Each plotted value b is taken to cover resting heart rates from b up to b + 1. The dashed mean
# lines in the figure sit half a beat above the mean of the plotted whole values, which is what
# that reading predicts and what rounding to the nearest beat would not.
BIN_OFFSET = 0.5


def measure():
    rgb = load_rgb("quer_2020_fig2.png")
    black = rgb.sum(axis=2) < 120
    frame_cols = np.flatnonzero(black.mean(axis=0) > 0.6)
    frame_rows = np.flatnonzero(black.mean(axis=1) > 0.6)
    left = np.mean([c for c in frame_cols if c - frame_cols.min() < 12])
    right = np.mean([c for c in frame_cols if frame_cols.max() - c < 12])
    top = np.mean([r for r in frame_rows if r - frame_rows.min() < 12])
    bottom = np.mean([r for r in frame_rows if frame_rows.max() - r < 12])
    px_per_bpm = (right - left) / (X_RANGE[1] - X_RANGE[0])
    px_per_unit = (bottom - top) / Y_TOP
    print(f"frame x {left:.1f} to {right:.1f}, y {top:.1f} to {bottom:.1f}; {px_per_bpm:.2f} px per beat/min; "
          f"one pixel = {1 / px_per_unit:.6f} of individuals")

    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    masks = {
        "Male": near(rgb, (176, 196, 222), 45) & (b > r + 20),
        "Female": near(rgb, (85, 107, 47), 70) & (g > r + 10) & (g > b + 30),
    }
    fractions, mean_lines = {}, {}
    for sex, mask in masks.items():
        mask = mask.copy()
        mask[:, : int(left) + 6] = False
        mask[:, int(right) - 5 :] = False
        mask[: int(top) + 6] = False
        mask[int(bottom) - 5 :] = False
        mask[: int(top + 0.30 * (bottom - top)), int(left + 0.74 * (right - left)) :] = False  # legend
        values = {}
        for bpm in range(X_RANGE[0] + 1, X_RANGE[1]):
            x = round(left + (bpm - X_RANGE[0]) * px_per_bpm)
            segments = runs(mask[:, x - 1 : x + 2].any(axis=1))
            segments = [seg for seg in segments if seg[1] - seg[0] >= 3] or segments
            # The curve is the highest coloured run in the column.
            values[bpm] = (bottom - sum(segments[0]) / 2) / px_per_unit if segments else 0.0
        fractions[sex] = values
        dashes = np.array([len(runs(mask[:, x])) for x in range(mask.shape[1])])
        line_x = np.flatnonzero(dashes >= dashes.max() - 1).mean()
        mean_lines[sex] = X_RANGE[0] + (line_x - left) / px_per_bpm
    return fractions, mean_lines


def summarise(values: dict[int, float]) -> dict[str, float]:
    bpm = np.array(sorted(values), dtype=float)
    share = np.array([values[int(b)] for b in bpm])
    total = share.sum()
    share = share / total
    centre = bpm + BIN_OFFSET
    mean = float((centre * share).sum())
    # Within-bin spread of a one-beat bin adds 1/12 to the variance.
    sd = float(np.sqrt(((centre - mean) ** 2 * share).sum() + 1 / 12))
    out = {"mean": mean, "sd": sd, "_sum": float(total)}
    cumulative = np.concatenate([[0.0], np.cumsum(share)])
    edges = np.concatenate([bpm, [bpm[-1] + 1]])
    for p in PERCENTILES:
        out[f"p{p:g}"] = float(np.interp(p / 100, cumulative, edges))  # linear within each one-beat bin
    return out


def main() -> None:
    fractions, mean_lines = measure()
    lines = ["sex,age_band,n,statistic,estimate,ci_low,ci_high,locator"]
    stats = {}
    for sex, values in fractions.items():
        stats[sex] = summarise(values)
        s = stats[sex]
        print(f"{sex}: fractions at 41 to 89 sum to {s['_sum']:.4f}; mean {s['mean']:.2f} "
              f"(dashed line in the figure at {mean_lines[sex]:.2f}); sd {s['sd']:.2f}; "
              f"p2.5 {s['p2.5']:.1f}, p97.5 {s['p97.5']:.1f}")
        for name, value in s.items():
            if not name.startswith("_"):
                lines.append(f"{sex},All,{N[sex]},{name},{value:.1f},,,Fig 2")
    total = sum(N.values())
    mean = sum(N[k] * stats[k]["mean"] for k in N) / total
    variance = sum(N[k] * (stats[k]["sd"] ** 2 + (stats[k]["mean"] - mean) ** 2) for k in N) / total
    print(f"both sexes combined by the caption's counts: mean {mean:.2f}, sd {np.sqrt(variance):.2f} "
          "(the paper's text gives 65.5 and 7.7)")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
