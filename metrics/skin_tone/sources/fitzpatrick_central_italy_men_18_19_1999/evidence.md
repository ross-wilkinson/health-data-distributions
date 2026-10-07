# Evidence: Fitzpatrick phototype, men aged 18-19, Central Italy (Ballone et al. 1999)

All quotes are verbatim. Retrieved 2026-10-06.

## 1. The numbers in data.csv

Source: Ballone E, Passamonti M, Lappa G, Di Blasio G, Fazii P. *Pigmentary traits, nevi and skin phototypes in a youth population of Central Italy.* Eur J Epidemiol 1999;15(2):189-195. doi:10.1023/A:1007539807705. PMID 10204650. First page: "© 1999 Kluwer Academic Publishers."

Where the text was read: the full article, on 2026-10-06, from a PDF supplied by Ross Wilkinson (`raw/papers/Ballone et al. 1999 - Eur. J. Epidemiol_.pdf`, kept untracked in the repo). Before that, only the abstract had been read (PubMed and Europe PMC records), and the entry held two numbers from it. Those are now replaced by Table 1.

### Locator: Table 1

Table 1 is titled "Distribution of 5837 young men by sun-reactive skin types according to Fitzpatrick's classification". Its columns are Phototype, N, %, and Valid %. As printed:

> I Always burn, never tan | 144 | 2.5 | 2.7
>
> II Usually burn, tan less than average (with difficulty) | 457 | 7.8 | 8.6
>
> III Sometimes burn mildly, tan about average | 2119 | 36.3 | 39.8
>
> IV Rarely burn, tan more than average (with ease) | 2598 | 44.5 | 48.9
>
> Not recorded/Not valid | 519 | 8.9 | Missing
>
> Total | 5837 | 100 | 100

Table footnote:

> 519 (8.9%) answers have been excluded from the analysis because many subjects did not know their sensitivity to the sun or because they had written more than one response.

Used for: the four shares, from the Valid % column (stored as 0.027, 0.086, 0.398, 0.489). `n` is 5,318 on every row: the 5,837 men less the 519 excluded, and the total printed in the paper's Tables 3 and 4.

### Population, sampling, and method (Materials and methods)

> During the period from January to December 1990, 11,862 men born in 1972 (a small percentage were born in 1971) were called for a preliminary medical visit at the Distretto Militare of Chieti (Central Italy). This group represents approximately 88% of the 18 year old residents in the region of Abruzzo and the province of Ascoli Piceno of the region of Marche (Figure 1). The remaining 12% were visited by the navy in another city (the distinction between these two groups is purely random). Due to organisational reasons, the dermatological examination was done in the early morning. Therefore, the number of young men randomly scheduled to be visited in the early morning was 5837.

> Due to the scarce immigration of this geographical area, this group was not intended to represent all of Italy but only the regions indicated.

> informed verbal consent in the presence of a military medical officer without any autorithy, direct or indirect, on the recruit was obtained (no one declined to participate).

> Each subject, prior to the physical examination, was given a questionnaire which included personal information and data necessary for a Fitzpatrick's sun-reactive skin type classification.

> All subjects were asked to report their skin response to an initial sun exposure (45–60 minutes of exposure to midday summer sun (corresponding to 3–4 MED), minimal erythema dose: 90–120 mJ/cm2) taking into account the reaction after 24 hours (propensity to burn) and after 7 days (ability to tan) using a self-questionnaire

> Since all subjects were Caucasians, phototype V and VI were not recorded.

From the Discussion:

> In this study, in order to increase the reliability of the responses, at least one examiner was present to explain (only when asked) the questionnaire while it was being answered.

> In any case, the response to the questionnaire have a subjective component. Therefore, the reliability is always questionable due to an inherent margin of error.

### The abstract's figures, and why they are not the ones used

> Almost half of the entire population (44.5%) had affirmed that they tanned easily and rarely burned (phototype IV), 10.3% had skin phototype I or II

Table 1 shows these are the "%" column: shares of all 5,837 men, including the 519 with no usable answer (2.5 + 7.8 = 10.3). The Valid % column, which excludes them, gives 48.9% for phototype IV and 2.7 + 8.6 = 11.3% for I or II.

### What the earlier abstract-only entry could not say, now resolved

Phototype III; the split between I and II; the years of data collection; how participants were selected; who assigned the phototype (self-report by questionnaire); why the scale stops at IV.

## 2. Support for the metric definition (metric.json)

Source: NCHS, NHANES 2003-2004 Dermatology data documentation, file DEX_C, https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2003/DataFiles/DEX_C.htm (read 2026-10-06; the page was downloaded and read as text).

> The Fitzpatrick skin type is a method of classifying individuals based on their response to sun exposure in terms of tanning and burning (photosensitivity) (Fitzpatrick, 1988).

> I - Always burns, never tans (pale white skin)

> VI - Never burns, (deeply pigmented dark brown to black skin)

## 3. A statement about lack of data, quoted and not adopted

Same NCHS page:

> Currently, the distribution of skin type across the U.S. population is unknown.

This is a statement in 2007-era data documentation (page header: "First Published: May 2007"). It describes what NCHS said then. It is not adopted here: the same page documents reader-assigned Fitzpatrick types collected in a national survey (see section 5), so a weighted distribution could probably be computed from public data (not checked here).

## 4. Search log

All searches 2026-10-06, run with the web-search tool unless stated. A result summary is a lead only; the "opened" column says whether the source itself was read.

| # | Date | Query or site | What it returned | Opened? | Outcome |
|---|---|---|---|---|---|
| 1 | 2026-10-06 | "distribution of Fitzpatrick skin type in a population-based sample adults proportion type I II III IV V VI" | A hospital and clinic series in Ireland (750 patients), a university sample (321), a Hangzhou sample (848), a five-country European volunteer study (569), a diverse sample (1,548) | Irish study: abstract only via a search snippet, not opened. European study: abstract opened (Copenhagen, Dublin, London, Muenster, Ioannina volunteers; "did not employ random population sampling") | Rejected: clinic or volunteer samples |
| 2 | 2026-10-06 | "Irish population Fitzpatrick skin phototype 750 adults ... random sample" | The Irish study (preprint, Research Square) recruited patients from dermatology and general medical clinics | Not opened | Rejected: clinic patients |
| 3 | 2026-10-06 | "Fitzpatrick skin phototype random sample of adults population-based survey Hispanic Community Health Study OR Sun Survey OR national survey ..." | He et al. 2014 (3,386 survey respondents, ethnically diverse), a Southern California postal-station study, a Chicago health-fair study of Latino adults (350) | He et al.: title and abstract opened; full text blocked by a bot check. Others not opened | Rejected: convenience samples |
| 4 | 2026-10-06 | "Fitzpatrick skin type prevalence population-based cohort Rotterdam Study OR Lifelines OR Generation R ..." | UK Biobank skin-colour publication page; no Fitzpatrick I-VI distribution from the named cohorts | Not opened | Nothing usable found |
| 5 | 2026-10-06 | "random sample general population Fitzpatrick skin type prevalence Queensland OR Australia OR Denmark OR Germany OR Brazil ..." | A Danish series of 892 Caucasians, a multi-country trial population, general statements | Not opened | Nothing usable found |
| 6 | 2026-10-06 | "Fitzpatrick skin type nationally representative OR random sample adults distribution percent ... self-reported cross-sectional" (extended) | Keiser et al. 2012, "Reliability and prevalence of digital image skin types in the United States: Results from NHANES 2003-2004" (J Am Acad Dermatol 66(1):163-165, doi:10.1016/j.jaad.2011.02.044) | Title, authors, journal only. PubMed has no abstract; JAAD page returned HTTP 403; ResearchGate 403; EM-consulte shows no text. **Full text not opened, so no number taken** | A probable usable published source that could not be read |
| 7 | 2026-10-06 | Site: wwwn.cdc.gov NHANES 2003-2004 file DEX_C (Dermatology) | Documentation of reader-assigned Fitzpatrick type from digital images, ages 20-59 | Opened and read as text (curl) | See section 5 |
| 8 | 2026-10-06 | "NHANES sun-reactive skin type OR 'skin reaction to sun' questionnaire US adults prevalence ..." | NHANES questionnaire item DED031 in files DEQ_C and later cycles | DEQ_C documentation opened | See section 5 |
| 9 | 2026-10-06 | "skin phototype distribution general population random sample electoral register OR 'random digit dialing' OR 'household survey' ..." | Ballone et al. 1999 (Central Italy) | Abstract opened by two routes (section 1) | **Chosen** |
| 10 | 2026-10-06 | "UK Biobank skin colour self-reported very fair fair light olive ..." | UK Biobank skin colour categories (very fair to black), a self-reported item with its own category names | Not opened | Not Fitzpatrick types; UK Biobank is a volunteer cohort. Rejected |
| 11 | 2026-10-06 | Site: PubMed and Europe PMC (via NCBI E-utilities and Europe PMC REST) | Metadata and abstract for Ballone et al. and Keiser et al. | Opened | As above |

## 5. What else was found (not entered)

- **NHANES 2003-2004, file DEX_C.** The documentation says: "Sample persons aged 20-59 years who do not meet any of the exclusion criteria." and lists variables `DEX1FITZ` ("Reader 1 Fitzpatrick skin type"), `DEX2FITZ` ("Reader 2 Fitzpatrick skin type") and `DEX6FITZ` ("Reader 6 Fitzpatrick Skin Type"). Images that the two readers did not agree on went to a consensus reading. NHANES is a national examination survey and the page refers readers to its analytic guidelines on sample weights; this file has a Fitzpatrick type read from digital images. It is public data. How the sample was drawn was not checked here. A recomputed source needs a script in `pipelines/`, which directive 03 does not allow, so it was not computed. Keiser et al. 2012 appears to report prevalence from it but could not be opened.
- **NHANES 2003-2004, file DEQ_C, item DED031**, ages 20-59: "If after several months of not being in the sun, {you/SP} then went out in the sun without sunscreen or protective clothing for a half hour, which one of these would happen to {your/his/her} skin?" Response options include "Get a severe sunburn with blisters" and "A severe sunburn for a few days with peeling" and "Mildly burned with some tanning". This is a sun-reaction questionnaire item, not an assigned Fitzpatrick type.
- **One more description of how Fitzpatrick is applied in practice** (from a convenience cohort at UCSF, medRxiv preprint doi:10.1101/2025.02.21.25322707, CC BY-NC-ND 4.0): "While there is no standard visual Fitzpatrick Scale, we implemented a 6-category ‘perception’ of the scale that is found online."
