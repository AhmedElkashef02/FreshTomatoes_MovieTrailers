class Movie():
    """This class helps to assign data associated with each movie instance"""
    def __init__(self, title, story, poster_image_url, trailer_youtube_url):
        """the constructor takes the following:
        movie title, the storyline, the poster image url, link to trailer"""
        self.title = title
        self.story = story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
