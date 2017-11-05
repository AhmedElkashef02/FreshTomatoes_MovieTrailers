import media
import fresh_tomatoes

# instances of the Movie class
# examples of movies that I would like to show on the website
the_help = media.Movie(
    "The Help",
    "African Americans working in white households in Jackson "
    "Mississippi during the early 1960s",
    "https://upload.wikimedia.org/wikipedia/en/e/ef/Thehelpbookcover.jpg",   # NOQA
    "https://www.youtube.com/watch?v=aT9eWGjLv6s"
)

before_sunrise = media.Movie(
    "Before Sunrise",
    "a young American and a young French woman who meet on a train "
    "and disembark in Vienna where they spend the night walking around "
    "the city and getting to know each other",
    "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=25v7N34d5HE"
)

into_the_wild = media.Movie(
    "Into the Wild",
    "A boy that leaves all society and goes into the wild "
    "exploring and living",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Into-the-wild.jpg/220px-Into-the-wild.jpg",  # NOQA
    "https://www.youtube.com/watch?v=g7ArZ7VD-QQ"
)

forest_gump = media.Movie(
    "Forest Gump",
    "a slow-witted but kind-hearted good natured and athletically "
    "prodigious man from Alabama who witnesses and in some cases "
    "influences some of the defining events of the latter half of "
    "the 20th century in the United States",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=uPIEn0M8su0"
)

cast_away = media.Movie(
    "Cast Away",
    "a FedEx employee marooned on an uninhabited island after his "
    "plane crashes in the South Pacific and his attempts to survive "
    "on the island using remnants of his plane's cargo",
    "https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=PJvosb4UCLs"
)

django_unchained = media.Movie(
    "Django Unchained",
    "With the help of a German bounty hunter a freed slave "
    "sets out to rescue his wife from a brutal Mississippi "
    "plantation owner",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=eUdM9vrCbow"
)

# open_movies_page function needs an array as an argument
movies = [
    into_the_wild,
    django_unchained,
    cast_away,
    forest_gump,
    before_sunrise, the_help
    ]

fresh_tomatoes.open_movies_page(movies)
