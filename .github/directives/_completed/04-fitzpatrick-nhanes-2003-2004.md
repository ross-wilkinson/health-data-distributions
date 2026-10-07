# Directive 04: Fitzpatrick skin type in US adults, NHANES 2003-2004

**Purpose:** The first probability-sample source for `skin_tone`, recomputed
from public data.

## Rationale

The only Fitzpatrick source so far is two numbers from the abstract of a 1999
study of Italian men aged 18 to 19. NHANES 2003-2004 photographed adults aged
20 to 59 and had dermatologist readers assign a Fitzpatrick type to each
person from the images. The file is public and uses the same survey design as
the resting pulse source, so the existing weighting and interval code applies.

## What Sentinel already established (verify, do not assume)

- `raw/nhanes/DEX_C.xpt` and `raw/nhanes/DEMO_C.xpt` are downloaded.
  Documentation: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2003/DataFiles/DEX_C.htm
- 2,992 examined adults aged 20 to 59 are in `DEX_C`; 2,696 have a reading
  from both readers (`DEX1FITZ`, `DEX2FITZ`).
- **The two readers often disagree.** They gave the same type for 1,657 of
  the 2,696 people, adjacent types for most of the rest, and
  a third "consensus" value (`DEX6FITZ`) exists for only 260. The
  documentation's consensus rule sends only "reject" combinations to
  consensus, so most disagreements were accepted as they stood.
- Code 9 appears in a few rows. Find its meaning in the documentation.
- Design variables are `SDMVSTRA`, `SDMVPSU`, weight `WTMEC2YR`. One cycle, so
  the weight is not halved. Race and ethnicity is `RIDRETH1`.

## Design decision

Do **not** invent a single "final" skin type. The disagreement between readers
is the most important thing a user needs to know about this source. Report the
distribution separately for each reader:

- Subgroup column `rater` with values `Reader 1` and `Reader 2`.
- Further subgroup columns `sex` and `race_ethnicity` (`All` when not split).
  Report: all adults; by sex; by race and ethnicity. No age split.
- `category` is `Type I` to `Type VI`. `statistic` is `proportion`.
- `n` is the number of people in the subgroup with a reading from that reader
  (the denominator), the same on each of the six rows.
- Weighted proportions with 95% intervals from the Rao-Wu replicate weights,
  built once on everyone examined, as `pipelines/resting_pulse.py` does.
- Subgroups with fewer than 50 people are not reported.

## Changes

1. `pipelines/survey.py`: add one function for weighted category proportions
   with replicate-based intervals. Do not change the existing functions.
2. `pipelines/fitzpatrick_nhanes.py`: writes
   `metrics/skin_tone/sources/nhanes_2003_2004_fitzpatrick_image_readers/data.csv`.
   Print the eligible, read, and missing counts when run.
3. `source.json` for that source, `origin` `"recomputed"`. Read the
   documentation page and quote from it (in `source.json` text fields; there
   is no `evidence.md` for a recomputed source) for: who the readers were,
   what they looked at, which body sites, the exclusion criteria, what code 9
   means, and the consensus rule. Where the page does not say, write
   `Not stated`.
4. In `analysis`, state the reader agreement, computed by the pipeline and
   printed by it: the unweighted share of people given the same type by both
   readers, and the share within one type. Put these two numbers in
   `source.json` from the pipeline's output, not from this directive.
5. Draft `use_for`, `do_not_use_for`, `caveats`; `review_status` `"draft"`.
   The caveats must cover at least: reader disagreement; type assigned from
   photographs by readers, not from a person's reported reaction to sun and
   not by instrument; ages 20 to 59 only; data from 2003-2004; people examined
   but not read, with no adjustment; and that the survey's own documentation
   describes the US distribution as unknown (quote it).
6. `metrics/skin_tone/metric.json`: update `comparison_note` to place this
   source beside the Italian one and the two gap sources. Do not delete the
   Italian source.
7. Tests in a new `tests/test_fitzpatrick_nhanes.py`: the new survey function
   against a hand calculation and with equal weights against plain shares;
   proportions sum to 1 within each rater and subgroup; `n` is constant
   within each rater and subgroup.
8. Verification: the published analysis of this file is Keiser et al. 2012
   (already row 1 of `ACCESS_REQUESTS.md`, paywalled). Try once to open it.
   If still blocked, say so in `verification` and leave the row open. Do not
   take its numbers from a search summary.

## Do not touch

`pipelines/validate.py`, `pipelines/render.py`, `pipelines/resting_pulse.py`,
existing functions in `pipelines/survey.py`, existing tests, other metrics,
the three existing `skin_tone` sources. If the format cannot hold this
(for example the `rater` column), stop and report rather than changing it.

## Acceptance checks

1. `.venv/Scripts/python -m pytest` passes.
2. `.venv/Scripts/python pipelines/validate.py` exits 0.
3. `.venv/Scripts/python pipelines/fitzpatrick_nhanes.py` run twice produces
   a byte-identical `data.csv` (report the sha256).
4. `.venv/Scripts/python pipelines/render.py` runs and `entries/skin-tone.md`
   shows the new source with both readers.
5. The unweighted reader counts printed by the pipeline match Sentinel's:
   2,696 read by both, 1,657 identical.
6. The implementation report gives the weighted Type I to VI shares for all
   adults for each reader, and lists any source added to
   `ACCESS_REQUESTS.md`.

## Implementation report

Implemented by Pragma. No git; folder is not a repository. One acceptance check (1) fails because of an existing test; see check 1.

### Files

Created:
- `pipelines/fitzpatrick_nhanes.py`
- `metrics/skin_tone/sources/nhanes_2003_2004_fitzpatrick_image_readers/source.json`
- `metrics/skin_tone/sources/nhanes_2003_2004_fitzpatrick_image_readers/data.csv` (96 rows: 2 readers x 8 subgroups x 6 types)
- `tests/test_fitzpatrick_nhanes.py` (4 tests)

Changed:
- `pipelines/survey.py`: appended `category_proportions` only; existing functions untouched.
- `metrics/skin_tone/metric.json`: `comparison_note` only (the last sentences replaced; the Italian source and the two gaps are still described).
- Generated by `pipelines/render.py`: `entries/skin-tone.md`, `entries/resting-heart-rate.md` (content unchanged), `CATALOG.md`.

Not touched: `validate.py`, `render.py`, `resting_pulse.py`, existing tests, other metrics, the three existing `skin_tone` sources, `ACCESS_REQUESTS.md` (no row added or changed).

### Acceptance checks (real output)

1. `.venv/Scripts/python -m pytest -q`: **FAIL**, `1 failed, 35 passed`. The failure is an existing test, `tests/test_skin_tone.py::test_metric_is_available_with_one_source_per_scale`, which asserts `len(SOURCES) <= 3` and `len(TRANSCRIBED) + len(GAPS) == len(SOURCES)`. It encodes "three sources, none recomputed", so any fourth source (and any recomputed one) breaks it. The directive forbids editing existing tests, so I left it. All 4 new tests pass. Suggested fix for Sentinel or Ross: `len(SOURCES) <= 4`, and count recomputed sources in the second assertion.
2. `.venv/Scripts/python pipelines/validate.py`: prints `ok`, exit code 0. The `rater` and `category` columns are accepted by the validator (any columns before `n`), so no format change was needed.
3. `.venv/Scripts/python pipelines/fitzpatrick_nhanes.py` run twice: sha256 `ce9b35940a3ffbb7ced86d0c6b6e99260eb69c16daeb017d50d4c4b70407c7b5` both times. Identical.
4. `.venv/Scripts/python pipelines/render.py`: `wrote entries/resting-heart-rate.md, entries/skin-tone.md and CATALOG.md`. `entries/skin-tone.md` has a section for the new source with one table, `Rater | Sex | Race and ethnicity | Category | n | Proportion (95% CI)`, containing both Reader 1 and Reader 2. (The generic renderer puts all 96 rows in one table; I did not change it.)
5. Pipeline output:
   ```
   eligible (examined, aged 20-59): 2,992
   rows in DEX_C: 2,992
   Reader 1: read 2,693; blank 296; code 9 (picture missing) 3
   Reader 2: read 2,691; blank 296; code 9 (picture missing) 5
   a value (1-6 or 9) from both readers: 2,696; same value incl. 9: 1,660
   a type (1-6) from both readers: 2,691
     same type: 1,657 (61.6%)
     within one type: 2,551 (94.8%)
     one reader I-III and the other IV-VI (consensus matrix 'reject'): 212
   ```
   2,696 read by both: matches. 1,657 identical: matches only over the 2,691 people with a valid type 1-6 from both readers. Over the 2,696 with any value from both, counting code 9, the identical count is 1,660 (the extra 3 are people both readers coded 9). So Sentinel's 1,657 must have excluded code 9; I did not force a match, and `source.json` states both.
6. Weighted shares, all adults aged 20-59 (95% interval, Rao-Wu, 500 replicates):

| Type | Reader 1 (n = 2,693) | Reader 2 (n = 2,691) |
|---|---|---|
| I | 0.0018 (0.0009-0.0029) | 0.0331 (0.0192-0.0460) |
| II | 0.0761 (0.0560-0.0983) | 0.2933 (0.2606-0.3262) |
| III | 0.7144 (0.6593-0.7582) | 0.4614 (0.3997-0.5198) |
| IV | 0.0793 (0.0616-0.0994) | 0.1018 (0.0786-0.1280) |
| V | 0.0111 (0.0027-0.0207) | 0.0195 (0.0077-0.0339) |
| VI | 0.1173 (0.0883-0.1535) | 0.0908 (0.0621-0.1252) |

- `.venv/Scripts/python -m ruff check --line-length 110 .`: `All checks passed!`

### Reader agreement (unweighted, printed by the pipeline)

Among 2,691 people with a type 1-6 from both readers: same type 1,657 (61.6%); within one type 2,551 (94.8%); 212 had one reader in I-III and the other in IV-VI. Among 2,696 with a value (1-6 or 9) from both: 1,660 identical, including 3 pairs of 9-9.

### Code 9 and missing readings

Code 9 and a blank entry are both treated as "no type from that reader": the person is dropped from that reader's table (and its `n`), not from the other reader's. Blank: 296 for both readers (the same 296 rows; no row has one blank and one filled). Code 9: Reader 1, 3 people; Reader 2, 5 people. No weight adjustment. `population.n` is 2,693, the number of people with a type from at least one reader; `n_eligible` is 2,992.

### What the documentation says (DEX_C.htm, fetched with curl and read as text on 2026-10-06)

- Readers: "The dermatology digital images were read by two separate dermatologists." Who they were, their training, and whether the same two read every image: Not stated. What they were told to judge type from: Not stated.
- What they looked at: "The exam consists of four digital images taken by a health technician using a Kodak DCS760 digital camera with a 50mm lens." Poses: "BACK with ELBOWS", "INNER ARM", "FRONT OF LEGS with HANDS", "BACK OF LEGS with PALMS". Which images or sites the Fitzpatrick type was read from: Not stated.
- Eligibility and exclusions: "Sample persons aged 20-59 years who do not meet any of the exclusion criteria." and "A person using a wheelchair did not receive the photos of the back or back of the legs. He/she would be eligible for the other photos. There are no safety exclusions for this component."
- Code 9 (codebook value description for DEX1FITZ and DEX2FITZ): "Not determined, picture missing".
- Consensus: "When the finding of the two readers disagreed, the image reading software program required a third consensus reading." Rule 3: "Any outcome that resulted in "reject" went to consensus." The matrix accepts types 1-3 with 1-3 and 4-6 with 4-6, and rejects any pair that crosses 3/4. Rule 4: a missing critical value (including Fitzpatrick type) sends the image to consensus; "In addition, a consensus reading was required for any condition requiring follow-up." Codebook count for the consensus reading: 260.
- US distribution: "Currently, the distribution of skin type across the U.S. population is unknown."
- Definition: "The Fitzpatrick skin type is a method of classifying individuals based on their response to sun exposure in terms of tanning and burning (photosensitivity)".
- Weights: "the full sample MEC examination sample weight should be used for data analysis."
- Race and ethnicity (DEMO_C): RIDRETH1 codes 1 Mexican American, 2 Other Hispanic, 3 Non-Hispanic White, 4 Non-Hispanic Black, 5 "Other Race - Including Multi-Racial". There is no separate Asian group in 2003-2004.

### Sources added to ACCESS_REQUESTS.md

None. Keiser et al. 2012 (row 1) was tried once more and is still blocked: `https://doi.org/10.1016/j.jaad.2011.02.044` redirects to `https://linkinghub.elsevier.com/retrieve/pii/S0190962211003872`, which returns a 2.7 kB page that only forwards by JavaScript (no article text); `https://www.jaad.org/article/S0190-9622(11)00360-7/fulltext` returned HTTP 403; an NCBI E-utilities query by DOI returned no text. No number taken. Row 1 left open and `verification` says so.

### Judgment calls

1. Replicate weights are built on everyone examined in `DEMO_C` (9,643 people of all ages), as `resting_pulse.py` does, not only on the 2,992 adults aged 20-59.
2. Eligible = examined (`RIDSTATR == 2`) and aged 20-59. This equals the 2,992 rows in `DEX_C`.
3. The agreement figures in `source.json` use the 2,691 people with a valid type from both readers; the 2,696 version (with 9-9) is stated alongside.
4. `population.n` = 2,693 (a type from at least one reader); stated in `analysis` and `exclusions`.
5. I added one printed line to the pipeline beyond the directive: how many of the 2,691 pairs the consensus matrix would call "reject" (212). It supports the statement that most disagreements were accepted as they stood: 1,034 pairs differ, 212 of them cross the I-III / IV-VI line.
6. Estimates and intervals are rounded to 4 decimals, so a subgroup's six proportions sum to 1 only within 0.0003; the test tolerance is 0.001. Categories nobody falls in stay as rows (`0 (0-0)`), so each subgroup has six rows and one `n`.
7. `race_ethnicity` uses the `RIDRETH1` labels from the codebook (`Other Race - Including Multi-Racial`); `sex` is Male/Female from `RIAGENDR`.
8. `measurement.method` holds most of the quotes (reader, definition, code 9, consensus) because the format has no other place for them; the renderer prints it in the Which-source table, which makes that cell long.
9. `use_for`, `do_not_use_for` and `caveats` are drafts; `review_status` is `"draft"`. The two Type III shares quoted in the first caveat (71.4% and 46.1%) come from this pipeline's output.
10. `comparison_note` was rewritten from "So far this entry holds ..." onward; earlier sentences are unchanged.
11. The Italian source's `evidence.md` still says NHANES "was not computed" because directive 03 forbade it; it is a dated search log and I left it.

### Possible defects in the directive

- "Adjacent types for most of the rest" and "accepted as they stood" are right but incomplete: the documentation's matrix groups I-III and IV-VI, not adjacent types, so a III/IV pair (adjacent) is a reject and goes to consensus. 212 pairs cross the line.
- The consensus reading exists for 260 people, but not all are reject pairs: the page also sends images to consensus for missing critical values and follow-up conditions, so DEX6FITZ is not a clean "resolved disagreement" variable.
- The 1,657 figure counts 1-6 pairs only; with code 9 it is 1,660 (see check 5).
- `tests/test_skin_tone.py::test_metric_is_available_with_one_source_per_scale` conflicts with adding a fourth source, and the directive forbids editing existing tests.
- The renderer puts a proportions source with several subgroup columns in one 96-row table, with no per-reader or per-subgroup headings.

## Audit

**Result: pass, after one fix by Sentinel.** Audited 2026-10-06.

| Check | Result | Evidence |
|---|---|---|
| 1. pytest | pass after fix | The failure was a directive 03 test asserting at most three sources, none recomputed. This directive made that assertion wrong. Sentinel replaced it with a check that every source has a known origin. 36 passed |
| 2. validate | pass | `ok`, exit 0 |
| 3. Reproducible | pass | sha256 `ce9b3594…c7b5` on re-run |
| 4. Render | pass | both readers shown |
| 5. Counts | pass | 2,696 with a value from both; 1,657 identical among the 2,691 with a type 1 to 6 from both. Sentinel's 1,657 excluded code 9; Pragma's reading is right |
| 6. Shares reported | pass | |

Independent recomputation by Sentinel (separate script, same raw files): all
twelve all-adult weighted shares match to four decimals, as do the agreement
counts 1,657, 2,551 and 212.

Corrections to the directive, accepted from Pragma:
- The consensus matrix groups types I to III and IV to VI. A III/IV pair is
  adjacent but a "reject". 212 pairs cross that line.
- `DEX6FITZ` is not a clean record of resolved disagreements; images also
  went to consensus for other reasons.

Findings:
- The two readers give materially different national distributions: Type III
  is 71% for Reader 1 and 46% for Reader 2; Type II is 8% and 29%. The
  disagreement is concentrated in types I to III. Type VI is 12% and 9%.
- Keiser et al. 2012 remains unread (ACCESS_REQUESTS row 1), so there is no
  published cross-check yet.
- Renderer shows all 96 rows in one table. Add to format defects: group a
  proportions table by any extra subgroup column.

### Audit addendum, 2026-10-06: published cross-check obtained

Ross supplied Keiser et al. 2012. Sentinel read it in full and reproduced its
Table I from the raw file: all six counts and weighted shares, the sample
size, race and sex counts, both kappas, and the 95% within-one-type figure.
The match holds only if half-point averages of the two readers are rounded
down, a rule the letter does not state. Recorded in the source's
`verification`, with two added caveats. ACCESS_REQUESTS row 1 is resolved.

### Change after audit, 2026-10-06 (approved by Ross)

Added a third `rater` series, "Both readers averaged, half-points rounded
down", following Keiser et al. 2012. This reverses the directive's "no single
final type" decision in one respect: the two readers are still reported
separately, and the averaged series is labelled with its rounding rule. A new
test pins its all-adult shares to the published Table I (1.6, 33.1, 47.8,
4.9, 3.6, 9.0%; n 2,691). `data.csv` is now 144 rows, sha256
`cf4412e1…44cc`, reproducible on re-run. 37 tests pass.
