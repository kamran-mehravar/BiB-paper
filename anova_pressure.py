#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two-way analysis of variance on the internal pressure of palletised Bag-in-Box units.

Supporting code for:
    "Effect of Palletisation and Temperature on Bag-in-Box Wine Packaging under
     Simulated Export Conditions" (manuscript foods-4411772)

This script reproduces every statistic reported in Sections 2.4 and 3.2 of the paper:

    peak DP (fourth day of testing)   position  F(1,8) = 9.14   p = 0.017
                                      chamber   F(1,8) = 0.21   p = 0.66
                                      interaction              p = 0.56
    DP on the twentieth day           position  F(1,8) = 0.35   p = 0.57
                                      chamber   F(1,8) = 0.81   p = 0.39

Model (Eq. 1 in the paper), fitted for each response separately:

    y_ijk = mu + alpha_i + beta_j + (alpha*beta)_ij + eps_ijk

    y_ijk  summary value of the DP curve of one sensor (peak, or day-20 residual)
    alpha_i  effect of stack position i   (Top / Bottom)
    beta_j   effect of chamber j          (19 degC / 50 degC)
    eps_ijk  residual, assumed N(0, sigma^2)

Each factor is tested with F = MS_factor / MS_error (Eq. 2). The design is unbalanced
(one bottom sensor at 19 degC returned no record, leaving cells of 3, 3, 3 and 2 units),
so sums of squares are computed by the Type II method, in which each factor is adjusted
for the other -- the recommended choice for unbalanced data when the interaction is not
significant (Langsrud, Stat. Comput. 2003, 13, 163-167).

USAGE
    python3 anova_pressure.py                 # uses the embedded summary values
    python3 anova_pressure.py --from-raw      # re-derives them from 'Results - Compare.csv'

The --from-raw path shows exactly how each summary value was extracted from the logger
export, so the whole chain from raw record to reported F ratio can be checked.

REQUIREMENTS
    python >= 3.8, pandas, numpy, statsmodels   (pip install pandas numpy statsmodels)

DATA
    'Results - Compare.csv' -- the export of the main trial: 979 records at 30-minute
    intervals spanning 489 h (20.4 days), 11 sensors, each contributing a temperature
    and a pressure column. Column indices are given in SENSORS below.

Author: K. Mehravar.  Licence: CC BY 4.0, as for the article.
"""

import argparse
import sys

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------------------
# Sensor map of 'Results - Compare.csv'.
# Column 0 = Time (Days), column 1 = Time (h); every sensor then contributes a
# (temperature, pressure) pair of columns, in the order the file stores them.
# --------------------------------------------------------------------------------------
SENSORS = [
    # id     position   chamber  T_col  P_col
    ("V50",  "Top",     "50",     2,     3),
    ("V53",  "Top",     "50",     4,     5),
    ("V71",  "Top",     "50",     6,     7),
    ("V51",  "Bottom",  "19",     8,     9),
    ("V59",  "Bottom",  "19",    10,    11),
    ("V52",  "Bottom",  "50",    12,    13),
    ("V56",  "Bottom",  "50",    14,    15),
    ("V70",  "Bottom",  "50",    16,    17),
    ("V55",  "Top",     "19",    18,    19),
    ("V57",  "Top",     "19",    20,    21),
    ("V58",  "Top",     "19",    22,    23),
]

CSV_PATH = "Results - Compare.csv"

BASELINE_END_D = 0.02   # baseline = median pressure over the first 30 min
HANDLING_END_D = 0.21   # first ~5 h = transport of the units + assembly into stacks
STORAGE_END_D = 20.0    # end of the 20-day storage window
DAY20_START_D = 19.5    # residual DP = mean over the last 12 h

# --------------------------------------------------------------------------------------
# Summary values used in the paper (mbar), as produced by extract_summary() below.
# Embedded so that the ANOVA can be re-run without the raw export.
# --------------------------------------------------------------------------------------
EMBEDDED = pd.DataFrame(
    [
        # sensor  position  chamber   peak_dP   dP_day20
        ("V50",   "Top",    "50",     63.4638,  33.5127),
        ("V53",   "Top",    "50",     58.3335,  32.5126),
        ("V71",   "Top",    "50",     77.9051,  60.2513),
        ("V52",   "Bottom", "50",     92.1697,  55.9552),
        ("V56",   "Bottom", "50",     63.1891,  17.0045),
        ("V70",   "Bottom", "50",     93.7639,  43.7397),
        ("V55",   "Top",    "19",     56.4339,  36.1306),
        ("V57",   "Top",    "19",     56.9113,  38.1726),
        ("V58",   "Top",    "19",     65.4962,  50.7070),
        ("V51",   "Bottom", "19",     91.0728,  62.5850),
        ("V59",   "Bottom", "19",     78.5783,  52.3243),
    ],
    columns=["sensor", "position", "chamber", "peak_dP", "dP_day20"],
)


def extract_summary(csv_path=CSV_PATH):
    """Derive the per-sensor summary values from the raw logger export.

    For every sensor:
      1. baseline P0 = median pressure over the first 30 minutes;
      2. DP(t) = P(t) - P0, so the comparison rests on the change measured by a single
         device (stability +/-1 mbar/yr) rather than on agreement between devices, whose
         absolute accuracy is +/-1.5 mbar only at 20 degC between 300 and 1100 mbar;
      3. peak DP  = maximum of DP after the handling transient and within 20 days;
      4. day-20 DP = mean of DP over the last 12 hours of the window.
    """
    df = pd.read_csv(csv_path, decimal=",")
    t = pd.to_numeric(df.iloc[:, 0], errors="coerce")
    valid = t.notna()
    t = t[valid].values
    window = t <= STORAGE_END_D
    t = t[window]

    rows = []
    for sid, position, chamber, _t_col, p_col in SENSORS:
        p = pd.to_numeric(df.iloc[:, p_col], errors="coerce")[valid].values[window]
        p0 = np.nanmedian(p[t <= BASELINE_END_D])
        dp = p - p0
        post = t >= HANDLING_END_D                       # exclude transport + stacking
        peak = np.nanmax(np.where(post, dp, -np.inf))
        day20 = np.nanmean(dp[t >= DAY20_START_D])
        rows.append((sid, position, chamber, round(peak, 4), round(day20, 4)))
    return pd.DataFrame(rows, columns=["sensor", "position", "chamber", "peak_dP", "dP_day20"])


def two_way_anova(data, response, label):
    """Fit y ~ position + chamber (Type II SS) and report it; also test the interaction."""
    import statsmodels.api as sm
    import statsmodels.formula.api as smf

    print("=" * 78)
    print(label)
    print("=" * 78)

    cells = data.groupby(["chamber", "position"])[response].agg(["mean", "std", "count"])
    print("\ncell means (mbar):\n")
    print(cells.round(1).to_string())

    additive = smf.ols("%s ~ C(position) + C(chamber)" % response, data=data).fit()
    table = sm.stats.anova_lm(additive, typ=2)
    print("\ntwo-way ANOVA, Type II sums of squares (additive model):\n")
    print(table.round(4).to_string())

    for factor, name in [("C(position)", "position"), ("C(chamber)", "chamber")]:
        ss = table.loc[factor, "sum_sq"]
        df_num = int(table.loc[factor, "df"])
        df_den = int(table.loc["Residual", "df"])
        print("\n  %-9s SS = %7.1f mbar^2   F(%d,%d) = %.2f   p = %.3f"
              % (name, ss, df_num, df_den, table.loc[factor, "F"], table.loc[factor, "PR(>F)"]))
    print("\n  total SS  = %.1f mbar^2 (residual %.1f)"
          % (table["sum_sq"].sum(), table.loc["Residual", "sum_sq"]))

    full = smf.ols("%s ~ C(position) * C(chamber)" % response, data=data).fit()
    inter = sm.stats.anova_lm(full, typ=2)
    key = "C(position):C(chamber)"
    print("  interaction p = %.3f  (not significant -> the additive model above is reported)"
          % inter.loc[key, "PR(>F)"])

    top = data[data.position == "Top"][response].mean()
    bot = data[data.position == "Bottom"][response].mean()
    print("  bottom - top = %+.1f mbar (pooled over both chambers)\n" % (bot - top))
    return table


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--from-raw", action="store_true",
                    help="re-derive the summary values from '%s' instead of using the "
                         "embedded copy" % CSV_PATH)
    args = ap.parse_args()

    if args.from_raw:
        print("deriving summary values from %r ...\n" % CSV_PATH)
        try:
            data = extract_summary()
        except FileNotFoundError:
            sys.exit("error: %r not found. Run without --from-raw to use the embedded "
                     "values." % CSV_PATH)
        merged = EMBEDDED.merge(data, on=["sensor", "position", "chamber"],
                                suffixes=("_published", "_recomputed"))
        drift = (merged.peak_dP_published - merged.peak_dP_recomputed).abs().max()
        print("largest deviation from the published values: %.4f mbar\n" % drift)
    else:
        data = EMBEDDED.copy()

    print("per-sensor summary (mbar), n = %d sensors\n" % len(data))
    print(data.to_string(index=False))
    print()

    two_way_anova(data, "peak_dP",
                  "RESPONSE 1 -- peak DP, reached on the fourth day of the testing period")
    two_way_anova(data, "dP_day20",
                  "RESPONSE 2 -- residual DP on the twentieth day of testing")

    print("=" * 78)
    print("Note: the two chambers were set to 19 degC and 50 degC, but the wine in the")
    print("hot chamber reached only 25-34 degC (Section 3.2); 'chamber' is therefore the")
    print("nominal factor, not the temperature actually experienced by the wine.")
    print("=" * 78)


if __name__ == "__main__":
    main()
