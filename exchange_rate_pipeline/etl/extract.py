# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# def fetch_exchange_rates():
#     url = os.getenv("EXCHANGE_RATE_API_URL")

#     if not url:
#         print("API URL not found in environment variables.")
#         return None

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()

#         # Check for required keys
#         if "base_code" not in data or "rates" not in data:
#             print("Missing 'base_code' or 'rates' in response.")
#             print("Response data:", data)
#             return None

#         print("✅ Exchange rate data fetched successfully.")
#         return data

#     except requests.RequestException as e:
#         print(f"Request failed: {e}")
#         return None
#     except ValueError as e:
#         print(f"❌ Failed to parse JSON: {e}")
#         return None
import os
import requests

def fetch_exchange_rates():
    url = os.getenv("EXCHANGE_RATE_API_URL")  # This will now be read directly from the environment

    if not url:
        print("API URL not found in environment variables.")
        return None

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "base_code" not in data or "rates" not in data:
            print("Missing 'base_code' or 'rates' in response.")
            print("Response data:", data)
            return None

        print("✅ Exchange rate data fetched successfully.")
        return data

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except ValueError as e:
        print(f"❌ Failed to parse JSON: {e}")
        return None
