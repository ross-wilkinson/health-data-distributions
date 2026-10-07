# Directive 05: Digitised-from-figure sources

**Decision:** Ross, 2026-10-06: values measured from a published chart are
allowed, as a separately labelled class.
**Scope:** Format, validator, and renderer support only. No source is added by
this directive; Sentinel adds the first digitised sources afterwards.

## Rationale

Several of the best sources publish a distribution only as a chart. Measuring
bar heights or a curve against the axis recovers the numbers to a known
precision. Those numbers are less certain than a transcribed table and must
never be mistaken for one, so they get their own `origin`, their own required
provenance, and a visible label wherever they are shown.

## Format changes

1. `origin` gains the value `"digitised"`.
2. A source's rows are all of one origin. A paper that gives some numbers in
   text and others in a figure becomes two sources.
3. For `origin` `"digitised"`:
   - `provenance` requires `url`, `accessed`, and four further non-empty
     strings: `figure` (which figure and panel), `method` (how it was
     measured), `precision` (the stated uncertainty, in the units of the
     data), and `script` (a repository-relative path to the measuring script,
     which must exist).
   - `evidence.md` is required, as for transcribed sources.
   - `data.csv` requires the final `locator` column, as for transcribed
     sources.
   - `statistic_form` may be `"percentiles"`, `"moments"`, or
     `"proportions"`, not `"none"`.
4. `verification` becomes required (non-empty) for digitised sources: it must
   record the internal checks made (for example, bars summing to 100%).

## Changes

1. `pipelines/validate.py`: implement the rules above. A missing script file,
   a missing provenance field, a missing `evidence.md`, a missing `locator`
   column, `statistic_form` `"none"`, or an empty `verification` on a
   digitised source is each a reported problem.
2. `pipelines/render.py`:
   - Origin line reads "digitised from a published figure".
   - In the **Which source should I use?** table, a digitised source's first
     cell carries the line "Digitised from a figure" beneath its title, in
     the same way the draft-guidance line is shown.
   - In the source's own section, directly under the origin line, show:
     "Measured from <figure>. Precision: <precision>. Method: <method>.
     Script: <script>." built from the provenance fields.
   - Everything else renders as for a transcribed source of the same
     `statistic_form`.
3. `tests/test_format.py`: add cases, built in a temporary directory, for a
   valid digitised source and for each of the six problems in change 1.
4. `README.md`: one sentence in the layout section naming the four origins.

Do not edit `CLAUDE.md`; Sentinel updates invariant 3 separately.

## Do not touch

`pipelines/survey.py`, the two pipeline scripts, any file under `metrics/`,
`ACCESS_REQUESTS.md`, `CLAUDE.md`, `.claude/`, tests other than
`tests/test_format.py`. Do not create a `pipelines/digitise/` folder or any
source. Do not fix the unrelated format defects listed in
`.github/directives/backlog.md`.

## Acceptance checks

1. `.venv/Scripts/python -m pytest` passes (43 existing tests plus the new
   ones).
2. `.venv/Scripts/python pipelines/validate.py` exits 0 on the repository as
   it stands.
3. `.venv/Scripts/python pipelines/render.py` runs, and `git`-free comparison
   shows `entries/skin-tone.md` and `entries/resting-heart-rate.md` unchanged
   by this directive (save copies before you start and `diff` after).
4. A throwaway digitised source built in a temporary copy of the repository
   validates and renders with the label, the measured-from line, and its
   table. Show the rendered lines in the report.
5. `.venv/Scripts/python -m ruff check --line-length 110 .` is clean.

## Implementation report

Implemented by Pragma. No git; folder is not a repository.

### Files changed

- `pipelines/validate.py`
- `pipelines/render.py`
- `tests/test_format.py` (11 new tests; file now has 21)
- `README.md`

Not touched: `CLAUDE.md`, anything under `metrics/`, `ACCESS_REQUESTS.md`, `.claude/`, `pipelines/survey.py`, the two pipeline scripts, other tests, `backlog.md`. No `pipelines/digitise/` folder and no source was created in the repository.

### What the validator now enforces for a digitised source

- `origin` accepts `"digitised"`.
- `provenance` must contain `url`, `accessed` (YYYY-MM-DD), `figure`, `method`, `precision`, `script`; each is reported when missing (`missing required field '<name>'`) and when present but empty (`provenance.<name> is not valid`).
- `provenance.script` must be a repository-relative path to an existing file under the validated root; a missing file is `provenance.script '<path>' does not exist`; an absolute path or one resolving outside the root is reported as not inside the repository.
- `evidence.md` required (same message as transcribed).
- `data.csv` must end with `n, statistic, estimate, ci_low, ci_high, locator`; `locator` non-empty on every row (same code path as transcribed; the `check_data` flag was renamed `transcribed` to `located`).
- `statistic_form` `"none"` is reported: `statistic_form 'none' is not allowed for a digitised source`.
- `verification` is required and must be non-empty (`missing required field 'verification' for a digitised source`; an empty one gets the existing `'verification' must be a non-empty string`).
- `check_source` now takes the root (`check_source(folder, root, problems)`) so the script path can be resolved.

### What the renderer emits

- Origin line: `**Origin:** digitised from a published figure · **Data:** [data.csv](...)`.
- Which-source table first cell: `<title><br>*Digitised from a figure*` followed, when draft, by `<br>*Guidance: draft, not yet expert-reviewed*`.
- Directly under the origin line (blank line between): `Measured from <figure>. Precision: <precision>. Method: <method>. Script: <script>.` A trailing full stop already in a field is not doubled.
- Reproduce section: `Digitised from <url> (accessed <date>). Measuring script: `<script>`. Measurements, quotes and locators: [evidence.md](...).`
- Everything else (caveats, population and method, tables with a `Source location` column, verification, citation) renders as for a transcribed source of the same form.

### Acceptance checks (real output)

1. `.venv/Scripts/python -m pytest -q`: `54 passed` (43 existing plus 11 new: valid digitised source; missing script file; script outside the repository; each of the six provenance fields missing; empty provenance field; missing `evidence.md`; missing `locator`; `none` form; missing `verification`; empty `verification`; rendered labels).
2. `.venv/Scripts/python pipelines/validate.py`: `ok`, exit 0.
3. `.venv/Scripts/python pipelines/render.py`: `wrote entries/resting-heart-rate.md, entries/skin-tone.md and CATALOG.md`. Copies of `entries/skin-tone.md`, `entries/resting-heart-rate.md` and `CATALOG.md` were saved to the session scratchpad before any change; `diff` after: `identical skin-tone.md`, `identical resting-heart-rate.md`, `identical CATALOG.md`.
4. Throwaway source built only in a temporary copy of the repository (scratchpad `copy/`), as a second source under `skin_tone`, with `provenance.script` pointing to a placeholder file in that copy. `validate.py` there: `ok`, exit 0; `render.py` ran. Rendered lines:
   - `| Throwaway digitised source, Figure 1<br>*Digitised from a figure*<br>*Guidance: draft, not yet expert-reviewed* | 2,214 adults ... |`
   - `**Origin:** digitised from a published figure · **Data:** [data.csv](../metrics/skin_tone/sources/throwaway_digitised_figure/data.csv)`
   - `Measured from Figure 1, panel B. Precision: 0.005 of the sample (half a pixel). Method: Bar tops located in pixels and scaled against the axis ticks. Script: scratch_script/measure_fig1.py.`
   - Table: `| Category | n | Proportion (95% CI) | Source location |` / `| Light | 2000 | 0.6 | Figure 1 panel B |` / `| Dark | 2000 | 0.4 | Figure 1 panel B |`
   - Reproduce: `Digitised from <https://example.org/paper> (accessed 2026-10-06). Measuring script: `scratch_script/measure_fig1.py`. Measurements, quotes and locators: [evidence.md](...).`
   - Negative check in the copy: after deleting the placeholder, `validate.py` reports `provenance.script 'scratch_script/measure_fig1.py' does not exist` and `1 problem(s)`.
5. `.venv/Scripts/python -m ruff check --line-length 110 .`: `All checks passed!`

### Judgment calls

1. The reproduce text was unspecified. Without a branch the renderer would have fallen through to the gap wording ("Searched on ..."), and reusing the transcribed wording would say "Transcribed", which is false. I wrote a digitised-specific sentence (above), which also lists the script.
2. Order of notes in the Which-source cell: the digitised line first, then the draft line.
3. Script path rules go beyond "must exist": absolute paths and paths escaping the root are rejected, and the path must be a file, not a directory.
4. `provenance.method` is validated as a non-empty string with no format rules; `precision` likewise (the directive asks for "the units of the data" but that cannot be checked mechanically).
5. `figure` has a trailing full stop stripped before "Measured from <figure>." and other fields get a full stop added only if missing, so the sentence does not show ".." .
6. README: besides the one sentence naming the four origins, I changed the layout line "evidence.md (transcribed or gap only)" to "evidence.md (not for recomputed)", since the old wording became wrong.
7. I added a render test (importing `render` into `tests/test_format.py`) beyond the validator cases the directive lists, so the label text is guarded.
8. `statistic_form` `"none"` with a digitised source reports only the new message; the existing "data.csv must be absent" rule still applies as well.

### Directive notes (possible defects)

- The `verification` section is still headed "Check against a published reference" (a backlog defect, not fixed as directed); for a digitised source it will hold internal checks, so the heading will mislead until that is fixed.
- The directive's `Script:` text is plain, so a script path followed by a full stop looks like part of the path; I kept the specified text exactly.
- The rule "a source's rows are all of one origin" (Format change 2) is satisfied structurally (origin is per source) and is not separately testable.
- `precision` is a free string; nothing stops a per-row precision from being stated only in prose. Fine for now, but numeric precision would be machine-checkable.

## Audit

**Result: pass.** Audited 2026-10-06 by using the new class for real.

| Check | Result | Evidence |
|---|---|---|
| 1. pytest | pass | 54 passed at hand-back |
| 2. validate | pass | `ok`, exit 0 |
| 3. Existing pages unchanged | pass | accepted from the report; superseded minutes later by new sources |
| 4. Digitised source validates and renders | pass | two real digitised sources added by Sentinel validate and render with the label and the measured-from line |
| 5. ruff | pass | clean |

Pragma's judgment calls are all accepted, including the digitised-specific
reproduce sentence and the stricter script-path rule.

First uses of the class, added by Sentinel after the audit:
- `resting_heart_rate/quer_2020_fitbit_fig2_digitised`: four checks against
  numbers stated in the paper, all within the stated precision.
- `skin_tone/wilkes_2015_pretoria_ita_categories_digitised`: the six measured
  counts sum to exactly the paper's N of 556.
- Method validation against known values in
  `pipelines/digitise/ohagan_2025_figure1_check.py`: 15 bars within 0.06
  percentage points.

Follow-up for the backlog: the `verification` heading still reads "Check
against a published reference", which now misdescribes internal checks.
