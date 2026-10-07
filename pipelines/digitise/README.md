# Measuring values from published figures

Each script here measures one published chart and writes the `data.csv` of one
source whose `origin` is `"digitised"`. The chart images are not in the
repository; they go in `raw/figures/`, which is git-ignored.

| Script | Figure | Image expected in `raw/figures/` | How to get it |
|---|---|---|---|
| `quer_2020_fig2.py` | Quer et al. 2020, Fig 2 (CC BY) | `quer_2020_fig2.png` | `curl -L -o raw/figures/quer_2020_fig2.png "https://journals.plos.org/plosone/article/figure/image?size=large&id=10.1371/journal.pone.0227709.g002"` |
| `wilkes_2015_figure_b.py` | Wilkes et al. 2015, Figure panel B | `wilkes_2015_figure_panel_b.png` | From your own copy of the article: `pdftoppm -r 600 -f 1 -l 1 -png article.pdf page`, then crop the right-hand column from 52% to 90% of the width and 50% to 72% of the height |
| `ohagan_2025_figure1_check.py` | O'Hagan et al. 2025, Figure 1 panels A and B | `ohagan_2025_figure1_ab.png` | From your own copy of the article: `pdfimages -png -f 1 -l 1 article.pdf img`; the first image |

## How accurate is this?

`ohagan_2025_figure1_check.py` writes no data. It exists because that figure
plots values that can also be computed exactly from the public SCIN dataset.
Measured against those, all 15 bars came out within 0.06 percentage points,
with a small consistent underestimate (about 0.05 points) from the pixel row
lost at the base of each bar.

Every digitising script prints its calibration (pixels per unit) and at least
one internal check (bars summing to a known total, or agreement with a number
stated in the paper's text). Those go into the source's `evidence.md` and
`verification`.

Needs Pillow: `.venv/Scripts/python -m pip install pillow`.
