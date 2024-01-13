import os
import requests
from datetime import datetime

URL = "https://www.alphavantage.co/query"
STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"
STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY_ENV")

def final_price_on_day(day):
    return float(daily_stock_data[f"2024-01-{day}"]["4. close"])

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

daily_stock_data = requests.get(url=URL, params=parameters).json()["Time Series (Daily)"]
# print(daily_stock_data)

price_1 = final_price_on_day(11)
price_2 = final_price_on_day(12)

change = abs(price_1 - price_2) / price_1 * 100
print(change)
