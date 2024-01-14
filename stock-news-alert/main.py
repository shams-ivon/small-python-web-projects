from stock_news import StockNews
from stock_price import StockPrice
from send_email import send_email
from datetime import date, timedelta

today = date.today()
to_day = str(today - timedelta(days=3))
from_day = str(today - timedelta(days=4))

stock_news = StockNews(to_day, to_day)
stock_price = StockPrice()

price_1 = stock_price.final_price_on_day(to_day)
price_2 = stock_price.final_price_on_day(from_day)

if abs(price_1 - price_2) / price_2 * 100 >= 5:
    send_email("whatever@whoever.com", stock_news.get_text_format())

