import pandas as pd

def long_flat_backtest(
    returns: pd.Series,
    position: pd.Series,
    cost_bps: float = 0.0,
    lag: int = 1,
) -> pd.DataFrame:
    """
    Vectorized backtest:
    - 'position' is 0/1 (flat/long)
    - position is lagged by `lag` to avoid look-ahead
    - transaction cost applied on position changes: abs(diff(pos_lag)) * cost
    """
    df = pd.DataFrame({"ret": returns, "pos": position}).copy()
    df["pos_lag"] = df["pos"].shift(lag).fillna(0)

    df["turnover"] = df["pos_lag"].diff().abs().fillna(0)  # 1 on enter/exit
    df["cost"] = df["turnover"] * (cost_bps / 10000.0)

    df["strategy_ret_gross"] = df["pos_lag"] * df["ret"]
    df["strategy_ret_net"] = df["strategy_ret_gross"] - df["cost"]

    return df
