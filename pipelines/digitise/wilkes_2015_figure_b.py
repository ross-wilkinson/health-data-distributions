"""ITA category counts measured from Wilkes et al. 2015, Figure panel B.

Usage:
    python pipelines/digitise/wilkes_2015_figure_b.py

Reads raw/figures/wilkes_2015_figure_panel_b.png (the bar chart cropped from
page 902 rendered at 600 dpi) and writes
metrics/skin_tone/sources/wilkes_2015_pretoria_ita_categories_digitised/data.csv.

The chart shows the number of participants in each skin category twice: by
ITA (dark bars) and by a device-derived Fitzpatrick type (light bars). Only
the ITA series is written; the other is printed as a check.
"""

from __future__ import annotations

import numpy as np
from figure import ROOT, load_rgb, near, runs

OUT = ROOT / "metrics" / "skin_tone" / "sources" / "wilkes_2015_pretoria_ita_categories_digitised" / "data.csv"
N_PARTICIPANTS = 556  # stated in the paper's Methods
GRID_STEP = 25  # participants between adjacent gridlines
CATEGORIES = ["Very light", "Light", "Intermediate", "Tanned", "Brown", "Dark"]
SERIES = {"ITA": ((57, 90, 104), 60), "Device-derived Fitzpatrick": ((150, 177, 190), 45)}


def measure() -> dict[str, np.ndarray]:
    rgb = load_rgb("wilkes_2015_figure_panel_b.png")
    grey = near(rgb, (225, 225, 225), 30)
    dark = rgb.sum(axis=2) < 150
    # Zero axis: the long dark horizontal line under the bars.
    long_rows = np.flatnonzero(dark[:, 150:1750].mean(axis=1) > 0.9)
    zero = min(r for r in long_rows if r < 1200 and long_rows[long_rows < 1200].max() - r < 8)
    gridlines = np.array([(s + e) / 2 for s, e in runs(grey[: zero - 5, 400])])
    step = float(np.median(np.diff(gridlines)))
    per_participant = step / GRID_STEP
    print(f"zero axis at row {zero}; {len(gridlines)} gridlines, {step:.2f} px apart = {GRID_STEP} participants")
    print(f"{per_participant:.3f} px per participant (one pixel = {1 / per_participant:.2f} participants)")

    ink = (rgb.sum(axis=2) < 600) & ~grey  # anything that is not white or a gridline
    out = {}
    for name, (colour, tolerance) in SERIES.items():
        mask = near(rgb, colour, tolerance)
        columns = (mask[:zero].sum(axis=0) > 5) & mask[zero - 6 : zero - 1].any(axis=0)  # bars reach the axis
        values = []
        for start, end in [(s, e) for s, e in runs(columns) if e - s > 40]:
            lo, hi = start + (end - start) // 4, end - (end - start) // 4
            fill_top = np.median([np.flatnonzero(mask[:zero, k]).min() for k in range(lo, hi)])
            # The bar's outline sits above its fill; walk up through it.
            top = int(fill_top)
            row_is_ink = ink[:zero, lo:hi].mean(axis=1) > 0.8
            while top > 0 and row_is_ink[top - 1]:
                top -= 1
            values.append((zero - top) / per_participant)
        out[name] = np.array(values)
        print(f"{name}: measured {np.round(values, 2).tolist()}; sum {sum(values):.1f}; "
              f"rounded {np.round(values).astype(int).tolist()} sum {int(np.round(values).sum())}")
    return out


def main() -> None:
    measured = measure()["ITA"]
    counts = np.round(measured).astype(int)
    if len(counts) != len(CATEGORIES):
        raise SystemExit(f"expected {len(CATEGORIES)} ITA bars, found {len(counts)}")
    print(f"ITA counts sum to {counts.sum()} against {N_PARTICIPANTS} participants stated in the paper")
    lines = ["category,n,statistic,estimate,ci_low,ci_high,locator"]
    for category, count in zip(CATEGORIES, counts):
        lines.append(f"{category},{N_PARTICIPANTS},proportion,{count / counts.sum():.3f},,,Figure panel B")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
