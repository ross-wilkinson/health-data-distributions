"""Check every metric.json, source.json, and data.csv against the entry format.

Usage:
    python pipelines/validate.py

Prints each problem and exits non-zero if there are any. Tests call
validate(root) directly.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

ORIGINS = ("recomputed", "transcribed", "digitised", "gap")
FORMS = ("percentiles", "moments", "proportions", "none")
SAMPLING = ("probability sample", "convenience sample", "other")
REVIEW = ("draft", "reviewed")

METRIC_COMMON = ("id", "name", "category", "units", "priority", "status")
METRIC_AVAILABLE = ("definition", "comparison_note")
METRIC_PLANNED = ("candidate_sources", "note")
POPULATION_FIELDS = ("description", "country", "years", "age_range", "n", "sampling", "exclusions")
MEASUREMENT_FIELDS = ("method", "device", "protocol")
CITATION_FIELDS = ("text", "url", "license")
PROVENANCE_FIELDS = {
    "recomputed": ("pipeline", "raw_files"),
    "transcribed": ("url", "accessed"),
    "digitised": ("url", "accessed", "figure", "method", "precision", "script"),
    "gap": ("accessed",),
}
CSV_TAIL = ["n", "statistic", "estimate", "ci_low", "ci_high"]
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
PERCENTILE_NAME = re.compile(r"p\d+(\.\d+)?")
MISSING = object()  # a field that is absent; the caller has already reported it


def read_json(path: Path, problems: list[str]) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        problems.append(f"{path}: cannot read as JSON ({error})")
        return None
    if not isinstance(data, dict):
        problems.append(f"{path}: top level must be an object")
        return None
    return data


def is_text(value: object) -> bool:
    return isinstance(value, str) and value.strip() != ""


def is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_text_list(value: object) -> bool:
    return isinstance(value, list) and all(is_text(v) for v in value)


def check_object(where: str, value: object, fields: tuple[str, ...], problems: list[str]) -> dict:
    """Report a non-object value and any missing field; absent objects are skipped."""
    if value is MISSING:
        return {}
    if not isinstance(value, dict):
        problems.append(f"{where}: must be an object")
        return {}
    for field in fields:
        if field not in value:
            problems.append(f"{where}: missing required field '{field}'")
    return value


def check_metric(path: Path, has_sources: bool, problems: list[str]) -> dict | None:
    metric = read_json(path, problems)
    if metric is None:
        return None
    where = str(path)
    for field in METRIC_COMMON:
        if field not in metric:
            problems.append(f"{where}: missing required field '{field}'")
    if metric.get("id") != path.parent.name:
        problems.append(f"{where}: id {metric.get('id')!r} must equal the folder name {path.parent.name!r}")
    for field in ("name", "category", "units"):
        if field in metric and not is_text(metric[field]):
            problems.append(f"{where}: '{field}' must be a non-empty string")
    if "priority" in metric and not (is_int(metric["priority"]) and metric["priority"] >= 1):
        problems.append(f"{where}: 'priority' must be an integer of at least 1")

    expected = "available" if has_sources else "planned"
    status = metric.get("status")
    if status not in ("available", "planned"):
        problems.append(f"{where}: 'status' must be 'available' or 'planned', not {status!r}")
    elif status != expected:
        problems.append(
            f"{where}: status is {status!r} but the metric has {'a' if has_sources else 'no'} source folder"
        )

    required, other = (
        (METRIC_AVAILABLE, METRIC_PLANNED) if status == "available" else (METRIC_PLANNED, METRIC_AVAILABLE)
    )
    if status in ("available", "planned"):
        for field in required:
            if field not in metric:
                problems.append(f"{where}: missing required field '{field}' for a {status} metric")
        for field in other:
            if field in metric:
                problems.append(f"{where}: field '{field}' is not allowed on a {status} metric")
    if status == "available":
        if "definition" in metric and not is_text(metric["definition"]):
            problems.append(f"{where}: 'definition' must be a non-empty string")
        if "comparison_note" in metric and not isinstance(metric["comparison_note"], str):
            problems.append(f"{where}: 'comparison_note' must be a string")
    elif status == "planned":
        if "candidate_sources" in metric and not is_text_list(metric["candidate_sources"]):
            problems.append(f"{where}: 'candidate_sources' must be a list of non-empty strings")
        if "note" in metric and not isinstance(metric["note"], str):
            problems.append(f"{where}: 'note' must be a string")
    return metric


def check_source(folder: Path, root: Path, problems: list[str]) -> None:
    path = folder / "source.json"
    if not path.exists():
        problems.append(f"{folder}: missing source.json")
        return
    source = read_json(path, problems)
    if source is None:
        return
    where = str(path)
    for field in (
        "id",
        "title",
        "origin",
        "statistic_form",
        "population",
        "measurement",
        "use_for",
        "do_not_use_for",
        "caveats",
        "review_status",
        "citation",
        "provenance",
    ):
        if field not in source:
            problems.append(f"{where}: missing required field '{field}'")
    if source.get("id") != folder.name:
        problems.append(f"{where}: id {source.get('id')!r} must equal the folder name {folder.name!r}")
    if "title" in source and not is_text(source["title"]):
        problems.append(f"{where}: 'title' must be a non-empty string")

    origin, form = source.get("origin"), source.get("statistic_form")
    for field, value, allowed in (
        ("origin", origin, ORIGINS),
        ("statistic_form", form, FORMS),
        ("review_status", source.get("review_status"), REVIEW),
    ):
        if field in source and value not in allowed:
            problems.append(f"{where}: '{field}' must be one of {list(allowed)}, not {value!r}")

    population = check_object(
        f"{where}: population", source.get("population", MISSING), POPULATION_FIELDS, problems
    )
    if "population" in source:
        for field in ("description", "country", "years", "age_range", "exclusions"):
            if field in population and not is_text(population[field]):
                problems.append(f"{where}: population.{field} must be a non-empty string")
        if "sampling" in population and population["sampling"] not in SAMPLING:
            problems.append(
                f"{where}: population.sampling must be one of {list(SAMPLING)}, not {population['sampling']!r}"
            )
        if "n" in population:
            if origin == "gap":
                if population["n"] is not None:
                    problems.append(f"{where}: population.n must be null for a gap source")
            elif not (is_int(population["n"]) and population["n"] >= 0):
                problems.append(f"{where}: population.n must be a non-negative integer")
        if "n_eligible" in population and not (
            is_int(population["n_eligible"]) and population["n_eligible"] >= 0
        ):
            problems.append(f"{where}: population.n_eligible must be a non-negative integer")

    measurement = check_object(
        f"{where}: measurement", source.get("measurement", MISSING), MEASUREMENT_FIELDS, problems
    )
    for field in MEASUREMENT_FIELDS:
        if field in measurement and not is_text(measurement[field]):
            problems.append(f"{where}: measurement.{field} must be a non-empty string")

    for field in ("use_for", "do_not_use_for", "caveats"):
        if field in source:
            if not is_text_list(source[field]):
                problems.append(f"{where}: '{field}' must be a list of non-empty strings")
            elif not source[field] and origin != "gap":
                problems.append(f"{where}: '{field}' may be empty only for a gap source")
    if "analysis" in source and not is_text_list(source["analysis"]):
        problems.append(f"{where}: 'analysis' must be a list of non-empty strings")
    if "verification" in source and not is_text(source["verification"]):
        problems.append(f"{where}: 'verification' must be a non-empty string")
    if origin == "digitised" and "verification" not in source:
        problems.append(f"{where}: missing required field 'verification' for a digitised source")
    if origin == "digitised" and form == "none":
        problems.append(f"{where}: statistic_form 'none' is not allowed for a digitised source")

    citation = check_object(f"{where}: citation", source.get("citation", MISSING), CITATION_FIELDS, problems)
    for field in (*CITATION_FIELDS, "doi"):
        if field in citation and not is_text(citation[field]):
            problems.append(f"{where}: citation.{field} must be a non-empty string")

    if origin in PROVENANCE_FIELDS:
        provenance = check_object(
            f"{where}: provenance", source.get("provenance", MISSING), PROVENANCE_FIELDS[origin], problems
        )
        if "provenance" in source:
            for field in PROVENANCE_FIELDS[origin]:
                value = provenance.get(field)
                if field == "raw_files":
                    ok = is_text_list(value) and bool(value)
                elif field == "accessed":
                    ok = is_text(value) and DATE.fullmatch(value) is not None
                else:
                    ok = is_text(value)
                if field in provenance and not ok:
                    problems.append(f"{where}: provenance.{field} is not valid ({value!r})")
            if origin == "digitised" and is_text(provenance.get("script")):
                script = provenance["script"]
                target = (root / script).resolve()
                if Path(script).is_absolute() or not target.is_relative_to(root.resolve()):
                    problems.append(f"{where}: provenance.script must be a path inside the repository ({script!r})")
                elif not target.is_file():
                    problems.append(f"{where}: provenance.script {script!r} does not exist")

    if origin in ("transcribed", "digitised", "gap") and not (folder / "evidence.md").exists():
        problems.append(f"{folder}: missing evidence.md (required when origin is {origin!r})")

    csv_path = folder / "data.csv"
    if form == "none":
        if csv_path.exists():
            problems.append(f"{csv_path}: must be absent when statistic_form is 'none'")
    elif form in FORMS:
        if csv_path.exists():
            check_data(csv_path, form, origin in ("transcribed", "digitised"), problems)
        else:
            problems.append(f"{folder}: missing data.csv (statistic_form is {form!r})")


def check_data(path: Path, form: str, located: bool, problems: list[str]) -> None:
    where = str(path)
    try:
        data = pd.read_csv(path, dtype=str, keep_default_na=False)
    except (OSError, ValueError) as error:
        problems.append(f"{where}: cannot read ({error})")
        return
    columns = list(data.columns)
    tail = CSV_TAIL + (["locator"] if located else [])
    if columns[len(columns) - len(tail) :] != tail or len(columns) < len(tail):
        problems.append(f"{where}: columns must end with {tail}, found {columns}")
        return
    groups = columns[: len(columns) - len(tail)]
    if "locator" in groups:
        problems.append(f"{where}: 'locator' must be the last column")
    if form == "proportions" and "category" not in groups:
        problems.append(f"{where}: a proportions data.csv needs a 'category' column")
    if form != "proportions" and "category" in groups:
        problems.append(f"{where}: 'category' column is only for statistic_form 'proportions'")
    if data.empty:
        problems.append(f"{where}: no rows")
        return

    def bad_rows(mask: pd.Series) -> str:
        return ", ".join(str(i + 2) for i in data.index[mask][:5])

    blank = (data[groups + ["n", "statistic", "estimate"]].apply(lambda c: c.str.strip() == "")).any(axis=1)
    if blank.any():
        problems.append(
            f"{where}: empty value in a subgroup, n, statistic, or estimate column (lines {bad_rows(blank)})"
        )
    n = pd.to_numeric(data["n"], errors="coerce")
    bad_n = n.isna() | (n < 0) | (n != n.round())
    if bad_n.any():
        problems.append(f"{where}: 'n' must be a non-negative integer (lines {bad_rows(bad_n)})")
    numbers = {
        c: pd.to_numeric(data[c].replace("", pd.NA), errors="coerce")
        for c in ("estimate", "ci_low", "ci_high")
    }
    for column, values in numbers.items():
        bad = values.isna() & (data[column].str.strip() != "")
        if bad.any():
            problems.append(f"{where}: '{column}' must be numeric or empty (lines {bad_rows(bad)})")
    if numbers["estimate"].isna().any() and not blank.any():
        problems.append(f"{where}: 'estimate' must be numeric (lines {bad_rows(numbers['estimate'].isna())})")
    one_end = numbers["ci_low"].isna() != numbers["ci_high"].isna()
    if one_end.any():
        problems.append(
            f"{where}: ci_low and ci_high must be both given or both empty (lines {bad_rows(one_end)})"
        )
    outside = (numbers["ci_low"] > numbers["estimate"]) | (numbers["estimate"] > numbers["ci_high"])
    if outside.any():
        problems.append(f"{where}: estimate lies outside its interval (lines {bad_rows(outside)})")

    statistic = data["statistic"]
    if form == "proportions":
        bad = statistic != "proportion"
        if bad.any():
            problems.append(f"{where}: statistic must be 'proportion' (lines {bad_rows(bad)})")
    elif form == "moments":
        bad = ~statistic.isin(["mean", "sd"])
        if bad.any():
            problems.append(f"{where}: moments statistics must be 'mean' or 'sd' (lines {bad_rows(bad)})")
    elif form == "percentiles":
        bad = ~(statistic.isin(["mean", "sd"]) | statistic.str.fullmatch(PERCENTILE_NAME))
        if bad.any():
            problems.append(
                f"{where}: percentiles statistics must be 'mean', 'sd', or 'p<number>' (lines {bad_rows(bad)})"
            )
    duplicated = data.duplicated(groups + ["statistic"], keep=False)
    if duplicated.any():
        problems.append(f"{where}: repeated subgroup and statistic (lines {bad_rows(duplicated)})")
    if located:
        missing = data["locator"].str.strip() == ""
        if missing.any():
            problems.append(f"{where}: every row needs a locator (lines {bad_rows(missing)})")


def validate(root: Path = ROOT) -> list[str]:
    """Return a list of problems found under root/metrics; empty means valid."""
    problems: list[str] = []
    metrics_dir = Path(root) / "metrics"
    if not metrics_dir.is_dir():
        return [f"{metrics_dir}: not found"]
    priorities: dict[int, str] = {}
    for folder in sorted(p for p in metrics_dir.iterdir() if p.is_dir()):
        sources_dir = folder / "sources"
        source_folders = (
            sorted(p for p in sources_dir.iterdir() if p.is_dir()) if sources_dir.is_dir() else []
        )
        path = folder / "metric.json"
        if not path.exists():
            problems.append(f"{folder}: missing metric.json")
        else:
            metric = check_metric(path, bool(source_folders), problems)
            priority = metric.get("priority") if metric else None
            if is_int(priority):
                if priority in priorities:
                    problems.append(f"{path}: priority {priority} is also used by {priorities[priority]}")
                priorities[priority] = folder.name
        for source_folder in source_folders:
            check_source(source_folder, Path(root), problems)
    return problems


def main() -> int:
    problems = validate()
    for problem in problems:
        print(problem)
    print(f"{len(problems)} problem(s)" if problems else "ok")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
