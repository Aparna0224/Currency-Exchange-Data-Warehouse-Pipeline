# from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, TIMESTAMP, select, and_
# import os

# def load_data(data):
    
#     engine = create_engine(os.getenv("DATABASE_URL"))
#     metadata = MetaData()

#     exchange_rates = Table(
#         "exchange_rates", metadata,
#         Column("id", Integer, primary_key=True),
#         Column("base_currency", String(10)),
#         Column("target_currency", String(10)),
#         Column("rate", Float),
#         Column("timestamp", TIMESTAMP)
#     )

#     with engine.connect() as conn:
#         inserted_count = 0
#         skipped_count = 0

#         for entry in data:
#             # Check if this entry already exists
#             query = select(exchange_rates).where(
#                 and_(
#                     exchange_rates.c.base_currency == entry['base_currency'],
#                     exchange_rates.c.target_currency == entry['target_currency'],
#                     exchange_rates.c.timestamp == entry['timestamp']
#                 )
#             )
#             result = conn.execute(query).fetchone()

#             if result:
#                 skipped_count += 1
#                 print(f"⚠️ Skipped duplicate: {entry['target_currency']} at {entry['timestamp']}")
#                 continue

#             # If not duplicate, insert
#             stmt = exchange_rates.insert().values(**entry)
#             conn.execute(stmt)
#             inserted_count += 1

#         conn.commit()
#         print(f"✅ Inserted: {inserted_count}, Skipped: {skipped_count}")
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, TIMESTAMP, select, and_
import os

def load_data(data):
    engine = create_engine(os.getenv("DATABASE_URL"), echo=False, future=True)
    metadata = MetaData()

    exchange_rates = Table(
        "exchange_rates", metadata,
        Column("id", Integer, primary_key=True),
        Column("base_currency", String(10)),
        Column("target_currency", String(10)),
        Column("rate", Float),
        Column("timestamp", TIMESTAMP)
    )

    metadata.create_all(engine)

    with engine.connect() as conn:
        inserted_count = 0
        skipped_count = 0

        for entry in data:
            query = select(exchange_rates).where(
                and_(
                    exchange_rates.c.base_currency == entry['base_currency'],
                    exchange_rates.c.target_currency == entry['target_currency'],
                    exchange_rates.c.timestamp == entry['timestamp']
                )
            )
            result = conn.execute(query).fetchone()

            if result:
                skipped_count += 1
                print(f"⚠️ Skipped duplicate: {entry['target_currency']} at {entry['timestamp']}")
                continue

            stmt = exchange_rates.insert().values(**entry)
            conn.execute(stmt)
            inserted_count += 1

        conn.commit()
        print(f"✅ Inserted: {inserted_count}, Skipped: {skipped_count}")
