# Health Data Distributions

Population and subgroup distributions of health measures, in one consistent,
citable format, for people planning health and wearable research.

Each entry gives percentiles and descriptive statistics by subgroup, states
exactly how the measure was taken and who was measured, and points to the
primary source to cite.

**Status:** proof of concept. Two entries have sources
([resting heart rate and pulse](entries/resting-heart-rate.md)); thirteen more are listed as
planned in the [catalog](CATALOG.md).

## Why

Sizing a validation study needs the spread of the measure and the makeup of
the population. Those numbers exist, but scattered across survey tables, PDF
reports, and papers, in different formats and with the measurement method
often left implicit. The measurement method matters most: a clinic pulse, an
ECG heart rate, and a wearable's overnight resting heart rate are three
different distributions.

## What an entry contains

- A tidy CSV: one row per subgroup and statistic, with `estimate`, `ci_low`,
  `ci_high`, and the number of people measured.
- A page stating what was measured and how, the population, the exclusions,
  the caveats that limit how the numbers may be used, and how to cite.
- The script that produced it from public data.

## Layout

```
metrics/<metric_id>/metric.json                 what the metric is, status, how its sources compare
metrics/<metric_id>/sources/<source_id>/        source.json, data.csv, evidence.md (not for recomputed)
entries/          one generated page per available metric (do not edit)
CATALOG.md        the metric list, generated from the metric.json files (do not edit)
pipelines/        survey.py (weighted statistics), one script per recomputed source,
                  validate.py (format checks), render.py (entries and catalog)
tests/
```

A metric can have several sources, shown side by side, and each source states
its statistics as it reports them (percentiles, mean and SD, category
proportions, or none for a documented gap).

Every source has one of four origins: recomputed from public data by a script
here, transcribed from a table or text, digitised from a published figure
(measured against the axis, with its precision and script stated and labelled
as such), or a gap (a documented absence).

## Reproduce the resting pulse entry

```sh
python -m venv .venv
.venv/Scripts/python -m pip install numpy pandas pytest

mkdir -p raw/nhanes && cd raw/nhanes
for f in 2015/DataFiles/DEMO_I 2015/DataFiles/BPX_I 2017/DataFiles/DEMO_J 2017/DataFiles/BPX_J; do
  curl -sLO "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/$f.xpt"
done
cd ../..

.venv/Scripts/python pipelines/resting_pulse.py
.venv/Scripts/python pipelines/validate.py
.venv/Scripts/python pipelines/render.py
.venv/Scripts/python -m pytest
```

## Other raw data

```sh
# NHANES 2003-2004 dermatology examination (Fitzpatrick type from photographs)
cd raw/nhanes && for f in DEX_C DEMO_C; do
  curl -sLO "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2003/DataFiles/$f.xpt"; done; cd ../..
.venv/Scripts/python pipelines/fitzpatrick_nhanes.py

# SCIN dermatology image dataset: the two tables only, no images
mkdir -p raw/scin && cd raw/scin && for f in scin_cases.csv scin_labels.csv; do
  curl -sLO "https://storage.googleapis.com/dx-scin-public-data/dataset/$f"; done; cd ../..
.venv/Scripts/python pipelines/scin_skin_tone.py
```

Sources measured from published figures are described in
[pipelines/digitise/README.md](pipelines/digitise/README.md).

## Related resources

Found in a brief search in October 2026; not an exhaustive review.

- CDC/NCHS reference reports from NHANES (anthropometry, resting pulse):
  authoritative, but published as PDF tables, one measure per report.
- R packages `nhanesA` and `RNHANES`: retrieve NHANES data and compute
  weighted quantiles, for people who will do the analysis themselves.
- All of Us Data Browser and UK Biobank Showcase: summary views of single
  cohorts, not designed as subgroup reference tables.
- 1000 Norms Project: musculoskeletal and neurological reference values from
  one Australian cohort.
- Published wearable norms from single large cohorts (for example gait and
  sleep measures from UK Biobank wrist sensors).

None of these is a cross-source lookup with a common format and explicit
measurement-method notes, which is the gap this project aims at.

## Limits

- Statistics are computed by this project, not by the data owners. For a
  regulatory or ethics submission, cite the primary source and state the
  version of this project used.
- Intervals reflect sampling uncertainty only, not measurement error or
  non-response.
