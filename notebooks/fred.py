import requests
import pandas as pd

class FredClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.stlouisfed.org/fred/series/observations"

    def get_series(self, series_id):
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json"
        }

        r = requests.get(self.base_url, params=params)
        data = r.json()["observations"]

        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["date"])
        df["value"] = pd.to_numeric(df["value"], errors="coerce")

        return df[["date", "value"]].set_index("date")
