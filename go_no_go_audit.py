#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scientific go/no-go audit helpers for the BiB resubmission package.

The script reads only the original study workbooks through ``reanalyse_raw_data``
and writes derived diagnostics used to audit pressure common-mode behaviour,
leave-one-out robustness, and the verification-trial thermal response.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd

import reanalyse_raw_data as rr


OUT = Path(".")


def _main_delta_series() -> pd.DataFrame:
    """Return sensor-level main-trial pressure traces as baseline-referred dP."""
    raw = rr.load_main_trial()
    series = rr.main_series(raw)
    rows: list[pd.DataFrame] = []
    for (sensor, position, chamber), group in series.groupby(
        ["sensor", "position", "chamber"], sort=False
    ):
        group = group.sort_values("time_days").copy()
        group = group[group["time_days"].le(rr.MAIN_STORAGE_END_D)]
        pressure = group["pressure_mbar"].astype(float)
        first_valid = pressure[np.isfinite(pressure)].iloc[0]
        group["dP_mbar"] = pressure - first_valid
        group["baseline_mbar"] = float(first_valid)
        rows.append(group)
    return pd.concat(rows, ignore_index=True)


def pressure_common_mode() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    dps = _main_delta_series()
    wide = dps.pivot_table(index="time_days", columns="sensor", values="dP_mbar", aggfunc="mean")
    common = wide.mean(axis=1)
    leave_one_common = pd.DataFrame(index=wide.index)
    for sensor in wide.columns:
        leave_one_common[sensor] = wide.drop(columns=[sensor]).mean(axis=1)

    corr_rows = []
    meta = dps[["sensor", "position", "chamber"]].drop_duplicates().set_index("sensor")
    for sensor in wide.columns:
        corr_rows.append(
            {
                "sensor": sensor,
                "position": meta.loc[sensor, "position"],
                "nominal_chamber_degC": meta.loc[sensor, "chamber"],
                "leave_one_common_mode_corr": wide[sensor].corr(leave_one_common[sensor]),
            }
        )
    correlations = pd.DataFrame(corr_rows)

    merged = dps.join(common.rename("global_common_mode_mbar"), on="time_days")
    merged["common_mode_residual_mbar"] = merged["dP_mbar"] - merged["global_common_mode_mbar"]

    position_trace = (
        merged.groupby(["time_days", "chamber", "position"], as_index=False)["dP_mbar"]
        .mean()
        .pivot_table(index=["time_days", "chamber"], columns="position", values="dP_mbar")
        .reset_index()
    )
    position_trace["bottom_minus_top_mbar"] = position_trace.get("Bottom") - position_trace.get("Top")

    summary_rows = []
    for (sensor, position, chamber), group in merged.groupby(["sensor", "position", "chamber"], sort=False):
        post = group[group["time_days"].ge(rr.HANDLING_END_D)]
        day20 = group[group["time_days"].ge(rr.DAY20_START_D)]
        original_peak = post.loc[post["dP_mbar"].idxmax()]
        resid_peak = post.loc[post["common_mode_residual_mbar"].idxmax()]
        summary_rows.append(
            {
                "sensor": sensor,
                "position": position,
                "chamber": chamber,
                "peak_dP_mbar": float(original_peak["dP_mbar"]),
                "peak_day": float(original_peak["time_days"]),
                "residual_at_original_peak_mbar": float(original_peak["common_mode_residual_mbar"]),
                "peak_common_residual_mbar": float(resid_peak["common_mode_residual_mbar"]),
                "peak_common_residual_day": float(resid_peak["time_days"]),
                "day20_dP_mbar": float(day20["dP_mbar"].mean()),
                "day20_common_residual_mbar": float(day20["common_mode_residual_mbar"].mean()),
            }
        )
    summary = pd.DataFrame(summary_rows)
    return correlations, position_trace, summary


def leave_one_out(summary: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for sensor in summary["sensor"]:
        subset = summary[summary["sensor"] != sensor].copy()
        anova, contrasts = rr.type2_anova(subset.rename(columns={"peak_dP_mbar": "response"}), "response")
        pos = anova[anova["factor"] == "position"].iloc[0]
        contrast = contrasts[contrasts["contrast"] == "bottom_minus_top"].iloc[0]
        removed = summary[summary["sensor"] == sensor].iloc[0]
        rows.append(
            {
                "removed_sensor": sensor,
                "removed_position": removed["position"],
                "removed_chamber": removed["chamber"],
                "n_remaining": len(subset),
                "position_F": pos["F"],
                "position_p": pos["p"],
                "bottom_minus_top_estimate_mbar": contrast["estimate_mbar"],
                "ci95_low_mbar": contrast["ci95_low_mbar"],
                "ci95_high_mbar": contrast["ci95_high_mbar"],
            }
        )
    return pd.DataFrame(rows)


def verification_thermal_response() -> pd.DataFrame:
    df = rr.load_verification_compare()
    rows = []
    for sensor, position, temp_col, _pressure_col in rr.VERIFICATION_SENSORS:
        trace = df[["Time(days)", temp_col]].dropna()
        trace = trace[trace["Time(days)"].le(15.0)].copy()
        t = trace["Time(days)"].astype(float)
        temp = trace[temp_col].astype(float)
        if sensor == "V26":
            plateau_window = trace[trace["Time(days)"].ge(max(0.0, float(t.max()) - 0.25))]
        else:
            plateau_window = trace[trace["Time(days)"].between(14.0, 15.0)]
        plateau = float(plateau_window[temp_col].mean())
        t0 = float(t.iloc[0])
        temp0 = float(temp.iloc[0])
        delta = plateau - temp0
        t90 = np.nan
        t95 = np.nan
        within_1c_day = np.nan
        if delta > 0:
            target90 = temp0 + 0.90 * delta
            target95 = temp0 + 0.95 * delta
            hit90 = trace[temp.ge(target90)]
            hit95 = trace[temp.ge(target95)]
            within = trace[(plateau - temp).abs().le(1.0)]
            if not hit90.empty:
                t90 = float(hit90["Time(days)"].iloc[0] - t0)
            if not hit95.empty:
                t95 = float(hit95["Time(days)"].iloc[0] - t0)
            if not within.empty:
                within_1c_day = float(within["Time(days)"].iloc[0] - t0)
        rows.append(
            {
                "sensor": sensor,
                "position": position,
                "first_day": t0,
                "last_day": float(t.iloc[-1]),
                "initial_temp_degC": temp0,
                "max_temp_degC": float(temp.max()),
                "plateau_estimate_degC": plateau,
                "time_to_90_percent_plateau_days": t90,
                "time_to_95_percent_plateau_days": t95,
                "first_time_within_1C_of_plateau_days": within_1c_day,
                "tau_from_t90_days": t90 / math.log(10.0) if np.isfinite(t90) else np.nan,
                "tau_from_t95_days": t95 / math.log(20.0) if np.isfinite(t95) else np.nan,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    correlations, position_trace, residual_summary = pressure_common_mode()
    loo = leave_one_out(residual_summary)
    anova_common_peak, common_peak_contrasts = rr.type2_anova(
        residual_summary.rename(columns={"peak_common_residual_mbar": "response"}), "response"
    )
    anova_resid_at_peak, resid_peak_contrasts = rr.type2_anova(
        residual_summary.rename(columns={"residual_at_original_peak_mbar": "response"}), "response"
    )
    thermal = verification_thermal_response()

    correlations.to_csv(OUT / "pressure_common_mode_correlations.csv", index=False)
    position_trace.to_csv(OUT / "pressure_position_difference_trace.csv", index=False)
    residual_summary.to_csv(OUT / "pressure_common_mode_residual_summary.csv", index=False)
    loo.to_csv(OUT / "pressure_leave_one_out.csv", index=False)
    anova_common_peak.to_csv(OUT / "pressure_common_mode_peak_anova.csv", index=False)
    common_peak_contrasts.to_csv(OUT / "pressure_common_mode_peak_contrasts.csv", index=False)
    anova_resid_at_peak.to_csv(OUT / "pressure_residual_at_original_peak_anova.csv", index=False)
    resid_peak_contrasts.to_csv(OUT / "pressure_residual_at_original_peak_contrasts.csv", index=False)
    thermal.to_csv(OUT / "verification_thermal_response.csv", index=False)

    print("Common-mode correlations")
    print(correlations.to_string(index=False, float_format=lambda x: f"{x:.4f}"))
    print("\nCommon-mode residual peak ANOVA")
    print(anova_common_peak.to_string(index=False, float_format=lambda x: f"{x:.4f}"))
    print("\nResidual at original peak ANOVA")
    print(anova_resid_at_peak.to_string(index=False, float_format=lambda x: f"{x:.4f}"))
    print("\nLeave-one-out peak position effect")
    print(loo.to_string(index=False, float_format=lambda x: f"{x:.4f}"))
    print("\nVerification thermal response")
    print(thermal.to_string(index=False, float_format=lambda x: f"{x:.4f}"))


if __name__ == "__main__":
    main()
