from bs4 import BeautifulSoup
import requests

def fix(song_title):

    song_title = song_title.lstrip("\n\t")
    song_title = song_title.rstrip("\n\t")
    
    return song_title

date = input("Music from date? (YYYY-MM-DD): ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}/"

responses = requests.get(url=billboard_url)
soup = BeautifulSoup(responses.text, "html.parser")

topmost_class = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"
rest_song_class = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"


topmost = soup.find_all(name="h3", class_=topmost_class)
topmost_title_as_list = [fix(title.getText()) for title in topmost]
print(topmost_title_as_list)

rest_song_titles = soup.find_all(name="h3", class_=rest_song_class)
rest_song_titles_list = [fix(title.getText()) for title in rest_song_titles]
print(rest_song_titles_list)