from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
print(response.text)

yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")


movies = soup.find_all(name="h3", class_="title")
movie_list = []
for titles in movies:
    movie_list.append(titles.get_text())

movie_list = movie_list[::-1]
print(movie_list)