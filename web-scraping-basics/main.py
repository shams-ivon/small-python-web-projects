from bs4 import BeautifulSoup
import requests

responses = requests.get("https://news.ycombinator.com/show")
yc_web_page = responses.text

soup = BeautifulSoup(yc_web_page, "html.parser")

news_articles = soup.find_all(name="span", class_="titleline")
news_upvotes = soup.find_all(name="span", class_="subline")

for article in news_articles:
    print(article.getText())
    print(article.a.get("href"))