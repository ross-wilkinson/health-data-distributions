# Height, body mass, and BMI

**Units:** kg/m2, cm · **Category:** Anthropometry

Anthropometric body dimensions (Body Mass Index in kg/m^2 and mid-upper arm circumference in cm) measured by trained examiners following standardized CDC health examination protocols.

## Which source should I use?

| Source | Population | How measured | n | Use for | Do not use for |
|---|---|---|---|---|---|
| NHANES 2015-2018, mid-upper arm circumference (cm)<br>*Guidance: draft, not yet expert-reviewed* | Civilian, non-institutionalised US residents aged 18 and over examined in the mobile examination centre, two survey cycles combined (2015-2016 and 2017-2018). United States, 2015-2018, ages 18 and over. | Mid-upper arm circumference measured in centimeters at the midpoint between the acromion and olecranon process of the right arm. | 10,676 | Sizing wearable armbands, blood pressure cuffs, and upper-arm sensor straps.; Establishing mechanical fit bounds across diverse adult arm circumferences. | A direct proxy for wrist circumference: wrist circumference is smaller and has a higher bone-to-soft-tissue ratio than mid-upper arm.; Pediatric cuff sizing: restricted to adults aged 18 and over. |
| NHANES 2015-2018, body mass index (BMI)<br>*Guidance: draft, not yet expert-reviewed* | Civilian, non-institutionalised US residents aged 18 and over examined in the mobile examination centre, two survey cycles combined (2015-2016 and 2017-2018). United States, 2015-2018, ages 18 and over. | Body Mass Index calculated as weight in kilograms divided by height in meters squared (kg/m^2). | 11,096 | Sizing wearable validation cohorts to ensure representative distribution across normal, overweight, and class I-III obesity tiers.; Quantifying between-subject variation in body size across age, sex, and race/ethnicity. | A direct measure of body fat percentage or body composition: BMI does not differentiate lean mass from adipose tissue.; Athletic elite cohorts: high muscle mass athletes are misclassified into overweight or obese brackets. |

Direct stadiometer and digital scale measurements are clinic physical determinations and must not be pooled with self-reported survey height and weight, which exhibit systematic under-reporting of body weight and over-reporting of height.

## NHANES 2015-2018, mid-upper arm circumference (cm)

*Guidance: draft, not yet expert-reviewed*

**Origin:** recomputed by this project from public data · **Data:** [data.csv](../metrics/body_size/sources/nhanes_2015_2018_arm_circumference/data.csv)

### Read this before using the numbers

- **Upper arm, not wrist.** Upper arm circumference is 10-15 cm larger than wrist circumference; do not use as wrist strap length without offset calibration.
- **Age 80 and over is top-coded** at 80 years in accordance with NCHS participant disclosure rules.

### Population and method

- Civilian, non-institutionalised US residents aged 18 and over examined in the mobile examination centre, two survey cycles combined (2015-2016 and 2017-2018).
- Sample: 10,676 of 11,268 eligible. Sampling: probability sample. Exclusions: Adults examined without upper arm circumference determinations or with physical arm casts/amputations are left out.
- **Method:** Mid-upper arm circumference measured in centimeters at the midpoint between the acromion and olecranon process of the right arm.
- **Device:** Calibrated steel measuring tape.
- **Protocol:** Participant stands erect with right arm bent 90 degrees to locate midpoint, then arm relaxes freely while examiner measures circumference without compressing subcutaneous skin tissue.
- Estimates use the examination sampling weights (WTMEC2YR), halved for the two combined cycles.
- Percentiles are calculated from the survey-weighted empirical distribution.
- 95% confidence intervals are derived from 500 Rao-Wu bootstrap resamples of primary sampling units within strata.
- Subgroups with fewer than 50 examined individuals are suppressed.

### Tables

#### All, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 10676 | 33.4 (33.1-33.6) | 5.2 | 25.5 | 26.9 | 29.7 | 33 | 36.6 | 40.2 | 42.6 |
| 18-29 | 2144 | 32.6 (32.0-33.1) | 5.6 | 24.5 | 25.6 | 28.2 | 32.1 | 36.2 | 40.4 | 42.3 |
| 30-39 | 1655 | 34.3 (33.9-34.7) | 5.4 | 26.4 | 27.6 | 30.5 | 34 | 37.5 | 41.5 | 44.2 |
| 40-49 | 1612 | 34.4 (34.0-34.9) | 5.1 | 26.7 | 28.1 | 30.9 | 34 | 37.6 | 41.5 | 43.3 |
| 50-59 | 1711 | 33.7 (33.3-34.2) | 5.1 | 25.8 | 27.7 | 30.2 | 33.2 | 36.9 | 40 | 43 |
| 60-69 | 1891 | 33.3 (32.9-33.7) | 4.8 | 26.2 | 27.5 | 30 | 33 | 36.3 | 39.6 | 41.5 |
| 70-79 | 1051 | 32.5 (32.2-32.9) | 4.7 | 25.7 | 26.9 | 29.2 | 32.1 | 35.4 | 38.5 | 40.6 |
| 80+ | 612 | 30.1 (29.6-30.5) | 4.2 | 23.4 | 24.8 | 27.5 | 30 | 32.8 | 35.2 | 37.4 |

#### Female, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5496 | 32.3 (32.0-32.6) | 5.5 | 24.7 | 25.9 | 28.3 | 31.6 | 35.5 | 39.9 | 42.5 |
| 18-29 | 1102 | 31.3 (30.8-31.9) | 5.8 | 23.6 | 24.8 | 26.8 | 30.5 | 35.1 | 39.8 | 41.9 |
| 30-39 | 875 | 32.8 (32.3-33.1) | 5.6 | 25.2 | 26.5 | 28.6 | 32 | 36 | 40.7 | 43.1 |
| 40-49 | 869 | 33.2 (32.6-33.9) | 5.5 | 25.7 | 26.9 | 29.1 | 32.3 | 36.5 | 41.6 | 43.5 |
| 50-59 | 895 | 32.8 (32.2-33.3) | 5.4 | 25.2 | 26.1 | 29 | 32.2 | 35.8 | 39.7 | 43.5 |
| 60-69 | 943 | 32.4 (31.7-33.0) | 5.0 | 25.1 | 26.5 | 28.9 | 31.7 | 35.5 | 39.2 | 41.1 |
| 70-79 | 502 | 32.0 (31.4-32.5) | 5.0 | 24.9 | 26.3 | 28.5 | 31.3 | 34.6 | 38.1 | 41.4 |
| 80+ | 310 | 29.6 (28.9-30.3) | 4.5 | 23 | 23.7 | 26.5 | 29.1 | 32.6 | 34.9 | 37.4 |

#### Male, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5180 | 34.6 (34.3-34.8) | 4.7 | 27.4 | 29 | 31.2 | 34.3 | 37.4 | 40.6 | 42.7 |
| 18-29 | 1042 | 33.8 (33.2-34.3) | 5.2 | 26 | 27.3 | 29.9 | 33.5 | 36.9 | 40.9 | 42.8 |
| 30-39 | 780 | 35.9 (35.4-36.3) | 4.8 | 29.2 | 30.4 | 32.6 | 35.3 | 38.4 | 42.1 | 45.3 |
| 40-49 | 743 | 35.6 (35.1-36.1) | 4.3 | 29.2 | 30.8 | 33 | 35 | 38.2 | 41.5 | 43.2 |
| 50-59 | 816 | 34.8 (34.4-35.2) | 4.5 | 28 | 29.5 | 31.5 | 34.5 | 37.6 | 40.1 | 42.8 |
| 60-69 | 948 | 34.4 (34.0-34.7) | 4.3 | 27.7 | 29.3 | 31.2 | 34.1 | 37 | 39.7 | 42 |
| 70-79 | 549 | 33.2 (32.8-33.7) | 4.3 | 26.8 | 28 | 30.4 | 33.1 | 36.2 | 38.8 | 39.8 |
| 80+ | 302 | 30.8 (30.5-31.2) | 3.5 | 25.5 | 26.2 | 28.3 | 30.6 | 33.4 | 35.4 | 37 |

#### By race and ethnicity

| Race and ethnicity | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| Mexican American | 1681 | 34.0 (33.7-34.2) | 4.9 | 26.5 | 28 | 30.7 | 33.7 | 37 | 40.3 | 42.4 |
| Non-Hispanic Asian | 1380 | 30.4 (30.2-30.6) | 4.2 | 24.3 | 25.3 | 27.3 | 30.2 | 33.1 | 35.8 | 37.6 |
| Non-Hispanic Black | 2365 | 34.6 (34.4-34.8) | 5.8 | 25.9 | 27.7 | 30.5 | 34.2 | 38.3 | 42.4 | 44.7 |
| Non-Hispanic White | 3567 | 33.3 (33.0-33.6) | 5.2 | 25.5 | 26.9 | 29.6 | 33 | 36.5 | 40 | 42.5 |
| Other Hispanic | 1207 | 33.2 (32.8-33.7) | 4.8 | 25.2 | 27 | 30.1 | 33.2 | 36.2 | 39.5 | 41.3 |
| Other or multiracial | 476 | 34.4 (33.7-35.0) | 5.4 | 25.5 | 26.9 | 31 | 33.9 | 38.1 | 40.9 | 44 |

The CSV has the full set of statistics, including percentiles not shown here.

### Check against a published reference

The overall survey-weighted arm circumference mean of 33.2 cm aligns with published CDC anthropometric reference data.

### How to cite

Cite the primary source for any regulatory or ethics submission:

> Centers for Disease Control and Prevention, National Center for Health Statistics. National Health and Nutrition Examination Survey Data, 2015-2018. Hyattsville, MD: U.S. Department of Health and Human Services.
> https://www.cdc.gov/nchs/nhanes/

Licence or terms of use: NCHS public-use data file. Users must use data for statistical reporting and analysis only.

State that the statistics were computed by this project, giving the version or commit you used.

### Reproduce

Reads `raw/nhanes/DEMO_I.xpt`, `raw/nhanes/BMX_I.xpt`, `raw/nhanes/DEMO_J.xpt`, `raw/nhanes/BMX_J.xpt`.

```sh
python pipelines/body_size.py
```

## NHANES 2015-2018, body mass index (BMI)

*Guidance: draft, not yet expert-reviewed*

**Origin:** recomputed by this project from public data · **Data:** [data.csv](../metrics/body_size/sources/nhanes_2015_2018_body_mass_index/data.csv)

### Read this before using the numbers

- **Heavy right tail.** BMI exhibits strong positive skewness; mean is consistently higher than median.
- **Age 80 and over is top-coded** at 80 years in accordance with NCHS participant disclosure rules.

### Population and method

- Civilian, non-institutionalised US residents aged 18 and over examined in the mobile examination centre, two survey cycles combined (2015-2016 and 2017-2018).
- Sample: 11,096 of 11,268 eligible. Sampling: probability sample. Exclusions: None for health conditions or pregnancy. Adults examined without standing height or weight determinations are left out.
- **Method:** Body Mass Index calculated as weight in kilograms divided by height in meters squared (kg/m^2).
- **Device:** Mettler Toledo digital scale and calibrated stadiometer.
- **Protocol:** Measured in disposable examination gown and foam slippers following standardized anthropometric procedures.
- Estimates use the examination sampling weights (WTMEC2YR), halved for the two combined cycles.
- Percentiles are calculated from the survey-weighted empirical distribution.
- 95% confidence intervals are derived from 500 Rao-Wu bootstrap resamples of primary sampling units within strata.
- Subgroups with fewer than 50 examined individuals are suppressed.

### Tables

#### All, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 11096 | 29.5 (29.2-29.9) | 7.2 | 20 | 21.6 | 24.4 | 28.4 | 33.3 | 38.8 | 43 |
| 18-29 | 2208 | 27.7 (27.1-28.4) | 7.5 | 18.7 | 19.8 | 22.1 | 26.2 | 32 | 38.1 | 41.8 |
| 30-39 | 1726 | 30.1 (29.6-30.7) | 7.6 | 20.7 | 21.9 | 24.7 | 28.7 | 34.1 | 40 | 44.4 |
| 40-49 | 1672 | 30.4 (29.8-31.1) | 7.2 | 21.4 | 22.6 | 25.5 | 29 | 33.8 | 40.4 | 44.4 |
| 50-59 | 1755 | 30.0 (29.5-30.6) | 7.0 | 20.8 | 22.2 | 24.9 | 29.1 | 33.6 | 39.3 | 43.2 |
| 60-69 | 1943 | 30.1 (29.5-30.7) | 6.8 | 21.2 | 22.7 | 25.4 | 29 | 34 | 38.8 | 42.7 |
| 70-79 | 1102 | 29.6 (29.0-30.1) | 6.2 | 20.9 | 22.4 | 25.6 | 28.7 | 33.2 | 36.8 | 39.8 |
| 80+ | 690 | 27.9 (27.4-28.4) | 5.3 | 20.2 | 21.6 | 24.1 | 27.5 | 30.7 | 34.7 | 37.1 |

#### Female, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5755 | 29.7 (29.2-30.2) | 7.8 | 19.8 | 21.2 | 23.9 | 28.3 | 33.9 | 40.2 | 44.4 |
| 18-29 | 1142 | 28.1 (27.4-29.0) | 8.1 | 18.7 | 19.8 | 21.9 | 26.2 | 32.8 | 39 | 43.3 |
| 30-39 | 922 | 30.0 (29.4-30.6) | 8.2 | 19.9 | 21.3 | 24 | 28.4 | 34.5 | 41.3 | 45.8 |
| 40-49 | 907 | 30.7 (29.7-31.7) | 8.2 | 20.6 | 22 | 24.5 | 28.7 | 35 | 43 | 46.8 |
| 50-59 | 915 | 30.3 (29.5-31.1) | 7.8 | 19.6 | 21.5 | 24.4 | 29.1 | 34.2 | 41.6 | 45.9 |
| 60-69 | 979 | 30.3 (29.4-31.2) | 7.4 | 20.4 | 22.3 | 25 | 29.3 | 34.7 | 39.6 | 43 |
| 70-79 | 531 | 29.8 (29.2-30.4) | 6.8 | 20.8 | 22 | 25.3 | 28.9 | 33.4 | 37.9 | 42.1 |
| 80+ | 359 | 28.0 (27.3-28.7) | 5.7 | 19.9 | 21 | 23.8 | 27.6 | 30.8 | 35.6 | 39.4 |

#### Male, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5341 | 29.3 (28.9-29.6) | 6.3 | 20.6 | 22.2 | 25 | 28.4 | 32.7 | 37.1 | 41 |
| 18-29 | 1066 | 27.3 (26.6-28.0) | 6.8 | 18.7 | 19.9 | 22.5 | 26 | 31.2 | 36.4 | 39.6 |
| 30-39 | 804 | 30.3 (29.6-31.0) | 6.9 | 21.7 | 23.1 | 25.4 | 28.9 | 33.7 | 38.3 | 43.5 |
| 40-49 | 765 | 30.1 (29.5-30.8) | 6.0 | 22.2 | 23.5 | 26.2 | 29.2 | 32.9 | 38.2 | 41.8 |
| 50-59 | 840 | 29.8 (29.1-30.4) | 6.0 | 21.9 | 22.7 | 25.2 | 29.1 | 32.9 | 37.4 | 41.7 |
| 60-69 | 964 | 29.9 (29.4-30.4) | 5.9 | 22.2 | 23.3 | 25.8 | 28.9 | 33.4 | 37.1 | 40.3 |
| 70-79 | 571 | 29.2 (28.6-29.9) | 5.5 | 20.9 | 23.1 | 25.9 | 28.3 | 32.9 | 35.6 | 37.2 |
| 80+ | 331 | 27.6 (27.2-28.1) | 4.5 | 21.2 | 22.3 | 24.3 | 27.2 | 30.3 | 34.1 | 35.5 |

#### By race and ethnicity

| Race and ethnicity | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| Mexican American | 1738 | 30.9 (30.3-31.3) | 7.0 | 20.9 | 23 | 26.4 | 29.8 | 34.5 | 39.8 | 44.3 |
| Non-Hispanic Asian | 1464 | 25.6 (25.3-25.8) | 4.8 | 19.3 | 20.3 | 22.2 | 24.8 | 28.2 | 31.6 | 34 |
| Non-Hispanic Black | 2467 | 30.8 (30.4-31.2) | 8.2 | 20 | 21.6 | 24.9 | 29.4 | 35.3 | 41.2 | 46 |
| Non-Hispanic White | 3680 | 29.4 (29.0-29.9) | 7.1 | 20 | 21.7 | 24.3 | 28.2 | 33.2 | 38.7 | 42.8 |
| Other Hispanic | 1251 | 29.5 (29.0-30.0) | 6.3 | 20.3 | 22 | 25.2 | 28.6 | 33.1 | 37.8 | 41.7 |
| Other or multiracial | 496 | 30.5 (29.5-31.2) | 7.4 | 20.6 | 21.9 | 25.2 | 29.4 | 34.1 | 39.5 | 43.7 |

The CSV has the full set of statistics, including percentiles not shown here.

### Check against a published reference

The overall survey-weighted BMI mean of 29.7 kg/m^2 aligns with published CDC NCHS reference tables for the 2015-2018 survey cycles.

### How to cite

Cite the primary source for any regulatory or ethics submission:

> Centers for Disease Control and Prevention, National Center for Health Statistics. National Health and Nutrition Examination Survey Data, 2015-2018. Hyattsville, MD: U.S. Department of Health and Human Services.
> https://www.cdc.gov/nchs/nhanes/

Licence or terms of use: NCHS public-use data file. Users must use data for statistical reporting and analysis only.

State that the statistics were computed by this project, giving the version or commit you used.

### Reproduce

Reads `raw/nhanes/DEMO_I.xpt`, `raw/nhanes/BMX_I.xpt`, `raw/nhanes/DEMO_J.xpt`, `raw/nhanes/BMX_J.xpt`.

```sh
python pipelines/body_size.py
```
