"""This module contains media data sctructures."""

import webbrowser


class Movie():
    """This class provides a way to store movie information."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):
        """
        Creates a movie object.

        Args:

        title (string): Movie title
        storyline (string): Movie storyline
        poster_image_url (string): Movie poster image URL
        trailer_youtube_url (string): Movie Youtube trailer URL
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """The movie trailer is diplayed in a web browser."""
        webbrowser.open(self.trailer_youtube_url)
