# Revision Changelog

Major revision for Reviewer 2 and Reviewer 3.

## Scientific Interpretation

- Reframed the manuscript around nominal chamber set points and measured in-bag temperature, rather than implying that the main trial exposed wine to 50 degC.
- Changed the title to emphasise in-bag thermal exposure.
- Rewrote the Abstract to report actual package temperatures, pressure effect estimates and the limited role of the verification trial.
- Removed the binary claim that palletisation "governs" physical behaviour while temperature "governs" chemical stability.
- Replaced broad causal language with condition-specific wording:
  - bottom stack position was associated with higher peak Delta P;
  - chemistry differed between bulk samples from nominal chamber conditions;
  - verification observations were limited and supporting.
- Added explicit storage-stability caution: lower SO2 values may indicate reduced antioxidant/antimicrobial reserve, but post-transport shelf life and sensory quality were not measured.

## Methods and Design

- Clarified the main-trial design: one 4-box stack and two 3-box stacks per nominal chamber condition, with top and bottom sensors in each stack.
- Stated that stack height was not independently analysed because it was not balanced or replicated as a factor.
- Clarified the missing bottom-position sensor and resulting unbalanced cells of n = 3, 3, 3 and 2.
- Added that chamber condition is unreplicated at chamber level; chamber identity and nominal set point cannot be separated.
- Added that chamber model, volume, fan power, airflow rate and pallet occupancy ratio were not recorded.
- Clarified that chemical sampling was not resolved by stack position and that microbiological analyses/viable cell counts were not performed.

## Statistics and Reproducibility

- Recomputed the embedded pressure ANOVA values independently.
- Added adjusted effect estimates and confidence intervals to the revised pressure interpretation.
- Replaced "no effect" language with "no statistically detectable nominal chamber-condition effect."
- Labelled pressure p-values as exploratory sensor-level results because the embedded summary data do not retain stack IDs for paired or blocked stack-level analysis.
- Removed wording implying Type II sums of squares form a simple share of total variability in the unbalanced design.
- Updated `anova_pressure.py` so it runs without `statsmodels` using explicit least-squares Type II calculations.
- Updated `anova_pressure.py` to print model-adjusted contrasts and approximate 95% CIs.
- Added `pressure_summary_embedded.csv` with the embedded per-sensor pressure summaries.
- Added `requirements.txt`.
- Added `analysis_verification.md` documenting commands, reproduced statistics, raw-data absence and unresolved reproducibility limitations.

## Chemistry

- Downgraded the lactic-acid interpretation: malolactic fermentation is not supported by malic acid data but cannot be ruled out without microbiology and sensitivity data.
- Corrected the lactic-acid table entry to the conservative `0.29 +/- 0.20` g/L value because available repository files conflicted on the SD and raw chemical replicates were absent; no significant lactic-acid difference is claimed.
- Removed unsupported exclusion of residual microbial activity.
- Clarified that volatile-acidity changes are consistent with warmer storage but are not mechanistically resolved.
- Rephrased SO2 and acidity language as after-20-day between-condition differences rather than undocumented temporal losses or increases.
- Corrected Table 2 sample labels so they refer to nominal chamber conditions rather than actual wine temperature.
- Marked `Nota_per_Nicola_acido_lattico.docx` as a stale internal note in `analysis_verification.md`; it should not be circulated as support for the revised interpretation.

## Verification Trial

- Replaced confirm/prove/establish language with limited-support wording.
- Stated that the verification trial used one three-box stack for 15 days and cannot independently establish a general position effect.
- Discussed the main-vs-verification thermal discrepancy as consistent with chamber/loading/airflow/scale differences, without claiming a measured cause.

## Limitations

- Expanded limitations to cover:
  - small sample size and missing sensor;
  - unbalanced pressure design;
  - unreplicated chamber factor;
  - nominal-vs-achieved temperature mismatch;
  - unavailable chamber specifications;
  - non-position-resolved chemistry;
  - lack of microbiology;
  - unknown grape variety/vintage;
  - lack of shelf-life and sensory follow-up;
  - first-five-hour exclusion and unavailable full-record sensitivity;
  - lack of sensor techno-economic analysis.

## Response Package

- Created `reviewer_resolution_matrix.md`.
- Reconstructed the R2/R3 response letter source in `Response_to_Reviewers_R2_R3.md`.
- Regenerated `Response_to_Reviewers.docx` from that source.
