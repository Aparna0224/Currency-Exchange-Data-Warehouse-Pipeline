# etl/load.py

from sqlalchemy import Table, Column, Integer, String, Float, MetaData, TIMESTAMP, insert
from db.db_config import engine
from datetime import datetime

metadata = MetaData()

exchange_rates = Table(
    'exchange_rates',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('base_currency', String(10)),
    Column('target_currency', String(10)),
    Column('rate', Float),
    Column('timestamp', TIMESTAMP, default=datetime.utcnow)
)

# Ensure table exists
metadata.create_all(engine)

def load_data(transformed_data: list):
    with engine.connect() as conn:
        conn.execute(insert(exchange_rates), transformed_data)
        conn.commit()
        print("✅ Data inserted into PostgreSQL successfully!")
