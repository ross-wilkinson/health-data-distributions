# Evidence: resting heart rate distributions measured from Quer et al. 2020, Fig 2

Quer G, Gouda P, Galarnyk M, Topol EJ, Steinhubl SR. *PLOS ONE* 2020;15(2):e0227709. doi:10.1371/journal.pone.0227709. Creative Commons Attribution License. Verbatim quotes from the paper's text are in the `quer_2020_fitbit_92457_adults` source's evidence.md.

## What was measured

### Locator: Fig 2

The figure plots "Fraction of Individuals" (0 to 0.06) against "Average Daily Resting Heart Rate" (40 to 90), with one curve for men and one for women and a vertical dashed line for each. The image is the publisher's full-size version, 2180 x 1512 pixels:

`https://journals.plos.org/plosone/article/figure/image?size=large&id=10.1371/journal.pone.0227709.g002`

saved as `raw/figures/quer_2020_fig2.png` (not in the repo).

The numbers of men and women are from the paper (quoted in the companion source's evidence.md): 57,836 women and 34,621 men.

## Measurement (output of `pipelines/digitise/quer_2020_fig2.py`)

```
frame x 249.5 to 2142.5, y 26.0 to 1341.5; 37.86 px per beat/min; one pixel = 0.000046 of individuals
Male: fractions at 41 to 89 sum to 1.0000; mean 63.37 (dashed line in the figure at 63.43); sd 7.55; p2.5 49.8, p97.5 79.6
Female: fractions at 41 to 89 sum to 0.9999; mean 66.61 (dashed line in the figure at 66.69); sd 7.39; p2.5 53.0, p97.5 81.9
both sexes combined by the caption's counts: mean 65.40, sd 7.62 (the paper's text gives 65.5 and 7.7)
```

## Checks against the paper's own statements

| Check | Paper | Measured |
|---|---|---|
| Men, central 95% | "between 50 and 80 bpm" | 49.8 to 79.6 |
| Women, central 95% | "between 53 and 82 bpm" | 53.0 to 81.9 |
| All, mean | "65.5" | 65.40 |
| All, spread | "± 7.7" | 7.62 |
| Men, mean line in the figure | 63.43 (measured position of the dashed line) | 63.37 |
| Women, mean line in the figure | 66.69 (measured position of the dashed line) | 66.61 |

## The half-beat question

The curves have a vertex at each whole beat per minute. If each vertex were the share of people whose average rounded to that value, the mean of the plotted values would equal the mean line. It does not: it falls 0.5 below (62.87 and 66.11). Treating each vertex as covering the beat upward from its value puts the computed means within 0.1 of the lines. That reading is used, and is an inference, not something the paper states.
