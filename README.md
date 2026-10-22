# ELEC 594 — Midterm Report

**An Automated Pipeline for Offline Deployment of Custom Computer-Vision Models on iOS**
Author: Anh Pham (Rice University, ELEC 594)

This repository contains the LaTeX source, figures, and compiled PDF for the midterm report.

## Build

Requires a LaTeX distribution (TeX Live / MacTeX) with `pdflatex` and `bibtex`.
`IEEEtran.cls` and `IEEEtran.bst` are included so the report compiles without an
IEEE package install.

```bash
pdflatex main.tex
bibtex   main
pdflatex main.tex
pdflatex main.tex
```

or, with latexmk:

```bash
latexmk -pdf main.tex
```

The build produces `main.pdf` (identical to the committed `report.pdf`).

## Files

| File | Purpose |
|------|---------|
| `main.tex` | Report source (IEEE conference style) |
| `refs.bib` | Bibliography (IEEE format) |
| `IEEEtran.cls`, `IEEEtran.bst` | IEEE class and bibliography style |
| `figures/quantization.png` | Fig. 3 — FP16 vs INT8 results |
| `figures/detection.png` | Fig. 2 — on-device detection screenshot |
| `scripts/make_quant_figure.py` | Regenerates `figures/quantization.png` |
| `report.pdf` | Compiled report |

## Regenerate the results figure

```bash
python3 scripts/make_quant_figure.py
```
