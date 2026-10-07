# Evidence: ITA categories measured from Wilkes et al. 2015, Figure panel B

Wilkes M, Wright CY, du Plessis JL, Reeder A. *JAMA Dermatol* 2015;151(8):902-903. doi:10.1001/jamadermatol.2015.0351. Read in full on 2026-10-06 from a PDF supplied by Ross Wilkinson, kept untracked in `raw/papers/`. Verbatim quotes from the text are in the `ita_colorimetry_gap` source's evidence.md.

## What was measured

### Locator: Figure panel B

The figure's caption for panel B reads:

> Frequency of participants by spectrophotometer-derived Del Bino skin type category (ITA) and Fitzpatrick skin type (FST) derived from a pigment-measuring device.

The chart has six pairs of bars labelled Very Light I, Light II, Intermediate III, Tanned IV, Brown V, Dark VI, a vertical axis in participants with gridlines every 25 from 0 to 375, and a legend naming the darker bars ITA and the lighter bars FST.

## Measurement (output of `pipelines/digitise/wilkes_2015_figure_b.py`)

```
zero axis at row 1156; 11 gridlines, 68.00 px apart = 25 participants
2.720 px per participant (one pixel = 0.37 participants)
ITA: measured [58.09, 45.59, 13.24, 52.57, 348.16, 38.24]; sum 555.9; rounded [58, 46, 13, 53, 348, 38] sum 556
Device-derived Fitzpatrick: measured [36.76, 61.4, 16.91, 52.57, 354.41, 29.04]; sum 551.1; rounded [37, 61, 17, 53, 354, 29] sum 551
ITA counts sum to 556 against 556 participants stated in the paper
```

| Category | Measured | Count used | Share |
|---|---|---|---|
| Very light | 58.09 | 58 | 10.4% |
| Light | 45.59 | 46 | 8.3% |
| Intermediate | 13.24 | 13 | 2.3% |
| Tanned | 52.57 | 53 | 9.5% |
| Brown | 348.16 | 348 | 62.6% |
| Dark | 38.24 | 38 | 6.8% |

## Checks

- The ITA counts sum to 556, the N stated in the paper's Methods.
- The lighter (device-derived Fitzpatrick) series sums to 551, five short of 556. The paper does not say whether every participant had a melanin reading. That series is not entered.
- Method accuracy: see `pipelines/digitise/ohagan_2025_figure1_check.py`, where the same approach reproduced 15 known bar heights to within 0.06 percentage points.

## How the image was made

`pdftoppm -r 600 -f 1 -l 1 -png` on the article PDF, then a crop of the right-hand column containing panel B, saved as `raw/figures/wilkes_2015_figure_panel_b.png` (not in the repo).
