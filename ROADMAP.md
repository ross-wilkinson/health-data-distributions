# Roadmap: the portfolio project group

One plan for five linked public projects, with progress against each
milestone. It lives in this repository because this is where the state
documents are; it covers all five.

**Last updated:** 2026-10-06. Update this file whenever a milestone changes
status. State documents in `.github/directives/` are dated snapshots; this is
the running record.

Status: **Done**, **Started**, **Not started**, **Blocked** (says on what),
**Unknown** (needs Ross to say).

## Why these projects

Public portfolio work that combines machine learning, signal processing, and
dashboarding, tied to Ross's background in biomechanics and wearable
validation, on questions that are useful to others and that industry tends
not to publish.

## At a glance

| | Project | Folder | End point | Progress |
|---|---|---|---|---|
| A | Validation toolkit | `C:\repos\agreekit` | Citable release: PyPI, docs, DOI, JOSS paper | 1 of 6 milestones, plus extras |
| B | Pulse oximeter accuracy by skin tone | `C:\repos\spo2-skin-tone` | Public dashboard, reproducible repo, preprint | 0 of 8; one script written |
| C | Designer repeated-measures module | `C:\repos\validation-study-designer` (clone from GitHub) | Live module on the existing site | 0 of 3 |
| D | Wearable change-point false-alarm benchmark | none yet | Open benchmark and dashboard | 0 of 6 |
| E | Health data distributions | `C:\repos\health-data-distributions` | Public reference site for 15 metrics with usage guidance | 5 of 12 |

Project E was not in the original plan. It was proposed and started on
2026-10-06 and absorbed most of that session.

---

## A. Validation toolkit (agreekit)

**End point:** a citable release on PyPI with documentation, a Zenodo DOI, and
a Journal of Open Source Software submission.

| # | Milestone | Done when | Status |
|---|---|---|---|
| A1 | Core estimands | Bias, limits of agreement, variance components, error percentiles, equivalence test, with tests | **Done** |
| A2 | Oximetry prerequisites | A check for error that varies across the measurement range, limits that vary with the range, and a Bland-Altman plot | **Not started** |
| A3 | Analytic repeated-measures interval | Zou 2013 implemented and reaching 95% coverage in simulation, checked against a reference | **Not started** (no copy of the paper yet) |
| A4 | Subgroup comparison | Differences between groups with intervals; partial pooling for small subgroups | **Not started** |
| A5 | First public release | Name checked on PyPI, docs site, worked example, CI | **Not started** |
| A6 | Paper and DOI | Submitted, after project B has used the package for real | **Not started** |

Done beyond the plan: heart-rate reporting metrics (MAPE, within-tolerance
shares); categorical agreement for sleep stages; 15 tests against numbers
printed in Carkeet 2015 and Bland and Altman 2007. 44 tests pass.

Open: a copyright question on the published data used as test fixtures
(`agreekit/PAPERS.md`).

## B. Pulse oximeter accuracy by skin tone

**End point:** a public dashboard, a reproducible repository, and a preprint.

| # | Milestone | Done when | Status |
|---|---|---|---|
| B1 | Clearance | The Google-era question in the Designer's `HANDOFF.md` section 7 is resolved, and the data terms are confirmed to allow publishing aggregates | **Not started** |
| B2 | Inventory | `scripts/inventory.py` run by Ross on the download and its report reviewed | **Started**: script written and tested on synthetic data; download not confirmed complete |
| B3 | Analysis plan | Estimands, subgroups, thresholds, and small-cell rules committed before any results are seen | **Not started** |
| B4 | Data pipeline | Cleaning, pairing, exclusions; run locally by Ross | **Not started** |
| B5 | Core analysis | Agreement by device, skin tone, and saturation band; occult hypoxemia rate | **Not started** (needs A2) |
| B6 | Modelling | Error as a function of covariates; signal-quality work if waveforms exist | **Not started** |
| B7 | Dashboard | On Tableau Public with a clinical disclaimer, reviewed by a clinician or peer | **Not started** |
| B8 | Write-up | Preprint, linked from the Designer | **Not started** |

Standing rule: Claude never reads subject-level OpenOximetry data. Claude
writes scripts, Ross runs them, only schemas and aggregates come back.

Project E's skin tone entry feeds this directly: it documents how unreliable
"Fitzpatrick V to VI" is as a recruitment or stratification variable.

## C. Designer repeated-measures module

**End point:** a live module on the Validation Study Designer that sizes a
study by subjects and samples per subject.

| # | Milestone | Done when | Status |
|---|---|---|---|
| C1 | Model and fixtures | Effective sample size and precision from between- and within-subject variance, tested against agreekit | **Not started** |
| C2 | Page | Inputs, chart, and methods text in the site's existing style | **Not started** |
| C3 | Worked example | Real variance components from the oximetry analysis | **Not started** (needs B5) |

The local folder is an extracted copy without git history. Clone the
repository from GitHub before working on it.

## D. Wearable change-point false-alarm benchmark

**End point:** an open benchmark and dashboard reporting false alarms per
person-year for wearable alarm rules. Prompted by Lautman et al. 2026.

| # | Milestone | Done when | Status |
|---|---|---|---|
| D1 | Start collecting | Garmin Instinct 2X Solar and Fitbit Inspire 3 worn together, with a dated confounder log | **Unknown**. Time-critical: baseline accrues only with calendar time |
| D2 | Export pipelines | Automated pulls from both devices | **Not started** |
| D3 | Dataset survey | Open records with many months per person identified | **Not started** |
| D4 | Simulation study | False-positive rates of standard change-point tests under autocorrelation and seasonality; detectors that handle them | **Not started** |
| D5 | Benchmark | Alarm rules run over the open records | **Not started** |
| D6 | Dashboard and write-up | Published | **Not started** |

No folder exists. The Lautman paper is held in this repository's
`raw/papers/` until one does.

## E. Health data distributions

**End point:** a public reference site giving population and subgroup
distributions for 15 health metrics, each source with stated measurement
method, population, and expert guidance on what it should and should not be
used for, citable with a DOI.

| # | Milestone | Done when | Status |
|---|---|---|---|
| E1 | Prior-art check | Existing resources surveyed and the gap confirmed | **Done** (a brief search, not an exhaustive review) |
| E2 | Single-entry proof | One metric end to end from public data | **Done**: resting pulse from NHANES |
| E3 | Format proofs | Every kind of source the catalog needs has been entered at least once | **Done**: recomputed, transcribed, digitised, and documented gap |
| E4 | Working process | Directive, implement, audit loop with written rules | **Done**: directives 01 to 05 |
| E5 | Skin tone entry | Sources across Fitzpatrick, Monk, and instrument measures | **Done** as far as available data allow: 12 sources; Monk and ITA remain gaps for any defined population |
| E6 | Presentation fixes | Directive 06 implemented and audited; comparison notes rewritten as points | **Started**: directive written, not run |
| E7 | Guidance review | Ross has reviewed `use_for`, `do_not_use_for`, and `caveats` for every source | **Not started**: all 15 are draft |
| E8 | Copyright cleared | Every row in `COPYRIGHT_QUESTIONS.md` closed | **Not started**: 10 open here, 1 in agreekit |
| E9 | Remaining metrics | The other 13 catalogued metrics have at least one source or a documented gap | **Not started**: 2 of 15 metrics have sources |
| E10 | Hosting decision | Stack chosen | **Not started**. Recommendation on record: GitHub Pages, DuckDB and Parquet, Zenodo; Tableau Public optional |
| E11 | Website | Entries browsable and searchable online | **Not started**: pages are generated Markdown |
| E12 | First public release | Published with a DOI | **Blocked** on E7 and E8 |

## Order of work

| Phase | Work | Status |
|---|---|---|
| Now | D1 (start wearing), B1 (clearance), A2 (range dependence and plot) | None confirmed done |
| When the oximetry download finishes | B2, then B3 | B2 started |
| Main build | B4 to B6, with A3 and A4 as the analysis demands | Not started |
| Publish | B7, B8, A5, A6, C1 to C3 | Not started |
| Then | D2 to D6 | Not started |
| Alongside, as time allows | E6 to E12 | E6 started |

The original order did not include project E. On 2026-10-06 it ran ahead of
everything else. Whether it keeps priority over B is a decision for Ross.

## Decision gates

| Gate | If it goes the wrong way | Status |
|---|---|---|
| After B1 | If clearance is refused, the oximetry project needs reframing before more work goes in | Open |
| After B2 | If there are no waveforms, B is a statistics and dashboard project and the signal-processing weight moves to D | Open |
| After D3 | If no open dataset has long enough records, D becomes a methods paper on simulation and Ross's own data | Open |
| Before E12 | If a copyright row cannot be cleared, that source is reduced to a citation and guidance with no numbers | Open |

## Parked

Road-surface vibration map from a bike-mounted IMU; open sleep-staging
benchmark with subgroup reporting; cycling durability modelling. The NHANES
accelerometry reference curves became the `daily_activity` placeholder in
project E.
