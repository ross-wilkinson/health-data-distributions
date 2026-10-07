"""Monk Skin Tone and Fitzpatrick type in the SCIN dermatology image dataset.

Usage:
    python pipelines/scin_skin_tone.py

Reads raw/scin/scin_cases.csv and raw/scin/scin_labels.csv (see README for the
download commands; no images are needed) and writes two sources under
metrics/skin_tone/sources/:

    scin_2023_monk_lay_annotators/data.csv
    scin_2023_fitzpatrick_self_and_dermatologist/data.csv

Each rater is reported separately. Shares are unweighted: the contributors are
volunteers who answered a search advertisement, not a sample of a population.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "scin"
SOURCES = ROOT / "metrics" / "skin_tone" / "sources"

MIN_CELL = 50  # subgroups with fewer rated contributions are not reported
MONK_RATERS = {"US annotators": "monk_skin_tone_label_us", "India annotators": "monk_skin_tone_label_india"}
MONK = {str(i): f"MST {i}" for i in range(1, 11)}
FITZPATRICK_RATERS = {
    "Self-reported": "fitzpatrick_skin_type",
    "Dermatologist": "dermatologist_fitzpatrick_skin_type_label_1",
}
FITZPATRICK = {f"FST{i}": f"Type {numeral}" for i, numeral in enumerate(["I", "II", "III", "IV", "V", "VI"], 1)}
RACE_ETHNICITY = {
    "WHITE": "White",
    "BLACK_OR_AFRICAN_AMERICAN": "Black or African American",
    "HISPANIC_LATINO_OR_SPANISH_ORIGIN": "Hispanic, Latino, or Spanish origin",
    "ASIAN": "Asian",
    "TWO_OR_MORE_AFTER_MITIGATION": "Two or more",
}


def load() -> pd.DataFrame:
    cases = pd.read_csv(RAW / "scin_cases.csv", dtype=str)
    labels = pd.read_csv(RAW / "scin_labels.csv", dtype=str)
    data = cases.merge(labels, on="case_id", how="inner", validate="one_to_one")
    # Only contributors who gave a single listed group, or the dataset's own "two or more".
    data["race_ethnicity"] = data["combined_race"].map(RACE_ETHNICITY)
    return data


def shares(data: pd.DataFrame, raters: dict[str, str], categories: dict[str, str]) -> pd.DataFrame:
    rows = []
    for rater, column in raters.items():
        rated = data[data[column].isin(categories)]
        groups = [("All", rated)] + [
            (name, frame) for name, frame in rated.groupby("race_ethnicity") if len(frame) >= MIN_CELL
        ]
        for race, frame in groups:
            counts = frame[column].value_counts().reindex(categories, fill_value=0)
            for code, label in categories.items():
                rows.append((rater, race, label, len(frame), "proportion", round(counts[code] / len(frame), 4)))
    table = pd.DataFrame(rows, columns=["rater", "race_ethnicity", "category", "n", "statistic", "estimate"])
    table["ci_low"] = ""
    table["ci_high"] = ""
    return table


def agreement(data: pd.DataFrame, first: str, second: str, categories: dict[str, str], label: str) -> None:
    both = data[data[first].isin(categories) & data[second].isin(categories)]
    order = list(categories)
    gap = (both[first].map(order.index) - both[second].map(order.index)).abs()
    print(f"{label}: both present {len(both):,}; same {(gap == 0).mean():.1%}; within one {(gap <= 1).mean():.1%}")


def write(table: pd.DataFrame, source_id: str) -> None:
    out = SOURCES / source_id / "data.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(out, index=False, lineterminator="\n")
    groups = table.groupby(["rater", "race_ethnicity"]).ngroups
    print(f"wrote {out.relative_to(ROOT)}: {groups} rater-by-group tables")


def main() -> None:
    data = load()
    print(f"contributions: {len(data):,}; year values: {sorted(data['year'].dropna().unique().tolist())}")
    for rater, column in MONK_RATERS.items():
        print(f"Monk, {rater}: {data[column].isin(MONK).sum():,} rated")
    self_answer = data["fitzpatrick_skin_type"]
    print(f"Fitzpatrick, self-reported: {self_answer.isin(FITZPATRICK).sum():,} gave a type; "
          f"{(self_answer == 'NONE_IDENTIFIED').sum():,} answered that none fit; {self_answer.isna().sum():,} blank")
    print(f"Fitzpatrick, dermatologist: {data[FITZPATRICK_RATERS['Dermatologist']].isin(FITZPATRICK).sum():,} rated")
    agreement(data, *MONK_RATERS.values(), MONK, "Monk, US against India annotators")
    agreement(data, *FITZPATRICK_RATERS.values(), FITZPATRICK, "Fitzpatrick, self against dermatologist")

    write(shares(data, MONK_RATERS, MONK), "scin_2023_monk_lay_annotators")
    write(shares(data, FITZPATRICK_RATERS, FITZPATRICK), "scin_2023_fitzpatrick_self_and_dermatologist")


if __name__ == "__main__":
    main()
