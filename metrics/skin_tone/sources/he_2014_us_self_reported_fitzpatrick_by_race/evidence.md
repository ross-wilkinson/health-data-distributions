# Evidence: self-reported Fitzpatrick phototype by race, US convenience survey (He et al. 2014)

All quotes are verbatim. Read in full on 2026-10-06 from a PDF of the published article supplied by Ross Wilkinson (`raw/papers/He et al. 2014 - J. Am. Acad. Dermatol_.pdf`, kept untracked in the repo). The journal page had blocked the fetch tool earlier the same day.

Source: He SY, McCulloch CE, Boscardin WJ, Chren M-M, Linos E, Arron ST. Self-reported pigmentary phenotypes and race are significant but incomplete predictors of Fitzpatrick skin phototype in an ethnically diverse population. *J Am Acad Dermatol* 2014;71:731-7. http://dx.doi.org/10.1016/j.jaad.2014.05.023

First page: "© 2014 by the American Academy of Dermatology, Inc."

## 1. The numbers in data.csv

### Locator: Table II

Table II is titled "Descriptive characteristics of study participants". Its columns are Variable, FSPT I, FSPT II, FSPT III, FSPT IV, FSPT V, FSPT VI, N (total = 3386), %, and P value. Its footnote says: "Data presented as n (%), P values obtained using χ2 statistical testing. Sum of categories may not total to 3386 as a result of missing data points." The race rows used, as printed (FSPT I to VI, then N):

> White | 97 (9.5) | 222 (21.7) | 301 (29.5) | 219 (21.4) | 126 (12.3) | 56 (5.5) | 1021
>
> Asian | 8 (1.3) | 34 (5.9) | 75 (13.0) | 151 (26.2) | 193 (33.5) | 115 (19.9) | 576
>
> Black | 8 (1.4) | 17 (3.0) | 36 (6.5) | 64 (11.5) | 162 (29.1) | 269 (48.4) | 556
>
> Native American | 3 (1.2) | 19 (7.8) | 20 (8.2) | 67 (27.3) | 88 (35.9) | 48 (19.6) | 245
>
> Latino | 27 (7.9) | 37 (10.8) | 64 (18.7) | 95 (27.8) | 77 (22.5) | 40 (11.7) | 342
>
> Multiracial | 11 (1.9) | 42 (7.4) | 104 (18.4) | 129 (22.9) | 184 (32.6) | 94 (16.7) | 564

Used for: the share of each phototype within each race group (the percentage in brackets, stored as a fraction), with `n` the N printed for that group.

Rows of Table II not entered: "Other" (N 54), "Missing/prefer not to respond" (N 21), and the breakdowns by sex, age, self-reported skin colour, hair colour, and eye colour.

### Locator: Results

> In the collective study population, FSPT distribution was approximately 4.6% type I, 11.1% type II, 18.1% type III, 22.2% type IV, 25.0% type V, and 18.8% type VI.

> A total of 3386 participant responses were collected from an ethnically diverse general population, of which 69% (2351) were female and 31% (1024) were male (Table II). Overall, the mean (SD) participant age was 37.0 (14.8) years.

Used for: the `All` rows, with `n` 3386.

## 2. Recruitment and method (Methods)

> A 6-month cross-sectional survey study collected Internet and paper responses from 3386 individuals regarding age, sex, self-reported FSPT, eye color, hair color, constitutive skin color determined from the inside of the wrist, and race/ethnicity. FSPT was determined based on each participant's self-reported response to the question "How does your skin react if you go outside without sunscreen for half an hour?" (Table I). There was no physician assessment of skin phototype for study participants.

> An electronic link to the survey was distributed using social media sites (Facebook, Twitter) and was open to response from all over the United States. To enrich for nonwhite participants, we targeted minority group pages on these social media World Wide Web sites. Chain-referral sampling (recruitment by participants among their acquaintances) was used to further maximize participant responses. In addition, English and Spanish paper versions of the survey were distributed during community events, including church gatherings; community lectures; and seminars at University of California at San Francisco Medical Center.

> Individuals younger than 18 years were excluded from the study.

Table I, "Determination of Fitzpatrick skin phototype", gives the answer options as sunburn tendency and suntan tendency: I "Always burns easily", "Never tan"; II "Always burns easily", "Tans slightly"; III "Burns moderately", "Tans gradually"; IV "Burns minimally", "Tans moderately"; V "Rarely burns", "Tans profusely"; VI "Never burns", "Tans profusely".

## 3. The authors on the limits of the sample (Abstract and Discussion)

> Limitations: Our study enriched for responses from ethnic minorities and does not fully represent the demographics of the US population.

> One potential limitation of this study is that the sample population is not representative of the demographics of the United States. However, our goal was to investigate whether race and pigmentary features are predictive of FSPT in an ethnically diverse, multiracial population; therefore we enriched for nonwhite responses. The implemented survey was not validated for reliability

## 4. Findings quoted in the source's caveats (Results)

> the entire range of FSPT (I-VI) was observed in each racial group and in individuals reporting any range from light to dark pigmentary phenotypes.

> However, 61 blacks (11%) also reported burning moderately or very easily (FSPT I, II, III) and 401 whites (39%) reported tanning moderately or profusely (FSPT IV, V, VI).

## 5. Checks on the printed table

- Each race row's six counts sum to its printed N, except Latino: the six counts sum to 340 against a printed N of 342. The printed percentages for that row match either denominator to one decimal.
- The six overall percentages in the Results text sum to 99.8. Summing the counts in all eight race rows of Table II by type gives 155, 376, 613, 752, 846, and 635, which over 3,386 reproduce the six printed overall percentages.
- The race Ns in Table II sum to 3,379, seven short of 3,386, consistent with the table's note on missing data.
