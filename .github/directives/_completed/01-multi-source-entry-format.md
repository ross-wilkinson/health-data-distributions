# Directive 01: Multi-source entry format

**Priority:** Blocks directives 02 and 03.
**Scope:** Restructure only. No statistic may change.

## Rationale

The proof entry assumes one source per metric and percentiles as the only
kind of statistic. The catalog needs several sources per metric shown side by
side, statistics exactly as a source reports them (percentiles, mean and SD,
category proportions, or nothing at all for a documented gap), and usage
guidance as structured fields rather than prose inside a renderer.

## Target layout

```
metrics/<metric_id>/metric.json
metrics/<metric_id>/sources/<source_id>/source.json
metrics/<metric_id>/sources/<source_id>/data.csv        (absent when statistic_form is "none")
metrics/<metric_id>/sources/<source_id>/evidence.md     (required when origin is "transcribed" or "gap")
```

`catalog.json` is deleted; the 15 `metric.json` files replace it.

### `metric.json`

| Field | Required | Notes |
|---|---|---|
| `id` | yes | equals the folder name |
| `name`, `category`, `units` | yes | |
| `priority` | yes | integer 1 to 15, the current catalog order |
| `status` | yes | `"available"` if at least one source folder exists, else `"planned"` |
| `definition` | available only | one or two sentences: what the metric is |
| `comparison_note` | available only | how the sources differ and why they must not be merged; may be `""` with one source |
| `candidate_sources`, `note` | planned only | carried over from `catalog.json` unchanged |

### `source.json`

| Field | Required | Notes |
|---|---|---|
| `id`, `title` | yes | `id` equals the folder name |
| `origin` | yes | `"recomputed"`, `"transcribed"`, or `"gap"` |
| `statistic_form` | yes | `"percentiles"`, `"moments"`, `"proportions"`, or `"none"` |
| `population` | yes | object: `description`, `country`, `years`, `age_range`, `n`, `sampling` (`"probability sample"`, `"convenience sample"`, or `"other"`), `exclusions` |
| `measurement` | yes | object: `method`, `device`, `protocol` |
| `use_for`, `do_not_use_for`, `caveats` | yes | arrays of strings; may be empty only for `"gap"` |
| `review_status` | yes | `"draft"` or `"reviewed"` |
| `citation` | yes | object: `text`, `url`, `license`; `doi` optional |
| `provenance` | yes | `"recomputed"`: `pipeline`, `raw_files`. `"transcribed"`: `url`, `accessed` (date). `"gap"`: `accessed` |
| `verification` | no | free text: any cross-check against another published value |

For a `"gap"` source, `population` and `measurement` describe what was looked
for, and `n` is `null`.

### `data.csv`

Columns, in this order: any subgroup columns (for the existing entry: `sex`,
`age_band`, `race_ethnicity`, each `All` when not split), then `n`,
`statistic`, `estimate`, `ci_low`, `ci_high`. `ci_low` and `ci_high` are empty
when the source gives no interval. When `statistic_form` is `"proportions"`
there is also a `category` column and `statistic` is `proportion`. When
`origin` is `"transcribed"` there is a final `locator` column (for example
`Table 2`) on every row.

## Changes

1. Create `metrics/` with 15 `metric.json` files from `catalog.json`.
   Rename the first metric: id `resting_heart_rate`, name
   `Resting heart rate and pulse`. Keep the other 14 ids.
2. Move the existing entry to
   `metrics/resting_heart_rate/sources/nhanes_2015_2018_clinic_pulse/`.
   `data.csv` must be byte-identical to the current
   `data/resting_pulse/nhanes_2015_2018.csv`. Update
   `pipelines/resting_pulse.py` to write there. Delete `data/`.
3. Move every statement currently hard-coded in `pipelines/render.py`
   (`RESTING_PULSE_HEADER`, `RESTING_PULSE_FOOTER`) into that source's
   `source.json` fields. Set `review_status` to `"draft"`. Record the eligible
   and measured counts (11,268 and 10,848) in the JSON rather than in code.
4. Add `pipelines/validate.py`: checks every `metric.json`, `source.json`, and
   `data.csv` against the rules above, prints each problem, and exits non-zero
   if there are any. Importable as a function so tests can call it.
5. Rewrite `pipelines/render.py` to be generic, with no metric-specific text:
   - `entries/<metric-id-with-hyphens>.md` for each available metric: name,
     units, definition; a **Which source should I use?** table with one row
     per source (source, population, how measured, n, use for, do not use
     for); the comparison note; then one section per source with caveats,
     population and method, tables, verification, citation, and how to
     reproduce. Show "Guidance: draft, not yet expert-reviewed" on any source
     whose `review_status` is `"draft"`.
   - Table layout by `statistic_form`: `percentiles` as now (mean with
     interval, SD, P5 to P95, one table per value of `sex`, plus one by
     `race_ethnicity`); `moments` as mean, SD and n per subgroup;
     `proportions` as one row per category; `none` as no table.
   - `CATALOG.md` from the `metric.json` files, ordered by `priority`.
6. Tests in `tests/test_format.py`: the repository validates cleanly; the
   validator reports a missing required field, a bad enumeration value, a
   transcribed `data.csv` without `locator`, and a transcribed source without
   `evidence.md` (build these cases in a temporary directory).
7. Update the layout section of `README.md`.

## Do not touch

`pipelines/survey.py`, `tests/test_survey.py`, `raw/`, `CLAUDE.md`,
`.claude/`. Do not add sources, metrics, or a website.

## Acceptance checks

1. `.venv/Scripts/python -m pytest` passes, including the 7 existing tests.
2. `.venv/Scripts/python pipelines/validate.py` exits 0.
3. `.venv/Scripts/python pipelines/resting_pulse.py` reproduces a `data.csv`
   byte-identical to the one committed by this directive.
4. `entries/resting-heart-rate.md` shows the same numbers as the current
   `entries/resting-pulse.md` (which is then deleted) and every caveat that
   page had.
5. `CATALOG.md` has 15 rows in the current order.
6. `pipelines/render.py` contains no metric names or metric-specific prose.

## Implementation report

Implemented by Pragma. No git; folder is not a repository.

### What changed

Created:
- `metrics/<id>/metric.json` x 15 (generated once from `catalog.json`; `resting_pulse` renamed `resting_heart_rate`, name `Resting heart rate and pulse`; priority 1 to 15 in the old catalog order; `note` and `candidate_sources` carried over unchanged for the 14 planned metrics).
- `metrics/resting_heart_rate/sources/nhanes_2015_2018_clinic_pulse/source.json`
- `metrics/resting_heart_rate/sources/nhanes_2015_2018_clinic_pulse/data.csv` (moved, not rewritten)
- `pipelines/validate.py`
- `tests/test_format.py` (10 tests)

Rewritten: `pipelines/render.py` (generic, reads `metrics/`; refuses to render if `validate()` reports problems; deletes stale `entries/*.md` it did not write), `entries/resting-heart-rate.md` and `CATALOG.md` (generated).

Edited: `pipelines/resting_pulse.py` (docstring and `OUT` path only), `README.md` (layout block, link to the new entry, `validate.py` added to the reproduce steps).

Deleted: `catalog.json`, `data/` (the CSV was moved out first), `entries/resting-pulse.md` (replaced by `entries/resting-heart-rate.md`).

Not touched: `pipelines/survey.py`, `tests/test_survey.py`, `raw/`, `CLAUDE.md`, `.claude/`, directives 02 and 03.

### Acceptance checks (real output)

1. `.venv/Scripts/python -m pytest -v`: `17 passed in 0.87s` (7 `test_survey.py` + 10 `test_format.py`).
2. `.venv/Scripts/python pipelines/validate.py`: prints `ok`, exit code 0.
3. `data.csv` sha256 before the move: `bf48212ab8ce650e7df22193d431017c98feabce5837a9a318c84fdd71d08792`. After the move: same. After re-running `.venv/Scripts/python pipelines/resting_pulse.py` (output `examined adults: 11,268; with a pulse reading: 10,848` and `wrote ...data.csv: 30 subgroups`): `bf48212ab8ce650e7df22193d431017c98feabce5837a9a318c84fdd71d08792`. Identical.
4. All 30 table rows (header rows excluded) of the old `entries/resting-pulse.md` and the new `entries/resting-heart-rate.md` compared with `diff`: identical, so every number is unchanged. Every caveat, population and method bullet, the CDC cross-check text (71.2 and 73.6) and the citation are present (grep of each phrase, one or more hits each). A copy of the old entry was kept in the session scratchpad for the comparison.
5. `CATALOG.md`: 15 data rows, `#` column 1 to 15 in order; metric names diff identical to the old catalog except row 1 (renamed, as directed).
6. `grep -niE 'pulse|nhanes|heart|beats|resting|wearable'` on `pipelines/render.py`: no hits. The only metric-adjacent strings are the column names the format itself defines (`sex`, `race_ethnicity`, `age_band` and their display labels).
- `.venv/Scripts/python -m ruff check --line-length 110 .`: `All checks passed!`
- Extra: rendered synthetic sources of form `moments`, `proportions`, `none` (gap) and a transcribed percentiles subset in a temp directory; all rendered without error (not kept as a test).

### Could not do / open items

- Licence: no licence name is stated on the NCHS pages I could open. `citation.license` holds a verbatim quote of the NCHS data-use restriction ("Use the data in this dataset for statistical reporting and analysis only.", https://www.cdc.gov/nchs/data_access/restrictions.htm, fetched 2026-10-06) and says no licence name is stated. Ross should confirm the wording.
- The Ostchega et al. means (71 and 74) in `verification` are carried over unchanged from the old page. I did not re-open that report and there is no `evidence.md` for them. Audit may want that.

### Judgment calls (directive silent or ambiguous)

1. `source.json` has two fields beyond the directive's table: `analysis` (optional array of strings: weights, bootstrap, minimum cell size, no non-response adjustment) and `population.n_eligible` (11,268). The directive had no field for statistical-method statements; `population.n` is 10,848. The validator allows these and checks their type.
2. `use_for` and `do_not_use_for` did not exist on the old page. I drafted them from the old caveats (clinic pulse is not a wearable reference; not a healthy range) and set `review_status` to `"draft"`. `definition` and `comparison_note` in the metric file are also my wording.
3. The old "What was measured" paragraph is split into `measurement.method` (30-second count doubled, `BPXPLS`), `measurement.protocol` (5 minutes seated rest at the mobile examination centre) and `measurement.device`. The old page named no device; I wrote "Counted by an examiner; no device is recorded in this entry" rather than invent one.
4. The "420 without a reading" figure is no longer printed as a number; the entry says "10,848 of 11,268 eligible" and the analysis line says "No adjustment was made for examined adults without a pulse reading". The old "examined adults" wording became "eligible" because render is generic.
5. Table headings are generic: `All, by age`, `Female, by age`, `Male, by age`, `By race and ethnicity` (old: "All adults", "Women", "Men"). The `n examined` column is now `n`. Rows come in CSV order with `All` first, so there is no hard-coded age order.
6. Tables use `####` under a `### Tables` heading; the Which-source table joins `use_for` items with `<br>`; the draft notice appears both in the Which-source table cell and in the source section.
7. `priority` is validated as a unique integer of at least 1 (not capped at 15) so adding metrics later does not break validation.
8. Validator extras beyond the listed rules: id equals folder name for both metric and source; `status` must match whether a source folder exists; `definition` and `comparison_note` not allowed on planned, `candidate_sources` and `note` not allowed on available; `data.csv` required unless form is `none` and forbidden when it is `none`; for non-gap sources `n` must be an integer, for gap it must be null; `accessed` must be `YYYY-MM-DD`; CSV `n` integer, estimate numeric, interval both-or-neither with `ci_low <= estimate <= ci_high`, no repeated (subgroup, statistic) rows, statistic names restricted by form (`mean`, `sd`, `p<number>` for percentiles; `mean`, `sd` for moments; `proportion` for proportions); `category` column required for proportions and not allowed otherwise; `locator` must be the last column and non-empty on every row when transcribed.
9. The `category` column position is unspecified in the directive; the validator accepts it anywhere before `n`.
10. Rendering for transcribed data adds a trailing `Source location` column from `locator`; percentile columns not present in a source are omitted rather than shown empty; `moments` tables show the mean with its interval when given.
11. `render.py` runs the validator first and aborts on problems, and deletes any `entries/*.md` it did not just write (so the old `resting-pulse.md` cannot linger).
12. `CATALOG.md` "Note" column for available metrics is `comparison_note`; for planned metrics it is `note`. "Source or candidate" for available metrics is the source titles.

### Directive notes (possible defects)

- The directive gives no field for the statistical-method statements (weights, bootstrap, cell-size rule) or for `n_eligible`; the `source.json` table is closed over those. Suggest adding both.
- `use_for` and `do_not_use_for` cannot come from "move what is hard-coded in render.py", because the old render had none; the directive implies a pure move but needs new draft text.
- `population.exclusions` and `measurement.device` are required but may be unknown or not applicable for some sources; consider stating a convention such as "Not stated".
- Acceptance check 3 says "byte-identical to the one committed by this directive", but nothing is committed (no git); I used the sha256 given in the task.
- Check 6 ("no metric names or metric-specific prose") cannot be tested mechanically; the format's own column names (`sex`, `race_ethnicity`, `age_band`) are necessarily in render.py.

## Audit

**Result: pass.** Audited 2026-10-06 by re-running every check, not from the report.

| Check | Result | Evidence |
|---|---|---|
| 1. pytest | pass | 17 passed |
| 2. validate | pass | prints `ok`, exit 0 |
| 3. CSV reproduction | pass | sha256 `bf48212a…08792` before and after re-running the pipeline; matches the pre-directive file |
| 4. Same numbers | pass | all 30 table rows identical to the saved pre-directive page; caveats present |
| 5. Catalog | pass | 15 rows |
| 6. Generic renderer | pass | no metric-specific text |

Accepted additions to the format: `analysis` (optional array) and
`population.n_eligible`. Convention adopted for required fields a source does
not state: the literal string `Not stated`.

Carried to backlog:
- The claim that wearable resting heart rate is "typically lower" than a
  clinic pulse is asserted without a source. Directive 02 must replace it with
  numbers from the two data files or remove it.
- The Ostchega cross-check (71 and 74 beats/min) has no `evidence.md`. It was
  confirmed from a web search summary of the CDC report, not from the report
  itself.
- NHANES licence wording needs Ross's confirmation.
