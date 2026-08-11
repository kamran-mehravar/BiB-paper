# Analysis Verification Report

Revision branch: `major-revision-r2-r3`

## Repository Data Inspected

Files inspected:

- `sent-foods-4487055.docx` and `sent-foods-4487055.pdf`: reviewed submitted manuscript.
- `foods-4411772_revised_v3.docx`: older revision material.
- `comment-R2.txt` and `comment-R3.txt`: current reviewer reports.
- `Response_to_Reviewers.docx`: previous response letter, replaced in this revision with the current R2/R3 response.
- `Nota_per_Nicola_acido_lattico.docx`: internal lactic-acid note.
- `anova_pressure.py`: pressure-analysis script.
- Embedded figures and tables in the manuscript DOCX files.

No raw CSV, XLSX, raw chemical replicate file, plotting script, chamber log, barometric record, or supplementary dataset is present in the repository. The pressure script expects `Results - Compare.csv`, but that file is absent.

## Commands Run

```powershell
git status --short --branch
rg --files
Get-Content -Raw comment-R2.txt
Get-Content -Raw comment-R3.txt
Get-Content -Raw anova_pressure.py
python -m compileall anova_pressure.py
python anova_pressure.py
python anova_pressure.py --from-raw
python -c "import pandas, numpy; print(pandas.__version__, numpy.__version__)"
pdftotext -layout sent-foods-4487055.pdf -
```

DOCX text and table extraction was performed with `python-docx`.

## Software Environment

Verified locally:

- Python 3.12.10
- pandas 3.0.3
- numpy 2.4.6
- python-docx available
- statsmodels not installed
- scipy not installed

`anova_pressure.py` was updated so that it uses `statsmodels` when available and otherwise falls back to explicit least-squares Type II calculations using only NumPy/Pandas.

## Pressure Summary Values

The repository contains embedded per-sensor summary values in `anova_pressure.py`. They have also been exported unchanged to `pressure_summary_embedded.csv`.

| Sensor | Position | Nominal chamber | Peak Delta P (mbar) | Day-20 Delta P (mbar) |
|---|---|---:|---:|---:|
| V50 | Top | 50 | 63.4638 | 33.5127 |
| V53 | Top | 50 | 58.3335 | 32.5126 |
| V71 | Top | 50 | 77.9051 | 60.2513 |
| V52 | Bottom | 50 | 92.1697 | 55.9552 |
| V56 | Bottom | 50 | 63.1891 | 17.0045 |
| V70 | Bottom | 50 | 93.7639 | 43.7397 |
| V55 | Top | 19 | 56.4339 | 36.1306 |
| V57 | Top | 19 | 56.9113 | 38.1726 |
| V58 | Top | 19 | 65.4962 | 50.7070 |
| V51 | Bottom | 19 | 91.0728 | 62.5850 |
| V59 | Bottom | 19 | 78.5783 | 52.3243 |

## Reproduced Statistics from Embedded Data

Peak Delta P cell summaries:

| Nominal chamber | Position | n | Mean | SD |
|---|---|---:|---:|---:|
| 19 | Bottom | 2 | 84.8255 | 8.8349 |
| 19 | Top | 3 | 59.6138 | 5.0999 |
| 50 | Bottom | 3 | 83.0409 | 17.2106 |
| 50 | Top | 3 | 66.5675 | 10.1482 |

Peak Delta P Type II ANOVA:

- Position: SS = 1118.9144, F(1,8) = 9.1399, p = 0.0165.
- Nominal chamber condition: SS = 25.4467, F(1,8) = 0.2079, p = 0.6606.
- Interaction: p = 0.5552.
- Corrected total SS = 2169.3731.
- Adjusted bottom-minus-top effect = 20.3571 mbar, approximate 95% CI = 4.8295 to 35.8848 mbar.
- Adjusted nominal 50-minus-19 degC chamber effect = 3.0700 mbar, approximate 95% CI = -12.4577 to 18.5976 mbar.

Day-20 Delta P cell summaries:

| Nominal chamber | Position | n | Mean | SD |
|---|---|---:|---:|---:|
| 19 | Bottom | 2 | 57.4546 | 7.2554 |
| 19 | Top | 3 | 41.6701 | 7.8925 |
| 50 | Bottom | 3 | 38.8998 | 19.9213 |
| 50 | Top | 3 | 42.0922 | 15.7342 |

Day-20 Delta P Type II ANOVA:

- Position: SS = 74.1869, F(1,8) = 0.3479, p = 0.5716.
- Nominal chamber condition: SS = 173.3223, F(1,8) = 0.8127, p = 0.3937.
- Interaction: p = 0.3198.
- Corrected total SS = 1933.2553.
- Adjusted bottom-minus-top effect = 5.2418 mbar, approximate 95% CI = -15.2529 to 25.7366 mbar.
- Adjusted nominal 50-minus-19 degC chamber effect = -8.0121 mbar, approximate 95% CI = -28.5068 to 12.4827 mbar.

The headline pressure statistics in the submitted manuscript are reproduced from the embedded values.

## Discrepancies and Cautions

- Raw extraction cannot be verified because `Results - Compare.csv` is absent.
- `python anova_pressure.py --from-raw` fails with the expected missing-file error.
- Sensor-column mapping, baseline extraction, first-five-hour exclusion, peak extraction and day-20 averaging are described in the script but cannot be audited from raw records.
- The original wording that Type II sums of squares "account for" a share of total variability was not statistically clean in an unbalanced design. The revised manuscript reports Type II tests and effect estimates instead.
- The embedded data lack stack IDs and stack height. A paired or stack-level sensitivity analysis cannot be reported unless the sensor-to-stack mapping is restored. The revised manuscript therefore labels the pressure ANOVA as exploratory and sensor-level.
- The chemical table and internal lactic-acid note contain a repository inconsistency (`0.29 +/- 0.02` versus `0.29 +/- 0.20` g/L for lactic acid in the nominal 50 degC chamber). Raw chemical replicate data are absent. The revised manuscript uses the conservative `0.29 +/- 0.20` g/L value, assigns the same significance letter to both lactic-acid means and treats lactic acid descriptively.
- `Nota_per_Nicola_acido_lattico.docx` is a stale internal note and is not part of the revised submission package. It still contains stronger lactic-acid and chamber-behaviour interpretations that were rejected during the final integrity audit.

## First-Five-Hour Exclusion

The script excludes the first approximately five hours (`HANDLING_END_D = 0.21`) from peak extraction. The manuscript figure shows this interval includes transport, filling-line and stack-assembly disturbances. Reviewer 2 correctly noted that such disturbances may be relevant to real logistics.

A full-record sensitivity analysis cannot be recomputed from this repository because the raw time series is absent. The revised manuscript therefore:

- retains the post-handling window as the primary analysis;
- explains why the interval was excluded;
- acknowledges that early transients may affect generalisability;
- states that the sensitivity analysis requires restoration of the raw logger export.

## Reproducibility Improvements Made

- `anova_pressure.py` now runs without `statsmodels`.
- `anova_pressure.py` now prints model-adjusted position and nominal-chamber contrasts with approximate 95% CIs.
- `pressure_summary_embedded.csv` records the embedded per-sensor pressure summaries.
- `requirements.txt` lists the packages needed for analysis/document generation.
- The revised manuscript clarifies baseline-referred Delta P, nominal chamber condition, missing sensor, unbalanced cells, low power and raw-data availability limitations.
- The pressure analysis is described as exploratory sensor-level inference because the embedded pressure summaries do not retain stack IDs for a paired or blocked stack-level sensitivity analysis.
- The chemical interpretation avoids temporal "loss/increase" language unless a baseline is documented; lower/higher values are reported as after-20-day between-condition differences.

## Reproducibility Commands

```powershell
python anova_pressure.py
python anova_pressure.py --from-raw
```

The first command runs from embedded values. The second requires adding `Results - Compare.csv` to the repository root.
