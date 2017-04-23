#Create class Movie
class Movie(object):
    #Docstring for class Movie
    """This class stores a Movie's title, description, poster image url and youtube trailer url."""

    #__init__ function initializes class Movie and takes 4 arguments
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #creates an instance variable title from the first argument - used by fresh_tomatoes
        self.title = movie_title
        #creates an instance variable storyline from the second argument - used by fresh_tomatoes
        self.storyline = movie_storyline
        #creates an instance variable poster_image_url from the third argument
        # - used by fresh_tomatoes
        self.poster_image_url = poster_image
        #creates an instance variable trailer_youtube_url from the
        #fourth argument - used by fresh_tomatoes
        self.trailer_youtube_url = trailer_youtube
