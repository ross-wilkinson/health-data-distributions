# Directive 02: Wearable-cohort source for resting heart rate

**Execute:** After directive 01 is implemented.
**Purpose:** Prove the transcribed-from-publication format and the
multi-source comparison, on the metric that already has a recomputed source.

## Rationale

The existing source is a clinic pulse count. Wearable studies need the
distribution of resting heart rate as a wearable reports it, which is a
different quantity. Putting the two side by side, with guidance on which to
use when, is the core of what this project offers.

## Task

Add one source under `metrics/resting_heart_rate/sources/`, transcribed from a
published, openly licensed study of a large wearable cohort.

**Candidate to check first:** Quer G, Gouda P, Galarnyk M, Topol EJ,
Steinhubl SR. Inter- and intraindividual variability in daily resting heart
rate and its associations with age, sex, sleep, BMI, and time of year:
retrospective, longitudinal cohort study of 92,457 adults. *PLOS ONE* 2020.
This citation is from memory: confirm every detail of it against the paper
itself before using it. If it does not tabulate or state a usable
distribution, find another openly licensed large wearable cohort that does,
and say why you switched.

Requirements:

1. Open and read the paper (and supplement if needed). Transcribe only
   numbers that appear as text or in tables. Nothing read off a figure,
   nothing computed, nothing from memory.
2. `evidence.md`: for every distinct locator used in `data.csv`, the locator,
   the URL, and a verbatim quote or the table rows as published.
3. `source.json` per directive 01. `statistic_form` is whatever the paper
   reports. `population.sampling` is almost certainly `"convenience sample"`;
   describe who the cohort is and how that differs from the US population.
   Under `measurement`, state the device family and how the manufacturer or
   authors define resting heart rate, quoting the paper's own definition in
   `evidence.md`. Record the license exactly as the paper states it.
4. Draft `use_for`, `do_not_use_for`, and `caveats` from what the paper
   supports. `review_status` is `"draft"`.
5. Set `comparison_note` in `metrics/resting_heart_rate/metric.json`: what
   differs between the clinic pulse and the wearable source (method,
   population, timing), and state the difference in central values only using
   numbers present in the two `data.csv` files.
6. Add this source's check to the tests only by adding
   `tests/test_resting_heart_rate.py` (for example: every `locator` in
   `data.csv` appears in `evidence.md`).

## Do not touch

The NHANES source folder, `pipelines/survey.py`, `pipelines/validate.py`,
`pipelines/render.py`, other metrics, existing test files. If the format from
directive 01 cannot represent what the paper reports, stop and report that
rather than changing the format.

## Acceptance checks

1. `.venv/Scripts/python -m pytest` passes.
2. `.venv/Scripts/python pipelines/validate.py` exits 0.
3. `.venv/Scripts/python pipelines/render.py` runs, and
   `entries/resting-heart-rate.md` shows two sources in the comparison table.
4. Every row of the new `data.csv` has a `locator` that appears in
   `evidence.md` with a verbatim quote containing that number.
5. The implementation report lists every number you wanted but could not
   transcribe, and why.

## Implementation report

Implemented by Pragma, 2026-10-06. No git; folder is not a repository.

### Paper used

The candidate citation was correct in every detail checked. Verified against the article page and two independent full-text XML renderings (PLOS JATS and Europe PMC JATS):

Quer G, Gouda P, Galarnyk M, Topol EJ, Steinhubl SR. Inter- and intraindividual variability in daily resting heart rate and its associations with age, sex, sleep, BMI, and time of year: Retrospective, longitudinal cohort study of 92,457 adults. *PLOS ONE* 2020;15(2):e0227709, published 5 February 2020. DOI 10.1371/journal.pone.0227709 (PMC7001906, PMID 32023264).

Licence, as stated: "© 2020 Quer et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited." (The Europe PMC XML also gives the CC BY 4.0 URL; the article text itself says only "Creative Commons Attribution License".)

I did not switch papers. The paper has no numbered tables and no supplementary files. Its numbers are in running text, so the locators are section headings, not table numbers.

### Files created or edited

- Created `metrics/resting_heart_rate/sources/quer_2020_fitbit_92457_adults/source.json`, `data.csv`, `evidence.md`.
- Edited `metrics/resting_heart_rate/metric.json` (`comparison_note` only).
- Created `tests/test_resting_heart_rate.py` (4 tests: every locator has an evidence section; every estimate and n appears inside a blockquote of its section; source is transcribed, draft, CC BY, DOI correct; comparison_note contains no "typically lower" and contains the NHANES mean 72.41 and the cohort mean 65.5, both read from the data files).
- Regenerated `entries/resting-heart-rate.md` and `CATALOG.md` with `pipelines/render.py` (not hand-edited).

### What was transcribed

`statistic_form` is `moments`. `data.csv` has one row: sex All, age_band All, n 92457, statistic `mean`, estimate 65.5, no interval, locator `Results, Resting heart rate (mean); Methods, Population (n)`.

- 65.5: Results, "Resting heart rate", first sentence: "The mean RHR for all individuals over all available monitored days was 65.5 ± 7.7 bpm, with a minimum and maximum average RHR for each individual ranging between 39.7 and 108.6 bpm, respectively."
- 92,457: Methods, "Population": "The final analysis population included 92,457 individuals with at least two RHR measurement days per week for a minimum of 35 weeks."
- The Abstract rounds the mean to 65 ("Mean daily RHR was 65 beats per minute (bpm), with a range of 40 to 109 bpm among all individuals."); recorded in `verification`.

### Acceptance checks (real output)

1. `.venv/Scripts/python -m pytest`: `21 passed in 0.73s` (7 test_survey + 10 test_format + 4 test_resting_heart_rate). PASS.
2. `.venv/Scripts/python pipelines/validate.py`: prints `ok`, exit 0. PASS.
3. `.venv/Scripts/python pipelines/render.py`: `wrote entries/resting-heart-rate.md and CATALOG.md`, exit 0. The "Which source should I use?" table in `entries/resting-heart-rate.md` has two rows (NHANES, Quer et al.). PASS.
4. Locator and quote: the single CSV locator appears as a `###` heading in `evidence.md`; the blockquotes under it contain "65.5" and "92,457" (enforced by `test_every_estimate_and_n_is_quoted_in_its_evidence_section`). In addition, all 18 blockquotes in `evidence.md` were string-matched, after whitespace normalisation, against both independent full-text renderings: 18 of 18 found in both (0 missing). The Data Availability quote lives in the XML metadata, so that one was matched against the two XML files. PASS.
5. See the next section. PASS (listed).
- `ruff check --line-length 110 tests/test_resting_heart_rate.py`: `All checks passed!`

### Two-fetch agreement

WebFetch of the PMC page versus the PLOS page: the numbers agreed (65.5 ± 7.7, 39.7 and 108.6, 50 to 80 and 53 to 82, 92,457, 45.8 ± 14.4, 63% women). One WebFetch answer was wrong in two places: it said "± indicates standard deviation throughout" and gave "women 65.5±7.7". Neither is in the paper (checked in the XML text). I therefore did not rely on WebFetch for anything transcribed, and took every quote from the two XML downloads, which I searched directly.

### Numbers wanted but not entered, and why

- 7.7 as `sd`: the paper writes "65.5 ± 7.7" and never says what "±" is (the words "standard deviation" appear only for other quantities). Entering it as `sd` would be an interpretation. It is quoted verbatim in `evidence.md` and in the source.json caveats and analysis. If Ross accepts reading it as an SD, add one row `All,All,92457,sd,7.7,,,<same locator>`.
- Women's and men's means, and means by age, BMI, sleep: figures only (Fig 2 dashed lines, Fig 3). Not in the text.
- "95% of men had an RHR between 50 and 80 bpm ... women between 53 and 82 bpm": the paper does not say these are the central 95% (P2.5 and P97.5), so they are not entered as percentiles; quoted in a caveat only.
- Minimum and maximum individual averages, 39.7 and 108.6: the format has no min/max statistic.
- Sex counts 57,836 women and 34,621 men (Fig 2 caption text): no statistic is attached to them, so no row. Quoted in evidence.md.
- Any percentile of the overall distribution: not in the paper's text.

### Judgment calls

1. Mean only, no SD row (above). Consequence: the `moments` table renders mean and n only.
2. `n` is 92,457 (individuals). The paper says the mean is "for all individuals over all available monitored days" and does not say whether this is a mean of per-person averages or of pooled daily values; stated as a caveat. The 32,741,021 daily values appear in evidence only.
3. The locator is a section description joined with a semicolon for the two sources (mean and n), because the format allows one locator per row and the paper has no tables. It contains commas, so the CSV field is quoted.
4. Columns `sex` and `age_band` only (both All); no `race_ethnicity` because the paper reports none.
5. `population.years` is "March 2016 to February 2018"; `age_range` is "18 to 100 (self-reported); average 45.8"; `n_eligible` is not set (the 200,000 starting sample is not an eligible-population count in the NHANES sense; it is in the description text instead).
6. `exclusions` lists the paper's rules and says no medication or condition exclusion "is stated" (absence in the text read, not a claim about the cohort).
7. `comparison_note` was rewritten. It states the two means (NHANES 72.41, median 72.0; Fitbit 65.5) and says the wearable mean is the lower, with no subtraction and no "typically lower" generalisation. It says the gap cannot be attributed to method alone because population, method and timing all differ. The test enforces that the two numbers match the data files.
8. `use_for`, `do_not_use_for`, `caveats` are my drafts; `review_status` is "draft".
9. `provenance.url` and `citation.url` are the PLOS article page; the DOI is given separately.
10. I removed a `validate(ROOT) == []` test from my test file before finishing, so it cannot fail on another agent's half-finished metric (acceptance check 2 covers validation).

### Directive notes (possible defects)

- The directive expects a distribution ("mean and SD" or percentiles). This paper gives one mean and an unlabelled "±" in text. The format coped, but the entry is a single mean, a weak comparator for the NHANES percentile tables.
- The NHANES `source.json` (which I was told not to edit) still says in `do_not_use_for` and in the first caveat that wearable resting heart rate "is typically lower". That is the same unsupported claim the audit flagged in `metric.json`. Sentinel or Ross should decide whether to reword it.
- Absence statements in my source.json ("no sampling weights ... described in the text read") are about my reading of the paper, not claims about the study.

## Audit

**Result: pass.** Audited 2026-10-06 against an independent download of the
paper's full text (Europe PMC, PMC7001906), not against the report.

| Check | Result | Evidence |
|---|---|---|
| 1. pytest | pass | new and existing tests pass |
| 2. validate | pass | re-run after directive 03 completes, see directive 03 audit |
| 3. Two sources rendered | pass | comparison table has two rows |
| 4. Locator and quote | pass | "65.5 ± 7.7 bpm" and "92,457 individuals" found verbatim in the independent download; title, licence sentence, and the 50 to 80 and 53 to 82 sentence also match |
| 5. Untranscribed numbers listed | pass | |

Findings:
- The paper has no tables, so this source holds one mean. It proves the
  transcribed format but is a thin comparator. A wearable cohort that
  tabulates percentiles by age and sex is still wanted (backlog).
- **Decision for Ross:** the paper writes "65.5 ± 7.7 bpm" and never defines
  "±". Pragma left 7.7 out as an SD, correctly under invariant 3. The same
  sentence style gives age as "45.8 ± 14.4 years", which can only be an SD,
  so reading 7.7 as the SD of per-person mean resting heart rate is very
  likely right. Entering it needs an expert call and a caveat.
- Audit fix applied by Sentinel: the two "typically lower" statements in the
  NHANES `source.json` were replaced with wording that makes no unsourced
  comparison.
