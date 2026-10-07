# Evidence: Quer et al. 2020, Fitbit cohort of 92,457 adults

Paper: Quer G, Gouda P, Galarnyk M, Topol EJ, Steinhubl SR. Inter- and intraindividual variability in daily resting heart rate and its associations with age, sex, sleep, BMI, and time of year: Retrospective, longitudinal cohort study of 92,457 adults. *PLOS ONE* 2020;15(2):e0227709.

URL: https://doi.org/10.1371/journal.pone.0227709 (article page: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0227709; also https://pmc.ncbi.nlm.nih.gov/articles/PMC7001906)

Accessed: 2026-10-06. Every quote below was checked against two independent renderings of the full text (the PLOS JATS XML and the Europe PMC JATS XML); the wording is identical in both. The paper has no numbered tables and no supplementary files; the numbers are in the running text. Section names are the paper's own headings.

Licence, as stated on the article: "© 2020 Quer et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited."

## Locators used in data.csv

### Results, Resting heart rate (mean); Methods, Population (n)

Results, Resting heart rate (first sentence), source of the mean 65.5:

> The mean RHR for all individuals over all available monitored days was 65.5 ± 7.7 bpm, with a minimum and maximum average RHR for each individual ranging between 39.7 and 108.6 bpm, respectively.

Methods, Population, source of n = 92,457:

> The final analysis population included 92,457 individuals with at least two RHR measurement days per week for a minimum of 35 weeks.

The paper does not say what "±" denotes in this sentence, so the 7.7 is not entered as a standard deviation (see the note under "Statements not entered" below). The Abstract rounds the same mean to 65:

> Mean daily RHR was 65 beats per minute (bpm), with a range of 40 to 109 bpm among all individuals.

## Statements used in source.json (not rows in data.csv)

### How resting heart rate is defined (Methods, Variables and statistical analysis)

> RHR was measured using interbeat intervals derived from the PPG sensor.

> RHR was calculated by a proprietary formula from Fitbit, which provides for each individual a single value each day. This value is expected to be representative of the true value of RHR that would be obtained in a supine position immediately after waking but before getting out of bed.

(Strengths and limitations)

> RHR was determined based on a proprietary algorithm developed by the manufacturer, which varies based on whether the device is being worn during sleep.

> However, this limitation seems to pertain primarily during activity and times of rapid heartbeat [20, 24, 32] and therefore would be unlikely to impact our findings, as the RHR was primarily calculated during periods of sleep.

### Devices (Methods, Study design)

> This was a retrospective, observational cohort study that used data collected from individuals wearing one of the following Fitbit devices: Charge HR versions 1–3 (65% of individuals), Blaze (21%), Alta HR (8%), Ionic (3%), Surge (2%), or Versa (1%). These devices continuously monitor heart rate every second as well as track and report the daily total duration of sleep.

### Cohort, selection and period (Methods, Population)

> The initial dataset included a convenience sample of 200,000 persons consistently using the device, from the United States—from all 50 states and the District of Columbia—and a total of 65,153,836 daily RHR measurements that had been collected between March 2016 and February 2018. We then excluded users who did not report their sex, whose self-reported age was under 18 years or over 100 years, and whose BMI was outside the range of 15–50 kg/m2 (calculated from self-reported height and weight), assuming the latter were more likely to be erroneous. Furthermore, we considered only measurements of the RHR for days in which the device was worn for at least 20 hours, with the wrist-worn time determined by the device based on the data collected.

(Abstract)

> Our retrospective, longitudinal cohort study includes 92,457 de-identified individuals from the United States (all 50 states), who consistently—over at least 35 weeks in the period from March 2016 to February 2018, for at least 2 days per week, and at least 20 hours per day—wore a heart rate wrist-worn tracker.

### Who the cohort is (Results, Population characteristics; Fig 2 caption)

> The 92,457 included individuals wore a device for at least 20 hours/day for a median of 320 days (IQR, 242–438) over a maximum possible monitoring period of 730 days, providing a total of 32,741,021 daily RHR values. Average age was 45.8 ± 14.4 years; 63% were women; average BMI was 28.4 ± 5.8 kg/m2; and average sleep duration was 6.8 ± 0.8 hours/day.

Fig 2 caption (text):

> The average daily RHR for 57,836 individual women (green line) and 34,621 men (blue line). The overall mean for each group is indicated by the dashed lines.

### Representativeness (Strengths and limitations)

> Beside the large number of participants, it has a unique length (2 years) and depth (measurements obtained daily in normal living conditions) that allowed the analysis of day-to-day variations not previously observed.

> The population included in this study was composed of persons who owned a wearable device measuring RHR. This cohort is not likely to be representative of the total socioeconomic and demographic diversity of the U.S., despite its unprecedented size.

> Our study used HR data from a commercial-grade wearable device, which may not consistently capture heart rate as accurately as an electrocardiogram, even if in other studies it has been shown that this difference is quite small.

### Sex and age differences (Results, Resting heart rate)

> We observed that 95% of men had an RHR between 50 and 80 bpm, while the corresponding range for women was between 53 and 82 bpm (Fig 2). Women had a significantly higher RHR in all age brackets (Fig 3A). Across age groups, average RHR increased until approximately 50 years of age and then began a downward trend.

### Variation over time (Results, Variability in individual resting heart rate)

> Over the course of a year, a small but significant seasonal change was observed. The change in the population’s average RHR was 2 bpm over the year. The RHR peaked in the first week of January for both men and women, after which the average RHR decreased to the yearly minimum at the end of July (Fig 4).

### Data availability (Data Availability statement)

> The owner of the third party data analyzed in our manuscript has restrictions upon sharing it publicly.

## Statements not entered as rows in data.csv

- The "± 7.7" after the mean of 65.5: the paper uses "±" for the age, BMI and sleep figures as well and, in the text read, never says it means a standard deviation, so it is left as written and not recorded as `sd`.
- The 95% ranges for men (50 to 80 bpm) and women (53 to 82 bpm), quoted above: the paper does not say whether these are the central 95% of individuals, so they are not recorded as percentiles.
- Separate means for women and men, and means by age, BMI and sleep: shown only in Fig 2 and Fig 3 (the dashed lines and plotted points); no value is given in the text.
- The minimum and maximum average RHR for individuals (39.7 and 108.6 bpm): the entry format has no statistic for a minimum or maximum.
