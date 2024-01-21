from bs4 import BeautifulSoup
import requests

responses = requests.get("https://news.ycombinator.com/show")
yc_web_page = responses.text

soup = BeautifulSoup(yc_web_page, "html.parser")

news_articles = soup.find_all(name="span", class_="titleline")
news_votes = soup.find_all(name="span", class_="score")

news_article_title_list = []
news_article_link_list = []
news_article_vote_list = []

for article in news_articles:
    news_article_title_list.append(article.getText())
    news_article_link_list.append(article.a.get("href"))

for article in news_votes:
    vote = article.text.split()[0]
    news_article_vote_list.append(int(vote))

for index in range(len(news_article_title_list)):
    print(news_article_title_list[index])
    print(news_article_link_list[index])
    print(news_article_vote_list[index])
    print("")