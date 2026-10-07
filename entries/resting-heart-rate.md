# Resting heart rate and pulse

**Units:** beats/min · **Category:** Cardiovascular

Heart or pulse rate, in beats per minute, while the person is at rest. The value depends on how and when it is taken, so each source below states its method.

## Which source should I use?

| Source | Population | How measured | n | Use for | Do not use for |
|---|---|---|---|---|---|
| NHANES 2015-2018, clinic pulse<br>*Guidance: draft, not yet expert-reviewed* | Civilian, non-institutionalised US residents aged 18 and over who were examined, two survey cycles combined (2015-2016 and 2017-2018). United States, 2015-2018, ages 18 and over. | Pulse counted for 30 seconds by an examiner and doubled (NHANES variable BPXPLS). | 10,848 | Sizing a study of clinic-measured pulse in US adults, by age, sex, and race and ethnicity.; Seeing the spread of a clinic pulse count in the general US adult population. | A reference for wearable resting heart rate: that is a different quantity. See the comparison of sources for this metric.; A healthy reference range: nobody was excluded for medication, medical conditions, pregnancy, or an irregular pulse. |
| Quer et al. 2020, Fitbit wearable cohort (92,457 US adults), daily resting heart rate<br>*Guidance: draft, not yet expert-reviewed* | Fitbit users in the United States (all 50 states) who consistently wore a wrist heart-rate tracker. Starting from a convenience sample of 200,000 users, the authors kept 92,457 adults with a reported sex, age, and BMI who met the wear-time rules below. About 63% were women; average age was 45.8 years and average BMI 28.4 kg/m2 (as the paper reports them). United States, March 2016 to February 2018, ages 18 to 100 (self-reported); average 45.8. | A single resting heart rate value per person per day, calculated by a proprietary Fitbit formula from interbeat intervals derived from the optical (PPG) sensor. The paper says this value is expected to represent the true resting heart rate that would be obtained supine immediately after waking, before getting out of bed, and that it was primarily calculated during periods of sleep. | 92,457 | Seeing the typical level of daily resting heart rate as a Fitbit wrist tracker reports it, in a large group of adult US users of that device.; Sizing a study of wearable-derived resting heart rate, with the caveat that this is a self-selected cohort of device owners. | A reference for a clinic pulse or any manually counted heart rate: the quantity and the setting differ.; A distribution for the US general population: the cohort is device owners, selected by wear-time rules, and the figures are not weighted.; Percentiles or a normal range: the paper's text gives a mean only, and this entry holds no percentiles.; A reference for devices other than the Fitbit models listed, or for other algorithms. |
| Fitbit daily resting heart rate by sex, 92,457 US adults, 2016-2018 (Quer et al. 2020, distribution digitised from Fig 2)<br>*Digitised from a figure*<br>*Guidance: draft, not yet expert-reviewed* | Fitbit users in the United States (all 50 states) who consistently wore a wrist heart-rate tracker. Starting from a convenience sample of 200,000 users, the authors kept 92,457 adults with a reported sex, age, and BMI who met the wear-time rules below. About 63% were women; average age was 45.8 years and average BMI 28.4 kg/m2 (as the paper reports them). United States, March 2016 to February 2018, ages 18 to 100 (self-reported); average 45.8. | A single resting heart rate value per person per day, calculated by a proprietary Fitbit formula from interbeat intervals derived from the optical (PPG) sensor. The paper says this value is expected to represent the true resting heart rate that would be obtained supine immediately after waking, before getting out of bed, and that it was primarily calculated during periods of sleep. | 92,457 | The spread of wearable-reported resting heart rate by sex in a large group of adult Fitbit users: the only percentiles available for this kind of measurement in this entry.; Sizing a study of wearable-derived resting heart rate, with the caveat that this is a self-selected group of device owners. | A reference for a clinic pulse: the quantity, setting, and population all differ.; A distribution for the US general population: the cohort is unweighted device owners selected by wear-time rules.; Percentiles by age: the figure gives the two sexes only.; The distribution of a single day's value: each person contributes their average over many days, so this is the spread between people. |

The two sources measure different quantities in different people and must not be merged. NHANES is a pulse counted for 30 seconds by an examiner after 5 minutes of seated rest in a clinic, in a probability sample of US adults aged 18 and over (2015-2018, weighted, no exclusions for medication or conditions). The Fitbit cohort (Quer et al. 2020) is a daily value from a proprietary algorithm that is meant to represent a supine rate on waking, taken in normal living conditions and averaged over many days per person, in a convenience sample of device owners (2016-2018, about 63% women, average age 45.8, unweighted). In the two data files the NHANES mean is 72.41 beats/min (median 72.0) and the Fitbit cohort mean is 65.5 beats/min, so the wearable mean is the lower of the two. Method, timing and population all differ, and the two files do not separate their effects, so the gap cannot be attributed to the device or the method alone. The Fitbit source records only a mean, so no other central or spread values can be compared. A third source gives the Fitbit cohort's distribution by sex, measured from the paper's Fig 2 and labelled as digitised: medians of 62.9 beats/min for men and 66.4 for women, against NHANES clinic-pulse medians of 70 and 72. The same cautions apply, and the digitised percentiles describe differences between people's long-run averages, not day-to-day values.

## NHANES 2015-2018, clinic pulse

*Guidance: draft, not yet expert-reviewed*

**Origin:** recomputed by this project from public data · **Data:** [data.csv](../metrics/resting_heart_rate/sources/nhanes_2015_2018_clinic_pulse/data.csv)

### Read this before using the numbers

- **This is a clinic pulse, not a wearable resting heart rate.** Overnight or daily resting heart rate from a wearable is a different quantity, taken by a different method at a different time. Do not use these values as a reference for one.
- **Values are even numbers.** A 30-second count doubled cannot be odd, so percentiles move in steps of 2 beats/min.
- **This is the general population, not a healthy reference sample.** Nobody was excluded for medication (for example beta blockers), medical conditions, pregnancy, or an irregular pulse.
- **Age 80 and over is one group** because NHANES records all such ages as 80.
- **Race and ethnicity groups are NHANES's own categories**, self-reported.

### Population and method

- Civilian, non-institutionalised US residents aged 18 and over who were examined, two survey cycles combined (2015-2016 and 2017-2018).
- Sample: 10,848 of 11,268 eligible. Sampling: probability sample. Exclusions: None for medication (for example beta blockers), medical conditions, pregnancy, or an irregular pulse. Adults examined without a pulse reading are left out.
- **Method:** Pulse counted for 30 seconds by an examiner and doubled (NHANES variable BPXPLS).
- **Device:** Counted by an examiner; no device is recorded in this entry.
- **Protocol:** The participant rested quietly, seated, for 5 minutes, during the NHANES mobile examination centre visit.
- Estimates use the examination sampling weights, halved for the two combined cycles. Percentiles are from the weighted empirical distribution.
- 95% intervals are from 500 bootstrap resamples of primary sampling units within strata (Rao-Wu), so they reflect the survey's clustered design.
- No adjustment was made for examined adults without a pulse reading.
- Subgroups with fewer than 50 people are not reported.

### Tables

#### All, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 10848 | 72.4 (72.0-72.9) | 11.7 | 56 | 58 | 64 | 72 | 80 | 88 | 94 |
| 18-29 | 2139 | 74.7 (74.0-75.5) | 11.9 | 56 | 60 | 66 | 74 | 82 | 90 | 94 |
| 30-39 | 1661 | 73.5 (72.9-74.0) | 11.6 | 56 | 60 | 66 | 74 | 80 | 88 | 94 |
| 40-49 | 1627 | 73.4 (72.6-74.3) | 11.4 | 58 | 60 | 66 | 72 | 80 | 88 | 94 |
| 50-59 | 1705 | 71.9 (70.9-73.0) | 12.0 | 56 | 58 | 64 | 70 | 78 | 88 | 92 |
| 60-69 | 1929 | 70.1 (69.2-70.9) | 11.1 | 54 | 56 | 62 | 70 | 76 | 84 | 90 |
| 70-79 | 1095 | 69.6 (68.7-70.7) | 10.9 | 54 | 58 | 62 | 68 | 76 | 84 | 90 |
| 80+ | 692 | 69.0 (68.0-69.8) | 10.4 | 54 | 58 | 62 | 68 | 76 | 82 | 88 |

#### Female, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5594 | 73.6 (73.1-74.1) | 11.3 | 58 | 60 | 66 | 72 | 80 | 88 | 94 |
| 18-29 | 1104 | 77.4 (76.5-78.3) | 11.8 | 60 | 64 | 70 | 76 | 84 | 92 | 96 |
| 30-39 | 875 | 74.8 (73.7-75.9) | 11.0 | 58 | 62 | 66 | 74 | 82 | 90 | 94 |
| 40-49 | 879 | 74.7 (73.6-76.0) | 11.4 | 58 | 60 | 66 | 74 | 82 | 90 | 96 |
| 50-59 | 888 | 72.1 (70.9-73.2) | 11.3 | 56 | 60 | 64 | 70 | 78 | 86 | 92 |
| 60-69 | 964 | 70.9 (69.8-72.0) | 10.1 | 56 | 60 | 64 | 70 | 78 | 84 | 88 |
| 70-79 | 527 | 70.8 (69.7-71.9) | 10.3 | 56 | 60 | 64 | 68 | 76 | 86 | 90 |
| 80+ | 357 | 69.7 (68.4-70.7) | 10.3 | 54 | 58 | 62 | 70 | 76 | 82 | 88 |

#### Male, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5254 | 71.2 (70.6-71.8) | 11.9 | 54 | 58 | 62 | 70 | 78 | 88 | 92 |
| 18-29 | 1035 | 72.2 (71.1-73.3) | 11.5 | 56 | 58 | 64 | 72 | 80 | 88 | 92 |
| 30-39 | 786 | 72.2 (71.0-73.4) | 12.0 | 54 | 58 | 64 | 72 | 80 | 88 | 94 |
| 40-49 | 748 | 72.0 (70.9-73.3) | 11.3 | 56 | 58 | 64 | 72 | 78 | 86 | 90 |
| 50-59 | 817 | 71.8 (70.5-73.3) | 12.8 | 56 | 58 | 62 | 70 | 78 | 88 | 96 |
| 60-69 | 965 | 69.2 (67.7-70.7) | 12.0 | 52 | 54 | 60 | 68 | 76 | 86 | 90 |
| 70-79 | 568 | 68.2 (66.9-69.5) | 11.6 | 52 | 56 | 60 | 66 | 74 | 82 | 92 |
| 80+ | 335 | 68.0 (66.7-69.2) | 10.5 | 54 | 56 | 60 | 66 | 74 | 82 | 88 |

#### By race and ethnicity

| Race and ethnicity | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| Mexican American | 1704 | 73.1 (72.2-73.7) | 11.5 | 56 | 60 | 64 | 72 | 80 | 88 | 94 |
| Non-Hispanic Asian | 1386 | 72.3 (71.3-73.2) | 11.0 | 56 | 58 | 64 | 72 | 80 | 86 | 92 |
| Non-Hispanic Black | 2414 | 72.2 (71.5-72.9) | 12.0 | 54 | 58 | 64 | 72 | 78 | 88 | 94 |
| Non-Hispanic White | 3638 | 72.2 (71.7-72.9) | 11.7 | 56 | 58 | 64 | 72 | 80 | 88 | 92 |
| Other Hispanic | 1214 | 72.4 (71.6-73.2) | 11.2 | 56 | 58 | 64 | 72 | 78 | 88 | 94 |
| Other or multiracial | 492 | 74.2 (72.7-75.8) | 12.6 | 56 | 58 | 64 | 74 | 82 | 90 | 96 |

The CSV has the full set of statistics, including percentiles not shown here.

### Check against a published reference

CDC's own reference report for 1999-2008 (Ostchega et al., National Health Statistics Reports no. 41) gives means of 71 beats/min for men and 74 for women aged 20 and over, in a sample that excluded conditions and medications affecting pulse. The values here, for a later period and with no exclusions, are 71.2 and 73.6. The report itself was read on 2026-10-06 (https://www.cdc.gov/nchs/data/nhsr/nhsr041.pdf). Its abstract states: "females aged 20 and over have an RPR of 74 beats/min, SE 0.2, and males aged 20 and over have an RPR of 71 beats/min, SE 0.3", and "The mean RPR in adulthood plateaus at 72 beats/min".

### How to cite

Cite the primary source for any regulatory or ethics submission:

> Centers for Disease Control and Prevention, National Center for Health Statistics. National Health and Nutrition Examination Survey Data, 2015-2018. Hyattsville, MD: U.S. Department of Health and Human Services.
> https://www.cdc.gov/nchs/nhanes/

Licence or terms of use: NCHS public-use data file. No licence name is stated; the NCHS terms (https://www.cdc.gov/nchs/data_access/restrictions.htm) say users must "Use the data in this dataset for statistical reporting and analysis only."

State that the statistics were computed by this project, giving the version or commit you used.

### Reproduce

Reads `raw/nhanes/DEMO_I.xpt`, `raw/nhanes/BPX_I.xpt`, `raw/nhanes/DEMO_J.xpt`, `raw/nhanes/BPX_J.xpt`.

```sh
python pipelines/resting_pulse.py
```

## Quer et al. 2020, Fitbit wearable cohort (92,457 US adults), daily resting heart rate

*Guidance: draft, not yet expert-reviewed*

**Origin:** transcribed from a publication · **Data:** [data.csv](../metrics/resting_heart_rate/sources/quer_2020_fitbit_92457_adults/data.csv)

### Read this before using the numbers

- **This is a wearable-derived daily value from a proprietary algorithm.** The paper states the formula is Fitbit's own and that the value is expected to represent a supine resting rate on waking; it is not a clinic measurement.
- **Only one overall mean is recorded.** The text gives no separate mean for women and men or for age groups (those appear only in figures), and no percentiles. The paper states that "95% of men had an RHR between 50 and 80 bpm, while the corresponding range for women was between 53 and 82 bpm" but does not say these are central percentile bounds, so they are not entered as data.
- **The mean is of people, over their days.** The paper says the mean is "for all individuals over all available monitored days"; it does not say whether this is the mean of per-person averages or of all daily values pooled.
- **The SD of 7.7 is an interpretation.** The paper writes "65.5 ± 7.7 bpm" without saying what the 7.7 denotes. It is entered as the between-person SD because nothing else fits; see verification.
- **Self-selected cohort.** The authors state the cohort "is not likely to be representative of the total socioeconomic and demographic diversity of the U.S." About 63% were women and the average age was 45.8; age was self-reported, BMI was calculated from self-reported height and weight, and sex was reported by the user.
- **Strict wear-time rules.** People needed at least 2 days per week with 20 or more hours of wear for at least 35 weeks, which selects consistent users.
- **Resting heart rate varies with age, sex, BMI, sleep, and time of year.** The authors report a change of 2 bpm in the population average over the year, peaking in the first week of January with a minimum at the end of July; a single overall mean mixes all of this.
- **The underlying data are not public.** Fitbit owns them and the authors state they cannot share them, so this value cannot be recomputed.

### Population and method

- Fitbit users in the United States (all 50 states) who consistently wore a wrist heart-rate tracker. Starting from a convenience sample of 200,000 users, the authors kept 92,457 adults with a reported sex, age, and BMI who met the wear-time rules below. About 63% were women; average age was 45.8 years and average BMI 28.4 kg/m2 (as the paper reports them).
- Sample: 92,457. Sampling: convenience sample. Exclusions: Users who did not report sex, whose self-reported age was under 18 or over 100, or whose BMI (from self-reported height and weight) was outside 15 to 50 kg/m2; days with the device worn under 20 hours; users without at least 2 qualifying days per week for at least 35 weeks. No exclusion for medication or medical conditions is stated.
- **Method:** A single resting heart rate value per person per day, calculated by a proprietary Fitbit formula from interbeat intervals derived from the optical (PPG) sensor. The paper says this value is expected to represent the true resting heart rate that would be obtained supine immediately after waking, before getting out of bed, and that it was primarily calculated during periods of sleep.
- **Device:** Fitbit wrist-worn trackers: Charge HR versions 1 to 3 (65% of individuals), Blaze (21%), Alta HR (8%), Ionic (3%), Surge (2%), Versa (1%).
- **Protocol:** Continuous wear, with measurements obtained daily in normal living conditions. Only days with at least 20 hours of wear count. The mean in data.csv is the paper's mean RHR "for all individuals over all available monitored days" (median 320 days per person, maximum possible 730).
- The paper reports the mean as a single sentence in the Results text, with no table and no confidence interval. No sampling weights or adjustment to the US population are described in the text read.
- The paper gives the mean as 65.5 ± 7.7 bpm and does not define the 7.7. It is recorded in data.csv as the SD, between people, of each person's average daily resting heart rate. That reading is Ross Wilkinson's (2026-10-06), on two grounds stated under verification. The Abstract rounds the mean to 65.

### Tables

| Sex | Age | n | Mean (95% CI) | SD | Source location |
|---|---|---|---|---|---|
| All | All | 92457 | 65.5 | 7.7 | Results, Resting heart rate (mean); Methods, Population (n) |

### Check against a published reference

The Abstract gives the mean daily RHR as 65 bpm; the Results give 65.5 bpm (both quoted in evidence.md), which agree to rounding. The wording of every quoted passage was checked in two independent renderings of the full text (PLOS and Europe PMC). Reading 7.7 as an SD was checked two ways. First, the same passage gives age as "45.8 ± 14.4 years", which for adults aged 18 to 100 can only be an SD. Second, the paper's Fig 2 (distribution of average daily resting heart rate for men and women) shows curves about 17 beats/min wide at half their peak height, which for a roughly normal shape is an SD of about 7; a standard error or confidence interval for 92,457 people would be near 0.03. The figure was used only to check the meaning of 7.7. No value was read from it into data.csv.

### How to cite

Cite the primary source for any regulatory or ethics submission:

> Quer G, Gouda P, Galarnyk M, Topol EJ, Steinhubl SR. Inter- and intraindividual variability in daily resting heart rate and its associations with age, sex, sleep, BMI, and time of year: Retrospective, longitudinal cohort study of 92,457 adults. PLOS ONE. 2020;15(2):e0227709.
> doi:10.1371/journal.pone.0227709
> https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0227709

Licence or terms of use: © 2020 Quer et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Reproduce

Transcribed from <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0227709> (accessed 2026-10-06). Quotes and locators: [evidence.md](../metrics/resting_heart_rate/sources/quer_2020_fitbit_92457_adults/evidence.md).

## Fitbit daily resting heart rate by sex, 92,457 US adults, 2016-2018 (Quer et al. 2020, distribution digitised from Fig 2)

*Guidance: draft, not yet expert-reviewed*

**Origin:** digitised from a published figure · **Data:** [data.csv](../metrics/resting_heart_rate/sources/quer_2020_fitbit_fig2_digitised/data.csv)

Measured from Fig 2 (distribution of average daily resting heart rate for men and women). Precision: about 0.5 beats/min for the percentiles and 0.1 beats/min for the means. Method: Publisher's 2180 x 1512 pixel image; plot frame located in pixels (40 to 90 beats/min, 0 to 0.06 of individuals); each curve's vertical centre read at every whole beat per minute by colour. Script: pipelines/digitise/quer_2020_fig2.py.

### Read this before using the numbers

- **Measured from a chart and then computed.** The percentiles are derived from curve heights read off the figure, not from the data. Treat them as good to about half a beat per minute.
- **The half-beat alignment is inferred.** Whether a plotted value of 60 means 60.0 to 60.9 or 59.5 to 60.4 is not stated. The first reading is used because it reproduces the figure's own mean lines; the second would lower every value here by 0.5.
- **Between-person spread of long-run averages.** A person's own day-to-day variation is not in these numbers.
- **This is a wearable-derived daily value from a proprietary algorithm.** The paper states the formula is Fitbit's own and that the value is expected to represent a supine resting rate on waking; it is not a clinic measurement.
- **Self-selected cohort.** The authors state the cohort "is not likely to be representative of the total socioeconomic and demographic diversity of the U.S." About 63% were women and the average age was 45.8; age was self-reported, BMI was calculated from self-reported height and weight, and sex was reported by the user.
- **Strict wear-time rules.** People needed at least 2 days per week with 20 or more hours of wear for at least 35 weeks, which selects consistent users.

### Population and method

- Fitbit users in the United States (all 50 states) who consistently wore a wrist heart-rate tracker. Starting from a convenience sample of 200,000 users, the authors kept 92,457 adults with a reported sex, age, and BMI who met the wear-time rules below. About 63% were women; average age was 45.8 years and average BMI 28.4 kg/m2 (as the paper reports them).
- Sample: 92,457. Sampling: convenience sample. Exclusions: Users who did not report sex, whose self-reported age was under 18 or over 100, or whose BMI (from self-reported height and weight) was outside 15 to 50 kg/m2; days with the device worn under 20 hours; users without at least 2 qualifying days per week for at least 35 weeks. No exclusion for medication or medical conditions is stated.
- **Method:** A single resting heart rate value per person per day, calculated by a proprietary Fitbit formula from interbeat intervals derived from the optical (PPG) sensor. The paper says this value is expected to represent the true resting heart rate that would be obtained supine immediately after waking, before getting out of bed, and that it was primarily calculated during periods of sleep.
- **Device:** Fitbit wrist-worn trackers: Charge HR versions 1 to 3 (65% of individuals), Blaze (21%), Alta HR (8%), Ionic (3%), Surge (2%), Versa (1%).
- **Protocol:** Continuous wear, with measurements obtained daily in normal living conditions. Only days with at least 20 hours of wear count. The mean in data.csv is the paper's mean RHR "for all individuals over all available monitored days" (median 320 days per person, maximum possible 730).
- The paper's Fig 2 plots, for men and for women, the fraction of individuals at each whole beat per minute of their average daily resting heart rate, from 40 to 90. The height of each curve was measured at every whole value from 41 to 89.
- The mean, SD, and percentiles here are computed from those measured fractions; none is printed in the paper. Each plotted value is treated as covering one beat per minute upward from that value, which is the reading under which the computed means match the dashed mean lines drawn in the figure.
- Percentiles are interpolated linearly within each one-beat step. Values below 41 and above 89 are not shown in the figure; the measured fractions sum to 1.000 for each sex, so little lies outside.
- n is the number of men (34,621) and women (57,836) stated in the figure caption.

### Tables

#### Male, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 | Source location |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All | 34621 | 63.4 | 7.5 | 51.8 | 54.1 | 58.1 | 62.9 | 68.2 | 73.4 | 76.6 | Fig 2 |

#### Female, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 | Source location |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All | 57836 | 66.6 | 7.4 | 55 | 57.3 | 61.5 | 66.4 | 71.5 | 76.3 | 79.3 | Fig 2 |

The CSV has the full set of statistics, including percentiles not shown here.

### Check against a published reference

Four checks against numbers the paper states. (1) The measured fractions sum to 1.0000 for men and 0.9999 for women. (2) The computed means, 63.37 and 66.61, sit 0.06 and 0.08 below the dashed mean lines measured in the same figure (63.43 and 66.69). (3) The text says "95% of men had an RHR between 50 and 80 bpm, while the corresponding range for women was between 53 and 82 bpm"; the computed 2.5th and 97.5th percentiles are 49.8 and 79.6 for men and 53.0 and 81.9 for women. (4) Combining the sexes by the caption's counts gives a mean of 65.40 and SD of 7.62 against the text's "65.5 ± 7.7 bpm".

### How to cite

Cite the primary source for any regulatory or ethics submission:

> Quer G, Gouda P, Galarnyk M, Topol EJ, Steinhubl SR. Inter- and intraindividual variability in daily resting heart rate and its associations with age, sex, sleep, BMI, and time of year: Retrospective, longitudinal cohort study of 92,457 adults. PLOS ONE. 2020;15(2):e0227709.
> doi:10.1371/journal.pone.0227709
> https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0227709

Licence or terms of use: © 2020 Quer et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Reproduce

Digitised from <https://journals.plos.org/plosone/article/figure?id=10.1371/journal.pone.0227709.g002> (accessed 2026-10-06). Measuring script: `pipelines/digitise/quer_2020_fig2.py`. Measurements, quotes and locators: [evidence.md](../metrics/resting_heart_rate/sources/quer_2020_fitbit_fig2_digitised/evidence.md).
