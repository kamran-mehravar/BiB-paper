# Supplementary material

## Supplementary Figure S1

`Supplementary_Figure_S1_common_mode_diagnostic.svg`

**Caption:** Supplementary Figure S1. Common-mode diagnostic for the main-trial pressure endpoint. (A) Leave-one-out correlation between each usable sensor trace and the common-mode pressure trace. Top-position and bottom-position sensors are distinguished in the legend, and each sensor is labelled by sensor ID, position and C19/C50 set-point group. The high correlations show strong shared absolute-pressure structure across the 11 usable sensor traces (mean r = 0.937; range 0.859–0.973). (B) Comparison of the original uncorrected peak-pressure position term with the corresponding common-mode residual endpoint. The uncorrected peak result remains detectable (F(1,8) = 9.14; p = 0.017), whereas the position term is not statistically detectable after common-mode residualisation (F(1,8) = 3.21; p = 0.111). (C) Leave-one-out robustness of the uncorrected peak-position result, with p-values ranging from 0.0007 to 0.0511 and one omitted-sensor case crossing the p = 0.05 reference line. These diagnostics support the revised interpretation that the pressure result should be treated as exploratory.

**Purpose:** This file is intended to support the reviewer response on pressure-trace interpretation and figure improvement. It is supplementary material, not a replacement for Figures 3–7 in the main manuscript.

**Source files:**

- `pressure_common_mode_correlations.csv`
- `pressure_common_mode_peak_anova.csv`
- `pressure_leave_one_out.csv`
- `go_no_go_audit.py`

**Important note:** The figure does not use external barometric data. Absolute trial dates were not available in the study records, so no external barometric correction was performed or fabricated.

**Format note:** The SVG file is vector-based and can be exported to PDF or high-resolution PNG if the journal submission portal does not accept SVG files.
