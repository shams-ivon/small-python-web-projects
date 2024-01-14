import os
import requests

STOCK_API_URL = "https://www.alphavantage.co/query"
STOCK = "AAPL"
STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY_ENV")

class StockPrice:

    def __init__(self):
        self.parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK,
            "apikey": STOCK_API_KEY,
        }
        self.daily_stock_data = requests.get(
            url=STOCK_API_URL, 
            params=self.parameters,
        ).json()["Time Series (Daily)"]

    def final_price_on_day(self, a_date):
        return float(self.daily_stock_data[a_date]["4. close"])
    