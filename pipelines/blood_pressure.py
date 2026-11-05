"""Clinic blood pressure (systolic and diastolic) in US adults, NHANES 2015-2018.

Usage:
    python pipelines/blood_pressure.py

Reads the public NHANES files in raw/nhanes/ (DEMO_I, BPX_I, DEMO_J, BPX_J) and writes:
  metrics/blood_pressure/sources/nhanes_2015_2018_clinic_systolic/data.csv
  metrics/blood_pressure/sources/nhanes_2015_2018_clinic_diastolic/data.csv
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from survey import describe, replicate_weights

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "nhanes"
BP_ROOT = ROOT / "metrics" / "blood_pressure" / "sources"

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


def compute_standard_bp(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate mean systolic and diastolic BP using standard CDC averaging protocol.

    - If only 1 reading: use that reading.
    - If >= 2 readings: average readings 2 and 3 (the first reading is discarded).
    - Diastolic readings of 0 are treated as missing.
    """
    sys_cols = ["BPXSY1", "BPXSY2", "BPXSY3"]
    dia_cols = ["BPXDI1", "BPXDI2", "BPXDI3"]

    for col in dia_cols:
        df[col] = df[col].replace(0, np.nan)

    def avg_readings(row: pd.Series, cols: list[str]) -> float:
        valid = [row[c] for c in cols if pd.notna(row[c])]
        if not valid:
            return np.nan
        if len(valid) == 1:
            return float(valid[0])
        return float(np.mean(valid[1:]))

    df["systolic"] = df.apply(lambda r: avg_readings(r, sys_cols), axis=1)
    df["diastolic"] = df.apply(lambda r: avg_readings(r, dia_cols), axis=1)
    return df


def load() -> pd.DataFrame:
    frames = []
    for cycle in CYCLES:
        demo = pd.read_sas(RAW / f"DEMO_{cycle}.xpt")
        bpx_cols = ["SEQN", "BPXSY1", "BPXDI1", "BPXSY2", "BPXDI2", "BPXSY3", "BPXDI3"]
        exam = pd.read_sas(RAW / f"BPX_{cycle}.xpt")[bpx_cols]
        exam = compute_standard_bp(exam)
        frames.append(demo.merge(exam[["SEQN", "systolic", "diastolic"]], on="SEQN", how="left"))

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
    print(f"[{column_name}] examined adults: {eligible.sum():,}; with valid reading: {measured.sum():,}")

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

    sys_out = BP_ROOT / "nhanes_2015_2018_clinic_systolic" / "data.csv"
    dia_out = BP_ROOT / "nhanes_2015_2018_clinic_diastolic" / "data.csv"

    process_measure(data, replicates, "systolic", sys_out)
    process_measure(data, replicates, "diastolic", dia_out)


if __name__ == "__main__":
    np.seterr(all="raise")
    main()
