#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two-way analysis of variance on the internal pressure of palletised Bag-in-Box units.

Supporting code for the revised manuscript:
    "Palletisation and In-Bag Thermal Exposure in Bag-in-Box Wine Packaging under
     Simulated Export Conditions"

This script reproduces every statistic reported in Sections 2.4 and 3.2 of the paper:

    peak DP (post-handling window)    position  F(1,8) = 9.14   p = 0.017
                                      chamber   F(1,8) = 0.21   p = 0.66
                                      interaction              p = 0.56
    DP on the twentieth day           position  F(1,8) = 0.35   p = 0.57
                                      chamber   F(1,8) = 0.81   p = 0.39

Primary model (Eq. 1 in the paper), fitted for each response separately:

    y_ijk = mu + alpha_i + beta_j + eps_ijk

    y_ijk  summary value of the DP curve of one sensor (peak, or day-20 residual)
    alpha_i  effect of stack position i   (Top / Bottom)
    beta_j   effect of chamber j          (19 degC / 50 degC)
    eps_ijk  residual, assumed N(0, sigma^2)

Each factor is tested with F = MS_factor / MS_error (Eq. 2). The design is unbalanced
(one bottom sensor at 19 degC returned no record, leaving cells of 3, 3, 3 and 2 units),
so sums of squares are computed by the Type II method, in which each factor is adjusted
for the other -- the recommended choice for unbalanced data when the interaction is not
significant (Langsrud, Stat. Comput. 2003, 13, 163-167).

The position-by-chamber interaction is checked separately with the full model. The
repository now contains the main-trial workbook (Results.xlsx), but neither the
workbook nor the embedded summary table preserves stack IDs for the individual sensors.
This script therefore performs the same exploratory sensor-level analysis reported in
the manuscript; it is not a substitute for a blocked or paired stack-level analysis.

USAGE
    python3 anova_pressure.py                 # uses the embedded summary values
    python3 anova_pressure.py --from-raw      # re-derives them from Results.xlsx
    python3 anova_pressure.py --from-raw --raw-path Results.xlsx

The --from-raw path shows exactly how each summary value was extracted from the logger
export, so the whole chain from raw record to reported F ratio can be checked.

REQUIREMENTS
    python >= 3.8, pandas, numpy, openpyxl.
    statsmodels is optional: when installed, it is used for the ANOVA table; otherwise
    the script falls back to explicit least-squares Type II calculations.

DATA
    Results.xlsx, sheet 'Compare' -- the processed main-trial logger workbook: 979
    records at 30-minute intervals spanning 489 h (20.4 days), 11 sensors, each
    contributing a temperature and a pressure column. Column indices are given in
    SENSORS below. A CSV export with the same column order can also be supplied with
    --raw-path, but Results.xlsx is the verified source in this repository.

Author: K. Mehravar.  Licence: CC BY 4.0, as for the article.
"""

import argparse
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------------------
# Sensor map of Results.xlsx / sheet 'Compare'.
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

RAW_PATH = "Results.xlsx"

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


def _read_raw_compare(raw_path):
    """Read the main-trial Compare table from the verified workbook or a CSV export."""
    path = Path(raw_path)
    if path.suffix.lower() in {".xlsx", ".xlsm", ".xls"}:
        return pd.read_excel(path, sheet_name="Compare", engine="openpyxl")
    return pd.read_csv(path, decimal=",")


def extract_summary(raw_path=RAW_PATH):
    """Derive the per-sensor summary values from the raw logger export.

    For every sensor:
      1. baseline P0 = the initial valid pressure reading at time zero;
      2. DP(t) = P(t) - P0, so the comparison rests on the change measured by a single
         device (stability +/-1 mbar/yr) rather than on agreement between devices, whose
         absolute accuracy is +/-1.5 mbar only at 20 degC between 300 and 1100 mbar;
      3. peak DP  = maximum of DP after the handling transient and within 20 days;
      4. day-20 DP = mean of DP over the last 12 hours of the window.
    """
    df = _read_raw_compare(raw_path)
    t = pd.to_numeric(df.iloc[:, 0], errors="coerce")
    valid = t.notna()
    t = t[valid].values
    window = t <= STORAGE_END_D
    t = t[window]

    rows = []
    for sid, position, chamber, _t_col, p_col in SENSORS:
        p = pd.to_numeric(df.iloc[:, p_col], errors="coerce")[valid].values[window]
        p0 = p[np.isfinite(p)][0]
        dp = p - p0
        post = t >= HANDLING_END_D                       # exclude transport + stacking
        peak = np.nanmax(np.where(post, dp, -np.inf))
        day20 = np.nanmean(dp[t >= DAY20_START_D])
        rows.append((sid, position, chamber, round(peak, 4), round(day20, 4)))
    return pd.DataFrame(rows, columns=["sensor", "position", "chamber", "peak_dP", "dP_day20"])


def _fit_lm(data, response, terms):
    """Least-squares fit for the small two-factor models used below."""
    cols = [np.ones(len(data))]
    if "position" in terms:
        cols.append((data["position"].values == "Top").astype(float))
    if "chamber" in terms:
        cols.append((data["chamber"].values == "50").astype(float))
    if "interaction" in terms:
        cols.append(
            ((data["position"].values == "Top") & (data["chamber"].values == "50")).astype(float)
        )
    x = np.column_stack(cols)
    y = data[response].values.astype(float)
    beta = np.linalg.lstsq(x, y, rcond=None)[0]
    residuals = y - x @ beta
    rank = np.linalg.matrix_rank(x)
    sse = float(residuals @ residuals)
    return {"beta": beta, "x": x, "residuals": residuals, "sse": sse, "df": len(y) - rank}


def _f_survival(f_value, df_num, df_den):
    """Survival function for F(df_num, df_den), avoiding a hard SciPy dependency."""
    if not np.isfinite(f_value) or f_value <= 0:
        return 1.0
    a = df_num / 2.0
    b = df_den / 2.0
    log_beta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    scale = df_num / df_den

    def pdf(x):
        if x <= 0:
            return 0.0
        return math.exp(
            a * math.log(scale)
            + (a - 1.0) * math.log(x)
            - (a + b) * math.log1p(scale * x)
            - log_beta
        )

    def simpson(fun, left, right):
        mid = (left + right) / 2.0
        return (right - left) * (fun(left) + 4.0 * fun(mid) + fun(right)) / 6.0

    def adaptive(fun, left, right, eps, whole, depth):
        mid = (left + right) / 2.0
        left_area = simpson(fun, left, mid)
        right_area = simpson(fun, mid, right)
        if depth <= 0 or abs(left_area + right_area - whole) <= 15.0 * eps:
            return left_area + right_area + (left_area + right_area - whole) / 15.0
        return adaptive(fun, left, mid, eps / 2.0, left_area, depth - 1) + adaptive(
            fun, mid, right, eps / 2.0, right_area, depth - 1
        )

    cdf = adaptive(pdf, 0.0, float(f_value), 1e-10, simpson(pdf, 0.0, float(f_value)), 30)
    return max(0.0, min(1.0, 1.0 - cdf))


def _type2_anova(data, response):
    """Compute Type II tests for the additive two-factor model."""
    additive = _fit_lm(data, response, ["position", "chamber"])
    no_position = _fit_lm(data, response, ["chamber"])
    no_chamber = _fit_lm(data, response, ["position"])
    full = _fit_lm(data, response, ["position", "chamber", "interaction"])
    mse = additive["sse"] / additive["df"]

    rows = []
    for label, reduced in [("C(position)", no_position), ("C(chamber)", no_chamber)]:
        ss = reduced["sse"] - additive["sse"]
        f_value = ss / mse
        rows.append((label, ss, 1, f_value, _f_survival(f_value, 1, additive["df"])))
    rows.append(("Residual", additive["sse"], additive["df"], np.nan, np.nan))
    table = pd.DataFrame(rows, columns=["factor", "sum_sq", "df", "F", "PR(>F)"]).set_index("factor")

    ss_interaction = additive["sse"] - full["sse"]
    mse_full = full["sse"] / full["df"]
    f_interaction = ss_interaction / mse_full
    p_interaction = _f_survival(f_interaction, 1, full["df"])
    return table, additive, p_interaction


def _t975(df):
    """Two-sided 95% t critical values for the small residual dfs used here."""
    table = {
        1: 12.7062,
        2: 4.3027,
        3: 3.1824,
        4: 2.7764,
        5: 2.5706,
        6: 2.4469,
        7: 2.3646,
        8: 2.3060,
        9: 2.2622,
        10: 2.2281,
        11: 2.2010,
        12: 2.1788,
        13: 2.1604,
        14: 2.1448,
        15: 2.1314,
        16: 2.1199,
        17: 2.1098,
        18: 2.1009,
        19: 2.0930,
        20: 2.0860,
    }
    return table.get(int(df), 1.96)


def _adjusted_contrasts(data, response):
    """Model-adjusted contrasts from y ~ position + chamber."""
    fit = _fit_lm(data, response, ["position", "chamber"])
    xtx_inv = np.linalg.inv(fit["x"].T @ fit["x"])
    mse = fit["sse"] / fit["df"]
    tcrit = _t975(fit["df"])
    contrasts = [
        ("bottom - top", np.array([0.0, -1.0, 0.0])),
        ("nominal 50 - 19 degC", np.array([0.0, 0.0, 1.0])),
    ]
    rows = []
    for label, c in contrasts:
        estimate = float(c @ fit["beta"])
        se = math.sqrt(float(mse * c @ xtx_inv @ c))
        rows.append((label, estimate, estimate - tcrit * se, estimate + tcrit * se))
    return rows


def two_way_anova(data, response, label):
    """Fit y ~ position + chamber (Type II SS) and report it; also test the interaction."""

    print("=" * 78)
    print(label)
    print("=" * 78)

    cells = data.groupby(["chamber", "position"])[response].agg(["mean", "std", "count"])
    print("\ncell means (mbar):\n")
    print(cells.round(1).to_string())

    try:
        import statsmodels.api as sm
        import statsmodels.formula.api as smf

        additive = smf.ols("%s ~ C(position) + C(chamber)" % response, data=data).fit()
        table = sm.stats.anova_lm(additive, typ=2)
        full = smf.ols("%s ~ C(position) * C(chamber)" % response, data=data).fit()
        inter = sm.stats.anova_lm(full, typ=2)
        interaction_p = inter.loc["C(position):C(chamber)", "PR(>F)"]
    except ModuleNotFoundError:
        print("\n(statsmodels not installed; using explicit least-squares Type II calculations)\n")
        table, additive, interaction_p = _type2_anova(data, response)

    print("\ntwo-way ANOVA, Type II sums of squares (additive model):\n")
    print(table.round(4).to_string())

    for factor, name in [("C(position)", "position"), ("C(chamber)", "chamber")]:
        ss = table.loc[factor, "sum_sq"]
        df_num = int(table.loc[factor, "df"])
        df_den = int(table.loc["Residual", "df"])
        print("\n  %-9s SS = %7.1f mbar^2   F(%d,%d) = %.2f   p = %.3f"
              % (name, ss, df_num, df_den, table.loc[factor, "F"], table.loc[factor, "PR(>F)"]))
    corrected_total_ss = float(((data[response] - data[response].mean()) ** 2).sum())
    print("\n  corrected total SS = %.1f mbar^2 (residual %.1f)"
          % (corrected_total_ss, table.loc["Residual", "sum_sq"]))

    print("  interaction p = %.3f  (not significant -> the additive model above is reported)"
          % interaction_p)

    print("\n  adjusted effects from the additive model:")
    for effect, estimate, lower, upper in _adjusted_contrasts(data, response):
        print("    %-22s %+.1f mbar   95%% CI %+.1f to %+.1f"
              % (effect, estimate, lower, upper))
    print()
    return table


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--from-raw", action="store_true",
                    help="re-derive the summary values from the main-trial workbook or "
                         "CSV export instead of using the embedded copy")
    ap.add_argument("--raw-path", default=RAW_PATH,
                    help="main-trial workbook or CSV export to use with --from-raw "
                         "(default: %(default)s)")
    args = ap.parse_args()

    if args.from_raw:
        print("deriving summary values from %r ...\n" % args.raw_path)
        try:
            data = extract_summary(args.raw_path)
        except FileNotFoundError:
            sys.exit("error: %r not found. Run without --from-raw to use the embedded "
                     "values." % args.raw_path)
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
                  "RESPONSE 1 -- peak DP in the post-handling storage window")
    two_way_anova(data, "dP_day20",
                  "RESPONSE 2 -- residual DP on the twentieth day of testing")

    print("=" * 78)
    print("Note: the two chambers were set to 19 degC and 50 degC, but the wine in the")
    print("hot chamber reached about 26.1 degC at bottom sensors and 34.2 degC at top")
    print("sensors late in storage (Section 3.2); 'chamber' is therefore the nominal")
    print("factor, not the temperature actually experienced by the wine.")
    print("=" * 78)


if __name__ == "__main__":
    main()
