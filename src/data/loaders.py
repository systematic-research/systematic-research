import pandas as pd

def load_sp500_fred_csv(path: str = "data/raw/sp500_fred.csv") -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"], index_col="date")
    df = df.rename(columns={"value": "price"}).dropna()
    df["ret"] = df["price"].pct_change()
    return df
