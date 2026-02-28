import math
import numpy as np
import pandas as pd

def equity_curve(returns: pd.Series) -> pd.Series:
    r = returns.fillna(0.0)
    return (1.0 + r).cumprod()

def drawdown(curve: pd.Series) -> pd.Series:
    peak = curve.cummax()
    return curve / peak - 1.0

def perf_stats(returns: pd.Series, periods_per_year: int = 252) -> dict:
    r = returns.dropna()
    if len(r) == 0:
        return {
            "Obs": 0,
            "Total Return": np.nan,
            "CAGR": np.nan,
            "Vol": np.nan,
            "Sharpe": np.nan,
            "Max Drawdown": np.nan,
        }

    total = float((1.0 + r).prod())
    years = len(r) / periods_per_year
    cagr = total ** (1.0 / years) - 1.0 if years > 0 else np.nan

    vol = float(r.std(ddof=0) * math.sqrt(periods_per_year))
    sharpe = float((r.mean() * periods_per_year) / vol) if vol > 0 else np.nan

    curve = equity_curve(r)
    dd = drawdown(curve)
    max_dd = float(dd.min()) if len(dd) else np.nan

    return {
        "Obs": int(len(r)),
        "Total Return": total - 1.0,
        "CAGR": cagr,
        "Vol": vol,
        "Sharpe": sharpe,
        "Max Drawdown": max_dd,
    }
