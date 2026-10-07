"""Checks on category_proportions and on the NHANES 2003-2004 Fitzpatrick data file."""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipelines"))

from survey import category_proportions

DATA = (
    Path(__file__).resolve().parents[1]
    / "metrics"
    / "skin_tone"
    / "sources"
    / "nhanes_2003_2004_fitzpatrick_image_readers"
    / "data.csv"
)


def test_hand_calculation():
    codes = np.array([1, 1, 2, 3])
    weights = np.array([1.0, 2.0, 3.0, 4.0])
    # Two replicates: [1, 2, 3, 4] and [2, 2, 3, 3].
    replicates = np.array([[1.0, 2.0], [2.0, 2.0], [3.0, 3.0], [4.0, 3.0]])
    got = category_proportions(codes, weights, replicates, (1, 2, 3, 4)).set_index("category")
    assert got["estimate"].to_dict() == pytest.approx({1: 0.3, 2: 0.3, 3: 0.4, 4: 0.0})
    # Category 1 shares across replicates are 0.3 and 0.4; the 2.5th and 97.5th percentiles
    # of two values interpolate linearly: 0.3 + 0.025 * 0.1 and 0.3 + 0.975 * 0.1.
    assert got.loc[1, "ci_low"] == pytest.approx(0.3025)
    assert got.loc[1, "ci_high"] == pytest.approx(0.3975)
    # Nobody is in category 4: its row is kept, at zero.
    assert got.loc[4, ["estimate", "ci_low", "ci_high"]].tolist() == [0.0, 0.0, 0.0]


def test_equal_weights_match_plain_shares():
    rng = np.random.default_rng(0)
    codes = rng.integers(1, 7, 400)
    replicates = rng.uniform(0.5, 1.5, (400, 50))
    got = category_proportions(codes, np.ones(400), replicates, tuple(range(1, 7)))
    plain = pd.Series(codes).value_counts(normalize=True).reindex(range(1, 7), fill_value=0)
    assert got["estimate"].to_numpy() == pytest.approx(plain.to_numpy())
    assert (got["ci_low"] <= got["ci_high"]).all()


def test_estimates_sum_to_one():
    rng = np.random.default_rng(1)
    codes = rng.integers(1, 4, 100)
    got = category_proportions(codes, rng.uniform(1, 5, 100), rng.uniform(0, 5, (100, 20)), (1, 2, 3))
    assert got["estimate"].sum() == pytest.approx(1.0)


def test_data_file_proportions_sum_to_one_and_n_is_constant():
    data = pd.read_csv(DATA)
    averaged = "Both readers averaged, half-points rounded down"
    assert set(data["rater"]) == {"Reader 1", "Reader 2", averaged}
    assert list(data["category"].unique()) == [f"Type {t}" for t in ("I", "II", "III", "IV", "V", "VI")]
    for key, frame in data.groupby(["rater", "sex", "race_ethnicity"]):
        assert len(frame) == 6, key
        assert frame["estimate"].sum() == pytest.approx(1.0, abs=1e-3), key
        assert frame["n"].nunique() == 1, key
        assert frame["n"].iloc[0] >= 50, key
        assert (frame["ci_low"] <= frame["estimate"]).all() and (frame["estimate"] <= frame["ci_high"]).all()
    assert (data["statistic"] == "proportion").all()


def test_averaged_series_reproduces_keiser_2012_table_1():
    # Keiser et al. 2012, Table I, survey-weighted shares for scores 1 to 6.
    published = [1.6, 33.1, 47.8, 4.9, 3.6, 9.0]
    data = pd.read_csv(DATA)
    rows = data[
        data["rater"].str.startswith("Both")
        & (data["sex"] == "All")
        & (data["race_ethnicity"] == "All")
    ]
    assert rows["n"].unique().tolist() == [2691]
    assert (rows["estimate"] * 100).round(1).tolist() == published
