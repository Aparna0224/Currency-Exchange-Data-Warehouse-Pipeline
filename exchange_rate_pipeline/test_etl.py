# test_etl.py

from etl.extract import fetch_exchange_rates
from etl.transform import transform_data
from etl.load import load_data

if __name__ == "__main__":
    raw = fetch_exchange_rates()
    transformed = transform_data(raw)
    load_data(transformed)
