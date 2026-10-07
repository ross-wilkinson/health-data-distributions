# Health Data Distributions

Population and subgroup distributions of health measures in one consistent,
citable format. The value of the project is not the numbers alone but the
statement, for each source, of how it was measured, who was measured, and what
it should and should not be used for.

## Invariants

1. **Every number is traceable.** A recomputed number comes from a script in
   `pipelines/` run on public data. A transcribed number carries a locator
   (table, page, URL) and a verbatim quote in the source's `evidence.md`.
2. **Never fill a number from memory.** If a source cannot be opened and read,
   the number does not go in. Report it instead.
3. **Report what the source reports.** Do not convert a mean and SD into
   percentiles or pool across sources. Values measured from a published chart
   are allowed only as a source of `origin` `"digitised"` (Ross, 2026-10-06):
   its own source folder, a measuring script in `pipelines/digitise/`, a stated
   precision, and internal checks recorded in `verification`. A digitised
   number never goes into a transcribed source.
4. **Measurement method is part of the data.** Two sources for the same metric
   are different distributions until shown otherwise; never merge them.
5. **Absence is "not found in this search", with the search recorded.** Never
   "does not exist".
6. **Usage guidance is drafted, then reviewed by Ross.** Anything under
   `use_for`, `do_not_use_for`, or `caveats` written by an agent is marked
   `"review_status": "draft"` until Ross changes it.
7. **Generated files are not edited by hand:** `entries/*.md`, `CATALOG.md`.
8. **Access-controlled data never enters the repo**, and aggregates from it are
   published only if the data terms allow.
9. **A blocked source is logged, not worked around.** When a paper or page
   cannot be read (paywall, bot check, login), add a row to
   `ACCESS_REQUESTS.md` with the citation, what blocked it, and what was
   wanted from it, and list it in the final report so Ross can try to get it.
10. **An abstract is not the paper.** A source entered from an abstract alone
    is provisional until the full text is read, and must say so (Ross,
    2026-10-06). Twice on this project the abstract misled: a denominator
    that included non-responders, and an unstated rounding rule.
11. **Copyright questions are logged, not decided.** When material comes from
    a source that is not clearly openly licensed, quote the source's own
    licence statement in `citation.license` and add a row to
    `COPYRIGHT_QUESTIONS.md`. Ross closes those rows before anything is
    published. No supplied PDF is ever copied into the repo.

## Layout

```
metrics/<metric_id>/metric.json                 what the metric is, status, cross-source guidance
metrics/<metric_id>/sources/<source_id>/        source.json, data.csv, evidence.md (transcribed only)
pipelines/                                      survey.py, one script per recomputed source, validate.py, render.py
pipelines/digitise/                             one measuring script per digitised figure; images live in raw/figures/
entries/, CATALOG.md                            generated
raw/                                            downloaded public data, git-ignored
.github/directives/                             pending directives; _completed/ after audit
ACCESS_REQUESTS.md                              sources agents could not read, for Ross to obtain
COPYRIGHT_QUESTIONS.md                          publication questions for Ross to close
```

## Commands

```sh
.venv/Scripts/python -m pytest
.venv/Scripts/python pipelines/validate.py
.venv/Scripts/python pipelines/render.py
```

## Agent workflow

Directive, implement, audit. Sentinel (Opus) designs and audits; Pragma
(Sonnet) implements. Specs are in `.claude/agents/`. They share no memory, so
everything that matters goes to disk.

1. Sentinel writes a directive to `.github/directives/<nn>-<kebab-name>.md`:
   the what and why, scope, acceptance checks, and what not to touch.
2. Pragma implements exactly that, runs the checks, and appends a
   `## Implementation report` to the directive. Pragma does not move the file.
3. Sentinel audits against the acceptance checks and the invariants above,
   re-opening primary sources for transcribed numbers, and appends
   `## Audit`. On a pass, Ross moves the directive to `_completed/`.
