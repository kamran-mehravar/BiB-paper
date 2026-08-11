# GO / NO-GO Review Before Resubmission

## Executive Decision

**GO after manual Word review.**

The current branch has been corrected for the pressure/common-mode issue and related scope limitations. The chemistry/Table 2 presentation has also been restored according to the author-approved analysis, while retaining cautious wording for lactic acid, microbiology and non-position-resolved chemistry. The package is scientifically safer for resubmission, subject to final manual Word review.

## Barometric/Common-Mode Pressure Audit

Trial dates:

- Main trial: absolute start/end dates were not recovered from `Results.xlsx` or manuscript records. The workbook contains relative time only.
- Verification trial: `Stack testing high temperature.xlsx` contains absolute timestamps beginning 2024-12-16 for the verification trial.
- Location: the study records identify the University of Pisa / INFN Pisa context, but no exact logger-location metadata for barometric correction were retained.

External ambient pressure correction:

- Not performed for the main-trial pressure ANOVA because the main-trial absolute dates are unavailable.
- No barometric data were fabricated or assigned by assumption.
- A future correction would require importing hourly/sub-hourly ambient pressure for the verified main-trial dates and nearest suitable Pisa-area station.

Internal common-mode diagnostics:

- Source: `Results.xlsx`.
- Script: `go_no_go_audit.py`.
- Derived files: `pressure_common_mode_correlations.csv`, `pressure_common_mode_residual_summary.csv`, `pressure_common_mode_peak_anova.csv`, `pressure_residual_at_original_peak_anova.csv`, `pressure_leave_one_out.csv`, `pressure_position_difference_trace.csv`.
- Leave-one-out correlations between each sensor trace and the mean of the remaining sensors ranged from 0.8590 to 0.9727; mean correlation was 0.9368.
- This supports the concern that the broad absolute pressure trace includes common-mode pressure behaviour and should not be interpreted only as package pressurisation/relaxation.

Original uncorrected peak endpoint:

- Position: F(1,8) = 9.1399, p = 0.0165.
- Nominal chamber: F(1,8) = 0.2079, p = 0.6606.
- Interaction: p = 0.5552.
- Adjusted bottom-minus-top difference: +20.4 mbar, 95% CI +4.8 to +35.9 mbar.

Common-mode residual endpoint:

- Maximum common-mode residual per sensor after handling: position F(1,8) = 3.2069, p = 0.1111.
- Adjusted bottom-minus-top difference: +14.4 mbar, 95% CI -4.1 to +32.9 mbar.
- Residual at each sensor's original uncorrected peak time: position F(1,8) = 9.0154, p = 0.0170.

Leave-one-out robustness:

- Original uncorrected peak-position p-values ranged from 0.0007 to 0.0511.
- Removing V51 gave p = 0.0511, showing that the nominal p = 0.0165 result is not robust to every single-sensor deletion.

Final pressure interpretation:

- The manuscript retains the reproducible uncorrected peak analysis but no longer treats it as definitive package-mechanics evidence.
- The revised interpretation is: an exploratory transient position-related offset was observed, superimposed on common-mode absolute-pressure variation.
- The manuscript now states that the absence of a barometric reference sensor limits interpretation of absolute pressure traces.

## Thermal Interpretation Audit

Verification thermal response:

| Sensor | Position | Plateau estimate (degC) | Time to 90% plateau (d) | Time to 95% plateau (d) | Approx. tau from t90 (d) |
|---|---|---:|---:|---:|---:|
| V26 | Top | 48.67 | 2.17 | 2.77 | 0.94 |
| V62 | Top | 47.62 | 2.87 | 3.42 | 1.25 |
| V27 | Bottom | 44.97 | 4.27 | 5.08 | 1.85 |
| V64 | Bottom | 47.54 | 3.73 | 4.73 | 1.62 |

Assumptions:

- Complete verification sensors used the day 14-15 mean as the plateau estimate.
- V26 used the final 6 h before dropout.
- These are descriptive first-order approximations only, not a fitted mechanistic model.

Main-trial comparison:

- Main nominal 50 degC late temperatures were stable far below the nominal set point: top 34.18 +/- 0.36 degC and bottom 26.08 +/- 0.23 degC.
- The verification trial approached high temperatures within a few days, whereas the main trial remained far below set point by day 20.
- The manuscript now describes the main-trial thermal mismatch as sustained under-delivery and/or stratification of the effective thermal environment rather than only transient lag.
- Because no chamber-air logger, chamber model, fan/airflow, or occupancy data were recorded, the chamber mechanism cannot be resolved.

## Chemistry/Table 2 Audit

What n = 3 means:

- The manuscript records report triplicate determinations by nominal chamber condition.
- The repository does not establish whether the triplicates were independent package-level samples or analytical repeat measurements.
- Raw replicate-level chemical records are unavailable.

Actions taken:

- Table 2 was restored to the author-approved chemistry presentation, including statistical markers where shown in the approved table.
- Lactic acid remains reported descriptively without significance letters, using the traceable `0.29 +/- 0.02 g/L` value.
- The manuscript retains the limitation that raw replicate-level chemical records are not available in the repository and that chemistry was not resolved by stack position.
- The response package no longer states that Table 2 chemistry markers were removed.

Lactic acid:

- Final descriptive values remain nominal 19 degC: 0.16 +/- 0.05 g/L; nominal 50 degC: 0.29 +/- 0.02 g/L.
- No significance claim is made.
- Malolactic fermentation is not ruled out.

## Metrology Audit

- MS5803-05BA data-sheet limits are reported in the manuscript.
- Baseline referencing reduces static sensor offsets but does not remove temperature-dependent pressure drift.
- No barometric reference logger was recorded.
- No chamber-air logger was recorded.
- No bench calibration in wine matrix under the tested temperature profile was found.
- The oil-filled casing and displaced headspace are now included as possible perturbations in the limitations.
- The ESP-M2 / ESP8285 reference was checked against Adafruit product documentation and was retained.

## Scope/Title Audit

The prior title phrase "under Simulated Export Conditions" was too broad because the study did not include vibration, humidity control, diurnal thermal cycling, a container thermal profile, or a standard transport-simulation protocol.

Title changed to:

**In-Bag Pressure and Temperature Monitoring of Palletised 3-L Bag-in-Box Wine under Static Chamber Conditions**

The Introduction, Materials and Methods, Conclusions, response letters, and submission README were updated consistently.

## Submission Hygiene Audit

Corrected:

- MDPI metadata placeholder table removed from the final clean and highlighted manuscripts.
- Author Contributions template boilerplate removed.
- Funding line-number artefacts removed.
- Table 2 empty column removed.
- Table 2 sample labels and note corrected while retaining the author-approved chemistry markers where applicable.
- Data Availability Statement revised to avoid confusing file-list wording.
- Reviewer-facing files retain original-data/re-analysis framing and do not imply post-review data collection.

Checked:

- No "Wine at 50 degC" sample label remains in Table 2.
- No main-trial statement describes actual wine exposure at 50 degC.
- No "new data" provenance framing remains in reviewer-facing or submission-facing files.

## Files Changed

- `sent-foods-4487055_major_revision_r2_r3_FINAL_CLEAN.docx`
- `sent-foods-4487055_major_revision_r2_r3_FINAL_HIGHLIGHTED.docx`
- `SUBMISSION_PACKAGE/Manuscripts/01_Manuscript_FINAL_HIGHLIGHTED.docx`
- `SUBMISSION_PACKAGE/Manuscripts/02_Manuscript_FINAL_CLEAN.docx`
- `Response_to_Reviewers.docx`
- `Response_to_Reviewers_R2_R3.md`
- `SUBMISSION_PACKAGE/Responses/03_Response_to_Reviewer_2.docx`
- `SUBMISSION_PACKAGE/Responses/03_Response_to_Reviewer_2.md`
- `SUBMISSION_PACKAGE/Responses/04_Response_to_Reviewer_3.docx`
- `SUBMISSION_PACKAGE/Responses/04_Response_to_Reviewer_3.md`
- `SUBMISSION_PACKAGE/Manuscripts/FIGURE_INSERTION_GUIDE.md`
- `SUBMISSION_PACKAGE/README_SUBMISSION.md`
- `analysis_verification.md`
- `reviewer_resolution_matrix.md`
- `REVIEWER_DRIVEN_CHANGES.md`
- `REVISION_CHANGELOG.md`
- `anova_pressure.py`
- `reanalyse_raw_data.py`
- `go_no_go_audit.py`
- `pressure_common_mode_correlations.csv`
- `pressure_common_mode_residual_summary.csv`
- `pressure_common_mode_peak_anova.csv`
- `pressure_common_mode_peak_contrasts.csv`
- `pressure_residual_at_original_peak_anova.csv`
- `pressure_residual_at_original_peak_contrasts.csv`
- `pressure_leave_one_out.csv`
- `pressure_position_difference_trace.csv`
- `verification_thermal_response.csv`

## Validation

Commands run successfully:

```bash
python reanalyse_raw_data.py
python anova_pressure.py
python anova_pressure.py --from-raw
python go_no_go_audit.py
python -m compileall anova_pressure.py reanalyse_raw_data.py go_no_go_audit.py
```

DOCX and package checks:

- Clean and highlighted manuscript scientific text matched after normalization.
- Clean manuscript contained zero yellow-highlighted runs.
- Highlighted manuscript retained yellow highlighting.
- Final manuscript DOCX files contain two tables: Table 1 and Table 2.
- Embedded manuscript images for Figures 3-7 matched the current `_FINAL.png` files byte-for-byte.
- Separate Reviewer 2 response contains R2 items only.
- Separate Reviewer 3 response contains R3 items only.

## Git

- Branch: `major-revision-r2-r3`
- Commit SHA: see final repository commit created after this report.
- Push status: to be completed after final validation and commit.
