# Response to Reviewers

Manuscript: "Palletisation and In-Bag Thermal Exposure in Bag-in-Box Wine Packaging under Simulated Export Conditions"

We thank Reviewer 2 and Reviewer 3 for the detailed assessment. The revision has been made conservatively. The most important change is that the main trial is no longer described as actual 50 degC wine exposure. We now distinguish chamber set point, nominal chamber condition and measured in-bag temperature throughout the manuscript. We also revised the pressure ANOVA wording as exploratory and sensor-level, and treated lactic acid descriptively because the available revision files contained inconsistent standard deviations and raw chemical replicates were unavailable.

## Reviewer 2

### R2.1 Main trial did not achieve 50 degC

Reviewer Comment: The chamber was set at 50 degC, but the wine experienced about 25-34 degC; this changes the hypothesis test.

Response: We agree. The original wording could imply that the wine in the main trial was exposed to 50 degC, which was not the case. The manuscript now states that the 50 degC value was a nominal chamber set point and that measured in-bag temperatures reached about 33.6 +/- 1.5 degC in top units and 25.5 +/- 0.9 degC in bottom units. The realised study is interpreted as a comparison between nominal chamber conditions and actual package temperatures.

Changes in Manuscript: Title, Abstract, Sections 2, 3.1, 3.2, 3.4, Conclusions, captions and Table 2 were revised to use nominal chamber condition and measured in-bag temperature terminology.

### R2.2 Abstract

Reviewer Comment: The Abstract should be condensed, restructured and explicit about the actual temperatures.

Response: The Abstract has been rewritten. It now reports the actual in-bag temperatures, the pressure effect estimate, the absence of a statistically detectable nominal chamber-condition effect, the scope of the bulk chemistry data and the limited role of the verification trial.

Changes in Manuscript: Abstract fully rewritten.

### R2.3 Chamber characteristics

Reviewer Comment: Chamber model, air circulation, fan power, chamber volume and pallet occupancy should be provided.

Response: We searched the repository and available notes. These details were not recorded in the available experimental record. We have not invented specifications. Instead, we now state that these chamber characteristics are unavailable and that this limits the diagnosis of the thermal lag and vertical gradient observed in the main trial.

Changes in Manuscript: Added this limitation in Materials and Methods and Section 3.4.

### R2.4 Small sample size and ANOVA power

Reviewer Comment: The pressure ANOVA has very limited power because n is small and one bottom sensor is missing.

Response: We agree. The revised manuscript now states the pressure cell sizes (n = 3, 3, 3 and 2), the missing sensor, the unbalanced design and the limited power. We retained the two-way ANOVA because it is the analysis used for the embedded pressure summaries, but interpret it as an exploratory sensor-level analysis and report effect estimates and confidence intervals alongside p-values. Because stack identifiers are not retained in the embedded summary table, the p-values are not presented as definitive stack-level tests.

Changes in Manuscript: Sections 2.2, 2.4, 3.2, 3.4 and Conclusions revised. `anova_pressure.py` was updated and `analysis_verification.md` added.

### R2.5 Verification trial n=1 stack

Reviewer Comment: The verification trial cannot confirm general conclusions because it used only one stack and one sensor failed.

Response: We agree. All confirmatory language has been removed. The verification trial is now described as a limited supporting observation under one three-box-stack configuration. The manuscript explicitly states that it cannot establish a general position effect.

Changes in Manuscript: Sections 2.3, 3.3, 3.4 and Conclusions revised.

### R2.6 Physical-vs-chemical binary conclusion

Reviewer Comment: The claim that palletisation governs physical behaviour and temperature governs chemical stability is overreaching because chemistry was not position-resolved.

Response: We agree. The revised manuscript no longer presents this binary causal attribution. It now states that pressure was position-resolved and showed a transient bottom-position peak, whereas chemistry was measured as bulk wine grouped by nominal chamber condition and cannot be linked directly to stack position.

Changes in Manuscript: Abstract, Section 3.2, Limitations and Conclusions revised.

### R2.7 Lactic acid interpretation

Reviewer Comment: The lactic-acid increase cannot be confidently attributed to heat-driven chemistry rather than malolactic fermentation without microbiological data.

Response: We agree. The manuscript no longer states that malolactic fermentation was ruled out. During revision we also found that the available files contained inconsistent standard deviations for lactic acid in the nominal 50 degC chamber (0.02 versus 0.20 g/L), while the raw chemical replicates were not available. We therefore revised Table 2 conservatively to use 0.29 +/- 0.20 g/L, assigned the same significance letter to both lactic-acid means, and now treat lactic acid descriptively rather than as an independently verified significant difference. We retained the observation that malic acid did not decrease significantly, but we now state that no microbiological analyses, viable cell counts or method-sensitivity study were available and that residual microbial activity cannot be excluded.

Changes in Manuscript: Sections 2.4 and 3.1, Table 2 and Limitations revised.

### R2.8 Table 2 labels

Reviewer Comment: "Wine at 19 degC" and "Wine at 50 degC" are misleading.

Response: Corrected. The row labels now read "Wine from nominal 19 degC chamber" and "Wine from nominal 50 degC chamber." The caption and table note clarify that these labels are chamber set points, not actual wine temperatures.

Changes in Manuscript: Table 2 labels, caption and note revised.

### R2.9 First five hours excluded

Reviewer Comment: The first five hours may represent realistic transport disturbances and should be discussed or tested by sensitivity analysis.

Response: We agree that these early transients may be relevant to some logistics scenarios. The revised manuscript explains why the interval was excluded from the primary storage analysis: it contained transport from the filling line, filling/sealing and stack assembly, and was sampled only every 30 minutes. A full-record sensitivity analysis could not be recomputed from the repository because the raw logger export is absent. We now state this limitation explicitly rather than implying that the exclusion is consequence-free.

Changes in Manuscript: Section 3.2 and Limitations revised; `analysis_verification.md` documents the missing raw-data constraint.

### R2.10 Wine identity

Reviewer Comment: Grape variety and vintage are unknown.

Response: Correct. The supplier did not provide grape variety or vintage information. We have retained this statement and list it as a limitation.

Changes in Manuscript: Materials and Methods and Limitations revised.

## Reviewer 3

### R3.1 Stacking configuration and interpretability

Reviewer Comment: It is difficult to evaluate stacking configuration because different configurations and temperatures may be confounded or averaged.

Response: We appreciate this point. The revised manuscript clarifies that the pressure analysis tested top versus bottom package position under the tested stack configuration. Stack height was not analysed as an independent factor because only one four-box stack and two three-box stacks were present per chamber. We also state that chamber condition is unreplicated at chamber level, and that the pressure ANOVA is an exploratory sensor-level analysis rather than a definitive paired stack-level test.

Changes in Manuscript: Figure 2 caption, Table 1 note, Sections 2.2, 2.4, 3.4 and Conclusions revised.

### R3.2 SO2 reduction and post-transport shelf life

Reviewer Comment: Could SO2 loss affect shelf life and storage after transport?

Response: We now discuss this conservatively. The wine from the nominally warmer chamber had lower total and free SO2 values after 20 days than the reference-chamber wine. This may indicate a lower antioxidant and antimicrobial reserve available after transport, but actual shelf life, sensory quality and microbial stability after transport were not measured. We therefore present post-transport storage impact as a potential implication, not a measured outcome.

Changes in Manuscript: Section 3.1, Limitations and Conclusions revised.

### R3.3 Economic feasibility of pressure sensors

Reviewer Comment: The feasibility of using pressure sensors at scale is unclear.

Response: We agree that the original recommendation was too broad. The revised manuscript does not recommend instrumenting every commercial BiB. It now frames sensor use as selected sentinel packages, validation deployments or quality-control monitoring. We also state that no techno-economic analysis was performed.

Changes in Manuscript: Limitations and Conclusions revised.

### R3.4 Thermal behaviour under nominal 19 degC and 50 degC conditions

Reviewer Comment: The nominal 50 degC packages stayed below set point, whereas the nominal 19 degC packages reached about 23 degC; this different behaviour needs explanation.

Response: We now quantify both observations and distinguish facts from hypotheses. The manuscript states that the nominal 19 degC packages stabilised around 23 degC and the nominal 50 degC packages stabilised at about 34 degC top and 26 degC bottom. Thermal inertia, chamber loading, limited heat transfer and airflow constraints are described as plausible explanations only, because chamber specifications and airflow data were not recorded.

Changes in Manuscript: Sections 3.2, 3.3 and Limitations revised.

### R3.5 Main experiment versus verification experiment discrepancy

Reviewer Comment: The large difference between the main and verification experiment may indicate an error or scale effect.

Response: We do not dismiss this discrepancy. The revised manuscript states that the verification stack approached 47 degC, whereas the main-trial nominal 50 degC chamber reached only about 25-34 degC in the packages. The difference is treated as consistent with chamber performance, loading, airflow or scale effects, but the available records do not identify a single cause.

Changes in Manuscript: Sections 3.2, 3.3 and Limitations revised.

### R3.6 English readability

Reviewer Comment: Several sentences are overly complex.

Response: The manuscript has been edited throughout for shorter and more precise scientific prose. The Abstract, Introduction, Methods, Results, Limitations and Conclusions were substantially rewritten.

Changes in Manuscript: Whole manuscript language edit.
