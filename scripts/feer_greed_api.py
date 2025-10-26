import requests
import pandas as pd
from datetime import datetime

def scrape_fear_greed_full():
    url = "https://api.alternative.me/fng/?limit=0"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()["data"]

    df = pd.DataFrame([{
        "date": datetime.fromtimestamp(int(d["timestamp"])),
        "value": int(d["value"]),
        "classification": d["value_classification"]
    } for d in data])

    df.sort_values("date", inplace=True)
    df.reset_index(drop=True, inplace=True)

    df.to_csv("data/fear_greed.csv", index=False)
    return df

if __name__ == "__main__":
    try:
        scrape_fear_greed_full()
    except Exception as e:
        print(f"⚠️ Erreur durant la récupération : {e}")
