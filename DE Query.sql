CREATE TABLE IF NOT EXISTS exchange_rates (
    id SERIAL PRIMARY KEY,
    base_currency VARCHAR(10),
    target_currency VARCHAR(10),
    rate FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from exchange_rates;

delete  from exchange_rates;


CREATE UNIQUE INDEX IF NOT EXISTS unique_rate_entry
ON exchange_rates (base_currency, target_currency, timestamp);

SHOW timezone;

SET TIMEZONE = 'Asia/Kolkata';

ALTER TABLE exchange_rates
ALTER COLUMN timestamp TYPE TIMESTAMP WITH TIME ZONE;

