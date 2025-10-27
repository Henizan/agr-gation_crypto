-- Création table du ohlv
CREATE TABLE ohlcv (
    id SERIAL PRIMARY KEY,
    crypto VARCHAR(10) NOT NULL,
    open_time TIMESTAMP,
    close_time TIMESTAMP,
    open NUMERIC(18,8),
    high NUMERIC(18,8),
    low NUMERIC(18,8),
    close NUMERIC(18,8),
    volume NUMERIC(30,10)
);

-- Création table du Fear & Greed Index
CREATE TABLE fear_greed (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP UNIQUE,               
    value INT CHECK (value BETWEEN 0 AND 100), 
    classification VARCHAR(50)            
);
