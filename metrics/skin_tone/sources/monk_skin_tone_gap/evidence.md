# Evidence: Monk Skin Tone scale, search log

Searched 2026-10-06. All quotes are verbatim. A search-result summary is a lead only; the "Opened?" column says whether the source itself was read. Full texts of open-access papers were read from the NCBI E-utilities PMC XML (efetch) and, for the UCSF paper, also from the Europe PMC REST full-text XML.

**Result: not found in this search.** No distribution of Monk Skin Tone categories in a defined population was found. This is a statement about the search below, not a claim that none exists.

## 1. Search log

| # | Date | Query or site | What it returned | Opened? | Outcome |
|---|---|---|---|---|---|
| 1 | 2026-10-06 | "Monk Skin Tone scale distribution nationally representative survey proportion of adults" | Google's launch of the scale; Heldreth et al. (2,214 US people compared three scales); news items; older US skin-colour studies (interviewer ratings) | Heldreth et al.: abstract opened (research.google page and Crossref); full text blocked (ACM HTTP 403) | Perceived-representation survey, not a distribution |
| 2 | 2026-10-06 | "Monk Skin Tone scale used in nationally representative probability survey respondents self-rated skin tone results distribution 2023 2024" (extended) | npj Digit Med 2025 (Fitzpatrick and Monk, San Francisco VA); Wikipedia; Heldreth et al.; a Dermatologic dataset-labelling study | npj Digit Med paper opened in full; Wikipedia opened (secondary) | Small clinical sample |
| 3 | 2026-10-06 | "Monk Skin Tone scale self-identified or rated distribution of participants Table proportion MST 1-10 study sample" | Face-dataset annotation papers (arXiv), a Duke ICU preprint, a Vienna poster | Duke preprint opened in full; arXiv and poster not opened | Enrolled samples and image datasets |
| 4 | 2026-10-06 | "Pew OR Census OR Gallup OR 'General Social Survey' Monk skin tone scale included in survey respondents rated skin tone 1-10" | Skin-colour measurement papers in sociology (interviewer-rated scales); Heldreth et al. | Not opened | No national survey using MST found in the results |
| 5 | 2026-10-06 | "Heldreth Monk Schumann Ricco 'Which Skin Tone Measures are the Most Inclusive' participants recruited survey panel nationally representative quota" | Same paper; no recruitment details in the results | Abstract only | Recruitment method not found |
| 6 | 2026-10-06 | Site: research.google (Heldreth et al. publication page) | Abstract; "2,214 people in the United States" | Opened | Does not report MST category shares |
| 7 | 2026-10-06 | Site: api.crossref.org, doi 10.1145/3632120 | Abstract identical to the Google page; licence CC BY 4.0 | Opened | As above |
| 8 | 2026-10-06 | Site: dl.acm.org (full text of Heldreth et al.) | HTTP 403 (bot check) | Not opened | Could not read recruitment or tables |
| 9 | 2026-10-06 | Site: jddonline.com, O'Hagan, Sharma, Ungar, letter on Fitzpatrick and Monk scales (J Drugs Dermatol 2025;24(7)) | Page states it uses the Skin Condition Image Network (SCIN) dataset, "patients recruited from Google search advertisements"; full text not visible | Page only | Patients recruited from advertisements; not a population sample |
| 10 | 2026-10-06 | Site: skintone.google | Title only ("Skin Tone Research @ Google") | Page returned no body text | Nothing to use |
| 11 | 2026-10-06 | Site: Add Health Navigator (addhealth-navigator.cpc.unc.edu), item "What is the respondent's skin color?" | Item text and five response options (black, dark brown, medium brown, light brown, white); no frequencies on the page | Opened | Different scale; see below |

## 2. Enrolled samples that recorded Monk Skin Tone (rejected as population distributions)

- **UCSF and San Francisco General cohort**, medRxiv preprint doi:10.1101/2025.02.21.25322707 (CC BY-NC-ND 4.0; a later journal version exists, British Journal of Dermatology, not compared). "We studied 789 participants, with 33,856 assessments." and "Study sites were chosen based on convenience and with the intent to capture the local diversity of pigment." Rejected: convenience sample recruited for diversity; its Table 4 gives ITA ranges by Monk category with no n per category.
- **Duke University Hospital ICU cohort**, medRxiv preprint doi:10.1101/2024.02.24.24303291 (CC BY-NC-ND 4.0). "128 patients (57 Black, 56 White) with 521 ABG-pulse oximetry pairs were recruited". Rejected: pilot sample chosen for a pulse oximetry question.
- **San Francisco VA cohort**, npj Digit Med 2025, doi:10.1038/s41746-025-01975-7 (CC BY 4.0). "Using prospectively collected facial images from 90 hospitalized adults at the San Francisco VA, three independent annotators rated facial regions in triplicate using Fitzpatrick (I-VI) and Monk (1-10) skin tone scales. Patients also self-identified their skin tone." The text says "Most patients reported Fitzpatrick scores of II and Monk scores of 4" in a histogram caption only; no table of counts. Rejected: small clinical sample, distribution only in a figure.

### O'Hagan, Sharma, Ungar 2025: read in full, no category shares in text or tables

O'Hagan R, Sharma D, Ungar B. Large Multiethnic Comparison Benchmark of the Fitzpatrick and Monk Skin Tone Scales. *J Drugs Dermatol* 2025;24(7):431-432. doi:10.36849/JDD.8618e. Read on 2026-10-06 from a PDF supplied by Ross Wilkinson (`raw/papers/O'Hagan et al. 2025 - J. Drugs Dermatol_.pdf`, kept untracked in the repo). The copy carries the publisher's notice that no portion may be reproduced without written consent, so only short quotations are given here.

What it is: an analysis of the Skin Condition Image Network (SCIN) dataset.

> We analyzed the 4292 patient images with all FST and MST scores available.

> SCIN includes images with dermatologist-rated FST, patient self-reported FST, and MST assigned by 2 trained non-clinical annotators, 1 from the United States (US) and the other from India.

> extensive dermatological images from patients recruited from Google search advertisements.

Why no numbers were entered: the distribution of Monk scores and of Fitzpatrick scores appears only as bar charts (Figure 1, panels A and B). The text and Table 1 give no share for any category. Under invariant 3, nothing is read off a figure.

What the text does report, used in the metric's comparison note:

> The Spearman correlation between dermatologist-rated FST and US evaluator-rated MST scores was strong and significant (rho=0.541, P<0.001); correlations between self-reported FST and US MST scores were significant but weaker (rho=0.299, P<0.001). There was a moderate correlation between self-reported and dermatologist-assigned FST (rho=0.318, P<0.001).

> The internal consistency of MST scores between the U.S. and Indian trained evaluators was robust (rho= 0.640, P<0.001).

The authors' own limit on the sample:

> participant recruitment via online advertisements may limit the generalizability of our findings.

Lead: the letter cites the dataset itself as Ward JA, Wang J, et al. Crowdsourcing dermatology images with Google Search Ads: creating a real-world skin condition dataset. arXiv, 28 February 2024, doi:10.48550/arXiv.2402.18545. If that dataset is openly licensed, the Monk and Fitzpatrick category shares could be recomputed from it directly. Not yet checked.

## 3. Quotes cited by metric.json (definition and comparison note)

From the Heldreth et al. abstract (Crossref record, doi:10.1145/3632120):

> a newly developed Monk 10-point scale from the social sciences

From the Duke preprint (doi:10.1101/2024.02.24.24303291), Methods:

> Three types of skin tone assessment were conducted using different devices: administered visual scales (Fitzpatrick, Monk30, and Von Luschan scales, visible in Supplemental Figures 6a, 6b and 6c); reflectance colorimetry (Delfin SkinColorCatch); and reflectance spectrophotometry (Variable Spectro 1 Pro Bridge Set and Konica Minolta CM-700D Spectrophotometer).

From the Duke preprint, Discussion:

> the Monk scale – designed to be easy-to-use for evaluation of technology, while representing a broad range of skin tones

From the npj Digit Med paper (doi:10.1038/s41746-025-01975-7):

> Patients also self-identified their skin tone.

From the UCSF preprint (doi:10.1101/2025.02.21.25322707), Results:

> Categorization of participants as light, medium, or dark was not consistent between scales (Figure 2a). For example, 41% of subjects categorized as dark by pFP (V-VI) were categorized as medium by MST (D-G).

> we found that self-identified ‘Black or African American’ and self-identified ‘White’ participants have a wide range of MST values with significant overlap.

From the Duke preprint, Abstract:

> The collected skin tone measurements were shown to yield differences among each other and overlap with self-reported racial groups

These describe convenience cohorts. They support the statement that scales applied to the same people can classify them differently, not any statement about a population.

## 4. Near misses on other scales (for the record)

- Add Health Wave III interviewer-rated skin colour, five categories (item text and options read on the Add Health Navigator page, see log row 11). A search-result summary quoted frequencies for 15,178 respondents; those numbers were not read from an opened source and are not entered. The scale has five categories and cannot be mapped to MST.
- A search-result summary said the General Social Survey 2010-2014 panel used the Massey-Martin scale for interviewer observation. Not opened.
