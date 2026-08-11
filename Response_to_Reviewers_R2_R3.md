# Response to Reviewers

Manuscript: "Palletisation and In-Bag Thermal Exposure in Bag-in-Box Wine Packaging under Simulated Export Conditions"

We thank Reviewer 2 and Reviewer 3 for their detailed assessment. After the first revision, additional pressure/temperature workbooks and figures became available in the repository. We therefore re-audited the data provenance, reran the pressure analysis from the main-trial workbook, quantified the first-five-hour sensitivity, reconstructed the verification trial from its workbook, regenerated Figures 3-7 with unambiguous nominal set-point labels, and updated the manuscript and response package accordingly. The new data improve traceability, but they do not add independent chamber replication, stack IDs for the main-trial sensors, raw chemical replicates, microbiology, shelf-life follow-up or cost data.

## Reviewer 2

### R2.1 Main trial did not achieve 50 degC

### Reviewer Comment

The chamber was set at 50 degC, but the wine experienced about 25-34 degC; this changes the hypothesis test.

### Response

We agree. The revised manuscript no longer treats the main trial as actual 50 degC wine exposure. The newly available `Results.xlsx` workbook allowed us to quantify the realised in-bag temperatures directly. During the late storage window (days 19.5-20), the nominal 50 degC chamber averaged 34.18 +/- 0.36 degC in top-position sensors and 26.08 +/- 0.23 degC in bottom-position sensors. The nominal 19 degC chamber averaged 23.50 +/- 0.21 degC in top-position sensors and 22.84 +/- 0.30 degC in bottom-position sensors. The study is therefore interpreted as a comparison between nominal chamber conditions and measured package temperatures, not as a direct 19 degC versus 50 degC wine-temperature comparison.

### Changes in Manuscript

The Title, Abstract, Sections 2, 3.1, 3.2, 3.4, Conclusions, captions and Table 2 now distinguish nominal chamber set point from measured in-bag temperature. The highlighted manuscript marks these changes.

### R2.2 Abstract

### Reviewer Comment

The Abstract should be condensed, restructured and explicit about the actual temperatures.

### Response

The Abstract has been rewritten again after the second-pass data audit. It now reports the raw-workbook late-temperature summaries, the exploratory pressure effect estimate, the absence of a statistically detectable nominal chamber-condition effect, the summary-only scope of the chemistry data, and the limited role of the verification trial.

### Changes in Manuscript

The Abstract was replaced with a shorter evidence-aligned version. It no longer states or implies that the main trial exposed wine to 50 degC and no longer describes all pressure peaks as occurring on a single day.

### R2.3 Chamber characteristics

### Reviewer Comment

Chamber model, air circulation, fan power, chamber volume and pallet occupancy should be provided.

### Response

We searched the original repository files and the newly added workbooks/figures. These chamber-control details were not present. We have not invented specifications. Instead, the manuscript now states that chamber model, chamber volume, fan power, airflow rate and pallet occupancy ratio were not recorded and that this limits diagnosis of the thermal lag and vertical gradient observed in the main trial.

### Changes in Manuscript

The Materials and Methods and Limitations sections state which chamber details were unavailable and restrict mechanism language to hypotheses.

### R2.4 Small sample size and ANOVA power

### Reviewer Comment

The pressure ANOVA has very limited power because n is small and one bottom sensor is missing.

### Response

We agree. The second-pass audit changes the reproducibility status but not the replication status. The newly available `Results.xlsx` workbook lets us reconstruct the pressure summaries from the main-trial data, and `anova_pressure.py --from-raw` now reads that workbook. The reconstructed values match the embedded summaries to 0.0000 mbar. However, the pressure cells remain n = 3, 3, 3 and 2, chamber condition remains one chamber per nominal set point, and the workbook does not retain stack IDs or sensor-to-stack pairings for a blocked or paired stack-level analysis. We therefore retain the ANOVA only as exploratory sensor-level inference and report effect estimates and confidence intervals alongside p-values.

### Changes in Manuscript

Sections 2.2, 2.4, 3.2, 3.4 and Conclusions now state the experimental unit, the missing sensor, the unbalanced design, the unreplicated chamber factor and the exploratory interpretation. The analysis report and `anova_pressure.py` were updated to document the raw-workbook reconstruction.

### R2.5 Verification trial n=1 stack

### Reviewer Comment

The verification trial cannot confirm general conclusions because it used only one stack and one sensor failed.

### Response

We agree. The verification workbook now allows a more precise description, but it does not create replication. The trial used one three-box stack. V26, one top-position sensor, stopped at day 4.35. Across the four verification sensors, maximum in-bag temperatures ranged from 45.0 to 48.8 degC, and no in-bag sensor reached 50 degC. Pressure changes from each sensor's first valid baseline were transient, with peaks of 9.6-26.5 mbar. The manuscript presents this trial as limited supporting evidence under one configuration, not as confirmation of a general position effect.

### Changes in Manuscript

Sections 2.3, 3.3, 3.4 and Conclusions were revised to remove confirmatory language and to report the verification trial's scale, V26 dropout and actual sensor maxima.

### R2.6 Physical-versus-chemical binary conclusion

### Reviewer Comment

The claim that palletisation governs physical behaviour and temperature governs chemical stability is overreaching because chemistry was not position-resolved.

### Response

We agree. The manuscript no longer presents this binary causal attribution. The new data do not add position-resolved chemistry. The final text states that pressure was measured by package position and showed a transient bottom-position peak, whereas chemistry was measured as bulk wine grouped by nominal chamber condition. These two datasets support different descriptive response patterns, but they do not demonstrate that palletisation and temperature act independently or exclusively on separate parts of the system.

### Changes in Manuscript

The Abstract, Discussion, Limitations and Conclusions were revised; unsupported "governs" language was removed.

### R2.7 Lactic acid interpretation

### Reviewer Comment

The lactic-acid increase cannot be confidently attributed to heat-driven chemistry rather than malolactic fermentation without microbiological data.

### Response

We agree. We inspected the newly added `Results.xlsx` workbook and confirmed that it contains pressure/temperature data only, not raw chemical replicates. The repository therefore still does not resolve the lactic-acid SD inconsistency in the original files or provide microbiological evidence. The manuscript keeps the conservative `0.29 +/- 0.20 g/L` value for the nominally warmer chamber and treats lactic acid descriptively. We state that malic acid did not show the clear decrease expected for a simple malolactic-conversion interpretation, but we no longer state that malolactic fermentation was ruled out. Residual microbial activity cannot be excluded.

### Changes in Manuscript

Sections 2.4 and 3.1, Table 2 and Limitations were revised to describe lactic acid as a descriptive observation and to state the absence of raw chemical replicates, microbiology, viable cell counts and method-sensitivity data.

### R2.8 Table 2 labels

### Reviewer Comment

"Wine at 19 degC" and "Wine at 50 degC" are misleading.

### Response

Corrected. Table 2 now labels the rows as wine from the nominal 19 degC chamber and wine from the nominal 50 degC chamber. The caption states that these labels are chamber set points, not actual in-bag wine temperatures.

### Changes in Manuscript

Table 2 row labels, caption and note were revised and highlighted.

### R2.9 First five hours excluded

### Reviewer Comment

The first five hours may represent realistic transport disturbances and should be discussed or tested by sensitivity analysis.

### Response

The newly available `Results.xlsx` workbook allowed us to perform the sensitivity analysis that was impossible in the first pass. Including the first five hours did not change the primary peak-pressure endpoint: for all 11 usable sensors, the full-record maximum dP was identical to the post-handling maximum used in the primary analysis. The individual maxima occurred after the handling window, between 85.0 and 138.5 h. We still do not treat the first five hours as settled storage exposure because the interval contained transport/handling/stack assembly and the available workbook contains duplicated early rows. The final manuscript therefore keeps the primary post-handling analysis but now reports the full-record sensitivity result and discusses the logistics relevance of early transients.

### Changes in Manuscript

Section 3.2 and Limitations now report the sensitivity analysis and no longer say that raw pressure data were absent.

### R2.10 Wine identity

### Reviewer Comment

Grape variety and vintage are unknown.

### Response

Correct. The new workbooks were also checked and contain no grape variety or vintage metadata. The supplier did not provide this information, and the manuscript retains it as a limitation.

### Changes in Manuscript

Materials and Methods and Limitations state that grape variety and vintage were unavailable.

## Reviewer 3

### R3.1 Stacking configuration and interpretability

### Reviewer Comment

It is difficult to evaluate stacking configuration because different configurations and temperatures may be confounded or averaged.

### Response

We appreciate this point. The final manuscript clarifies that the pressure analysis evaluates top versus bottom package position under the tested stack configuration. Stack height was not analysed as an independent factor because the design contained one four-box stack and two three-box stacks per nominal chamber condition. The newly available `Results.xlsx` workbook restores the main-trial traces but does not restore stack IDs or sensor-to-stack pairings. Chamber condition also remains unreplicated at the chamber level. The pressure ANOVA is therefore presented as exploratory sensor-level analysis rather than a definitive test of stack height, chamber temperature or paired stack effects.

### Changes in Manuscript

Figure 2 caption, Table 1 note, Sections 2.2, 2.4, 3.4 and Conclusions were revised to define the tested factors and inference limits.

### R3.2 SO2 reduction and post-transport shelf life

### Reviewer Comment

Could SO2 loss affect shelf life and storage after transport?

### Response

We discuss this conservatively. The final manuscript reports that wine from the nominally warmer chamber had lower total and free SO2 values after 20 days than the reference-chamber wine. This may indicate a lower antioxidant and antimicrobial reserve after transport, but actual post-transport shelf life, sensory quality and microbial stability were not measured. We therefore present shelf-life impact as a potential implication, not a measured outcome.

### Changes in Manuscript

Section 3.1, Limitations and Conclusions were revised.

### R3.3 Economic feasibility of pressure sensors

### Reviewer Comment

The feasibility of using pressure sensors at scale is unclear.

### Response

We agree. The manuscript no longer recommends instrumenting every commercial BiB. It frames sensor use as selected sentinel packages, validation campaigns and quality-control deployments. We also state that no techno-economic analysis or deployment-density study was performed.

### Changes in Manuscript

Limitations and Conclusions were revised.

### R3.4 Thermal behaviour under nominal 19 degC and nominal 50 degC conditions

### Reviewer Comment

The nominal 50 degC packages stayed below set point, whereas nominal 19 degC packages reached about 23 degC; this different behaviour needs explanation.

### Response

The newly available `Results.xlsx` workbook lets us answer this quantitatively. Late in the main trial, nominal 50 degC packages averaged 34.18 +/- 0.36 degC at top sensors and 26.08 +/- 0.23 degC at bottom sensors; nominal 19 degC packages averaged 23.50 +/- 0.21 degC at top sensors and 22.84 +/- 0.30 degC at bottom sensors. The manuscript now separates observed facts from interpretation. The observations are consistent with thermal inertia, chamber loading, heat-transfer resistance through the pallet/stack and airflow constraints, but the chamber model, airflow and occupancy data were not recorded, so these remain hypotheses rather than established causes.

### Changes in Manuscript

Sections 3.2, 3.3, 3.4 and the captions to Figures 3 and 6 were revised with the quantified temperatures and cautious interpretation.

### R3.5 Main experiment versus verification experiment discrepancy

### Reviewer Comment

The large difference between the main and verification experiment may indicate an error or scale effect.

### Response

We do not dismiss the discrepancy. The verification workbook shows that the single three-box stack reached much warmer in-bag temperatures than the main nominal 50 degC trial, although no verification sensor reached 50 degC. Sensor maxima were 48.8 degC (V26 top, before dropout), 47.7 degC (V62 top), 45.0 degC (V27 bottom) and 47.6 degC (V64 bottom). Compared with the main trial late means, the verification trial was about 13.4 degC warmer at the top and about 20.2 degC warmer at the bottom. The final manuscript states that the discrepancy may reflect scale, chamber loading, stack geometry, airflow, chamber performance or sensor-location differences, but the available records do not identify a single cause. We therefore do not use the verification trial to correct or override the main trial; it is treated as a separate limited observation.

### Changes in Manuscript

Sections 3.3 and 3.4, Figure 6 caption, Figure 7 caption and Conclusions were revised to quantify the discrepancy and avoid unsupported causal attribution.

### R3.6 English readability

### Reviewer Comment

Several sentences are overly complex.

### Response

The manuscript was edited throughout in the first revision and then edited again after the second-pass data audit. The final version uses shorter sentences and consistent terminology for nominal set point, nominal chamber condition and measured in-bag temperature.

### Changes in Manuscript

The Abstract, Methods, Results, figure/table captions, Limitations and Conclusions were substantially revised and highlighted where changes were reviewer-driven.
