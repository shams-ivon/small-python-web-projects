import os
import requests
from datetime import date, timedelta

NEWS_API_URL = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Apple Inc"
NEWS_API_KEY = os.environ.get("NEWSAPI_KEY_ENV")

class StockNews:

    def __init__(self, from_date, to_date):
        self.parameters = {
            "q": COMPANY_NAME,
            "from": from_date,
            "to": to_date,
            "sortBy": "popularity",
            "apiKey": NEWS_API_KEY,
        }
        self.news_data = requests.get(
            url=NEWS_API_URL,
            params=self.parameters,
        ).json()["articles"][:3]

    def get_text_format(self):
        text_0 = f"{self.news_data[0]['description']}\nVisit: {self.news_data[0]['url']}"
        text_1 = f"{self.news_data[1]['description']}\nVisit: {self.news_data[1]['url']}"
        text_2 = f"{self.news_data[2]['description']}\nVisit: {self.news_data[2]['url']}"
        return f"{text_0}\n\n{text_1}\n\n{text_2}"

# parameters_price = {
# }

# daily_stock_data = requests.get(url=STOCK_API_URL, params=parameters_price).json()["Time Series (Daily)"]

# today = date.today()
# two_days_before = str(today - timedelta(days=2))
# three_days_before = str(today - timedelta(days=3))

# price_1 = final_price_on_day(two_days_before)
# price_2 = final_price_on_day(three_days_before)

# print(price_1, price_2)

# parameters_news = {
#     "q": COMPANY_NAME,
    
# }
