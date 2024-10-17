import requests, bs4

time_togo = input("what year do you want to go? Type in this format YYYY-MM-DD:")
print(time_togo)

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{time_togo}")
html_page = response.text

html_soup = bs4.BeautifulSoup(html_page, 'html.parser')

# song_titles = [song.getText() for song in html_soup.select("h3.c-title")]
# print(song_titles)

song_titles = [title.getText().strip() for title in html_soup.select("li ul li h3.c-title")]

song_artist = [artist.getText().strip() for artist in html_soup.select("li ul li span.a-no-trucate")]


top100 = [f"{song} - {artist}" for song, artist in zip(song_titles, song_artist)]
print("\n".join(top100[0:10]))


