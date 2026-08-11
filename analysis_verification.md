# Analysis Verification

Second-pass verification after merging commit `989b7f4db1d9cfc2c81b0d4cb9c456ee1502c168`.

## Commands

Run from the repository root:

```bash
python -m compileall anova_pressure.py reanalyse_raw_data.py
python anova_pressure.py
python anova_pressure.py --from-raw
python reanalyse_raw_data.py
```

All commands completed successfully in this audit. `statsmodels` was not installed, so `anova_pressure.py` used its explicit least-squares Type II calculations.

## Analyses Based On Raw Or Processed Workbook Data

### Main Pressure Analysis

Source: `Results.xlsx`, sheet `Compare`.

Script: `anova_pressure.py --from-raw`; independently reproduced by `reanalyse_raw_data.py`.

Statistical unit: one instrumented BiB sensor trace. The workbook restores sensor IDs and position/nominal chamber mapping, but it does not restore stack IDs or top-bottom pairings. The analysis therefore remains exploratory and sensor-level. It is not a replicated chamber-level test and not a paired stack-level analysis.

Baseline rule: the initial valid pressure reading at time zero was used as each sensor-specific baseline. Historical code used a `t <= 0.02 d` threshold, but in `Results.xlsx` the next time point after zero is `0.020833 d`; therefore the reproduced analysis used the time-zero pressure only. The final scripts now select the initial valid reading explicitly, without changing any derived pressure values.

Primary peak rule: maximum baseline-referred pressure change after the handling window (`t >= 0.21 d`) and within the 20-day storage window.

Day-20 rule: mean baseline-referred pressure change for `t >= 19.5 d` to `20.0 d`; 25 readings per usable sensor.

Per-sensor summaries are written to `pressure_summary_raw.csv`.

| Sensor | Position | Nominal chamber | Peak dP (mbar) | Peak hour | Day-20 dP (mbar) |
|---|---|---:|---:|---:|---:|
| V50 | Top | 50 degC | 63.4638 | 101.0 | 33.5127 |
| V53 | Top | 50 degC | 58.3335 | 97.0 | 32.5126 |
| V71 | Top | 50 degC | 77.9051 | 97.0 | 60.2513 |
| V52 | Bottom | 50 degC | 92.1697 | 138.0 | 55.9552 |
| V56 | Bottom | 50 degC | 63.1891 | 96.0 | 17.0045 |
| V70 | Bottom | 50 degC | 93.7639 | 138.5 | 43.7397 |
| V55 | Top | 19 degC | 56.4339 | 85.0 | 36.1306 |
| V57 | Top | 19 degC | 56.9113 | 88.0 | 38.1726 |
| V58 | Top | 19 degC | 65.4962 | 85.0 | 50.7070 |
| V51 | Bottom | 19 degC | 91.0728 | 86.0 | 62.5850 |
| V59 | Bottom | 19 degC | 78.5783 | 86.0 | 52.3243 |

The raw-workbook extraction matches the embedded summary values to 0.0000 mbar.

### Pressure ANOVA

Source: `Results.xlsx`; derived file `pressure_anova_raw.csv`.

Model: additive two-factor model with position (`Top`, `Bottom`) and nominal chamber condition (`19`, `50`). The interaction was checked separately. Type II sums of squares were retained because the cell counts are unbalanced and the interaction was not statistically significant.

Cell sizes: nominal 50 top n=3, nominal 50 bottom n=3, nominal 19 top n=3, nominal 19 bottom n=2.

Peak dP:

- Position: F(1,8) = 9.1399, p = 0.0165.
- Nominal chamber condition: F(1,8) = 0.2079, p = 0.6606.
- Position by chamber interaction: F(1,7) = 0.3838, p = 0.5552.
- Adjusted bottom-minus-top effect: +20.4 mbar, 95% CI +4.8 to +35.9 mbar.
- Adjusted nominal 50-minus-19 effect: +3.1 mbar, 95% CI -12.5 to +18.6 mbar.

Day-20 dP:

- Position: F(1,8) = 0.3479, p = 0.5716.
- Nominal chamber condition: F(1,8) = 0.8127, p = 0.3937.
- Position by chamber interaction: F(1,7) = 1.1463, p = 0.3199.
- Adjusted bottom-minus-top effect: +5.2 mbar, 95% CI -15.3 to +25.7 mbar.
- Adjusted nominal 50-minus-19 effect: -8.0 mbar, 95% CI -28.5 to +12.5 mbar.

Interpretation: bottom-position sensors showed a larger post-handling peak dP in this small sensor-level dataset. Lack of statistical significance for nominal chamber condition or day-20 factors must be read only as no statistically detectable difference under this design.

### First-Five-Hour Sensitivity

Source: `Results.xlsx`; derived file `early_transient_sensitivity.csv`.

Question: would including the first five hours alter the primary pressure-peak endpoint?

Result: no. For every usable main-trial sensor, the full-record maximum dP equals the post-handling maximum dP. All primary peaks occur after 5 h, between 85.0 and 138.5 h.

Early-window maxima varied by sensor:

- Highest early dP values among top nominal 19 sensors were already close to their later maxima (V55 54.2 mbar at 1 h, V57 56.6 mbar at 1 h, V58 65.2 mbar at 1 h).
- Nominal 50 top early dP values were much lower than later maxima (6.7 to 10.9 mbar).
- Some bottom sensors had substantial early values, especially V56 (52.8 mbar at 1 h), but later peaks remained larger.

Caveat: the first-five-hour temperature/pressure block in `Results.xlsx` contains duplicated rows, so early transient shape should not be overinterpreted as a high-fidelity exposure record. The pressure peak sensitivity is still useful because the global maxima are all later than the duplicated block.

### Main-Trial Thermal Exposure

Source: `Results.xlsx`; derived files `thermal_summary_main_sensors.csv` and `thermal_summary_main_groups.csv`.

Group means:

| Nominal chamber | Position | n | Initial temp mean +/- SD (degC) | 5 h temp mean +/- SD (degC) | 16 h temp mean +/- SD (degC) | Late 19.5-20 d temp mean +/- SD (degC) | Post-handling max mean +/- SD (degC) |
|---|---|---:|---:|---:|---:|---:|---:|
| 19 degC | Bottom | 2 | 25.35 +/- 0.35 | 15.05 +/- 3.46 | 17.85 +/- 0.21 | 22.84 +/- 0.30 | 23.65 +/- 0.21 |
| 19 degC | Top | 3 | 25.27 +/- 1.20 | 12.97 +/- 0.15 | 18.23 +/- 0.81 | 23.50 +/- 0.21 | 24.83 +/- 0.21 |
| 50 degC | Bottom | 3 | 28.77 +/- 6.60 | 12.77 +/- 0.50 | 16.33 +/- 0.75 | 26.08 +/- 0.23 | 26.57 +/- 0.12 |
| 50 degC | Top | 3 | 28.17 +/- 4.66 | 21.40 +/- 2.25 | 19.73 +/- 1.16 | 34.18 +/- 0.36 | 34.83 +/- 0.42 |

Interpretation: the main nominal 50 degC trial did not expose the wine to 50 degC. The warmest main-trial package sensors reached approximately 35.3 degC individually and 34.8 degC as a top-position group maximum. The nominal 19 degC chamber packages stabilised above the set point, near 23 degC.

### Verification Trial

Source: `Stack testing high temperature.xlsx`, sheet `Compare`; derived file `verification_summary_raw.csv`.

Statistical unit: four sensors in one three-box verification stack; two top and two bottom sensors. This restores raw verification traces but not independent stack replication.

Temperature maxima:

- V26 top: 48.8 degC at day 4.27; record stops at 4.35 d.
- V62 top: 47.7 degC at day 10.22.
- V27 bottom: 45.0 degC at day 9.45.
- V64 bottom: 47.6 degC at day 10.35.

No in-bag verification sensor reached 50 degC.

Late day 14-15 temperatures:

- V62 top: 47.62 degC; V26 unavailable after day 4.35.
- V27 bottom: 44.97 degC.
- V64 bottom: 47.54 degC.

Pressure dP from each sensor's first valid pressure:

- V26 top: peak +26.52 mbar at day 1.47; minimum -3.84 mbar at day 3.55.
- V62 top: peak +9.58 mbar at day 0.26; minimum -27.19 mbar at day 6.32.
- V27 bottom: peak +15.18 mbar at day 0.03; minimum -14.87 mbar at day 6.34.
- V64 bottom: peak +15.65 mbar at day 0.25; minimum -21.79 mbar at day 6.35.

Main-vs-verification late thermal discrepancy:

- Top: verification late available top sensor 47.62 degC versus main nominal 50 top 34.18 degC, difference +13.44 degC.
- Bottom: verification bottom mean about 46.26 degC versus main nominal 50 bottom 26.08 degC, difference about +20.18 degC.

The difference is consistent with scale, chamber loading, airflow, geometry or chamber-performance differences, but the files do not identify a single cause.

## Analyses Based Only On Summary Data

### Chemistry

Raw chemical replicate data remain absent. `Results.xlsx` contains no chemical sheet, hidden sheet, defined names or chemistry table. The chemical values therefore remain summary-only values from Table 2 / manuscript records.

The repository contains an inconsistency in lactic-acid SD for wine from the nominal 50 degC chamber. The originally submitted Table 2 reports `0.29 +/- 0.02 g/L`, and this is the traceable tabulated experimental value. The alternative `0.29 +/- 0.20 g/L` appears in later revision/note material, but no raw chemical replicate data or other primary experimental record supporting the `0.20 g/L` SD was found. The final manuscript therefore reports `0.29 +/- 0.02 g/L` descriptively only. No significance claim is made for lactic acid, and microbiological activity cannot be ruled out because no viable cell counts or microbiological assays are available.

Summary-only chemical values used in the manuscript:

- Lactic acid: 0.16 +/- 0.05 g/L (nominal 19) vs 0.29 +/- 0.02 g/L (nominal 50), descriptive.
- Malic acid: 1.1 +/- 0.23 g/L vs 1.0 +/- 0.16 g/L.
- Volatile acidity: 0.30 +/- 0.02 g/L vs 0.39 +/- 0.03 g/L.
- Total SO2: 50 +/- 5.5 mg/L vs 25 +/- 8.2 mg/L.
- Free SO2: 31 +/- 2.5 mg/L vs 16 +/- 1.8 mg/L.

These values are not position-resolved and cannot be linked directly to top/bottom pressure observations.

## Remaining Statistical Limitations

- One physical chamber per nominal set point: chamber identity and nominal chamber condition are confounded.
- Main-trial pressure analysis has 11 usable sensor traces, one missing bottom-position trace and an unbalanced n=2 cell.
- Main-trial workbook does not retain stack IDs, preventing paired or blocked stack-level reanalysis.
- Time-series timestamps are not treated as replicates; the ANOVA uses one or two derived summaries per sensor.
- Verification trial has raw traces but only one stack and cannot establish population-level position effects.
- Chemistry remains summary-only and not position-resolved.
- No microbiology, sensory follow-up, shelf-life test, chamber airflow/volume/fan metadata, barometric reference or cost data were found.

## Manuscript Statistics Traceability

| Manuscript statistic | Data source | Script / file | Unit | Status |
|---|---|---|---|---|
| Peak dP means and SDs | `Results.xlsx` | `pressure_summary_raw.csv` | Sensor trace | Reproduced |
| Day-20 dP means and SDs | `Results.xlsx` | `pressure_summary_raw.csv` | Sensor trace | Reproduced |
| Peak dP ANOVA F/p | `Results.xlsx` | `anova_pressure.py --from-raw`; `pressure_anova_raw.csv` | Sensor trace | Reproduced |
| Day-20 dP ANOVA F/p | `Results.xlsx` | `anova_pressure.py --from-raw`; `pressure_anova_raw.csv` | Sensor trace | Reproduced |
| First-five-hour pressure sensitivity | `Results.xlsx` | `early_transient_sensitivity.csv` | Sensor trace | New second-pass analysis |
| Main actual in-bag temperatures | `Results.xlsx` | `thermal_summary_main_groups.csv` | Sensor trace | Reproduced from new data |
| Verification temperature and dP | `Stack testing high temperature.xlsx` | `verification_summary_raw.csv` | Sensor trace within one stack | Reproduced from new data |
| Chemical means and SDs | Manuscript Table 2 only | No raw replicate data | Bulk condition summary | Summary-only; not independently reproducible |
