import os
import requests
from datetime import date, timedelta

URL = "https://www.alphavantage.co/query"
STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"
STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY_ENV")

def final_price_on_day(a_date):
    return float(daily_stock_data[a_date]["4. close"])

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

daily_stock_data = requests.get(url=URL, params=parameters).json()["Time Series (Daily)"]

today = date.today()
two_days_before = str(today - timedelta(days=2))
three_days_before = str(today - timedelta(days=3))

price_1 = final_price_on_day(two_days_before)
price_2 = final_price_on_day(three_days_before)

print(price_1, price_2)
