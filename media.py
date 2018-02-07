import webbrowser

class Movie():
    def __init__(self, movie_title, movie_year, poster_image, trailer_youtube, movie_rated, movie_plot):
        self.title = movie_title
        self.year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rated = movie_rated
        self.plot = movie_plot

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
