# -*- coding: utf-8 -*-

from prefect import flow
from datetime import timedelta
from prefect.server.schemas.schedules import IntervalSchedule


from etl.extract import fetch_exchange_rates
from etl.transform import transform_data
from etl.load import load_data

@flow(name="exchange-rate-pipeline")
def exchange_rate_pipeline():
    print("🚀 Starting ETL pipeline...")
    raw_data = fetch_exchange_rates()
    if raw_data:
        transformed = transform_data(raw_data)
        load_data(transformed)
    else:
        print("No data fetched from API.")

# Run directly for testing
if __name__ == "__main__":
    exchange_rate_pipeline()
