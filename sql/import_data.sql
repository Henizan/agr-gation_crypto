-- importation des données de kaggle
COPY ohlcv (open, high, low, close, volume, open_time, close_time, crypto)
FROM 'C:/ece_B3/projet_agr_crypto/data/kaggle_data.csv'
DELIMITER ',' CSV HEADER;

-- importation des données api de coingecko
COPY ohlcv (open, high, low, close, volume, open_time, close_time, crypto)
FROM 'C:/ece_B3/projet_agr_crypto/data/coingecko_90d.csv'
DELIMITER ',' CSV HEADER;


