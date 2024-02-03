from scraped_data import top_songs

date = input("Music from date? (YYYY-MM-DD): ")

top_songs_list = top_songs(date)

print(top_songs_list)
