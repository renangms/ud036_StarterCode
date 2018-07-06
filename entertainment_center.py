"""Main module responsivle for:
       - movie database
       - creating web page
"""

import media
import fresh_tomatoes

godfather = media.Movie(
    "The Godfather",
    "The aging patriarch of an organized crime dynasty "
    "transfers control of his clandestine empire to his reluctant son.",
    "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",  # NOQA
    "https://www.youtube.com/watch?v=dNE2PvbesQU")

scarface = media.Movie(
    "Scarface",
    "In Miami in 1980, a determined Cuban immigrant takes "
    "over a drug cartel and succumbs to greed.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Scarface_-_1983_film.jpg/220px-Scarface_-_1983_film.jpg",  # NOQA
    "https://www.youtube.com/watch?v=cv276Wg3e7I")

goodfellas = media.Movie(
    "Goodfellas",
    "The story of Henry Hill and his life in "
    "the Italian-American crime syndicate.",
    "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xWMxvFvhAB8")

if __name__ == "__main__":
    movies = [godfather, scarface, goodfellas]
    fresh_tomatoes.open_movies_page(movies)
