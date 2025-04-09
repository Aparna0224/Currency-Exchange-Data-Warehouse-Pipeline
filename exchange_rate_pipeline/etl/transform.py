from datetime import datetime
from zoneinfo import ZoneInfo  # Available in Python 3.9+

def transform_data(raw_data):
    transformed = []

    # Convert UTC to IST
    timestamp_utc = datetime.utcnow().replace(tzinfo=ZoneInfo("UTC"))
    timestamp_ist = timestamp_utc.astimezone(ZoneInfo("Asia/Kolkata"))

    # Extract base currency using the correct key
    base_currency = raw_data.get("base_code", "UNKNOWN")

    # Iterate over conversion_rates instead of rates
    for target_currency, rate in raw_data.get("rates", {}).items():
        transformed.append({
            "base_currency": base_currency,
            "target_currency": target_currency,
            "rate": rate,
            "timestamp": timestamp_ist
        })

    return transformed
