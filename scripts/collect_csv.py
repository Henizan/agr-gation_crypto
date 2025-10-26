import pandas as pd
from pathlib import Path

# Charge les fichiers Binance
files = ["BTCUSD_1d_Binance.csv", "ETHUSD_1d_Binance.csv", "XRPUSD_1d_Binance.csv"]
merged_list = []

for file in files:
    df = pd.read_csv(DATA_DIR / file)

    # Ajoute les colonnes crypto & source
    df["crypto"] = file.split("USD")[0]  # ex: BTC, ETH, XRP
    df["source"] = "Binance CSV"

    # Prend uniquement les colonnes utiles
    df = df[["Open time", "Open", "High", "Low", "Close", "Volume", "crypto", "source"]]

    # Renomme les colonnes pour uniformiser
    df = df.rename(columns={
        "Open time": "date",
        "Close": "price_usd",
        "Volume": "volume_usd"
    })

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%d-%m-%Y")

    merged_list.append(df)

# Fusionne toutes les cryptos
merged = pd.concat(merged_list, ignore_index=True)

# Sauvegarde le CSV propre dans le fichier data
merged.to_csv("data/kaggle_data.csv", index=False)

