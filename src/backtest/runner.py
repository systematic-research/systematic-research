import pandas as pd
from typing import Callable, Dict

from src.backtest.vectorized import long_flat_backtest
from src.performance.metrics import perf_stats, equity_curve

def run_strategy(
    price: pd.Series,
    returns: pd.Series,
    signal_fn: Callable[..., pd.Series],
    signal_kwargs: dict,
    cost_bps: float = 0.0,
    lag: int = 1,
) -> Dict:
    pos = signal_fn(price, **signal_kwargs)
    bt = long_flat_backtest(returns, pos, cost_bps=cost_bps, lag=lag)
    stats = perf_stats(bt["strategy_ret_net"])
    curve = equity_curve(bt["strategy_ret_net"])
    return {"pos": pos, "bt": bt, "stats": stats, "curve": curve}

def compare_strategies(results: Dict[str, Dict]) -> pd.DataFrame:
    rows = []
    for name, r in results.items():
        row = {"name": name, **r["stats"]}
        rows.append(row)
    df = pd.DataFrame(rows).set_index("name")
    return df
