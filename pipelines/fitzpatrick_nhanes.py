"""Fitzpatrick skin type in US adults aged 20-59, NHANES 2003-2004, by image reader.

Usage:
    python pipelines/fitzpatrick_nhanes.py

Reads the public NHANES files in raw/nhanes/ (DEMO_C.xpt and DEX_C.xpt) and writes
metrics/skin_tone/sources/nhanes_2003_2004_fitzpatrick_image_readers/data.csv.

Reader 1 and Reader 2 are reported separately. A third series gives the single
score per person used by Keiser et al. 2012: the two readers averaged, with a
half-point rounded down.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from survey import category_proportions, replicate_weights

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "nhanes"
OUT = (
    ROOT / "metrics" / "skin_tone" / "sources" / "nhanes_2003_2004_fitzpatrick_image_readers" / "data.csv"
)

MIN_CELL = 50  # subgroups with fewer people read by a reader are not reported
AGE_RANGE = (20, 59)  # the dermatology exam covered these ages
READERS = {"Reader 1": "DEX1FITZ", "Reader 2": "DEX2FITZ"}
AVERAGED = "Both readers averaged, half-points rounded down"
TYPES = {1: "Type I", 2: "Type II", 3: "Type III", 4: "Type IV", 5: "Type V", 6: "Type VI"}
NOT_DETERMINED = 9  # "Not determined, picture missing"
SEX = {1: "Male", 2: "Female"}
RACE_ETHNICITY = {
    1: "Mexican American",
    2: "Other Hispanic",
    3: "Non-Hispanic White",
    4: "Non-Hispanic Black",
    5: "Other Race - Including Multi-Racial",
}


def load() -> pd.DataFrame:
    demo = pd.read_sas(RAW / "DEMO_C.xpt")
    dex = pd.read_sas(RAW / "DEX_C.xpt")[["SEQN", "DEX1FITZ", "DEX2FITZ"]]
    data = demo.merge(dex, on="SEQN", how="left")
    # The design is defined on everyone examined; subgroups are taken afterwards.
    data = data[data["RIDSTATR"] == 2].copy()
    # One 2-year cycle, so the weight is used as it is.
    data["weight"] = data["WTMEC2YR"]
    data["sex"] = data["RIAGENDR"].map(SEX)
    data["race_ethnicity"] = data["RIDRETH1"].map(RACE_ETHNICITY)
    for column in READERS.values():
        # Blank (no exam) and code 9 (picture missing) both mean no type was assigned.
        data[column] = data[column].where(data[column].between(1, 6))
    # Keiser et al. 2012 averaged the two readers. Their published counts are
    # reproduced only when a half-point is rounded down (a 2 and a 3 become 2).
    # A missing type from either reader leaves this missing.
    data[AVERAGED] = np.floor((data["DEX1FITZ"] + data["DEX2FITZ"]) / 2)
    return data


def report_counts(data: pd.DataFrame, eligible: pd.Series) -> None:
    """Print who was eligible, read, and missing, and how often the two readers agree."""
    raw = pd.read_sas(RAW / "DEX_C.xpt")[["SEQN", "DEX1FITZ", "DEX2FITZ"]]
    print(f"eligible (examined, aged {AGE_RANGE[0]}-{AGE_RANGE[1]}): {eligible.sum():,}")
    print(f"rows in DEX_C: {len(raw):,}")
    for name, column in READERS.items():
        read = data.loc[eligible, column].notna().sum()
        blank = raw[column].isna().sum()
        nine = (raw[column] == NOT_DETERMINED).sum()
        print(f"{name}: read {read:,}; blank {blank:,}; code 9 (picture missing) {nine:,}")

    both_given = raw["DEX1FITZ"].notna() & raw["DEX2FITZ"].notna()
    same_any = (raw["DEX1FITZ"] == raw["DEX2FITZ"]) & both_given
    print(f"a value (1-6 or 9) from both readers: {both_given.sum():,}; same value incl. 9: {same_any.sum():,}")

    both = data.loc[eligible, ["DEX1FITZ", "DEX2FITZ"]].dropna()
    gap = (both["DEX1FITZ"] - both["DEX2FITZ"]).abs()
    print(f"a type (1-6) from both readers: {len(both):,}")
    print(f"  same type: {(gap == 0).sum():,} ({(gap == 0).mean():.1%})")
    print(f"  within one type: {(gap <= 1).sum():,} ({(gap <= 1).mean():.1%})")
    # The documentation's consensus matrix accepts I-III with I-III and IV-VI with IV-VI only.
    across = (both["DEX1FITZ"] <= 3) != (both["DEX2FITZ"] <= 3)
    print(f"  one reader I-III and the other IV-VI (consensus matrix 'reject'): {across.sum():,}")


def main() -> None:
    data = load()
    replicates = replicate_weights(
        data["SDMVSTRA"].to_numpy(), data["SDMVPSU"].to_numpy(), data["weight"].to_numpy()
    )
    eligible = data["RIDAGEYR"].between(*AGE_RANGE)
    report_counts(data, eligible)

    groupings = [[], ["sex"], ["race_ethnicity"]]
    pieces = []
    for reader, column in {**READERS, AVERAGED: AVERAGED}.items():
        read = eligible & data[column].notna()
        for columns in groupings:
            groups = data[read].groupby(columns) if columns else [((), data[read])]
            for key, frame in groups:
                if len(frame) < MIN_CELL:
                    continue
                rows = data.index.get_indexer(frame.index)
                table = category_proportions(
                    frame[column].to_numpy(), frame["weight"].to_numpy(), replicates[rows], tuple(TYPES)
                )
                table["category"] = table["category"].map(TYPES)
                labels = dict.fromkeys(("sex", "race_ethnicity"), "All")
                labels.update(zip(columns, key if isinstance(key, tuple) else (key,)))
                table.insert(0, "race_ethnicity", labels["race_ethnicity"])
                table.insert(0, "sex", labels["sex"])
                table.insert(0, "rater", reader)
                table["n"] = len(frame)
                table["statistic"] = "proportion"
                pieces.append(table)

    result = pd.concat(pieces, ignore_index=True)
    result = result[
        ["rater", "sex", "race_ethnicity", "category", "n", "statistic", "estimate", "ci_low", "ci_high"]
    ]
    result[["estimate", "ci_low", "ci_high"]] = result[["estimate", "ci_low", "ci_high"]].round(4)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUT, index=False, lineterminator="\n")
    subgroups = result.groupby(["rater", "sex", "race_ethnicity"]).ngroups
    print(f"wrote {OUT.relative_to(ROOT)}: {subgroups} subgroups")


if __name__ == "__main__":
    np.seterr(all="raise")
    main()
