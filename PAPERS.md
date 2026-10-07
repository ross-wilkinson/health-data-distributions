# Source papers

A copy of every paper a source is built from is kept in `raw/papers/`. That
folder is git-ignored: the copies are for our own verification and stay
untracked until the questions in `COPYRIGHT_QUESTIONS.md` are closed. A fresh
clone will not contain them; this index says what should be there and where
each came from.

| File in `raw/papers/` | Citation | Obtained | Used by |
|---|---|---|---|
| `Ballone et al. 1999 - Eur. J. Epidemiol_.pdf` | Ballone E, et al. *Eur J Epidemiol* 1999;15(2):189-195. doi:10.1023/A:1007539807705 | Supplied by Ross, 2026-10-06 | `skin_tone/fitzpatrick_central_italy_men_18_19_1999` |
| `He et al. 2014 - J. Am. Acad. Dermatol_.pdf` | He SY, et al. *J Am Acad Dermatol* 2014;71(4):731-737. doi:10.1016/j.jaad.2014.05.023 | Supplied by Ross, 2026-10-06 | `skin_tone/he_2014_us_self_reported_fitzpatrick_by_race` |
| `Heldreth et al. 2023 - ACM J. Responsib. Comput_.pdf` | Heldreth CM, et al. *ACM J Responsib Comput* 2024;1(1):Article 7. doi:10.1145/3632120 (CC BY 4.0) | Supplied by Ross, 2026-10-06 | `skin_tone/heldreth_2024_us_online_survey_light_medium_dark`; `skin_tone/monk_skin_tone_gap` |
| `Keiser et al. 2012 - J. Am. Acad. Dermatol_.pdf` | Keiser E, et al. *J Am Acad Dermatol* 2012;66(1):163-165. doi:10.1016/j.jaad.2011.02.044 | Supplied by Ross, 2026-10-06 | Cross-check for `skin_tone/nhanes_2003_2004_fitzpatrick_image_readers` |
| `O'Hagan et al. 2025 - J. Drugs Dermatol_.pdf` | O'Hagan R, Sharma D, Ungar B. *J Drugs Dermatol* 2025;24(7):431-432. doi:10.36849/JDD.8618e | Supplied by Ross, 2026-10-06 | `skin_tone/monk_skin_tone_gap`; `pipelines/digitise/ohagan_2025_figure1_check.py`; cross-check for both SCIN sources |
| `Ostchega et al. 2011 - Natl Health Stat Report 41.pdf` | Ostchega Y, et al. *Natl Health Stat Report* no. 41, 2011 | Downloaded 2026-10-06 from https://www.cdc.gov/nchs/data/nhsr/nhsr041.pdf (US government publication) | Cross-check for `resting_heart_rate/nhanes_2015_2018_clinic_pulse` |
| `Pichon et al. 2010 - Ethn. Dis_.pdf` | Pichon LC, et al. *Ethn Dis* 2010;20(2):174-179 | Supplied by Ross, 2026-10-06 | `skin_tone/pichon_2010_california_black_adults_fitzpatrick_with_none` |
| `Quer et al. 2020 - PLOS ONE.pdf` | Quer G, et al. *PLOS ONE* 2020;15(2):e0227709. doi:10.1371/journal.pone.0227709 (CC BY) | Downloaded 2026-10-06 from the publisher | `resting_heart_rate/quer_2020_fitbit_92457_adults`; `resting_heart_rate/quer_2020_fitbit_fig2_digitised` |
| `Sommers et al. 2019 - Ethn. Dis_.pdf` | Sommers MS, et al. *Ethn Dis* 2019;29(3):505-512. doi:10.18865/ed.29.3.505 | Supplied by Ross, 2026-10-06 | `skin_tone/sommers_2019_women_self_reported_fitzpatrick_by_race`; `skin_tone/sommers_2019_lstar_by_self_reported_fitzpatrick` |
| `Wilkes et al. 2015 - JAMA Dermatol.pdf` | Wilkes M, et al. *JAMA Dermatol* 2015;151(8):902-903. doi:10.1001/jamadermatol.2015.0351 | Supplied by Ross, 2026-10-06 (as `wilkes2015.pdf`) | `skin_tone/wilkes_2015_pretoria_ita_categories_digitised`; `skin_tone/ita_colorimetry_gap` |

## Held here for another project

| File in `raw/papers/` | Citation | Obtained | For |
|---|---|---|---|
| `Lautman et al. 2026 - JACC Case Rep_.pdf` | Lautman Z, et al. Longitudinal Changes in Wearable-Captured Physiology Before Sudden Cardiac Death. *JACC Case Rep* 2026:110397. doi:10.1016/j.jaccas.2026.110397 (CC BY-NC-ND) | Supplied by Ross, 2026-10-06 | The planned wearable change-point false-alarm benchmark, which has no repository yet. Move it there when one exists. Not used by any source here |

## Not held as a paper

- NHANES and SCIN sources are computed from public data files in `raw/nhanes/`
  and `raw/scin/`; their documentation is online (links in each
  `source.json`).
- Papers read only as an abstract or web page while searching are listed in
  the gap sources' `evidence.md` search logs, not here.

## Adding a paper

Save it in `raw/papers/` with a name of the form
`<First author> et al. <year> - <journal>.pdf`, add a row above, and add a row
to `COPYRIGHT_QUESTIONS.md` unless the paper states an open licence.
