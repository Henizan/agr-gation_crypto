import pandas as pd
from pathlib import Path

DATA_DIR = Path("C:/ece_B3/projet_agr_crypto/data")

files = ["BTCUSD_1d_Binance.csv", "ETHUSD_1d_Binance.csv", "XRPUSD_1d_Binance.csv"]
merged_list = []

for file in files:
    print(f"📄 Traitement de {file}...")
    df = pd.read_csv(DATA_DIR / file)

    df["Crypto"] = file.split("USD")[0]

    df = df[["Open", "High", "Low", "Close", "Volume", "Open time", "Close time", "Crypto"]]

    df = df.rename(columns={
        "Open": "Open",
        "High": "High",
        "Low": "Low",
        "Close": "Close",
        "Volume": "Volume",
        "Open time": "Open Time",
        "Close time": "Close Time",
        "Crypto": "Crypto"
    })

    df["Open Time"] = pd.to_datetime(df["Open Time"]).dt.strftime("%Y-%m-%d %H:%M:%S")
    df["Close Time"] = pd.to_datetime(df["Close Time"]).dt.strftime("%Y-%m-%d %H:%M:%S")

    merged_list.append(df)

merged = pd.concat(merged_list, ignore_index=True)

merged.to_csv(DATA_DIR / "kaggle_data.csv", index=False)
