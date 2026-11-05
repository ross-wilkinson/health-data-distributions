"""Export static API endpoints, Tidy CSVs, and BibTeX citations for Health Data Distributions.

Usage:
    python pipelines/export_api.py [--out public/data]

Generates:
    <out>/catalog.json                - Global index of all 15 metrics, statuses, and metadata
    <out>/metrics/<metric_id>.json     - Strongly typed distribution endpoints with subgroup slices
    <out>/metrics/<metric_id>.csv      - Unified Tidy CSV export with source_id column
    <out>/citations/<metric_id>.bib    - BibTeX citations for all sources within the metric
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

# Academy module mapping for curriculum integration
ACADEMY_MAPPINGS: dict[str, dict[str, str]] = {
    "resting_heart_rate": {
        "module": "Module 3 (Repeated Measures) & Module 5 (Cadence Lock)",
        "methodological_warning": (
            "Never pool clinic seated pulse (NHANES 30s count) with ambulatory/nocturnal wearable resting heart rate (Fitbit). "
            "A 7 bpm physiological offset exists between seated clinic exam counts and waking basal wearable rates."
        ),
    },
    "skin_tone": {
        "module": "Module 4: Regulatory SpO2 & Demographic Quotas (ISO 80601-2-61)",
        "methodological_warning": (
            "Never pool self-reported Fitzpatrick phototypes with dermatologist photograph ratings or instrument ITA. "
            "Never apply hierarchical shrinkage across skin tones (ADR-006: anti-whitewashing invariant)."
        ),
    },
    "spo2": {
        "module": "Module 4: Regulatory SpO2 & Demographic Quotas (ISO 80601-2-61)",
        "methodological_warning": (
            "Never pool normoxic ambient baseline saturation with controlled laboratory hypoxic desaturation (70%-100%). "
            "Never pool transmission finger-clip hospital monitors with reflective wrist optical sensors."
        ),
    },
    "body_size": {
        "module": "Module 2 & Hardware Tiers (ADR-012 Tier 1: Mechanical/Coupling)",
        "methodological_warning": (
            "Wrist and arm circumference directly govern sensor optical coupling and motion artifact vulnerability. "
            "Subcutaneous adipose tissue (BMI) alters optical photon path lengths."
        ),
    },
    "heart_rate_variability": {
        "module": "Module 3: HIIT Repeated Measures & Variance Decomposition (sigma_b vs sigma_w)",
        "methodological_warning": (
            "Never pool daytime short-epoch (5-minute seated) ECG HRV with nocturnal continuous PPG HRV. "
            "Autonomic circadian rhythms and breathing rates create non-stationary baselines."
        ),
    },
    "sleep_duration": {
        "module": "Meridian PulseBand 2 Feature Validation",
        "methodological_warning": (
            "Self-reported questionnaire sleep hours and wearable actigraphy/PPG sleep duration systematically diverge. "
            "Questionnaires reflect time in bed; sensors reflect detected immobility."
        ),
    },
    "sleep_architecture": {
        "module": "Meridian PulseBand 2 Feature Validation",
        "methodological_warning": (
            "Never pool gold-standard in-lab polysomnography (PSG 30s EEG epochs) with wearable surrogate stage heuristics. "
            "Wake after sleep onset (WASO) is systematically underestimated by optical/motion sensors."
        ),
    },
}


def clean_nan(val: Any) -> Any:
    """Recursively replace NaN/float('nan') with None for clean JSON serialization."""
    if isinstance(val, float) and pd.isna(val):
        return None
    if isinstance(val, dict):
        return {k: clean_nan(v) for k, v in val.items()}
    if isinstance(val, list):
        return [clean_nan(v) for v in val]
    return val


def parse_source_data(csv_path: Path, form: str) -> tuple[list[str], list[dict[str, Any]], pd.DataFrame | None]:
    """Parse a source's data.csv into structured subgroup rows and a pandas DataFrame."""
    if not csv_path.exists():
        return [], [], None

    df = pd.read_csv(csv_path)
    if "n" not in df.columns:
        return [], [], df

    subgroup_cols = list(df.columns[: list(df.columns).index("n")])
    keys = [*subgroup_cols, "n"]

    subgroups: list[dict[str, Any]] = []
    for key, frame in df.groupby(keys, sort=False):
        key_tuple = key if isinstance(key, tuple) else (key,)
        subgroup_dict = dict(zip(subgroup_cols, key_tuple[:-1]))
        n_val = int(key_tuple[-1]) if pd.notna(key_tuple[-1]) else None

        stats_dict: dict[str, Any] = {}
        for _, row in frame.iterrows():
            stat_name = str(row["statistic"])
            stats_dict[stat_name] = {
                "estimate": clean_nan(row["estimate"]),
                "ci_low": clean_nan(row["ci_low"]) if "ci_low" in row else None,
                "ci_high": clean_nan(row["ci_high"]) if "ci_high" in row else None,
            }

        # Convenience summary for UI widgets
        summary: dict[str, Any] = {}
        if "mean" in stats_dict:
            summary["mean"] = stats_dict["mean"]["estimate"]
            if stats_dict["mean"]["ci_low"] is not None and stats_dict["mean"]["ci_high"] is not None:
                summary["ci_mean"] = [stats_dict["mean"]["ci_low"], stats_dict["mean"]["ci_high"]]
        if "sd" in stats_dict:
            summary["sd"] = stats_dict["sd"]["estimate"]
        if "p50" in stats_dict:
            summary["median"] = stats_dict["p50"]["estimate"]
        if "p25" in stats_dict and "p75" in stats_dict:
            p25 = stats_dict["p25"]["estimate"]
            p75 = stats_dict["p75"]["estimate"]
            if p25 is not None and p75 is not None:
                summary["iqr"] = round(p75 - p25, 2)
                summary["p25"] = p25
                summary["p75"] = p75
        if "p5" in stats_dict:
            summary["p5"] = stats_dict["p5"]["estimate"]
        if "p95" in stats_dict:
            summary["p95"] = stats_dict["p95"]["estimate"]
        if "proportion" in stats_dict:
            summary["proportion"] = stats_dict["proportion"]["estimate"]
            if stats_dict["proportion"]["ci_low"] is not None and stats_dict["proportion"]["ci_high"] is not None:
                summary["ci_proportion"] = [
                    stats_dict["proportion"]["ci_low"],
                    stats_dict["proportion"]["ci_high"],
                ]

        subgroups.append({
            "subgroup": subgroup_dict,
            "n": n_val,
            "statistics": stats_dict,
            "summary": summary,
        })

    return subgroup_cols, subgroups, df


def generate_bibtex(source_id: str, title: str, citation: dict[str, Any]) -> str:
    """Generate a clean BibTeX entry from citation metadata."""
    cite_text = citation.get("text", "")
    url = citation.get("url", "")
    doi = citation.get("doi", "")
    license_str = citation.get("license", "")

    # Extract year if present
    year_match = re.search(r"\b(19\d{2}|20\d{2})\b", cite_text)
    year = year_match.group(1) if year_match else "2026"

    # Identify author / title snippet
    first_period = cite_text.find(".")
    author = cite_text[:first_period].strip() if first_period > 0 else "Unknown Author"

    bibtex_lines = [
        f"@misc{{{source_id},",
        f"  title = {{{{{title}}}}},",
        f"  author = {{{author}}},",
        f"  year = {{{year}}},",
    ]
    if doi:
        bibtex_lines.append(f"  doi = {{{doi}}},")
    if url:
        bibtex_lines.append(f"  url = {{{url}}},")
    if license_str:
        bibtex_lines.append(f"  note = {{License: {license_str}}},")
    bibtex_lines.append(f"  howpublished = {{{cite_text}}}")
    bibtex_lines.append("}\n")
    return "\n".join(bibtex_lines)


def export_all(out_dir: Path) -> dict[str, Any]:
    """Compile raw metrics into static JSON, Tidy CSV, and BibTeX files."""
    metrics_out = out_dir / "metrics"
    citations_out = out_dir / "citations"
    metrics_out.mkdir(parents=True, exist_ok=True)
    citations_out.mkdir(parents=True, exist_ok=True)

    catalog_entries: list[dict[str, Any]] = []
    metrics_root = ROOT / "metrics"

    for metric_folder in sorted(metrics_root.iterdir()):
        if not metric_folder.is_dir():
            continue
        metric_json_path = metric_folder / "metric.json"
        if not metric_json_path.exists():
            continue

        with open(metric_json_path, encoding="utf-8") as f:
            metric_data = json.load(f)

        metric_id = metric_data["id"]
        sources_folder = metric_folder / "sources"

        sources_list: list[dict[str, Any]] = []
        tidy_frames: list[pd.DataFrame] = []
        bibtex_entries: list[str] = []

        if sources_folder.exists() and sources_folder.is_dir():
            for src_folder in sorted(sources_folder.iterdir()):
                if not src_folder.is_dir():
                    continue
                src_json_path = src_folder / "source.json"
                if not src_json_path.exists():
                    continue

                with open(src_json_path, encoding="utf-8") as f:
                    src_meta = json.load(f)

                source_id = src_meta["id"]
                subgroup_cols, subgroups, src_df = parse_source_data(
                    src_folder / "data.csv", src_meta.get("statistic_form", "none")
                )

                if src_df is not None and not src_df.empty:
                    df_copy = src_df.copy()
                    df_copy.insert(0, "source_id", source_id)
                    tidy_frames.append(df_copy)

                citation = src_meta.get("citation", {})
                bibtex_text = generate_bibtex(source_id, src_meta.get("title", source_id), citation)
                bibtex_entries.append(bibtex_text)

                sources_list.append({
                    "id": source_id,
                    "title": src_meta.get("title", ""),
                    "origin": src_meta.get("origin", "gap"),
                    "statistic_form": src_meta.get("statistic_form", "none"),
                    "group": src_meta.get("group"),
                    "population": clean_nan(src_meta.get("population", {})),
                    "measurement": clean_nan(src_meta.get("measurement", {})),
                    "analysis": clean_nan(src_meta.get("analysis", [])),
                    "use_for": clean_nan(src_meta.get("use_for", [])),
                    "do_not_use_for": clean_nan(src_meta.get("do_not_use_for", [])),
                    "caveats": clean_nan(src_meta.get("caveats", [])),
                    "review_status": src_meta.get("review_status", "draft"),
                    "citation": clean_nan(citation),
                    "provenance": clean_nan(src_meta.get("provenance", {})),
                    "verification": clean_nan(src_meta.get("verification")),
                    "subgroup_columns": subgroup_cols,
                    "subgroups": clean_nan(subgroups),
                })

        academy_info = ACADEMY_MAPPINGS.get(metric_id, {})
        methodological_warning = academy_info.get(
            "methodological_warning",
            metric_data.get("comparison_note", "Measurement method is part of the data. Do not pool."),
        )

        # Build full metric JSON payload
        full_metric_payload = {
            "id": metric_id,
            "name": metric_data.get("name", ""),
            "category": metric_data.get("category", ""),
            "units": metric_data.get("units", ""),
            "priority": metric_data.get("priority", 99),
            "status": metric_data.get("status", "planned"),
            "definition": metric_data.get("definition", ""),
            "comparison_note": metric_data.get("comparison_note"),
            "methodological_warning": methodological_warning,
            "academy_module": academy_info.get("module"),
            "candidate_sources": metric_data.get("candidate_sources", []),
            "sources": sources_list,
            "tidy_csv_url": f"/data/metrics/{metric_id}.csv" if tidy_frames else None,
            "bibtex_url": f"/data/citations/{metric_id}.bib" if bibtex_entries else None,
        }

        # Write metric.json
        out_metric_file = metrics_out / f"{metric_id}.json"
        with open(out_metric_file, "w", encoding="utf-8") as f:
            json.dump(full_metric_payload, f, indent=2, ensure_ascii=False)

        # Write tidy CSV if sources present
        if tidy_frames:
            combined_df = pd.concat(tidy_frames, ignore_index=True)
            out_csv_file = metrics_out / f"{metric_id}.csv"
            combined_df.to_csv(out_csv_file, index=False, lineterminator="\n")

        # Write BibTeX if entries present
        if bibtex_entries:
            out_bib_file = citations_out / f"{metric_id}.bib"
            out_bib_file.write_text("\n\n".join(bibtex_entries), encoding="utf-8")

        # Add to catalog index
        sources_summary = [
            {
                "id": s["id"],
                "title": s["title"],
                "origin": s["origin"],
                "statistic_form": s["statistic_form"],
                "group": s.get("group"),
                "n": s["population"].get("n"),
            }
            for s in sources_list
        ]

        catalog_entries.append({
            "id": metric_id,
            "name": metric_data.get("name", ""),
            "category": metric_data.get("category", ""),
            "units": metric_data.get("units", ""),
            "priority": metric_data.get("priority", 99),
            "status": metric_data.get("status", "planned"),
            "definition": metric_data.get("definition", ""),
            "source_count": len(sources_list),
            "sources": sources_summary,
            "academy_module": academy_info.get("module"),
            "methodological_warning": methodological_warning,
        })

    # Sort catalog by priority
    catalog_entries.sort(key=lambda m: m["priority"])

    catalog_payload = {
        "version": "1.0.0",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_metrics": len(catalog_entries),
        "available_metrics": sum(1 for m in catalog_entries if m["status"] == "available"),
        "planned_metrics": sum(1 for m in catalog_entries if m["status"] == "planned"),
        "metrics": catalog_entries,
    }

    catalog_file = out_dir / "catalog.json"
    with open(catalog_file, "w", encoding="utf-8") as f:
        json.dump(catalog_payload, f, indent=2, ensure_ascii=False)

    print(f"Exported API to {out_dir}:")
    print(f"  - Catalog: {catalog_file.name} ({len(catalog_entries)} metrics)")
    print(f"  - Metrics: {len(list(metrics_out.glob('*.json')))} JSON, {len(list(metrics_out.glob('*.csv')))} CSV")
    print(f"  - Citations: {len(list(citations_out.glob('*.bib')))} BibTeX files")
    return catalog_payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Health Data Distributions static API.")
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "public" / "data",
        help="Output directory (default: public/data)",
    )
    args = parser.parse_args()
    export_all(args.out)


if __name__ == "__main__":
    main()
