import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipelines"))

from render import render
from validate import validate

METRIC = {
    "id": "m",
    "name": "A metric",
    "category": "Test",
    "units": "u",
    "priority": 1,
    "status": "available",
    "definition": "What it is.",
    "comparison_note": "",
}
SOURCE = {
    "id": "s",
    "title": "A source",
    "origin": "recomputed",
    "statistic_form": "percentiles",
    "population": {
        "description": "People.",
        "country": "Nowhere",
        "years": "2020",
        "age_range": "18 and over",
        "n": 100,
        "sampling": "probability sample",
        "exclusions": "None.",
    },
    "measurement": {"method": "Counted.", "device": "None.", "protocol": "Seated."},
    "use_for": ["a"],
    "do_not_use_for": ["b"],
    "caveats": ["c"],
    "review_status": "draft",
    "citation": {"text": "Someone.", "url": "https://example.org", "license": "Open"},
    "provenance": {"pipeline": "pipelines/x.py", "raw_files": ["raw/x.csv"]},
}
CSV = (
    "sex,n,statistic,estimate,ci_low,ci_high\n"
    "All,100,mean,70.0,69.0,71.0\n"
    "All,100,sd,10.0,9.0,11.0\n"
    "All,100,p50,70.0,68.0,72.0\n"
)
TRANSCRIBED_CSV = (
    "sex,n,statistic,estimate,ci_low,ci_high,locator\n"
    "All,100,mean,70.0,,,Table 2\n"
    "All,100,sd,10.0,,,Table 2\n"
)


DIGITISED_CSV = (
    "category,n,statistic,estimate,ci_low,ci_high,locator\n"
    "Light,100,proportion,0.6,,,Figure 1 panel B\n"
    "Dark,100,proportion,0.4,,,Figure 1 panel B\n"
)
SCRIPT = "pipelines/digitise/fig.py"


def build(root: Path, metric=None, source=None, csv=CSV, evidence=False) -> Path:
    """Write one metric with one source under root and return the source folder."""
    folder = root / "metrics" / "m" / "sources" / "s"
    folder.mkdir(parents=True)
    (root / "metrics" / "m" / "metric.json").write_text(json.dumps(metric or METRIC))
    (folder / "source.json").write_text(json.dumps(source or SOURCE))
    if csv is not None:
        (folder / "data.csv").write_text(csv)
    if evidence:
        (folder / "evidence.md").write_text("# Evidence\n")
    return folder


def transcribed() -> dict:
    return {
        **SOURCE,
        "origin": "transcribed",
        "provenance": {"url": "https://example.org", "accessed": "2026-10-06"},
    }


def test_repository_validates_cleanly():
    assert validate() == []


def test_a_valid_minimal_metric_passes(tmp_path):
    build(tmp_path)
    assert validate(tmp_path) == []


def test_missing_required_field_is_reported(tmp_path):
    source = {k: v for k, v in SOURCE.items() if k != "caveats"}
    build(tmp_path, source=source)
    assert any("missing required field 'caveats'" in p for p in validate(tmp_path))


def test_missing_required_metric_field_is_reported(tmp_path):
    metric = {k: v for k, v in METRIC.items() if k != "definition"}
    build(tmp_path, metric=metric)
    assert any("missing required field 'definition'" in p for p in validate(tmp_path))


def test_bad_enumeration_value_is_reported(tmp_path):
    build(tmp_path, source={**SOURCE, "statistic_form": "histogram"})
    assert any("statistic_form" in p and "histogram" in p for p in validate(tmp_path))


def test_bad_sampling_value_is_reported(tmp_path):
    population = {**SOURCE["population"], "sampling": "random"}
    build(tmp_path, source={**SOURCE, "population": population})
    assert any("population.sampling" in p for p in validate(tmp_path))


def test_transcribed_data_without_locator_is_reported(tmp_path):
    build(tmp_path, source=transcribed(), csv=CSV, evidence=True)
    assert any("columns must end with" in p and "locator" in p for p in validate(tmp_path))


def test_transcribed_data_with_locator_passes(tmp_path):
    build(tmp_path, source=transcribed(), csv=TRANSCRIBED_CSV, evidence=True)
    assert validate(tmp_path) == []


def test_transcribed_source_without_evidence_is_reported(tmp_path):
    build(tmp_path, source=transcribed(), csv=TRANSCRIBED_CSV, evidence=False)
    assert any("missing evidence.md" in p for p in validate(tmp_path))


def test_status_must_match_the_source_folders(tmp_path):
    build(tmp_path, metric={**METRIC, "status": "planned"})
    assert any("status is 'planned'" in p for p in validate(tmp_path))


def digitised(**changes) -> dict:
    """A valid digitised proportions source; keyword arguments replace top-level fields."""
    source = {
        **SOURCE,
        "origin": "digitised",
        "statistic_form": "proportions",
        "provenance": {
            "url": "https://example.org",
            "accessed": "2026-10-06",
            "figure": "Figure 1, panel B",
            "method": "Bar tops located in pixels and scaled to the axis ticks.",
            "precision": "0.005 of the sample (half a pixel)",
            "script": SCRIPT,
        },
        "verification": "The two bars sum to 1.000.",
        **changes,
    }
    return {k: v for k, v in source.items() if v is not None}


def build_digitised(root: Path, source=None, csv=DIGITISED_CSV, evidence=True, script=True) -> Path:
    if script:
        (root / SCRIPT).parent.mkdir(parents=True)
        (root / SCRIPT).write_text("# placeholder\n")
    return build(root, source=source or digitised(), csv=csv, evidence=evidence)


def test_a_valid_digitised_source_passes(tmp_path):
    build_digitised(tmp_path)
    assert validate(tmp_path) == []


def test_digitised_source_with_a_missing_script_file_is_reported(tmp_path):
    build_digitised(tmp_path, script=False)
    assert any("provenance.script" in p and "does not exist" in p for p in validate(tmp_path))


def test_digitised_script_outside_the_repository_is_reported(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    (tmp_path / "outside.py").write_text("# placeholder\n")
    source = digitised()
    source["provenance"] = {**source["provenance"], "script": "../outside.py"}
    build_digitised(root, source=source)
    assert any("provenance.script" in p and "inside the repository" in p for p in validate(root))


def test_digitised_source_with_a_missing_provenance_field_is_reported(tmp_path):
    for field in ("url", "accessed", "figure", "method", "precision", "script"):
        root = tmp_path / field
        root.mkdir()
        source = digitised()
        source["provenance"] = {k: v for k, v in source["provenance"].items() if k != field}
        build_digitised(root, source=source)
        assert any(f"missing required field '{field}'" in p for p in validate(root)), field


def test_digitised_source_with_an_empty_provenance_field_is_reported(tmp_path):
    source = digitised()
    source["provenance"] = {**source["provenance"], "precision": " "}
    build_digitised(tmp_path, source=source)
    assert any("provenance.precision is not valid" in p for p in validate(tmp_path))


def test_digitised_source_without_evidence_is_reported(tmp_path):
    build_digitised(tmp_path, evidence=False)
    assert any("missing evidence.md" in p and "digitised" in p for p in validate(tmp_path))


def test_digitised_data_without_locator_is_reported(tmp_path):
    csv = "category,n,statistic,estimate,ci_low,ci_high\nLight,100,proportion,0.6,,\nDark,100,proportion,0.4,,\n"
    build_digitised(tmp_path, csv=csv)
    assert any("columns must end with" in p and "locator" in p for p in validate(tmp_path))


def test_digitised_source_with_no_statistics_is_reported(tmp_path):
    build_digitised(tmp_path, source=digitised(statistic_form="none"), csv=None)
    assert any("statistic_form 'none' is not allowed for a digitised source" in p for p in validate(tmp_path))


def test_digitised_source_without_verification_is_reported(tmp_path):
    build_digitised(tmp_path, source=digitised(verification=None))
    assert any("missing required field 'verification'" in p for p in validate(tmp_path))


def test_digitised_source_with_empty_verification_is_reported(tmp_path):
    build_digitised(tmp_path, source=digitised(verification=" "))
    assert any("'verification' must be a non-empty string" in p for p in validate(tmp_path))


def test_digitised_source_is_labelled_when_rendered(tmp_path):
    build_digitised(tmp_path)
    render(tmp_path)
    page = (tmp_path / "entries" / "m.md").read_text(encoding="utf-8")
    assert "digitised from a published figure" in page
    assert "A source<br>*Digitised from a figure*<br>*Guidance: draft, not yet expert-reviewed*" in page
    assert (
        "Measured from Figure 1, panel B. Precision: 0.005 of the sample (half a pixel). "
        "Method: Bar tops located in pixels and scaled to the axis ticks. Script: pipelines/digitise/fig.py."
    ) in page
    assert "| Light | 100 | 0.6 | Figure 1 panel B |" in page
