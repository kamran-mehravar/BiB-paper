# Supplementary material

## Supplementary Figure S1

`Supplementary_Figure_S1_common_mode_diagnostic.svg`

**Caption:** Supplementary Figure S1. Common-mode diagnostic for the main-trial pressure analysis. (A) Leave-one-out correlation between each sensor trace and the common-mode pressure trace, showing strong shared structure across the 11 usable sensor traces (mean r = 0.937; range 0.859–0.973). (B) Comparison of the original uncorrected peak-pressure position term with the corresponding common-mode residual peak endpoint. The uncorrected peak result remains detectable (F(1,8) = 9.14; p = 0.017), whereas the position term is not statistically detectable after common-mode residualisation (F(1,8) = 3.21; p = 0.111). (C) Leave-one-out robustness of the uncorrected peak-position result, with p-values ranging from 0.0007 to 0.0511. These diagnostics support the revised interpretation that the pressure result should be treated as exploratory.

**Purpose:** This file is intended to support the reviewer response on pressure-trace interpretation and figure improvement. It is supplementary material, not a replacement for Figures 3–7 in the main manuscript.

**Source files:**

- `pressure_common_mode_correlations.csv`
- `pressure_common_mode_peak_anova.csv`
- `pressure_leave_one_out.csv`
- `go_no_go_audit.py`

**Important note:** The figure does not use external barometric data. Absolute trial dates were not available in the study records, so no external barometric correction was performed or fabricated.
