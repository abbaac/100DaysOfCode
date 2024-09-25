from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_wesbite = response.text

soup = BeautifulSoup(movie_wesbite, "html.parser")

movie_titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

with open("movies.txt", "w") as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie.getText()}\n")