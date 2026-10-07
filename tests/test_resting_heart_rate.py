import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipelines"))

METRIC = ROOT / "metrics" / "resting_heart_rate"
QUER = METRIC / "sources" / "quer_2020_fitbit_92457_adults"


def rows():
    with (QUER / "data.csv").open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def sections(evidence: str) -> dict[str, str]:
    """Map each '### locator' heading in evidence.md to the text under it."""
    parts = re.split(r"^### (.+)$", evidence, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def test_every_locator_has_an_evidence_section():
    evidence = sections((QUER / "evidence.md").read_text(encoding="utf-8"))
    for row in rows():
        assert row["locator"] in evidence, row["locator"]


def test_every_estimate_and_n_is_quoted_in_its_evidence_section():
    evidence = sections((QUER / "evidence.md").read_text(encoding="utf-8"))
    for row in rows():
        text = evidence[row["locator"]]
        quoted = "\n".join(line for line in text.splitlines() if line.startswith(">"))
        assert row["estimate"] in quoted, (row["locator"], row["estimate"])
        assert f"{int(row['n']):,}" in quoted, (row["locator"], row["n"])


def test_source_is_transcribed_with_an_open_licence():
    source = json.loads((QUER / "source.json").read_text(encoding="utf-8"))
    assert source["origin"] == "transcribed"
    assert source["review_status"] == "draft"
    assert "Creative Commons Attribution" in source["citation"]["license"]
    assert source["citation"]["doi"] == "10.1371/journal.pone.0227709"


def test_comparison_note_numbers_come_from_the_data_files():
    note = json.loads((METRIC / "metric.json").read_text(encoding="utf-8"))["comparison_note"]
    assert "typically lower" not in note
    nhanes = METRIC / "sources" / "nhanes_2015_2018_clinic_pulse" / "data.csv"
    with nhanes.open(newline="", encoding="utf-8") as handle:
        overall = {
            r["statistic"]: r["estimate"]
            for r in csv.DictReader(handle)
            if (r["sex"], r["age_band"], r["race_ethnicity"]) == ("All", "All", "All")
        }
    quer_mean = next(r["estimate"] for r in rows() if r["statistic"] == "mean")
    assert overall["mean"] in note
    assert quer_mean in note
