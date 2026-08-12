# Clarity Compression Audit

## Word/Phrase Counts

Counts refer to the manuscript body from Abstract through Conclusions, excluding references.

| Metric | Before | After | Change |
|---|---:|---:|---:|
| Body word count | 6030 | 4371 | -1659 words (-27.5%) |
| "nominal" count | 79 | 0 | -79 |
| Highlighted text runs | 94 | 59 | -35 runs (-37.2%) |
| Sentences over 35 words | 19 | 0 | -19 |

## Main Edits

- Abstract: rewritten into a shorter finding-first structure. It now defines C19 and C50 as chamber set-point labels and reports the main temperature, pressure and chemistry findings without burying them under repeated caveats.
- Methods condition labels: replaced "Condition 1/Condition 2" and repeated "nominal" phrasing with C19 and C50. These are explicitly defined as chamber set-point labels, not measured wine temperatures.
- Results caveat consolidation: removed repeated caveat blocks from Results where the same limitation is now handled in Section 3.4. Results paragraphs now open with the measured pattern or number.
- Captions: shortened Figures 3-7 captions and Table 2 caption. Captions now state what is plotted and the critical set-point-versus-measured-temperature distinction without repeating the full interpretation.
- Conclusions: compressed repeated reviewer-response language while retaining the measured in-bag temperature mismatch, exploratory pressure interpretation, chemistry caution and sentinel-monitoring implication.
- Editorial residue removed: manuscript-level discussion of the historical pressure-threshold implementation, the `0.020833 d` record interval, duplicated early workbook rows and the untraceable alternative lactic-acid SD was removed or moved into simpler limitation wording.
- Citation order: checked after compression and repaired by renumbering existing references so first citation order is contiguous.
- Results order: the Results sections were not reordered. The DOCX figure/table layout places Figures 3-5 and Table 2 in a fixed Word sequence; reordering section blocks would risk layout and cross-reference breakage. Instead, forward-reference clutter was reduced and the physical/chemical distinctions were compressed.

## Not Changed

- No numerical results were changed.
- Pressure ANOVA values were not changed.
- Common-mode audit values were not changed.
- Leave-one-out pressure results were not changed.
- Table 2 chemistry was not downgraded.
- Author-approved Table 2 statistical markers were retained.
- Lactic acid remains `0.29 ± 0.02 g/L`.
- Lactic acid remains descriptive and malolactic fermentation is not ruled out.
- The pressure/common-mode correction and exploratory interpretation were retained.
- The title remains `In-Bag Pressure and Temperature Monitoring of Palletised 3-L Bag-in-Box Wine under Static Chamber Conditions`.

## Remaining Risks

- Pressure inference remains exploratory because the design has small sensor-level n, one missing bottom sensor, no retained stack pairings and one chamber per set point.
- External barometric correction remains unavailable because main-trial absolute dates were not recovered.
- Reviewers may still ask for raw chemistry-replicate provenance, although the author-approved Table 2 presentation is retained.
- No chamber-air logger was recorded, so chamber under-delivery, stratification and heat-transfer limitation cannot be separated mechanistically.
