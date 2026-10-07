"""Shared helpers for measuring values off a published chart image.

A measurement locates the axis in pixels (gridlines or the plot frame), then
converts the pixel position of a bar top or a curve to data units. Every
script that uses these prints its own calibration and internal checks, and
those go into the source's evidence.md.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
FIGURES = ROOT / "raw" / "figures"


def load_rgb(name: str) -> np.ndarray:
    path = FIGURES / name
    if not path.exists():
        raise SystemExit(f"missing figure image: {path} (see pipelines/digitise/README.md)")
    return np.asarray(Image.open(path).convert("RGB")).astype(int)


def runs(mask: np.ndarray) -> list[tuple[int, int]]:
    """Start and end (inclusive) of each run of True in a 1-D mask."""
    idx = np.flatnonzero(mask)
    if idx.size == 0:
        return []
    breaks = np.flatnonzero(np.diff(idx) > 1)
    return list(zip(np.r_[idx[0], idx[breaks + 1]], np.r_[idx[breaks], idx[-1]]))


def near(rgb: np.ndarray, colour: tuple[int, int, int], tolerance: int) -> np.ndarray:
    """Pixels whose summed absolute RGB difference from `colour` is within `tolerance`."""
    return np.abs(rgb - np.array(colour)).sum(axis=2) <= tolerance
