"""Render the catalog and the entry for each available metric as Markdown.

Usage:
    python pipelines/render.py

Reads metrics/<metric_id>/metric.json and the source folders beneath it. All
wording about a metric or a source comes from those files; this script only
lays it out.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import validate

ROOT = Path(__file__).resolve().parents[1]
SHOWN = ["p5", "p10", "p25", "p50", "p75", "p90", "p95"]
DRAFT_NOTE = "Guidance: draft, not yet expert-reviewed"
DIGITISED_NOTE = "Digitised from a figure"
ORIGIN_TEXT = {
    "recomputed": "recomputed by this project from public data",
    "transcribed": "transcribed from a publication",
    "digitised": "digitised from a published figure",
    "gap": "no usable statistic found",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def entry_name(metric_id: str) -> str:
    return metric_id.replace("_", "-")


def markdown_table(frame: pd.DataFrame) -> str:
    header = "| " + " | ".join(frame.columns) + " |"
    rule = "|" + "|".join(["---"] * frame.shape[1]) + "|"
    rows = ["| " + " | ".join(str(v) for v in row) + " |" for row in frame.itertuples(index=False)]
    return "\n".join([header, rule, *rows])


def cell(text: object) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def number(value: float, places: int | None = None) -> str:
    if pd.isna(value):
        return ""
    return f"{value:.{places}f}" if places is not None else f"{value:g}"


def with_interval(est: float, low: float, high: float, places: int | None = None) -> str:
    text = number(est, places)
    if pd.isna(low) or pd.isna(high):
        return text
    return f"{text} ({number(low, places)}-{number(high, places)})"


def subgroup_columns(data: pd.DataFrame) -> list[str]:
    """The columns before n: the subgroup definition, plus category for proportions."""
    return list(data.columns[: list(data.columns).index("n")])


def wide(data: pd.DataFrame, form: str) -> tuple[pd.DataFrame, list[str]]:
    """One row per subgroup, in file order, with one display column per statistic.

    Returns the table and the names of the subgroup columns. Statistics a source
    does not report are left out rather than shown empty.
    """
    groups = subgroup_columns(data)
    keys = [*groups, "n"]
    rows = []
    for key, frame in data.groupby(keys, sort=False):
        stats = frame.set_index("statistic")
        row = dict(zip(keys, key if isinstance(key, tuple) else (key,)))
        if "locator" in frame.columns:
            row["Source location"] = frame["locator"].iloc[0]
        if form == "proportions":
            row["Proportion (95% CI)"] = with_interval(
                *stats.loc["proportion", ["estimate", "ci_low", "ci_high"]]
            )
        if "mean" in stats.index:
            row["Mean (95% CI)"] = with_interval(*stats.loc["mean", ["estimate", "ci_low", "ci_high"]], 1)
        if "sd" in stats.index:
            row["SD"] = number(stats.loc["sd", "estimate"], 1)
        if form == "percentiles":
            for name in SHOWN:
                if name in stats.index:
                    row[name.upper()] = number(stats.loc[name, "estimate"])
        rows.append(row)
    table = pd.DataFrame(rows).fillna("")
    # Keep the locator last, after the statistics.
    if "Source location" in table.columns:
        table = table[[c for c in table.columns if c != "Source location"] + ["Source location"]]
    return table, groups


def ordered(values: pd.Series) -> list[str]:
    """Distinct values in file order, with 'All' first."""
    distinct = list(dict.fromkeys(values))
    return sorted(distinct, key=lambda v: v != "All")


def percentile_tables(table: pd.DataFrame, groups: list[str]) -> list[str]:
    """One table per value of sex, plus one by race_ethnicity, when those columns exist."""
    sections = []
    others = [g for g in groups if g not in ("sex", "race_ethnicity")]
    in_all_race = (
        table["race_ethnicity"] == "All" if "race_ethnicity" in groups else pd.Series(True, index=table.index)
    )
    for sex in ordered(table["sex"]) if "sex" in groups else [None]:
        rows = table[in_all_race]
        by = " and ".join(label(g).lower() for g in others) if others else "group"
        title = f"{sex or 'All'}, by {by}"
        if sex is not None:
            rows = rows[rows["sex"] == sex]
        rows = rows.drop(columns=[g for g in ("sex", "race_ethnicity") if g in groups])
        sections.append(f"#### {title}\n\n" + markdown_table(labelled(rows, groups)))
    if "race_ethnicity" in groups:
        mask = table["race_ethnicity"] != "All"
        for column in [g for g in groups if g != "race_ethnicity"]:
            mask &= table[column] == "All"
        rows = table[mask].drop(columns=[g for g in groups if g != "race_ethnicity"])
        sections.append("#### By race and ethnicity\n\n" + markdown_table(labelled(rows, groups)))
    return sections


def label(name: str) -> str:
    return {"age_band": "Age", "race_ethnicity": "Race and ethnicity"}.get(
        name, name.replace("_", " ").capitalize()
    )


def labelled(frame: pd.DataFrame, groups: list[str]) -> pd.DataFrame:
    """Give the subgroup columns display names; statistic columns already have them."""
    return frame.rename(columns={g: label(g) for g in groups})


def tables_section(data: pd.DataFrame, form: str) -> str:
    table, groups = wide(data, form)
    if form == "percentiles":
        parts = percentile_tables(table, groups)
        parts.append("The CSV has the full set of statistics, including percentiles not shown here.")
    else:
        parts = [markdown_table(labelled(table, groups))]
    return "\n\n".join(parts)


def source_table_row(source: dict) -> list[str]:
    pop, meas = source["population"], source["measurement"]
    name = source["title"]
    if source["origin"] == "digitised":
        name += f"<br>*{DIGITISED_NOTE}*"
    if source["review_status"] == "draft":
        name += f"<br>*{DRAFT_NOTE}*"
    population = f"{pop['description']} {pop['country']}, {pop['years']}, ages {pop['age_range']}."
    n = f"{pop['n']:,}" if pop["n"] is not None else "none"
    return [
        name,
        population,
        meas["method"],
        n,
        "; ".join(source["use_for"]),
        "; ".join(source["do_not_use_for"]),
    ]


def reproduce_text(source: dict, folder_url: str) -> str:
    prov = source["provenance"]
    if source["origin"] == "recomputed":
        files = ", ".join(f"`{f}`" for f in prov["raw_files"])
        return f"Reads {files}.\n\n```sh\npython {prov['pipeline']}\n```"
    evidence = f"[evidence.md]({folder_url}/evidence.md)"
    if source["origin"] == "digitised":
        return (
            f"Digitised from <{prov['url']}> (accessed {prov['accessed']}). "
            f"Measuring script: `{prov['script']}`. Measurements, quotes and locators: {evidence}."
        )
    if source["origin"] == "transcribed":
        return f"Transcribed from <{prov['url']}> (accessed {prov['accessed']}). Quotes and locators: {evidence}."
    return f"Searched on {prov['accessed']}. What was searched and found: {evidence}."


def citation_text(source: dict) -> str:
    cite = source["citation"]
    lines = ["Cite the primary source for any regulatory or ethics submission:", "", f"> {cite['text']}"]
    if "doi" in cite:
        lines.append(f"> doi:{cite['doi']}")
    lines += [f"> {cite['url']}", "", f"Licence or terms of use: {cite['license']}"]
    if source["origin"] == "recomputed":
        lines += [
            "",
            "State that the statistics were computed by this project, giving the version or commit you used.",
        ]
    return "\n".join(lines)


def population_text(source: dict) -> str:
    pop, meas = source["population"], source["measurement"]
    items = [pop["description"]]
    if pop["n"] is not None:
        measured = f"{pop['n']:,}"
        if "n_eligible" in pop:
            measured += f" of {pop['n_eligible']:,} eligible"
        items.append(f"Sample: {measured}. Sampling: {pop['sampling']}. Exclusions: {pop['exclusions']}")
    else:
        items.append(f"Sampling: {pop['sampling']}. Exclusions: {pop['exclusions']}")
    items += [
        f"**Method:** {meas['method']}",
        f"**Device:** {meas['device']}",
        f"**Protocol:** {meas['protocol']}",
    ]
    items += source.get("analysis", [])
    return bullets(items)


def sentence(label: str, text: str) -> str:
    """'Label: text.' without doubling a full stop the text already ends with."""
    text = text.strip()
    return f"{label}: {text}" if text.endswith(".") else f"{label}: {text}."


def measured_text(prov: dict) -> str:
    return " ".join(
        [
            f"Measured from {prov['figure'].strip().rstrip('.')}.",
            sentence("Precision", prov["precision"]),
            sentence("Method", prov["method"]),
            sentence("Script", prov["script"]),
        ]
    )


def source_section(metric_id: str, source: dict, folder: Path) -> str:
    folder_url = f"../metrics/{metric_id}/sources/{source['id']}"
    form = source["statistic_form"]
    head = [f"## {source['title']}", ""]
    if source["review_status"] == "draft":
        head += [f"*{DRAFT_NOTE}*", ""]
    head += [f"**Origin:** {ORIGIN_TEXT[source['origin']]}"]
    if form != "none":
        head[-1] += f" · **Data:** [data.csv]({folder_url}/data.csv)"
    if source["origin"] == "digitised":
        head += ["", measured_text(source["provenance"])]
    parts = ["\n".join(head)]
    if source["caveats"]:
        parts.append("### Read this before using the numbers\n\n" + bullets(source["caveats"]))
    parts.append("### Population and method\n\n" + population_text(source))
    if form == "none":
        parts.append("### Statistics\n\nThis source reports no statistics for this metric.")
    else:
        data = pd.read_csv(folder / "data.csv", keep_default_na=False, na_values=[""])
        parts.append("### Tables\n\n" + tables_section(data, form))
    if "verification" in source:
        parts.append("### Check against a published reference\n\n" + source["verification"])
    parts.append("### How to cite\n\n" + citation_text(source))
    parts.append("### Reproduce\n\n" + reproduce_text(source, folder_url))
    return "\n\n".join(parts)


def render_entry(metric: dict, root: Path) -> str:
    folder = root / "metrics" / metric["id"] / "sources"
    sources = [(load_json(p / "source.json"), p) for p in sorted(folder.iterdir()) if p.is_dir()]
    columns = ["Source", "Population", "How measured", "n", "Use for", "Do not use for"]
    rows = pd.DataFrame([[cell(c) for c in source_table_row(s)] for s, _ in sources], columns=columns)
    parts = [
        f"# {metric['name']}",
        f"**Units:** {metric['units']} · **Category:** {metric['category']}",
        metric["definition"],
        "## Which source should I use?\n\n" + markdown_table(rows),
    ]
    if metric["comparison_note"]:
        parts.append(metric["comparison_note"])
    parts += [source_section(metric["id"], s, p) for s, p in sources]
    return "\n\n".join(parts) + "\n"


def render_catalog(metrics: list[dict], root: Path) -> str:
    lines = [
        "# Catalog",
        "",
        "| # | Metric | Category | Status | Source or candidate | Note |",
        "|---|---|---|---|---|---|",
    ]
    for m in sorted(metrics, key=lambda m: m["priority"]):
        if m["status"] == "available":
            name = f"[{m['name']}](entries/{entry_name(m['id'])}.md)"
            folder = root / "metrics" / m["id"] / "sources"
            titles = [load_json(p / "source.json")["title"] for p in sorted(folder.iterdir()) if p.is_dir()]
            sources, note = "; ".join(titles), m["comparison_note"]
        else:
            name, sources, note = m["name"], "; ".join(m["candidate_sources"]), m["note"]
        lines.append(f"| {m['priority']} | {name} | {m['category']} | {m['status']} | {sources} | {note} |")
    return "\n".join(lines) + "\n"


def render(root: Path = ROOT) -> list[str]:
    """Write entries/ and CATALOG.md under root; return the entry file names written."""
    problems = validate(root)
    if problems:
        raise SystemExit("\n".join([*problems, "not rendering: fix the problems above"]))
    metrics = [load_json(p) for p in sorted((root / "metrics").glob("*/metric.json"))]
    entries = root / "entries"
    entries.mkdir(exist_ok=True)
    written = []
    for metric in metrics:
        if metric["status"] == "available":
            name = f"{entry_name(metric['id'])}.md"
            (entries / name).write_text(render_entry(metric, root), encoding="utf-8", newline="\n")
            written.append(name)
    for stale in entries.glob("*.md"):
        if stale.name not in written:
            stale.unlink()
    (root / "CATALOG.md").write_text(render_catalog(metrics, root), encoding="utf-8", newline="\n")
    return written


if __name__ == "__main__":
    print("wrote " + ", ".join(f"entries/{n}" for n in render()) + " and CATALOG.md")
