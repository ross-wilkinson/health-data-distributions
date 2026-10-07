"""Validation of the bar-chart measuring method against known values.

Usage:
    python pipelines/digitise/ohagan_2025_figure1_check.py

O'Hagan et al. 2025, Figure 1 panels A and B, plot the share of 4,292 people
at each Monk Skin Tone point and each dermatologist-rated Fitzpatrick type.
The underlying SCIN dataset is public, so the true shares are known. This
script measures the bars from raw/figures/ohagan_2025_figure1_ab.png and
prints them beside the shares computed from raw/scin/. It writes no data.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from figure import ROOT, load_rgb, runs

TOP = 60  # rows below the panel titles
PANELS = {"A: Monk Skin Tone, US annotator": (190, 830), "B: Fitzpatrick, dermatologist": (1240, 1920)}


def measure(rgb: np.ndarray, x_lo: int, x_hi: int) -> np.ndarray:
    grey = rgb[:, x_lo:x_hi].mean(axis=2)
    # Gridlines: rows that are light grey across much of the panel width.
    light = (grey[TOP:1010] > 200) & (grey[TOP:1010] < 245)
    lines = np.array([(s + e) / 2 + TOP for s, e in runs(light.mean(axis=1) > 0.25)])
    step = float(np.median(np.diff(lines)))
    per_point = step / 5  # gridlines are 5 percentage points apart
    zero = lines.max()
    dark = grey[TOP : round(zero)] < 130
    bars = [(a, b) for a, b in runs(dark.sum(axis=0) >= 1) if b - a > 15]
    values = []
    for start, end in bars:
        middle = dark[:, start + (end - start) // 4 : end - (end - start) // 4 + 1]
        values.append(np.median(middle.sum(axis=0)) / per_point)
    return np.array(values)


def truth() -> dict[str, np.ndarray]:
    cases = pd.read_csv(ROOT / "raw" / "scin" / "scin_cases.csv", dtype=str)
    labels = pd.read_csv(ROOT / "raw" / "scin" / "scin_labels.csv", dtype=str)
    data = cases.merge(labels, on="case_id")
    monk = data["monk_skin_tone_label_us"]
    fitzpatrick = data["dermatologist_fitzpatrick_skin_type_label_1"]
    subset = monk.notna() & data["monk_skin_tone_label_india"].notna() & fitzpatrick.notna()
    print(f"cases with a dermatologist Fitzpatrick label and both Monk labels: {subset.sum():,}")

    def share(column, order):
        return (column[subset].value_counts().reindex(order, fill_value=0) / subset.sum() * 100).to_numpy()

    return {
        "A: Monk Skin Tone, US annotator": share(monk, [str(i) for i in range(1, 11)]),
        "B: Fitzpatrick, dermatologist": share(fitzpatrick, [f"FST{i}" for i in range(1, 7)]),
    }


def main() -> None:
    rgb = load_rgb("ohagan_2025_figure1_ab.png")
    known = truth()
    for name, (x_lo, x_hi) in PANELS.items():
        measured = measure(rgb, x_lo, x_hi)
        true = known[name][: len(measured)]
        error = measured - true
        print(f"\n{name}: {len(measured)} bars measured")
        print("  measured:", np.round(measured, 2).tolist())
        print("  true:    ", np.round(true, 2).tolist())
        print(f"  largest error {np.abs(error).max():.2f} points; mean error {error.mean():+.2f} points")


if __name__ == "__main__":
    main()
