import pandas as pd

def ma_trend_position(price: pd.Series, lookback: int = 200) -> pd.Series:
    """
    Returns a 0/1 position series:
      1 when price > MA(lookback)
      0 otherwise
    """
    ma = price.rolling(lookback).mean()
    pos = (price > ma).astype(int)
    pos.name = f"pos_ma_{lookback}"
    return pos
