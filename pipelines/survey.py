"""Design-based descriptive statistics for complex survey samples.

A national survey such as NHANES does not sample people with equal
probability, and it samples them in geographic clusters. Point estimates
therefore use the sampling weights, and intervals come from resampling whole
clusters (primary sampling units) within strata rather than individuals.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

PERCENTILES = (1, 2.5, 5, 10, 25, 50, 75, 90, 95, 97.5, 99)


def percentile_name(p: float) -> str:
    return f"p{p:g}"


def replicate_weights(
    strata: np.ndarray, psu: np.ndarray, weights: np.ndarray, *, n_rep: int = 500, seed: int = 0
) -> np.ndarray:
    """Rao-Wu rescaled bootstrap weights, shape (n_rows, n_rep).

    Within each stratum with n PSUs, each replicate draws n - 1 PSUs with
    replacement and scales a PSU's weights by n / (n - 1) times the number of
    times it was drawn. Build these once on the full sample and reuse them for
    every subgroup, so subgroup intervals reflect the whole design.
    """
    rng = np.random.default_rng(seed)
    out = np.empty((weights.size, n_rep), dtype=np.float32)
    for stratum in np.unique(strata):
        in_stratum = np.flatnonzero(strata == stratum)
        units, unit_index = np.unique(psu[in_stratum], return_inverse=True)
        n = units.size
        if n < 2:
            raise ValueError(f"stratum {stratum} has a single PSU")
        drawn = rng.integers(0, n, (n_rep, n - 1))
        times_drawn = np.stack([np.bincount(row, minlength=n) for row in drawn])  # (n_rep, n)
        factor = times_drawn * (n / (n - 1))
        out[in_stratum] = weights[in_stratum, None] * factor.T[unit_index]
    return out


def weighted_quantiles(values: np.ndarray, weights: np.ndarray, probs: np.ndarray) -> np.ndarray:
    """Inverse of the weighted empirical CDF: the smallest value whose
    cumulative weight share reaches each probability.

    `values` must be sorted ascending. `weights` may be (n,) or (n, n_rep);
    the result is (n_probs,) or (n_probs, n_rep).
    """
    cumulative = np.cumsum(weights, axis=0, dtype=np.float64)
    share = cumulative / cumulative[-1]
    if share.ndim == 1:
        return values[np.searchsorted(share, probs, side="left").clip(max=values.size - 1)]
    reached = share[None, :, :] >= np.asarray(probs)[:, None, None] - 1e-12
    return values[reached.argmax(axis=1)]


def describe(
    values: np.ndarray,
    weights: np.ndarray,
    replicates: np.ndarray,
    *,
    percentiles: tuple[float, ...] = PERCENTILES,
    confidence: float = 0.95,
) -> pd.DataFrame:
    """Weighted mean, SD, and percentiles with replicate-based intervals.

    Returns one row per statistic: `statistic`, `estimate`, `ci_low`, `ci_high`.
    """
    order = np.argsort(values, kind="stable")
    x = values[order].astype(float)
    w = weights[order].astype(float)
    reps = replicates[order].astype(np.float64)
    probs = np.asarray(percentiles) / 100

    def mean_sd(weight):
        total = weight.sum(axis=0)
        mean = (x[:, None] * weight).sum(axis=0) / total if weight.ndim == 2 else (x * weight).sum() / total
        centred = (x[:, None] - mean) ** 2 if weight.ndim == 2 else (x - mean) ** 2
        return mean, np.sqrt((centred * weight).sum(axis=0) / total)

    mean, sd = mean_sd(w)
    rep_mean, rep_sd = mean_sd(reps)
    estimates = np.concatenate([[mean, sd], weighted_quantiles(x, w, probs)])
    draws = np.vstack([rep_mean, rep_sd, weighted_quantiles(x, reps, probs)])

    tail = (1 - confidence) / 2
    low, high = np.quantile(draws, [tail, 1 - tail], axis=1)
    names = ["mean", "sd"] + [percentile_name(p) for p in percentiles]
    return pd.DataFrame({"statistic": names, "estimate": estimates, "ci_low": low, "ci_high": high})


def category_proportions(
    codes: np.ndarray,
    weights: np.ndarray,
    replicates: np.ndarray,
    categories: tuple,
    *,
    confidence: float = 0.95,
) -> pd.DataFrame:
    """Weighted share of each category with replicate-based intervals.

    `codes` holds one category per person; every person must be in one of
    `categories`. Returns one row per category, in the order given and including
    categories nobody falls in: `category`, `estimate`, `ci_low`, `ci_high`.
    """
    w = weights.astype(float)
    reps = replicates.astype(np.float64)
    total = w.sum()
    rep_total = reps.sum(axis=0)
    estimates, draws = [], []
    for category in categories:
        is_category = codes == category
        estimates.append(w[is_category].sum() / total)
        draws.append(reps[is_category].sum(axis=0) / rep_total)
    tail = (1 - confidence) / 2
    low, high = np.quantile(np.vstack(draws), [tail, 1 - tail], axis=1)
    return pd.DataFrame(
        {"category": list(categories), "estimate": estimates, "ci_low": low, "ci_high": high}
    )
