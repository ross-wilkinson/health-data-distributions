# Roadmap: tools for people who measure humans

**Last updated:** 2026-10-06 (rewritten around the north star below; the
earlier version organised the same work as five separate projects, A to E).
Update this file whenever a milestone changes status. State documents in
`.github/directives/` are dated snapshots; this is the running record. It
lives in this repository but covers the whole group.

Status: **Done**, **Started**, **Not started**, **Blocked** (says on what),
**Unknown** (needs Ross to say).

## North star

Someone validating a measurement of the human body, whether a wearable
feature, a sensor, or a field test, should be able to do the whole job with
free, citable tools that say plainly what each number is fit for:

| Stage | The question | Tool | State today |
|---|---|---|---|
| 1. Plan | How many people, which people, how long, how precise? | Validation Study Designer | Live |
| 2. Know what is normal | What does this measure look like in the population I care about? | Health Data Distributions | 2 of 15 metrics, unpublished |
| 3. Know the device | How accurate have devices like this been shown to be? | Wearable Validation Evidence Index | Idea |
| 4. Analyse | Did it agree, and how sure am I? | agreekit | Working package, unreleased |
| 5. Know the bar | What have regulators accepted for a feature like this? | Regulatory Precedent Lookup | Idea |

**The end point for the group:** all five tools live, citable, and linking to
one another at the point where a user would need the next one; and at least
one published case study that went through every stage using them.

What every tool shares, and what makes the group worth more than its parts:

- Each number is traceable to a public source or a script.
- Each source states how it was measured, in whom, and what it should and
  should not be used for.
- Things that look comparable but are not are kept apart and explained.
- Gaps are documented as gaps.

Why Ross: a decade of human measurement research, validation of consumer
wearable features at scale, and two regulatory submissions. The aim is to
ease the load on people doing that work without those resources.

## At a glance

| | Piece | Folder | Milestones done |
|---|---|---|---|
| S1 | Validation Study Designer | `C:\repos\validation-study-designer` (clone from GitHub) | Live site; 0 of 4 new |
| S2 | Health Data Distributions | `C:\repos\health-data-distributions` | 5 of 13 |
| S3 | Wearable Validation Evidence Index | none yet | 0 of 6 |
| S4 | agreekit | `C:\repos\agreekit` | 1 of 6 |
| S5 | Regulatory Precedent Lookup | none yet | 0 of 6 |
| H | The hub that joins them | none yet | 0 of 4 |
| CS1 | Case study: pulse oximeter accuracy by skin tone | `C:\repos\spo2-skin-tone` | 0 of 8 |
| CS2 | Case study: cadence-lock checker | `C:\repos\cadence-lock-investigator` | 0 of 4 new |
| CS3 | Case study: wearable change-point false alarms | none yet | 0 of 6 |

Old letters, for reading the 2026-10-06 state document: A is S4, B is CS1,
C is S1, D is CS3, E is S2.

---

## S1. Plan: Validation Study Designer

**End point:** the planning tool covers repeated-measures studies and points
users to the other four stages.

| # | Milestone | Done when | Status |
|---|---|---|---|
| S1.0 | Existing site | Five modules and two explainers live | **Done** (before this roadmap) |
| S1.1 | Repeated-measures model | Effective sample size and precision from between- and within-subject variance, tested against agreekit | **Not started** |
| S1.2 | Repeated-measures page | Inputs, chart, and methods text in the site's style | **Not started** |
| S1.3 | Worked example from real data | Variance components from case study CS1 | **Not started** (needs CS1.5) |
| S1.4 | Informed defaults | Presets for spread and subgroup mix drawn from S2, and for accepted thresholds from S5, each linked to its source | **Not started** (needs S2 and S5 content) |

The local folder is an extracted copy without git history. Clone from GitHub
before working on it.

## S2. Know what is normal: Health Data Distributions

**End point:** a public reference site giving population and subgroup
distributions for 15 metrics, each source with stated method, population, and
reviewed guidance, citable with a DOI.

| # | Milestone | Done when | Status |
|---|---|---|---|
| S2.1 | Prior-art check | Existing resources surveyed and the gap confirmed | **Done** (a brief search, not exhaustive) |
| S2.2 | Single-entry proof | One metric end to end from public data | **Done**: resting pulse from NHANES |
| S2.3 | Format proofs | Every kind of source entered at least once | **Done**: recomputed, transcribed, digitised, documented gap |
| S2.4 | Working process | Directive, implement, audit loop with written rules | **Done**: directives 01 to 05 |
| S2.5 | Skin tone entry | Sources across Fitzpatrick, Monk, and instrument measures | **Done** as far as data allow: 12 sources; Monk and ITA remain gaps for any defined population |
| S2.6 | Presentation fixes | Directive 06 implemented and audited; comparison notes rewritten as points | **Started**: directive written, not run |
| S2.7 | Guidance review | Ross has reviewed the guidance on every source | **Not started**: all 15 are draft |
| S2.8 | Copyright cleared | Every row in `COPYRIGHT_QUESTIONS.md` closed | **Not started**: 10 open |
| S2.9 | Body dimensions for device design | Wrist, hand, foot, and head dimensions by sex and percentile from a public survey, with notes on how the surveyed population differs from consumers | **Not started**. Fills the `wrist_circumference` placeholder |
| S2.10 | Remaining metrics | Each of the 15 has at least one source or a documented gap | **Not started**: 2 of 15 |
| S2.11 | Hosting decision | Stack chosen | **Not started**. On record: GitHub Pages, DuckDB and Parquet, Zenodo |
| S2.12 | Website | Entries browsable and searchable online | **Not started** |
| S2.13 | First public release | Published with a DOI | **Blocked** on S2.7 and S2.8 |

## S3. Know the device: Wearable Validation Evidence Index

**End point:** a public index of published accuracy studies for consumer
wearables, per device and metric, in one format: reference method, protocol,
population, and agreement statistics as reported, with guidance on what each
study does and does not show.

| # | Milestone | Done when | Status |
|---|---|---|---|
| S3.1 | Prior-art check | Living reviews, endpoint libraries, and existing databases surveyed | **Not started**. Gate: if this is already well covered, S3 becomes a guided pointer page |
| S3.2 | Entry format | A study-by-device-by-metric-by-condition record that holds statistics as reported and flags which agreekit could recompute | **Not started**. Start from S2's format and validator |
| S3.3 | Copyright approach | A decision on what may be reproduced from papers, informed by how S2.8 resolves | **Not started** |
| S3.4 | Single-metric proof | One metric and condition (for example wrist heart rate at rest) across several devices, every number located and quoted | **Not started** |
| S3.5 | First complete metric | All studies found for that metric entered, with the search logged | **Not started** |
| S3.6 | Site and release | Browsable, citable, linked from S2 entries for the same metric | **Not started** |

Standing rule: public literature only. Nothing from Ross's own unpublished
validation work.

## S4. Analyse: agreekit

**End point:** a citable release on PyPI with documentation, a Zenodo DOI, and
a Journal of Open Source Software submission.

| # | Milestone | Done when | Status |
|---|---|---|---|
| S4.1 | Core estimands | Bias, limits of agreement, variance components, error percentiles, equivalence test, with tests | **Done** |
| S4.2 | Range dependence and plot | A check for error that varies across the measurement range, limits that vary with it, and a Bland-Altman plot | **Not started**. Needed by CS1 |
| S4.3 | Analytic repeated-measures interval | Zou 2013 implemented, reaching 95% coverage in simulation | **Not started** (no copy of the paper yet) |
| S4.4 | Subgroup comparison | Differences between groups with intervals; partial pooling for small subgroups | **Not started** |
| S4.5 | First public release | Name checked on PyPI, docs site, worked example, CI | **Not started** |
| S4.6 | Paper and DOI | Submitted, after CS1 has used the package for real | **Not started** |

Done beyond the plan: heart-rate reporting metrics; categorical agreement for
sleep stages; 15 tests against numbers printed in Carkeet 2015 and Bland and
Altman 2007. 44 tests pass. One copyright question is open on the published
data used as test fixtures (`agreekit/PAPERS.md`).

## S5. Know the bar: Regulatory Precedent Lookup

**End point:** a public lookup of what regulators have accepted for wearable
health features: accuracy criteria, sample sizes, demographic composition, and
reference methods, each taken from a public decision document and quoted.

| # | Milestone | Done when | Status |
|---|---|---|---|
| S5.1 | Public-only protocol | A written rule that every fact cites a public document and nothing comes from memory of confidential work; Ross confirms there is no conflict with ongoing obligations | **Not started**. Gate: nothing else in S5 starts before this |
| S5.2 | Source survey and prior art | The public databases and document types identified; what they do and do not contain; any existing lookup found | **Not started** |
| S5.3 | Single-entry proof | One cleared feature end to end, every field located in the decision document and quoted | **Not started** |
| S5.4 | Format and validator | Reusing S2's machinery; fields for criterion, sample size, demographics, reference method, and what the document leaves unstated | **Not started** |
| S5.5 | First set | Every decision found for one feature type (for example irregular rhythm notification), with the search logged | **Not started** |
| S5.6 | Site and release | Browsable, citable, linked from the Designer's defaults | **Not started** |

The source documents are government publications, so the copyright questions
that slowed S2 should not arise. That is to be confirmed in S5.2, not assumed.

## H. The hub

**End point:** one page that presents the five stages as a workflow, links
each live tool, and says how to cite them.

| # | Milestone | Done when | Status |
|---|---|---|---|
| H.1 | Name and framing | A name for the group and one paragraph saying who it is for | **Not started**. Decision for Ross |
| H.2 | Landing page | Live, linking whichever tools are live (the Designer is already) and marking the rest as coming | **Not started**. Cheap, and useful as soon as it exists |
| H.3 | Cross-links | Each tool links to the next stage at the point a user needs it | **Not started** |
| H.4 | Shared citation and look | A common citation format and enough visual consistency to read as one family | **Not started** |

---

## Case studies

Each case study is a piece of applied work that uses the tools and shows they
hold up. CS1 is the one intended to pass through all five stages.

### CS1. Pulse oximeter accuracy by skin tone

**End point:** a public dashboard, a reproducible repository, and a preprint.

| # | Milestone | Done when | Status |
|---|---|---|---|
| CS1.1 | Clearance | The Google-era question in the Designer's `HANDOFF.md` section 7 resolved; data terms confirmed to allow publishing aggregates | **Not started** |
| CS1.2 | Inventory | `scripts/inventory.py` run by Ross on the download and its report reviewed | **Started**: script written; download not confirmed complete |
| CS1.3 | Analysis plan | Estimands, subgroups, thresholds, and small-cell rules committed before any results are seen. Uses S1 for size and precision, S2's skin tone entry for stratification, S5 for thresholds | **Not started** |
| CS1.4 | Data pipeline | Cleaning, pairing, exclusions; run locally by Ross | **Not started** |
| CS1.5 | Core analysis | Agreement by device, skin tone, and saturation band with agreekit; occult hypoxemia rate | **Not started** (needs S4.2) |
| CS1.6 | Modelling | Error as a function of covariates; signal-quality work if waveforms exist | **Not started** |
| CS1.7 | Dashboard | Public, with a clinical disclaimer, reviewed by a clinician or peer | **Not started** |
| CS1.8 | Write-up | Preprint that names each stage of the workflow it used | **Not started** |

Standing rule: Claude never reads subject-level OpenOximetry data. Claude
writes scripts, Ross runs them, only schemas and aggregates come back.

### CS2. Cadence-lock checker

**End point:** a public tool where a runner uploads a file and sees whether
their wrist heart rate locked onto their cadence, with a write-up of how often
it happens. This is the group's signal-processing and machine-learning piece.

| # | Milestone | Done when | Status |
|---|---|---|---|
| CS2.0 | Existing investigation | Ross's own multi-device runs, protocol, and detection work | **Done** (before this roadmap; not reviewed in detail on 2026-10-06) |
| CS2.1 | Labelled data beyond one person | A plan, and then data, for runs from several people with a chest-strap or ECG reference | **Not started**. Gate: without this the tool cannot be trusted |
| CS2.2 | Validated detector | Sensitivity and specificity against the reference, reported with agreekit, by subject | **Not started** |
| CS2.3 | Browser tool | Upload a run file, get a result and a plain explanation; nothing leaves the browser | **Not started** |
| CS2.4 | Release and write-up | Public, with the validation results and their limits | **Not started** |

### CS3. Wearable change-point false alarms

**End point:** an open benchmark and dashboard reporting false alarms per
person-year for wearable alarm rules. Prompted by Lautman et al. 2026.

| # | Milestone | Done when | Status |
|---|---|---|---|
| CS3.1 | Start collecting | Garmin Instinct 2X Solar and Fitbit Inspire 3 worn together, with a dated confounder log | **Unknown**. Time-critical: baseline accrues only with calendar time |
| CS3.2 | Export pipelines | Automated pulls from both devices | **Not started** |
| CS3.3 | Dataset survey | Open records with many months per person identified | **Not started** |
| CS3.4 | Simulation study | False-positive rates of standard change-point tests under autocorrelation and seasonality; detectors that handle them | **Not started** |
| CS3.5 | Benchmark | Alarm rules run over the open records | **Not started** |
| CS3.6 | Dashboard and write-up | Published | **Not started** |

---

## Order of work

The group is large for one person: 59 milestones, 8 done, two of which
predate this roadmap. The order below
favours unblocking, then finishing what exists, then one complete pass
through the workflow, before starting the two new tools in earnest.

| Phase | Goal | Milestones |
|---|---|---|
| 0. Unblock | Clear the things only Ross can do, which cost little and gate much | CS3.1 (start wearing), CS1.1 (clearance), S5.1 (confidentiality check), S2.8 (copyright rows), H.1 (name) |
| 1. Make what exists presentable | Two tools a visitor can use and understand | S2.6, S2.7, S4.2, H.2 |
| 2. One full pass | The oximetry case study through every stage it can reach | CS1.2 to CS1.5, S1.1 to S1.3, S4.4 as needed |
| 3. Prove the two new tools | A single convincing entry for each, and both prior-art gates passed | S5.2 to S5.4, S3.1 to S3.4 |
| 4. Publish the core | First releases | S2.9 to S2.13, S4.5, S4.6, CS1.6 to CS1.8, H.3, H.4 |
| 5. Widen | Fill the new tools; the other two case studies | S5.5, S5.6, S3.5, S3.6, S1.4, CS2, CS3.2 to CS3.6 |

## Decision gates

| Gate | If it goes the wrong way | Status |
|---|---|---|
| S5.1, confidentiality | If Ross cannot be confident of building S5 from public documents alone, S5 is dropped and stage 5 becomes a short guide to finding precedent | Open |
| CS1.1, clearance | If refused, the oximetry case study is reframed before more work goes in | Open |
| S3.1, prior art | If the evidence index is already well covered elsewhere, S3 becomes a guided pointer page | Open |
| CS1.2, inventory | If the data have no waveforms, CS1 is a statistics and dashboard study and the signal-processing weight rests on CS2 | Open |
| S2.8, copyright | A source whose row cannot be cleared is reduced to a citation and guidance with no numbers | Open |
| CS2.1, data | If runs from several people cannot be obtained, CS2 is published as a single-person investigation, not a checker | Open |
| CS3.3, datasets | If no open dataset has long enough records, CS3 becomes a methods paper on simulation and Ross's own data | Open |

## Outside the north star

Worth doing, but not part of the workflow and not scheduled.

- **World Food Map as a citable reference.** Downloadable country briefs and
  data, a methods page, a DOI. Already built in the same spirit; small effort.
- **Test reliability reference.** Typical error and minimal detectable change
  for common field and lab tests. A plausible sixth tool, or a section of S3.
- **Distribution-free price-move tables** from `volatility-underwriting`.
  Lowest priority: data licences, the line between reference and financial
  advice, and distance from Ross's field.
- **Parked earlier:** road-surface vibration map from a bike-mounted IMU; open
  sleep-staging benchmark; cycling durability modelling.
