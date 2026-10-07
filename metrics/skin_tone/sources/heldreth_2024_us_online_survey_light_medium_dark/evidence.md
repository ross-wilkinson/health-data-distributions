# Evidence: self-reported light, medium, and dark skin tone, US online survey (Heldreth et al. 2024)

All quotes are verbatim. Read in full on 2026-10-06 from a PDF of the published article supplied by Ross Wilkinson (`raw/papers/Heldreth et al. 2023 - ACM J. Responsib. Comput_.pdf`, kept untracked in the repo). The ACM page had returned HTTP 403 to the fetch tool earlier the same day.

Source: Heldreth CM, Monk EP, Clark AT, Ricco S, Schumann C, Eyee X. Which Skin Tone Measures Are the Most Inclusive? An Investigation of Skin Tone Measures for Artificial Intelligence. *ACM J. Responsib. Comput.* 1, 1, Article 7 (March 2024), 21 pages. https://doi.org/10.1145/3632120

Licence, from the first page: "This work is licensed under a Creative Commons Attribution International 4.0 License."

## 1. The numbers in data.csv

### Locator: Table 1

Table 1 is titled "Demographic Characteristics of Sample and Weighting To Be Nationally Representative of Race and Gender". Its columns are Variable, Levels, N, Unweighted % of Sample, Weighted % of Sample, and 2019 / 2020 ACS 5 Year Estimates. The rows for self-reported skin tone, under the heading "Not used for weighting", as printed:

> Self-reported skin tone | Light | 994 | 44.9% | 61.8% | no data available
>
> Self-reported skin tone | Medium | 582 | 27.1% | 23.2% | no data available
>
> Self-reported skin tone | Dark | 638 | 28.0% | 15.0% | no data available

Used for: the three weighted shares (stored as 0.618, 0.232, 0.150). `n` is the analytic sample of 2,214 on every row, because the shares are of the whole sample.

## 2. Sample size, recruitment, and weighting

Section 3, Survey Design:

> The final analytic sample contained 2,214 respondents. As shown in Table 1, the sample generally conformed to the population characteristics of the target population. To ensure adequate statistical power and representation of darker-skinned participants who represent a smaller part of the United States population, we oversampled respondents who self-reported having medium and dark skin tones.

> we launched an original data collection effort April–May 2021 in the United States through Qualtrics, a professional survey platform.

> Participants were randomly sampled on entry and then screened after answering to align with quotas based on population proportions from the US Census Bureau. Participants had to affirmatively answer that they agree to answer questions collecting potentially sensitive information, and to provide their best answers, and to be age 18 or older. The random sample was not nationally representative on entry, but data was weighted to be nationally representative on ethnoracial group and gender.

Footnote 6:

> Using a raking technique to weight representative population proportions for gender and race (including mixed race) in the U.S., per the 2019 American Communities Survey's 5-year demographics estimates.

## 3. How skin tone was recorded

Section 3, Survey Design:

> Next, respondents were randomly assigned to view one of the three skin tone scales

> We then asked participants to describe their own relative skin tone based on the scale they were assigned to. This question asked them, "Which of the following is closest to your skin tone?" Based on this question, participants were categorized into light (Fitzpatrick I and II, Monk points 1–3, Fenty 100–190), medium (Fitzpatrick III and IV, Monk points 4–6, Fenty 200–390) and dark (Fitzpatrick V and VI, Monk points 7–10, Fenty 400–490) skin tone groups. To improve the reliability of this question, we asked participants to hold the back of their hand up to the screen until they found the color on the scale that most closely matched their skin tone.

Footnote 4:

> While not all devices render colors in exactly the same way, we included use of desktop vs. mobile devices to answer the survey as a control in statistical modeling and found no significant effects.

Appendix A.1:

> If participants felt the skin tone measure did not contain a skin tone that matched them, then they could select "none of the above." This option was infrequently selected across all three skin tone measures (0.38% Fitzpatrick, 0.09% Fenty, 0.28% Monk).

Footnote 8:

> Skin tone, unsurprisingly, can be strongly connected with ethnoracial groups, but it is not a good proxy. 65.4% of light skin tone participants were white; 81.5% of dark participants were Black; medium skin tone participants were predominantly Black (28.9%), Latinx (27.0%), or white (20.6%)

## 4. Not in the paper

- The share of respondents choosing each of the 10 Monk points, each Fitzpatrick type, or each Fenty shade. Only the three pooled groups are reported.
- How many respondents were assigned to each scale.
- Any confidence interval on the skin tone shares.
- Age-weighted figures. Table 1 lists age under "Not used for weighting"; the weighted sample is 30.9% aged 18 to 29.

## 5. Checks on the printed table

Two of the unweighted percentages do not match their counts over 2,214: 582 is 26.3% (printed 27.1%) and 638 is 28.8% (printed 28.0%). 994 is 44.9% as printed. The three counts sum to 2,214. The weighted percentages, which are what data.csv holds, sum to 100.0% and cannot be checked from the paper. The data file records them as printed.

## 6. Leads from this paper's reference list (not opened)

- Reference 37: Wilkes M, Wright CY, du Plessis JL, Reeder A. 2015. Fitzpatrick skin type, individual typology angle, and melanin index in an African population. *JAMA Dermatol.* 151, 8 (2015), 902–903. This confirms the citation of the listing seen on ResearchGate (ACCESS_REQUESTS row 6).
- Reference 9: Pichon LC, et al. 2010. Measuring skin cancer risk in African Americans: Is the Fitzpatrick skin type classification scale culturally sensitive? *Ethnic. Dis.* 20, 2 (2010), 174–179. The paper says of it: "in a survey with over 2,000 Black adults, 59% were unable to identify their skin tone using the Fitzpatrick scale".
