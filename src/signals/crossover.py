import pandas as pd

def ma_crossover_position(price: pd.Series, fast: int = 50, slow: int = 200) -> pd.Series:
    """
    1 when MA(fast) > MA(slow)
    0 otherwise
    """
    ma_fast = price.rolling(fast).mean()
    ma_slow = price.rolling(slow).mean()
    pos = (ma_fast > ma_slow).astype(int)
    pos.name = f"pos_ma_{fast}_{slow}"
    return pos
