import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipelines"))

from survey import describe, replicate_weights, weighted_quantiles


def test_equal_weights_match_numpy_inverted_cdf():
    rng = np.random.default_rng(0)
    x = np.sort(rng.normal(70, 12, 501))
    probs = np.array([0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99])
    got = weighted_quantiles(x, np.ones(x.size), probs)
    assert got == pytest.approx(np.quantile(x, probs, method="inverted_cdf"))


def test_weights_act_like_repeated_observations():
    x = np.array([1.0, 2.0, 3.0, 4.0])
    weights = np.array([1, 5, 1, 3])
    expanded = np.repeat(x, weights)
    probs = np.array([0.1, 0.5, 0.7, 0.9])
    assert weighted_quantiles(x, weights.astype(float), probs) == pytest.approx(
        np.quantile(expanded, probs, method="inverted_cdf")
    )


def test_vectorised_quantiles_match_one_at_a_time():
    rng = np.random.default_rng(1)
    x = np.sort(rng.normal(size=300))
    weights = rng.uniform(0.5, 3, (300, 7))
    probs = np.array([0.05, 0.5, 0.95])
    together = weighted_quantiles(x, weights, probs)
    for j in range(7):
        assert together[:, j] == pytest.approx(weighted_quantiles(x, weights[:, j], probs))


def design(rng, n_strata=15, per_psu=120):
    strata = np.repeat(np.arange(n_strata), 2 * per_psu)
    psu = np.tile(np.repeat([1, 2], per_psu), n_strata)
    cluster_effect = rng.normal(0, 3, (n_strata, 2))[strata, psu - 1]
    values = 72 + cluster_effect + rng.normal(0, 12, strata.size)
    weights = rng.uniform(1000, 5000, strata.size)
    return strata, psu, values, weights


def test_replicates_keep_the_weighted_total_on_average():
    strata, psu, _, weights = design(np.random.default_rng(2))
    reps = replicate_weights(strata, psu, weights, n_rep=2000)
    assert reps.sum(axis=0).mean() == pytest.approx(weights.sum(), rel=0.01)
    # With two PSUs per stratum, each replicate keeps exactly one of them at double weight.
    assert set(np.unique(np.round(reps[:, 0] / weights, 6))) == {0.0, 2.0}


def test_bootstrap_variance_of_a_total_matches_the_textbook_formula():
    strata, psu, values, weights = design(np.random.default_rng(3))
    reps = replicate_weights(strata, psu, weights, n_rep=4000).astype(float)
    bootstrap = (reps * values[:, None]).sum(axis=0).var()
    # Stratified design, two PSUs per stratum: variance of the total is the
    # sum over strata of the squared difference between the two PSU totals.
    textbook = 0.0
    for s in np.unique(strata):
        totals = [(weights * values)[(strata == s) & (psu == p)].sum() for p in (1, 2)]
        textbook += (totals[0] - totals[1]) ** 2
    assert bootstrap == pytest.approx(textbook, rel=0.08)


def test_describe_reports_estimates_inside_their_intervals():
    strata, psu, values, weights = design(np.random.default_rng(4))
    reps = replicate_weights(strata, psu, weights)
    table = describe(values, weights, reps).set_index("statistic")
    assert table.loc["mean", "estimate"] == pytest.approx(np.average(values, weights=weights))
    assert (table["ci_low"] <= table["estimate"]).all()
    assert (table["estimate"] <= table["ci_high"]).all()
    assert table.loc["p5", "estimate"] < table.loc["p50", "estimate"] < table.loc["p95", "estimate"]


def test_clustering_widens_the_interval_on_the_mean():
    strata, psu, values, weights = design(np.random.default_rng(5))
    reps = replicate_weights(strata, psu, weights)
    row = describe(values, weights, reps).set_index("statistic").loc["mean"]
    naive_half_width = 1.96 * values.std() / np.sqrt(values.size)
    assert (row["ci_high"] - row["ci_low"]) / 2 > 1.5 * naive_half_width
