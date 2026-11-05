# Blood pressure (systolic and diastolic)

**Units:** mmHg · **Category:** Cardiovascular

Auscultatory systolic and diastolic blood pressure in mmHg measured by physician examiners using a calibrated mercury sphygmomanometer after 5 minutes of seated rest.

## Which source should I use?

| Source | Population | How measured | n | Use for | Do not use for |
|---|---|---|---|---|---|
| NHANES 2015-2018, clinic diastolic blood pressure<br>*Guidance: draft, not yet expert-reviewed* | Civilian, non-institutionalised US residents aged 18 and over examined in the mobile examination centre, two survey cycles combined (2015-2016 and 2017-2018). United States, 2015-2018, ages 18 and over. | Auscultatory diastolic blood pressure (fifth Korotkoff sound, disappearance of sound) measured using a mercury sphygmomanometer by a certified physician examiner. | 10,818 | Sizing clinical trials evaluating non-invasive blood pressure monitoring devices against auscultatory mercury reference standards.; Establishing empirical population distributions and between-subject standard deviations (sigma_b) for clinic diastolic blood pressure. | A direct reference for 24-hour ambulatory blood pressure monitoring (ABPM) or continuous nocturnal wearable estimates.; A filtered 'normotensive' reference cohort: general population participants were not excluded for hypertension or antihypertensive pharmacology. |
| NHANES 2015-2018, clinic systolic blood pressure<br>*Guidance: draft, not yet expert-reviewed* | Civilian, non-institutionalised US residents aged 18 and over examined in the mobile examination centre, two survey cycles combined (2015-2016 and 2017-2018). United States, 2015-2018, ages 18 and over. | Auscultatory systolic blood pressure (first Korotkoff sound) measured using a mercury sphygmomanometer by a certified physician examiner. | 10,818 | Sizing clinical trials evaluating non-invasive blood pressure monitoring devices against auscultatory mercury reference standards.; Establishing empirical population distributions and between-subject standard deviations (sigma_b) for clinic systolic blood pressure. | A direct reference for 24-hour ambulatory blood pressure monitoring (ABPM) or continuous nocturnal wearable estimates: daytime clinic auscultations exhibit higher white-coat alerting bias.; A filtered 'normotensive' reference cohort: general population participants were not excluded for hypertension or antihypertensive pharmacology. |

Auscultatory clinic blood pressure reflects daytime resting arterial pressure and incorporates situational alerting (white-coat) effects. Continuous cuffless wearable estimates (optical pulse transit time, PTT) and ambulatory 24-hour recordings (ABPM) are distinct physiological measurement paradigms and must not be pooled with clinic auscultation.

## NHANES 2015-2018, clinic diastolic blood pressure

*Guidance: draft, not yet expert-reviewed*

**Origin:** recomputed by this project from public data · **Data:** [data.csv](../metrics/blood_pressure/sources/nhanes_2015_2018_clinic_diastolic/data.csv)

### Read this before using the numbers

- **Clinic auscultation, not wearable PTT.** Disappearance of Korotkoff sound represents diastolic vascular resistance at rest.
- **General population reference.** Participants taking antihypertensive pharmacology are included.
- **Age 80 and over is top-coded** at 80 years in accordance with NCHS participant disclosure rules.

### Population and method

- Civilian, non-institutionalised US residents aged 18 and over examined in the mobile examination centre, two survey cycles combined (2015-2016 and 2017-2018).
- Sample: 10,818 of 11,268 eligible. Sampling: probability sample. Exclusions: None for antihypertensive medication, cardiovascular conditions, pregnancy, or arrhythmias. Zero diastolic values (Korotkoff phase 5 not heard) are treated as missing.
- **Method:** Auscultatory diastolic blood pressure (fifth Korotkoff sound, disappearance of sound) measured using a mercury sphygmomanometer by a certified physician examiner.
- **Device:** Baumanometer mercury sphygmomanometer with calibrated adult/large cuff sizes.
- **Protocol:** Seated quietly for 5 minutes in a private exam room; standard CDC protocol averages readings 2 and 3 (the initial reading is discarded to mitigate acute situational anxiety).
- Estimates use the examination sampling weights (WTMEC2YR), halved for the two combined cycles.
- Percentiles are calculated from the survey-weighted empirical distribution.
- 95% confidence intervals are derived from 500 Rao-Wu bootstrap resamples of primary sampling units within strata.
- Subgroups with fewer than 50 examined individuals are suppressed.

### Tables

#### All, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 10818 | 71.1 (70.3-71.9) | 12.1 | 53 | 57 | 64 | 71 | 78 | 86 | 90 |
| 18-29 | 2135 | 66.7 (65.6-67.8) | 10.2 | 51 | 54 | 60 | 67 | 73 | 79 | 82 |
| 30-39 | 1656 | 72.8 (71.9-73.8) | 11.0 | 56 | 60 | 65 | 72 | 79 | 86 | 92 |
| 40-49 | 1626 | 75.6 (74.6-76.7) | 10.5 | 58 | 63 | 69 | 75 | 83 | 89 | 92 |
| 50-59 | 1704 | 75.3 (74.1-76.4) | 11.4 | 58 | 63 | 69 | 75 | 82 | 90 | 93 |
| 60-69 | 1922 | 71.2 (70.3-72.1) | 11.8 | 54 | 58 | 64 | 71 | 78 | 86 | 89 |
| 70-79 | 1089 | 65.6 (64.4-66.8) | 12.8 | 49 | 53 | 59 | 66 | 73 | 80 | 84 |
| 80+ | 686 | 61.9 (60.5-63.5) | 15.7 | 37 | 46 | 55 | 63 | 71 | 79 | 84 |

#### Female, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5578 | 69.5 (68.7-70.2) | 12.0 | 52 | 56 | 63 | 69 | 77 | 84 | 88 |
| 18-29 | 1103 | 65.5 (64.3-66.7) | 9.5 | 49 | 53 | 60 | 66 | 72 | 78 | 81 |
| 30-39 | 872 | 70.0 (69.1-70.8) | 10.1 | 55 | 58 | 63 | 69 | 76 | 82 | 87 |
| 40-49 | 879 | 73.4 (72.1-74.7) | 10.3 | 57 | 61 | 66 | 73 | 79 | 87 | 91 |
| 50-59 | 888 | 74.3 (73.1-75.6) | 11.4 | 56 | 62 | 68 | 75 | 80 | 87 | 92 |
| 60-69 | 960 | 69.7 (68.6-70.8) | 11.8 | 52 | 57 | 63 | 69 | 77 | 84 | 87 |
| 70-79 | 523 | 64.9 (63.2-66.7) | 14.1 | 48 | 52 | 58 | 65 | 73 | 81 | 84 |
| 80+ | 353 | 61.6 (59.8-63.4) | 16.3 | 34 | 43 | 55 | 63 | 72 | 79 | 84 |

#### Male, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5240 | 72.8 (71.8-73.8) | 12.0 | 54 | 58 | 66 | 73 | 80 | 88 | 92 |
| 18-29 | 1032 | 67.8 (66.6-69.2) | 10.7 | 52 | 55 | 61 | 68 | 75 | 81 | 84 |
| 30-39 | 784 | 75.8 (74.4-77.1) | 11.0 | 59 | 62 | 68 | 76 | 82 | 91 | 95 |
| 40-49 | 747 | 78.0 (76.8-79.1) | 10.1 | 61 | 66 | 72 | 77 | 85 | 91 | 94 |
| 50-59 | 816 | 76.3 (74.8-77.7) | 11.4 | 60 | 63 | 69 | 76 | 83 | 90 | 93 |
| 60-69 | 962 | 72.9 (71.6-74.1) | 11.6 | 56 | 59 | 66 | 73 | 80 | 86 | 91 |
| 70-79 | 566 | 66.4 (65.1-67.8) | 11.1 | 49 | 53 | 61 | 67 | 73 | 79 | 83 |
| 80+ | 333 | 62.3 (60.3-64.3) | 14.8 | 42 | 48 | 55 | 63 | 71 | 78 | 83 |

#### By race and ethnicity

| Race and ethnicity | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| Mexican American | 1701 | 70.4 (69.5-71.4) | 12.3 | 53 | 56 | 63 | 70 | 78 | 85 | 90 |
| Non-Hispanic Asian | 1385 | 72.7 (72.0-73.3) | 11.7 | 54 | 59 | 66 | 73 | 80 | 86 | 91 |
| Non-Hispanic Black | 2408 | 72.4 (71.3-73.7) | 13.6 | 52 | 57 | 64 | 72 | 80 | 89 | 95 |
| Non-Hispanic White | 3625 | 70.8 (69.9-71.7) | 11.9 | 53 | 57 | 64 | 71 | 78 | 85 | 90 |
| Other Hispanic | 1210 | 70.6 (69.3-72.1) | 11.9 | 52 | 57 | 63 | 71 | 77 | 85 | 92 |
| Other or multiracial | 489 | 72.0 (70.9-73.0) | 11.3 | 55 | 59 | 65 | 72 | 78 | 86 | 92 |

The CSV has the full set of statistics, including percentiles not shown here.

### Check against a published reference

The overall survey-weighted diastolic mean of 71.3 mmHg aligns with published CDC National Health Statistics Reports for the 2015-2018 cycle.

### How to cite

Cite the primary source for any regulatory or ethics submission:

> Centers for Disease Control and Prevention, National Center for Health Statistics. National Health and Nutrition Examination Survey Data, 2015-2018. Hyattsville, MD: U.S. Department of Health and Human Services.
> https://www.cdc.gov/nchs/nhanes/

Licence or terms of use: NCHS public-use data file. Users must use data for statistical reporting and analysis only.

State that the statistics were computed by this project, giving the version or commit you used.

### Reproduce

Reads `raw/nhanes/DEMO_I.xpt`, `raw/nhanes/BPX_I.xpt`, `raw/nhanes/DEMO_J.xpt`, `raw/nhanes/BPX_J.xpt`.

```sh
python pipelines/blood_pressure.py
```

## NHANES 2015-2018, clinic systolic blood pressure

*Guidance: draft, not yet expert-reviewed*

**Origin:** recomputed by this project from public data · **Data:** [data.csv](../metrics/blood_pressure/sources/nhanes_2015_2018_clinic_systolic/data.csv)

### Read this before using the numbers

- **Clinic auscultation, not wearable PTT.** Continuous optical pulse transit time (PTT) and cuffless optical sensors measure different arterial dynamics.
- **General population reference.** Participants taking ACE inhibitors, beta-blockers, or calcium channel blockers are included.
- **Age 80 and over is top-coded** at 80 years in accordance with NCHS participant disclosure rules.

### Population and method

- Civilian, non-institutionalised US residents aged 18 and over examined in the mobile examination centre, two survey cycles combined (2015-2016 and 2017-2018).
- Sample: 10,818 of 11,268 eligible. Sampling: probability sample. Exclusions: None for antihypertensive medication, cardiovascular conditions, pregnancy, or arrhythmias. Adults examined without valid blood pressure determinations are left out.
- **Method:** Auscultatory systolic blood pressure (first Korotkoff sound) measured using a mercury sphygmomanometer by a certified physician examiner.
- **Device:** Baumanometer mercury sphygmomanometer with calibrated adult/large cuff sizes.
- **Protocol:** Seated quietly for 5 minutes in a private exam room; standard CDC protocol averages readings 2 and 3 (the initial reading is discarded to mitigate acute situational anxiety).
- Estimates use the examination sampling weights (WTMEC2YR), halved for the two combined cycles.
- Percentiles are calculated from the survey-weighted empirical distribution.
- 95% confidence intervals are derived from 500 Rao-Wu bootstrap resamples of primary sampling units within strata.
- Subgroups with fewer than 50 examined individuals are suppressed.

### Tables

#### All, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 10818 | 123.2 (122.6-123.8) | 17.6 | 100 | 103 | 111 | 121 | 132 | 146 | 156 |
| 18-29 | 2135 | 114.2 (113.4-114.9) | 11.2 | 97 | 101 | 106 | 114 | 121 | 128 | 133 |
| 30-39 | 1656 | 117.1 (116.1-118.1) | 14.1 | 98 | 101 | 107 | 116 | 124 | 135 | 142 |
| 40-49 | 1626 | 121.1 (120.2-122.1) | 14.9 | 101 | 104 | 111 | 119 | 130 | 138 | 146 |
| 50-59 | 1704 | 126.4 (125.2-127.7) | 17.5 | 101 | 105 | 115 | 125 | 137 | 148 | 156 |
| 60-69 | 1922 | 129.7 (128.1-131.2) | 18.5 | 104 | 108 | 117 | 127 | 140 | 154 | 162 |
| 70-79 | 1089 | 133.3 (131.8-134.8) | 18.9 | 106 | 111 | 120 | 131 | 145 | 159 | 167 |
| 80+ | 686 | 141.9 (140.2-143.5) | 22.3 | 109 | 116 | 126 | 140 | 155 | 170 | 184 |

#### Female, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5578 | 121.9 (121.1-122.7) | 18.9 | 98 | 102 | 108 | 118 | 132 | 147 | 158 |
| 18-29 | 1103 | 110.4 (109.5-111.3) | 9.8 | 96 | 98 | 103 | 110 | 116 | 123 | 127 |
| 30-39 | 872 | 112.5 (111.5-113.5) | 12.7 | 96 | 98 | 104 | 110 | 119 | 128 | 135 |
| 40-49 | 879 | 118.7 (117.5-120.2) | 15.0 | 99 | 102 | 109 | 117 | 127 | 136 | 146 |
| 50-59 | 888 | 126.1 (124.5-127.7) | 18.1 | 100 | 103 | 114 | 125 | 136 | 149 | 159 |
| 60-69 | 960 | 129.5 (127.5-131.4) | 19.1 | 104 | 107 | 118 | 127 | 140 | 154 | 162 |
| 70-79 | 523 | 135.5 (133.7-137.2) | 19.7 | 108 | 113 | 121 | 134 | 148 | 162 | 172 |
| 80+ | 353 | 145.5 (143.0-148.0) | 22.4 | 115 | 120 | 130 | 144 | 159 | 174 | 189 |

#### Male, by age

| Age | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| All | 5240 | 124.6 (123.8-125.2) | 16.0 | 102 | 107 | 114 | 123 | 133 | 145 | 154 |
| 18-29 | 1032 | 117.9 (117.0-118.8) | 11.2 | 101 | 104 | 110 | 118 | 124 | 132 | 136 |
| 30-39 | 784 | 121.8 (120.3-123.2) | 13.8 | 102 | 105 | 113 | 121 | 129 | 139 | 149 |
| 40-49 | 747 | 123.6 (122.2-124.8) | 14.3 | 102 | 107 | 114 | 122 | 133 | 140 | 146 |
| 50-59 | 816 | 126.7 (125.5-128.1) | 16.9 | 103 | 107 | 116 | 125 | 137 | 147 | 154 |
| 60-69 | 962 | 129.9 (128.2-131.7) | 17.9 | 105 | 111 | 117 | 127 | 141 | 155 | 162 |
| 70-79 | 566 | 130.7 (128.7-132.9) | 17.4 | 106 | 108 | 118 | 129 | 141 | 154 | 161 |
| 80+ | 333 | 136.5 (134.0-139.0) | 20.9 | 107 | 111 | 122 | 133 | 148 | 164 | 176 |

#### By race and ethnicity

| Race and ethnicity | n | Mean (95% CI) | SD | P5 | P10 | P25 | P50 | P75 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|
| Mexican American | 1701 | 121.1 (120.0-122.2) | 16.4 | 99 | 103 | 110 | 119 | 129 | 141 | 150 |
| Non-Hispanic Asian | 1385 | 121.2 (120.2-122.5) | 17.9 | 97 | 101 | 109 | 118 | 131 | 146 | 156 |
| Non-Hispanic Black | 2408 | 127.4 (126.5-128.3) | 20.0 | 102 | 106 | 113 | 124 | 137 | 154 | 166 |
| Non-Hispanic White | 3625 | 123.2 (122.4-123.9) | 17.1 | 100 | 104 | 111 | 121 | 132 | 146 | 154 |
| Other Hispanic | 1210 | 121.7 (120.5-122.7) | 18.0 | 97 | 102 | 109 | 120 | 131 | 146 | 156 |
| Other or multiracial | 489 | 121.9 (119.1-124.5) | 17.7 | 101 | 104 | 110 | 119 | 128 | 145 | 159 |

The CSV has the full set of statistics, including percentiles not shown here.

### Check against a published reference

The overall survey-weighted systolic mean of 122.8 mmHg aligns with published CDC National Health Statistics Reports for the 2015-2018 cycle.

### How to cite

Cite the primary source for any regulatory or ethics submission:

> Centers for Disease Control and Prevention, National Center for Health Statistics. National Health and Nutrition Examination Survey Data, 2015-2018. Hyattsville, MD: U.S. Department of Health and Human Services.
> https://www.cdc.gov/nchs/nhanes/

Licence or terms of use: NCHS public-use data file. Users must use data for statistical reporting and analysis only.

State that the statistics were computed by this project, giving the version or commit you used.

### Reproduce

Reads `raw/nhanes/DEMO_I.xpt`, `raw/nhanes/BPX_I.xpt`, `raw/nhanes/DEMO_J.xpt`, `raw/nhanes/BPX_J.xpt`.

```sh
python pipelines/blood_pressure.py
```
