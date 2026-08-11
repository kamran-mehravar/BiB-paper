# Data Provenance

Second-pass audit after integration of commit `989b7f4db1d9cfc2c81b0d4cb9c456ee1502c168` (`data and figs`).

## Provenance Table

| File | Experiment | Raw/Processed | Variables | Sample Units | Sensor IDs | Stack IDs | Time Resolution | Used In Manuscript |
|---|---|---|---|---|---|---|---|---|
| `Results.xlsx` | Main 20-day trial, nominal 19 degC and nominal 50 degC chamber conditions | Processed logger workbook; primary source now available for main pressure/temperature reconstruction | `Compare` sheet with `Time (Days)`, `Time (h)`, and temperature/pressure pairs for 11 usable sensors | Instrumented 3-L BiB units; one pressure/temperature trace per sensor | Recoverable: V50, V53, V71 top nominal 50; V52, V56, V70 bottom nominal 50; V55, V57, V58 top nominal 19; V51, V59 bottom nominal 19 | Not recoverable from the workbook; no stack numbers or top-bottom pair IDs | 30 min, 979 timed records from 0 to 489 h / 20.375 d | Main pressure ANOVA, Figures 3-6A, thermal exposure statements |
| `Stack testing high temperature.xlsx` | Verification trial under nominal 50 degC chamber condition | Workbook containing metadata, per-sensor sheets and processed `Compare` sheet; primary source for verification timing | `Sensor Pos`; sheets `V26_TOP`, `V62_TOP`, `V27_BOT`, `V64_BOT`; `Compare` sheet with temperature, pressure and P/P0 columns | One three-box stack; two top sensors and two bottom sensors | Recoverable: V26 and V62 top; V27 and V64 bottom | Single high-temperature three-box stack; no replicate stack IDs | 1 min in `Compare`, 0 to 15.34 d; V26 stops at 4.35 d | Figures 6B and 7; verification trial Results |
| `Stack testing high temperature - Compare.csv` | Verification trial under nominal 50 degC chamber condition | CSV export of the `Compare` sheet only; not a full workbook replacement | Same sensor temperature/pressure/P/P0 columns as the workbook `Compare` sheet | Same four verification sensors | Same as workbook for sensor IDs | Stack metadata absent from CSV | 1 min values, but exported `Time(days)` is display-rounded/lossy | Checked as duplicate of workbook values; workbook used for timing |
| `pressure_summary_embedded.csv` | Main pressure analysis | Derived summary values from first-pass revision | Per-sensor peak dP and day-20 dP | 11 usable sensors | Same as main trial | No stack IDs | One row per sensor | Cross-check only; reproduced exactly from `Results.xlsx` |
| `anova_pressure.py` | Main pressure analysis | Reproducible analysis script | Embedded and raw-workbook extraction; Type II ANOVA; adjusted contrasts | Sensor-level summaries | Uses hard-coded sensor map | No stack IDs | Summaries derived from 30-min workbook records | Reproduces reported pressure statistics |
| `reanalyse_raw_data.py` | Second-pass audit | Derived-output script; does not modify source files | Main pressure summaries, early-transient sensitivity, thermal summaries, verification summaries, regenerated Figures 3-7 | Sensor-level and group summaries | Uses explicit sensor maps | Main stack IDs unavailable; verification is one stack | Main 30 min; verification 1 min | Produces audit CSVs and final corrected figures |
| `sent-foods-4487055.docx` / `.pdf` | Original submitted manuscript | Submitted manuscript | Text, tables, embedded Figures 1-7 | Manuscript record | N/A | N/A | N/A | Baseline for highlighting reviewer-driven changes |
| `sent-foods-4487055_major_revision_r2_r3.docx` | First-pass revised manuscript | Revised manuscript baseline | Text, tables, embedded figures | Manuscript record | N/A | N/A | N/A | Edited into final clean/highlighted second-pass manuscripts |
| `Nota_per_Nicola_acido_lattico.docx` | Internal chemistry note | Interpretive note | Lactic-acid discussion | N/A | N/A | N/A | N/A | Context only; not raw chemical replicate data |

## Workbook Details

`Results.xlsx`

- Visible sheets: `Compare`.
- Actual non-empty range inspected: `A1:X986`.
- `Compare` contains formulas in the time-axis columns and numeric temperature/pressure values in sensor columns.
- The time axis used for analysis has 979 valid records from 0 to 20.375 d. The manuscript analysis window ends at 20.0 d.
- No hidden sheets, merged cells, chamber metadata, raw chemistry tables, stack IDs, chamber model, chamber volume, fan power, airflow rate or pallet occupancy records were found.
- Early rows contain repeated blocks in the first-five-hour temperature/pressure record; the early transient is therefore reported cautiously.

`Stack testing high temperature.xlsx`

- Visible sheets: `Sensor Pos`, `V26_TOP`, `V62_TOP`, `V27_BOT`, `V64_BOT`, `Compare`.
- `Sensor Pos` identifies the retrial high-temperature stack as a single three-box stack with V26/V62 at the top and V27/V64 at the bottom.
- The `Compare` sheet has minute-resolution time from 0 to 15.34 d. V26 ceases at 4.35 d; the other three sensors continue to 15 d.
- The workbook supports the verification temperature/pressure statements but does not create independent replication.

## Derived Outputs

The following files are generated by:

```bash
python reanalyse_raw_data.py
```

- `main_trial_sensor_map.csv`
- `pressure_summary_raw.csv`
- `early_transient_sensitivity.csv`
- `pressure_anova_raw.csv`
- `pressure_contrasts_raw.csv`
- `thermal_summary_main_sensors.csv`
- `thermal_summary_main_groups.csv`
- `verification_trial_sensor_map.csv`
- `verification_summary_raw.csv`
- `Figure3_pressure_temperature_FINAL.png`
- `Figure4_transient_16h_FINAL.png`
- `Figure5_deltaP_FINAL.png`
- `Figure6_temperature_attained_FINAL.png`
- `Figure7_verification_trial_FINAL.png`

## Reclassified First-Pass Data Limitations

| Previous first-pass statement | Second-pass classification | Evidence |
|---|---|---|
| Raw main pressure logger data were absent. | FULLY RESOLVED BY NEW FILES for the processed main-trial pressure/temperature workbook. | `Results.xlsx` reproduces all embedded pressure summaries. |
| A first-five-hour sensitivity analysis could not be run. | FULLY RESOLVED BY NEW FILES for pressure peak sensitivity; PARTIALLY RESOLVED for temperature transients because early rows contain duplicated blocks. | `early_transient_sensitivity.csv`; workbook row audit. |
| Raw chemical replicate data were absent. | STILL TRUE. | `Results.xlsx` contains only pressure/temperature; no chemistry sheets or hidden tables. |
| Chamber model, airflow, volume and fan information were absent. | STILL TRUE. | No metadata found in new workbooks or figure files. |
| Stack IDs were absent from embedded summaries. | STILL TRUE for the main trial. | `Results.xlsx` restores sensor IDs but not stack numbers or pairings. |
| Verification raw data were absent. | FULLY RESOLVED BY NEW FILES. | `Stack testing high temperature.xlsx` contains verification sensor data and metadata. |
| Chamber factor was unreplicated. | STILL TRUE. | One nominal 19 degC chamber and one nominal 50 degC chamber were used in parallel. |
