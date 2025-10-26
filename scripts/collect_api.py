import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

API_KEY = "CG-1Cf6z9WxxhNrx5Xby1YtpKhM"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": API_KEY
}

def get_market_chart_segment(coin_id, vs_currency, start, end):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency={vs_currency}&days=90"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    data = r.json()

    prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    volumes = pd.DataFrame(data["total_volumes"], columns=["timestamp", "volume"])
    prices["timestamp"] = pd.to_datetime(prices["timestamp"], unit="ms", utc=True)
    volumes["timestamp"] = pd.to_datetime(volumes["timestamp"], unit="ms", utc=True)

    df = prices.resample("1D", on="timestamp").agg(
        {"price": ["first", "max", "min", "last"]}
    )
    df.columns = ["Open", "High", "Low", "Close"]
    df["Volume"] = volumes.resample("1D", on="timestamp")["volume"].sum()
    df["Open Time"] = df.index
    df["Close Time"] = df["Open Time"].shift(-1)
    df.reset_index(drop=True, inplace=True)
    return df

def get_full_history(coin_id, symbol):
    """Récupère uniquement les 90 derniers jours"""
    print(f"Récupération des 90 derniers jours pour {symbol}")
    df = get_market_chart_segment(coin_id, "usd", None, None)
    df["Crypto"] = symbol
    return df

cryptos = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "ripple": "XRP"
}

frames = []
for cid, sym in cryptos.items():
    frames.append(get_full_history(cid, sym))

final = pd.concat(frames)
final.to_csv("data/coingecko_90d.csv", index=False)