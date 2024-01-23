from bs4 import BeautifulSoup
import requests

responses = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(responses.text, "html.parser")

movie_titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_title_list = [title.getText() for title in movie_titles]
movie_title_list.reverse()

with open("movies.txt", "a") as write_file:

    for movie in movie_title_list:
        write_file.write(f"{movie}\n")