# Copyright questions

Open questions about whether material in this repository may be published.
Nothing here has been published: the folder is not a git repository and has
no remote. Each question must be closed before the source it concerns goes
public.

Agents: add a row the moment you transcribe, quote, or measure from a source
that is not clearly openly licensed, and list new rows in your final report.
Record what the source says about its own licence, verbatim, in the source's
`citation.license`. Do not decide the question yourself.

How to close a row: Ross records the decision and its basis (publisher's
stated terms, a permission, or advice), with the date, and moves the row to
**Resolved**. If the answer is no, the source is reduced to a pointer (citation
and guidance, no numbers) before publication.

## Open

| # | Logged | Source | What the source says | What we hold | Question |
|---|---|---|---|---|---|
| 1 | 2026-10-06 | He et al. 2014, *J Am Acad Dermatol* 71(4):731-737 (`skin_tone/he_2014_us_self_reported_fitzpatrick_by_race`) | "© 2014 by the American Academy of Dermatology, Inc." Subscription article | 42 percentages transcribed from Table II, the group sizes, and short quotations | Is reproducing most of one table's numbers, with citation, acceptable? This is the largest extract from a non-open source |
| 2 | 2026-10-06 | Ballone et al. 1999, *Eur J Epidemiol* 15(2):189-195 (`skin_tone/fitzpatrick_central_italy_men_18_19_1999`) | "© 1999 Kluwer Academic Publishers." Subscription article | Four percentages from Table 1, counts, and short quotations | Acceptable with citation? |
| 3 | 2026-10-06 | Wilkes et al. 2015, *JAMA Dermatol* 151(8):902-903 (`skin_tone/wilkes_2015_pretoria_ita_categories_digitised`) | "Copyright 2015 American Medical Association. All rights reserved." | Six values measured from a bar chart (not the chart itself), and short quotations | Does measuring values off a copyrighted figure raise any issue beyond transcribing a table? |
| 4 | 2026-10-06 | O'Hagan, Sharma, Ungar 2025, *J Drugs Dermatol* 24(7):431-432 (quoted in `skin_tone/monk_skin_tone_gap/evidence.md`; figure used by `pipelines/digitise/ohagan_2025_figure1_check.py`) | The copy carries: "No reproduction or use of any portion of the contents of these materials may be made without the express written consent of JDD." | Five short quotations and three correlation values. No data source. The validation script measures the figure but stores no values from it; the image is not in the repo | Are the short quotations acceptable given that notice? Is it acceptable to name the figure as the validation case? |
| 5 | 2026-10-06 | Pichon et al. 2010, *Ethn Dis* 20(2):174-179 (`skin_tone/pichon_2010_california_black_adults_fitzpatrick_with_none`) | No licence statement on the article pages read | Five percentages from Table 1, counts, and quotations | What are the journal's terms for this volume? |
| 6 | 2026-10-06 | Sommers et al. 2019, *Ethn Dis* 29(3):505-512 (two sources: `sommers_2019_women_self_reported_fitzpatrick_by_race`, `sommers_2019_lstar_by_self_reported_fitzpatrick`) | No licence statement on the article pages read | 18 percentages and 12 means and SDs from Table 1, and quotations | What are the journal's terms for this volume? |
| 7 | 2026-10-06 | Keiser et al. 2012, *J Am Acad Dermatol* 66(1):163-165 (quoted in `skin_tone/nhanes_2003_2004_fitzpatrick_image_readers` `verification` and `measurement`) | Subscription article; no licence statement recorded | Six percentages and counts from its Table I, two kappa values, and short quotations, all used as a cross-check on our own analysis of public data | Acceptable as a cited cross-check? |
| 8 | 2026-10-06 | NHANES public-use files (three sources) | No licence name. NCHS terms say users must "Use the data in this dataset for statistical reporting and analysis only." | Our own weighted statistics | Confirm the wording to use in `citation.license`, and that publishing derived statistics is within the terms (expected yes) |
| 9 | 2026-10-06 | SCIN dataset (two sources) | "The SCIN Dataset is released under SCIN Data Use License": reuse and adaptation with attribution and a link to the licence; no re-identification | Unweighted shares computed from the two public tables | Confirm our attribution wording satisfies section 3(a) of that licence (expected yes) |
| 10 | 2026-10-06 | Verbatim quotations in every `evidence.md` | Varies by source | Sentences and table rows quoted to prove each number | Is the evidence-file practice acceptable for non-open sources, or should those files quote less and point more? |

Not in question: Quer et al. 2020 (Creative Commons Attribution License, stated
in the article) and Heldreth et al. 2024 (CC BY 4.0, stated on its first page).

No PDF supplied by Ross has been copied into the repository. The figure
images used for measurement are in `raw/figures/`, which is git-ignored.

## Resolved

None yet.
