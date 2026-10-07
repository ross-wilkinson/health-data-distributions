"""Checks on the skin_tone metric: transcribed numbers match their quotes, gaps carry a dated log."""

import json
import re
from pathlib import Path

import pandas as pd
import pytest

FOLDER = Path(__file__).resolve().parents[1] / "metrics" / "skin_tone"
SOURCES = sorted(p for p in (FOLDER / "sources").iterdir() if p.is_dir())
TRANSCRIBED = [p for p in SOURCES if json.loads((p / "source.json").read_text("utf-8"))["origin"] == "transcribed"]
GAPS = [p for p in SOURCES if json.loads((p / "source.json").read_text("utf-8"))["origin"] == "gap"]
SEARCH_ROW = re.compile(r"^\|\s*\d+\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)


def source(folder: Path) -> dict:
    return json.loads((folder / "source.json").read_text("utf-8"))


def test_metric_is_available_and_every_source_has_a_known_origin():
    metric = json.loads((FOLDER / "metric.json").read_text("utf-8"))
    assert metric["status"] == "available"
    assert {"candidate_sources", "note"}.isdisjoint(metric)
    origins = {source(folder)["origin"] for folder in SOURCES}
    assert origins <= {"recomputed", "transcribed", "digitised", "gap"}


@pytest.mark.parametrize("folder", SOURCES, ids=lambda p: p.name)
def test_guidance_is_draft(folder):
    assert source(folder)["review_status"] == "draft"


@pytest.mark.parametrize("folder", TRANSCRIBED, ids=lambda p: p.name)
def test_proportions_do_not_exceed_one(folder):
    """Reported shares can sum to less than 1 when a source omits categories, never to more."""
    if source(folder)["statistic_form"] != "proportions":
        pytest.skip("not a proportions source")
    data = pd.read_csv(folder / "data.csv", keep_default_na=False)
    groups = [c for c in data.columns[: list(data.columns).index("n")] if c != "category"]
    sums = data.groupby(groups)["estimate"].sum() if groups else pd.Series([data["estimate"].sum()])
    assert (sums <= 1.0005).all()
    assert (data["estimate"] >= 0).all()


@pytest.mark.parametrize("folder", TRANSCRIBED, ids=lambda p: p.name)
def test_every_locator_and_number_is_quoted_in_evidence(folder):
    """Each row's locator is a heading in evidence.md, and a quote under it holds the number as printed."""
    data = pd.read_csv(folder / "data.csv", keep_default_na=False, dtype=str)
    evidence = (folder / "evidence.md").read_text("utf-8")
    sections = re.split(r"^### Locator: ", evidence, flags=re.MULTILINE)[1:]
    quotes_by_locator = {}
    for section in sections:
        name, _, body = section.partition("\n")
        quotes_by_locator[name.strip()] = " ".join(
            line for line in body.splitlines() if line.startswith(">")
        )
    for row in data.itertuples():
        assert row.locator in quotes_by_locator, f"locator {row.locator!r} has no section in evidence.md"
        if source(folder)["statistic_form"] == "proportions":
            percent = float(row.estimate) * 100
            printed = {f"{percent:.1f}", f"{percent:g}"}  # tables often omit the % sign, and print 0 as "0"
        else:
            printed = {row.estimate}  # means and SDs are stored as printed
        quotes = quotes_by_locator[row.locator]
        assert any(p in quotes for p in printed), f"{printed} not in a quote under {row.locator!r}"


@pytest.mark.parametrize("folder", GAPS, ids=lambda p: p.name)
def test_gap_has_dated_search_log_with_five_distinct_entries(folder):
    evidence = (folder / "evidence.md").read_text("utf-8")
    rows = SEARCH_ROW.findall(evidence)
    assert len({query for _, query in rows}) >= 5
    accessed = source(folder)["provenance"]["accessed"]
    assert all(date <= accessed for date, _ in rows)


@pytest.mark.parametrize("folder", GAPS, ids=lambda p: p.name)
def test_gap_says_not_found_in_this_search_and_never_does_not_exist(folder):
    record = source(folder)
    text = " ".join(record["caveats"])
    assert "not found in this search" in text.lower()
    assert record["statistic_form"] == "none"
    assert record["population"]["n"] is None
    assert not (folder / "data.csv").exists()
    everything = json.dumps(record).lower() + (folder / "evidence.md").read_text("utf-8").lower()
    assert "does not exist" not in everything
