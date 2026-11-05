"""Body size distributions (BMI, height, weight, arm circumference) in US adults, NHANES 2015-2018.

Usage:
    python pipelines/body_size.py

Reads the public NHANES files in raw/nhanes/ (DEMO_I, BMX_I, DEMO_J, BMX_J) and writes:
  metrics/body_size/sources/nhanes_2015_2018_body_mass_index/data.csv
  metrics/body_size/sources/nhanes_2015_2018_arm_circumference/data.csv
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from survey import describe, replicate_weights

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "nhanes"
BODY_ROOT = ROOT / "metrics" / "body_size" / "sources"

CYCLES = ("I", "J")  # 2015-2016 and 2017-2018
MIN_CELL = 50  # subgroups with fewer examined people are not reported

SEX = {1: "Male", 2: "Female"}
RACE_ETHNICITY = {
    1: "Mexican American",
    2: "Other Hispanic",
    3: "Non-Hispanic White",
    4: "Non-Hispanic Black",
    6: "Non-Hispanic Asian",
    7: "Other or multiracial",
}
AGE_EDGES = [18, 30, 40, 50, 60, 70, 80, 200]
AGE_LABELS = ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"]


def load() -> pd.DataFrame:
    frames = []
    for cycle in CYCLES:
        demo = pd.read_sas(RAW / f"DEMO_{cycle}.xpt")
        bmx_cols = ["SEQN", "BMXBMI", "BMXHT", "BMXWT", "BMXARMC"]
        exam = pd.read_sas(RAW / f"BMX_{cycle}.xpt")[bmx_cols]
        frames.append(demo.merge(exam, on="SEQN", how="left"))

    data = pd.concat(frames, ignore_index=True)
    # The design is defined on everyone examined; subgroups are taken afterwards.
    data = data[data["RIDSTATR"] == 2].copy()
    data["weight"] = data["WTMEC2YR"] / len(CYCLES)
    data["sex"] = data["RIAGENDR"].map(SEX)
    data["race_ethnicity"] = data["RIDRETH3"].map(RACE_ETHNICITY)
    data["age_band"] = pd.cut(data["RIDAGEYR"], AGE_EDGES, right=False, labels=AGE_LABELS).astype(object)
    return data


def process_measure(data: pd.DataFrame, replicates: np.ndarray, column_name: str, out_csv: Path) -> None:
    eligible = (data["RIDAGEYR"] >= 18).to_numpy()
    measured = eligible & data[column_name].notna().to_numpy()
    print(f"[{column_name}] examined adults: {eligible.sum():,}; with valid measurement: {measured.sum():,}")

    groupings = [[], ["sex"], ["age_band"], ["age_band", "sex"], ["race_ethnicity"]]
    pieces = []
    for columns in groupings:
        groups = data[measured].groupby(columns) if columns else [((), data[measured])]
        for key, frame in groups:
            if len(frame) < MIN_CELL:
                continue
            rows = data.index.get_indexer(frame.index)
            table = describe(frame[column_name].to_numpy(), frame["weight"].to_numpy(), replicates[rows])
            labels = dict.fromkeys(("sex", "age_band", "race_ethnicity"), "All")
            labels.update(zip(columns, key if isinstance(key, tuple) else (key,)))
            for position, (col, val) in enumerate(labels.items()):
                table.insert(position, col, val)
            table.insert(3, "n", len(frame))
            pieces.append(table)

    result = pd.concat(pieces, ignore_index=True)
    result[["estimate", "ci_low", "ci_high"]] = result[["estimate", "ci_low", "ci_high"]].round(2)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(out_csv, index=False, lineterminator="\n")
    print(f"wrote {out_csv.relative_to(ROOT)}: {result.groupby(['sex', 'age_band', 'race_ethnicity']).ngroups} subgroups")


def main() -> None:
    data = load()
    replicates = replicate_weights(
        data["SDMVSTRA"].to_numpy(), data["SDMVPSU"].to_numpy(), data["weight"].to_numpy()
    )

    bmi_out = BODY_ROOT / "nhanes_2015_2018_body_mass_index" / "data.csv"
    arm_out = BODY_ROOT / "nhanes_2015_2018_arm_circumference" / "data.csv"

    process_measure(data, replicates, "BMXBMI", bmi_out)
    process_measure(data, replicates, "BMXARMC", arm_out)


if __name__ == "__main__":
    np.seterr(all="raise")
    main()
