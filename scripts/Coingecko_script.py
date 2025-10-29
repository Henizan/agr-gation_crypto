# import des libraries
import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

# Configuration de l'API
API_KEY = "CG-1Cf6z9WxxhNrx5Xby1YtpKhM"

# Définition des en-têtes pour les requêtes API
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": API_KEY
}

def get_market_chart_segment(coin_id, vs_currency): #Récupère les données de marché pour une crypto-monnaie spécifique sur une période de 90 jours
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency={vs_currency}&days=90" #URL de l'API pour récupérer les données de marché
    r = requests.get(url, headers=headers) #Effectue une requête GET à l'API
    r.raise_for_status() #Vérifie si la requête a réussi
    data = r.json() #Parse la réponse JSON

    prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])  #Créer un DataFrame pour les prix    
    volumes = pd.DataFrame(data["total_volumes"], columns=["timestamp", "volume"]) #Créer un DataFrame pour les volumes
    prices["timestamp"] = pd.to_datetime(prices["timestamp"], unit="ms", utc=True) # Convertir les timestamps en datetime
    volumes["timestamp"] = pd.to_datetime(volumes["timestamp"], unit="ms", utc=True)  # Convertir les timestamps en datetime

# 
    df = prices.resample("1D", on="timestamp").agg( # Resampler les données par jour et calculer les agrégats
        {"price": ["first", "max", "min", "last"]}  # Agrégats pour Open, High, Low, Close
    )
    df.columns = ["Open", "High", "Low", "Close"] # Renommer les colonnes

    df["Volume"] = volumes.resample("1D", on="timestamp")["volume"].sum() # Agréger les volumes par jour 

    df["Open Time"] = df.index # Utiliser l'index comme temps d'ouverture
    df["Close Time"] = df["Open Time"].shift(-1) # Temps de fermeture est le temps d'ouverture du jour suivant

    df["Open Time"] = pd.to_datetime(df["Open Time"]).dt.strftime("%Y-%m-%d %H:%M:%S") # Formater le temps d'ouverture
    df["Close Time"] = pd.to_datetime(df["Close Time"]).dt.strftime("%Y-%m-%d %H:%M:%S") # Formater le temps de fermeture

    df.reset_index(drop=True, inplace=True) # Réinitialiser l'index
    return df # Retourner le DataFrame final

def get_full_history(coin_id, symbol): #Récupère l'historique complet des données de marché pour une crypto-monnaie spécifique
    df = get_market_chart_segment(coin_id, "usd") # Appeler la fonction pour obtenir les données de marché
    df["Crypto"] = symbol # Ajouter une colonne pour le symbole de la crypto-monnaie
    return df # Retourner le DataFrame avec l'historique complet

cryptos = { # Dictionnaire des crypto-monnaies à récupérer
    "bitcoin": "BTC", 
    "ethereum": "ETH",
    "ripple": "XRP"
}

frames = [get_full_history(cid, sym) for cid, sym in cryptos.items()] # Récupérer les données pour chaque crypto-monnaie et stocker dans une liste de DataFrames

final = pd.concat(frames, ignore_index=True) # Concaténer tous les DataFrames en un seul

final.to_csv("data/coingecko_data.csv", index=False) # Exporter le DataFrame final vers un fichier CSV
