"""Tests for the static API export pipeline (pipelines/export_api.py)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from pipelines.export_api import export_all


@pytest.fixture(scope="module")
def exported_api(tmp_path_factory: pytest.TempPathFactory) -> Path:
    out_dir = tmp_path_factory.mktemp("api_export")
    export_all(out_dir)
    return out_dir


def test_catalog_structure(exported_api: Path) -> None:
    catalog_path = exported_api / "catalog.json"
    assert catalog_path.exists()

    with open(catalog_path, encoding="utf-8") as f:
        data = json.load(f)

    assert data["version"] == "1.0.0"
    assert data["total_metrics"] == 15
    assert data["available_metrics"] == 4
    assert data["planned_metrics"] == 11
    assert len(data["metrics"]) == 15

    # Check metrics are sorted by priority
    priorities = [m["priority"] for m in data["metrics"]]
    assert priorities == sorted(priorities)

    # Check available metrics have sources
    rhr = next(m for m in data["metrics"] if m["id"] == "resting_heart_rate")
    assert rhr["status"] == "available"
    assert rhr["source_count"] == 3
    assert "methodological_warning" in rhr
    assert "academy_module" in rhr

    bp = next(m for m in data["metrics"] if m["id"] == "blood_pressure")
    assert bp["status"] == "available"
    assert bp["source_count"] == 2

    bs = next(m for m in data["metrics"] if m["id"] == "body_size")
    assert bs["status"] == "available"
    assert bs["source_count"] == 2


def test_body_size_export(exported_api: Path) -> None:
    bs_path = exported_api / "metrics" / "body_size.json"
    assert bs_path.exists()

    with open(bs_path, encoding="utf-8") as f:
        bs = json.load(f)

    assert bs["id"] == "body_size"
    assert len(bs["sources"]) == 2

    bmi_src = next(s for s in bs["sources"] if s["id"] == "nhanes_2015_2018_body_mass_index")
    assert bmi_src["origin"] == "recomputed"
    assert len(bmi_src["subgroups"]) > 0
    assert bmi_src["subgroups"][0]["summary"]["median"] is not None


def test_blood_pressure_export(exported_api: Path) -> None:
    bp_path = exported_api / "metrics" / "blood_pressure.json"
    assert bp_path.exists()

    with open(bp_path, encoding="utf-8") as f:
        bp = json.load(f)

    assert bp["id"] == "blood_pressure"
    assert bp["units"] == "mmHg"
    assert len(bp["sources"]) == 2

    sys_src = next(s for s in bp["sources"] if s["id"] == "nhanes_2015_2018_clinic_systolic")
    assert sys_src["origin"] == "recomputed"
    assert len(sys_src["subgroups"]) > 0
    assert sys_src["subgroups"][0]["summary"]["mean"] is not None


def test_metric_json_structure(exported_api: Path) -> None:
    rhr_path = exported_api / "metrics" / "resting_heart_rate.json"
    assert rhr_path.exists()

    with open(rhr_path, encoding="utf-8") as f:
        rhr = json.load(f)

    assert rhr["id"] == "resting_heart_rate"
    assert rhr["units"] == "beats/min"
    assert len(rhr["sources"]) == 3

    nhanes = next(s for s in rhr["sources"] if s["id"] == "nhanes_2015_2018_clinic_pulse")
    assert nhanes["origin"] == "recomputed"
    assert nhanes["statistic_form"] == "percentiles"
    assert len(nhanes["subgroups"]) > 0

    first_subgroup = nhanes["subgroups"][0]
    assert "subgroup" in first_subgroup
    assert "n" in first_subgroup
    assert "statistics" in first_subgroup
    assert "summary" in first_subgroup
    assert "mean" in first_subgroup["summary"]
    assert "sd" in first_subgroup["summary"]
    assert "median" in first_subgroup["summary"]
    assert "p5" in first_subgroup["summary"]
    assert "p95" in first_subgroup["summary"]


def test_skin_tone_export(exported_api: Path) -> None:
    st_path = exported_api / "metrics" / "skin_tone.json"
    assert st_path.exists()

    with open(st_path, encoding="utf-8") as f:
        st = json.load(f)

    assert st["id"] == "skin_tone"
    assert st["status"] == "available"
    assert len(st["sources"]) == 12

    # Check Monk lay annotators source
    monk_src = next(s for s in st["sources"] if s["id"] == "scin_2023_monk_lay_annotators")
    assert monk_src["origin"] == "recomputed"
    assert monk_src["statistic_form"] == "proportions"
    assert len(monk_src["subgroups"]) > 0


def test_tidy_csv_export(exported_api: Path) -> None:
    rhr_csv = exported_api / "metrics" / "resting_heart_rate.csv"
    assert rhr_csv.exists()

    lines = rhr_csv.read_text(encoding="utf-8").splitlines()
    assert len(lines) > 10
    header = lines[0].split(",")
    assert header[0] == "source_id"
    assert "n" in header
    assert "statistic" in header
    assert "estimate" in header


def test_bibtex_export(exported_api: Path) -> None:
    rhr_bib = exported_api / "citations" / "resting_heart_rate.bib"
    assert rhr_bib.exists()

    content = rhr_bib.read_text(encoding="utf-8")
    assert "@misc{nhanes_2015_2018_clinic_pulse" in content
    assert "@misc{quer_2020_fitbit_92457_adults" in content
