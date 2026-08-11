# Revision Changelog

Major revision for Reviewer 2 and Reviewer 3, updated after second-pass integration of commit `989b7f4db1d9cfc2c81b0d4cb9c456ee1502c168`.

## Second-Pass Evidence Integration

- Merged the new main-trial and verification data files into the revision branch.
- Identified `Results.xlsx` as the main-trial pressure/temperature workbook.
- Identified `Stack testing high temperature.xlsx` as the verification-trial workbook.
- Identified `Stack testing high temperature - Compare.csv` as a lossy CSV export of the verification workbook's `Compare` sheet.
- Added `DATA_PROVENANCE.md` to document every raw/processed dataset and its relationship to manuscript figures and statistics.
- Added `reanalyse_raw_data.py` to generate derived CSV summaries and corrected Figures 3-7 from the verified workbooks.

## Scientific Interpretation

- Reframed the manuscript around nominal chamber set points and measured in-bag temperature, rather than implying that the main trial exposed wine to 50 degC.
- Updated main-trial thermal values from the raw workbook: late nominal 50 degC in-bag temperatures were 34.18 +/- 0.36 degC at top sensors and 26.08 +/- 0.23 degC at bottom sensors; the nominal 19 degC chamber packages were about 23 degC.
- Removed the binary claim that palletisation "governs" physical behaviour while temperature "governs" chemical stability.
- Replaced broad causal language with condition-specific wording:
  - bottom stack position was associated with higher peak dP in the exploratory sensor-level analysis;
  - chemistry differed between bulk samples from nominal chamber conditions;
  - verification observations were limited and supporting.
- Added explicit storage-stability caution: lower SO2 values may indicate reduced antioxidant/antimicrobial reserve, but post-transport shelf life and sensory quality were not measured.

## Methods and Design

- Clarified the main-trial design: one 4-box stack and two 3-box stacks per nominal chamber condition, with top and bottom sensors in each stack.
- Stated that stack height was not independently analysed because it was not balanced or replicated as a factor.
- Clarified the missing bottom-position sensor and resulting unbalanced pressure cells of n = 3, 3, 3 and 2.
- Added that chamber condition is unreplicated at chamber level; chamber identity and nominal set point cannot be separated.
- Added that chamber model, volume, fan power, airflow rate and pallet occupancy ratio were not recorded.
- Clarified that chemical sampling was not resolved by stack position and that microbiological analyses/viable cell counts were not performed.
- Updated the Data Availability Statement to distinguish available pressure/temperature workbooks from absent raw chemical replicates.

## Statistics and Reproducibility

- Updated `anova_pressure.py` so `--from-raw` reads `Results.xlsx`, with embedded summary values retained as a fallback.
- Recomputed the main pressure summaries from `Results.xlsx`; the raw-workbook extraction matches embedded values to 0.0000 mbar.
- Reproduced peak dP ANOVA: position F(1,8) = 9.14, p = 0.017; nominal chamber F(1,8) = 0.21, p = 0.66; interaction p = 0.56.
- Reproduced day-20 dP ANOVA: position F(1,8) = 0.35, p = 0.57; nominal chamber F(1,8) = 0.81, p = 0.39; interaction p = 0.32.
- Added adjusted effect estimates and confidence intervals to the pressure interpretation.
- Replaced "no effect" language with "no statistically detectable nominal chamber-condition effect."
- Labelled pressure p-values as exploratory sensor-level results because neither the raw workbook nor derived summaries retain stack IDs for paired or blocked stack-level analysis.
- Added first-five-hour sensitivity analysis: full-record pressure maxima equal post-handling maxima for all 11 sensors, while early transients remain uncontrolled and partly duplicated in the workbook.
- Added derived files: `pressure_summary_raw.csv`, `pressure_anova_raw.csv`, `pressure_contrasts_raw.csv`, `early_transient_sensitivity.csv`, `thermal_summary_main_sensors.csv`, `thermal_summary_main_groups.csv`, `verification_summary_raw.csv`, `main_trial_sensor_map.csv`, and `verification_trial_sensor_map.csv`.
- Regenerated corrected Figures 3-7 with nominal set-point labels.

## Chemistry

- Confirmed that raw chemical replicate data remain absent after inspection of the new workbooks.
- Downgraded the lactic-acid interpretation: malolactic fermentation is not supported by the reported malic-acid summary but cannot be ruled out without microbiology and sensitivity data.
- Kept the conservative `0.29 +/- 0.20 g/L` lactic-acid value because available repository files conflict on the SD and raw replicates are unavailable.
- Removed unsupported exclusion of residual microbial activity.
- Clarified that volatile-acidity changes are consistent with warmer storage but are not mechanistically resolved.
- Rephrased SO2 and acidity language as after-20-day between-condition differences rather than undocumented temporal losses or increases.
- Corrected Table 2 sample labels so they refer to nominal chamber conditions rather than actual wine temperature.

## Verification Trial

- Replaced confirm/prove/establish language with limited-support wording.
- Recomputed verification summaries from `Stack testing high temperature.xlsx`: sensor temperature maxima were 45.0-48.8 degC, and no in-bag sensor reached 50 degC.
- Quantified verification pressure peaks from each sensor's first valid baseline: 9.6-26.5 mbar.
- Stated that the verification trial used one three-box stack for 15 days and cannot independently establish a general position effect.
- Quantified the main-vs-verification thermal discrepancy and treated possible causes as hypotheses rather than established mechanisms.

## Limitations

- Retained limitations that remain true after new-data inspection:
  - small sample size and missing sensor;
  - unbalanced pressure design;
  - unreplicated chamber factor;
  - nominal-vs-achieved temperature mismatch in the main trial;
  - unavailable chamber specifications;
  - non-position-resolved chemistry;
  - absent raw chemical replicates;
  - lack of microbiology;
  - unknown grape variety/vintage;
  - lack of shelf-life and sensory follow-up;
  - partial uncertainty in the first-five-hour transient because of duplicated early workbook rows;
  - lack of sensor techno-economic analysis.
- Removed the first-pass limitation that main pressure/temperature raw data were absent.

## Response Package

- Rebuilt `reviewer_resolution_matrix.md` in the required second-pass format.
- Created `REVIEWER_DRIVEN_CHANGES.md` to document removed or materially weakened claims.
- Updated `analysis_verification.md` to distinguish raw-workbook pressure/temperature analyses from summary-only chemistry.
- Updated `Response_to_Reviewers_R2_R3.md` and regenerated `Response_to_Reviewers.docx`.
- Created clean and highlighted final manuscript DOCX files.
