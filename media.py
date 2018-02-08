class Movie():

    def __init__(self, movie_title, movie_year, poster_image, trailer_youtube,
                 movie_rated, movie_plot):
        """The __init_ method contains attributes of moive's information.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            movie_title (str): Moive's Name.
            movie_year (int): Moive's release year.
            poster_image (str): the url of image file of Poster
            trailer_youtube (str): the url of the moive trailer in Youtube.
            movie_rated (str): the rate of the movie.
            movie_plot (str): the storyline of the movie.

        """
        self.title = movie_title
        self.year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rated = movie_rated
        self.plot = movie_plot
