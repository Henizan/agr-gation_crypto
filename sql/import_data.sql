-- Import des données ohclv (open, high, low, close, volume) depuis les données Kaggle
COPY ohlcv (open, high, low, close, volume, open_time, close_time, crypto)
FROM 'C:/ece_B3/projet_agr_crypto/data/kaggle_data.csv'
DELIMITER ',' CSV HEADER;

-- Impoert des données ohclv depuis les données CoinGecko (90 jours)
COPY ohlcv (open, high, low, close, volume, open_time, close_time, crypto)
FROM 'C:/ece_B3/projet_agr_crypto/data/coingecko_data.csv'
DELIMITER ',' CSV HEADER;

-- Import des données fear and greed index depuis alternatif.me
COPY fear_greed (date, value, classification)
FROM 'C:/ece_B3/projet_agr_crypto/data/fear_greed_data.csv'
DELIMITER ',' CSV HEADER;


