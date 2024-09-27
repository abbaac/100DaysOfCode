import datetime as dt
import os
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

spotipy_client_id = os.getenv("SPOTIPY_CLIENT_ID")
spotipy_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
spotipy_redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

# date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
date = "2024-09-26"
# date = dt.datetime(year=2016, month=8, day=13)
year = date.split("-")[0]
response = requests.get(f"https://www.billboard.com/charts/hot-100/" + date)
data = response.text

soup = BeautifulSoup(data, "html.parser")

# songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
songs = soup.select("h3.c-title.a-no-trucate.a-font-primary-bold-s")
artists = soup.select("span.c-label.a-no-trucate.a-font-primary-s")

top_100 = {song.getText().strip(): artist.getText().strip() for song, artist in zip(songs, artists)}


replace_terms = [" x ", " X ", " Featuring ", " with "]
for song, artist in top_100.items():
    for term in replace_terms:
        artist = artist.replace(term, " ")
    top_100[song] = artist.replace("Featuring", "")

print(top_100)

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]

song_uris = []
for key, value in top_100.items():
    try:
        query = sp.search(q=f"artist:{value} track:{key}")
        uri = query["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"{key} by {value} found on Spotify with uri: {uri}")
    except IndexError:
        print(f"{key} by {value} not found on Spotify")


playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False,
                                   description=f"The Billboard 100 from the day {date}")
playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

