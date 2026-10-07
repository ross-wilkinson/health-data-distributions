# Directive 06: Presentation and format defects

**Priority:** Next. The skin tone page has 12 sources and is hard to read;
every new source hits the same defects.
**Scope:** Format, validator, renderer, and the mechanical field additions
listed below. No number changes. No guidance text is rewritten by Pragma.

## Rationale

Five directives and nine papers exposed a consistent set of weaknesses in how
entries are structured and shown. They are collected in
`.github/directives/backlog.md` under "Format defects". This directive fixes
them together because they all touch `validate.py` and `render.py`.

## Changes

### A. Grouping sources within a metric

1. `source.json` gains an optional string `group` (for example a scale name).
2. `metric.json` gains an optional array `groups`: the group names in display
   order. If present, every source's `group` must be one of them.
3. Renderer: when a metric has `groups`, the **Which source should I use?**
   table is ordered by group with a group column first, and the per-source
   sections are placed under a heading for each group. Sources without a
   group come last under "Other".
4. Apply to `skin_tone` only, mechanically, with these groups and
   assignments (Sentinel's, do not change them):
   - `Fitzpatrick type`: `nhanes_2003_2004_fitzpatrick_image_readers`,
     `scin_2023_fitzpatrick_self_and_dermatologist`,
     `pichon_2010_california_black_adults_fitzpatrick_with_none`,
     `he_2014_us_self_reported_fitzpatrick_by_race`,
     `sommers_2019_women_self_reported_fitzpatrick_by_race`,
     `fitzpatrick_central_italy_men_18_19_1999`
   - `Monk Skin Tone`: `scin_2023_monk_lay_annotators`, `monk_skin_tone_gap`
   - `Instrument measures`: `wilkes_2015_pretoria_ita_categories_digitised`,
     `sommers_2019_lstar_by_self_reported_fitzpatrick`, `ita_colorimetry_gap`
   - `Broad self-described groups`:
     `heldreth_2024_us_online_survey_light_medium_dark`

### B. Comparison note as points

5. `comparison_note` may be a string (as now) or an array of objects
   `{"heading": "...", "text": "..."}`. The renderer shows an array as a list
   with the heading in bold. Do not convert any existing note: Sentinel
   rewrites the two notes after this directive.

### C. Proportions tables

6. A proportions source renders wide: one row per subgroup, one column per
   category, in the order categories first appear in `data.csv`, values as
   percentages to one decimal, with `n` as a column. An interval, where
   present, is shown in brackets after the value.
7. When a proportions source has more than one subgroup column, the first
   subgroup column splits the output into one table per value, with that
   value as a sub-heading (for example one table per `rater`).
8. The `locator` for transcribed and digitised sources is shown once under
   the table when every row shares it, and as a column otherwise.

### D. Smaller defects

9. The `verification` section heading becomes "Checks".
10. Gap sources: `citation.url`, `citation.license`, and
    `population.sampling` are optional for `origin` `"gap"`. Remove the
    "Not applicable" placeholders from the two existing gap sources. In the
    comparison table a gap source's population cell reads "No data: a
    documented gap" in place of the "Any, Any, ages Any" text.
11. `n` may be empty on a row of a transcribed or digitised source, meaning
    the source does not state it. Rendered as "not stated".
12. `min` and `max` are allowed as statistics in the `moments` and
    `percentiles` forms.
13. The digitised "Script:" line puts the path in backticks so the sentence's
    full stop is not read as part of the path.

### E. Provisional sources

14. `source.json` gains an optional boolean `provisional`. When true, a
    non-empty string `provisional_reason` is required.
15. Renderer: a provisional source carries the line "Provisional:
    <provisional_reason>" beneath its title in the comparison table and at
    the top of its section, in the same style as the digitised label.
16. No existing source is provisional. Add tests only.

## Do not touch

`pipelines/survey.py`, the pipeline and digitising scripts, every `data.csv`,
every `evidence.md`, `CLAUDE.md`, `ACCESS_REQUESTS.md`,
`COPYRIGHT_QUESTIONS.md`, `.claude/`. In `source.json` and `metric.json`
files, change only what items 4 and 10 name. Do not edit any `use_for`,
`do_not_use_for`, `caveats`, `comparison_note`, or `definition` text.

## Acceptance checks

1. `.venv/Scripts/python -m pytest` passes: the 65 existing tests (1 skipped)
   plus new ones covering each of items 1 to 16.
2. `.venv/Scripts/python pipelines/validate.py` exits 0.
3. Every `data.csv` and `evidence.md` is byte-identical before and after
   (record sha256 of each before starting; compare after).
4. No number is lost from a page: for every row of every `data.csv`, its
   estimate appears in the rendered entry, as a percentage to one decimal for
   proportions and as stored otherwise. Add this as a test.
5. `entries/skin-tone.md` has the four group headings in the stated order,
   and the NHANES and SCIN sources each show one table per rater.
6. `.venv/Scripts/python -m ruff check --line-length 110 .` is clean.
7. The implementation report lists every source whose `source.json` changed
   and exactly which fields.

## After this directive (Sentinel, not Pragma)

- Rewrite the `skin_tone` and `resting_heart_rate` comparison notes as
  points, using only numbers present in the data files.
- Review whether any gap-source caveat lists should become structured
  "near miss" records.
