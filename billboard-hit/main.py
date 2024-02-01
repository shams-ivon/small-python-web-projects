from bs4 import BeautifulSoup
import requests

def fix(song_title):
    # strips "\n" and "\t" from the scaped strings and returns a clean string
    pass

date = input("Music from date? (YYYY-MM-DD): ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}/"

responses = requests.get(url=billboard_url)
soup = BeautifulSoup(responses.text, "html.parser")

class_name1 = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"
class_name2 = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

song_titles1 = soup.find_all(name="h3", class_=class_name1)
song_title_list1 = [fix(title.getText()) for title in song_titles1]
print(song_title_list1)

song_titles2 = soup.find_all(name="h3", class_=class_name2)
song_title_list2 = [fix(title.getText()) for title in song_titles2]
print(song_title_list2).write(f"{movie}\n")