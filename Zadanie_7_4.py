import random

class Movie:
    def __init__(self, title, publication_date, genre):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre
        self.number_of_plays = 0

    def __str__(self):
        return f'{self.title}, ({self.publication_date})'

    def play(self, step=1):
        self.number_of_plays += step

class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} S{self.season_number:02d} E{self.episode_number:02d}'

movie_1 = Movie(title = "Transporter 2", publication_date = "2005", genre = "Akcji")
movie_2 = Movie(title = "Pulp Fiction", publication_date = "1994", genre = "dramat")
movie_3 = Movie(title = "Venom", publication_date = "2018", genre = "science fiction")
movie_4 = Movie(title = "Druga twarz", publication_date = "2011", genre = "kryminalny")
movie_5 = Movie(title = "Wielka ucieczka", publication_date = "1963", genre = "przygodowy")

series_1 = Series(title = "Gra o Tron", publication_date = "2011", genre = "Fantasy", episode_number = "73", season_number = "8")
series_2 = Series(title = "The Walking Dead", publication_date = "2010", genre = "Horror", episode_number = "161", season_number = "11")
series_3 = Series(title = "Dr House", publication_date = "2004", genre = "medyczny", episode_number = "177", season_number = "8")
series_4 = Series(title = "Breaking Bed", publication_date = "2008", genre = "czarna komedia", episode_number = "62", season_number = "5")
series_5 = Series(title = "Przyjaciele", publication_date = "1994", genre = "sitcom", episode_number = "240", season_number = "10")

movies_and_series = [movie_1, movie_2, movie_3, movie_4, movie_5, series_1, series_2, series_3, series_4, series_5]

def add(self, title, type):
    movies_and_series = []
    if type == "M":
        title = Movie(self.title)
        movies_and_series.append(title)
    elif type == "S":
        title = Series(self.title)
        movies_and_series.append(title)
    else:
        print("Wprowadziłeś błędne dane!")
    return movies_and_series

def get_movie():
    movies = []
    for film in movies_and_series:
        if isinstance(film, Movie):
            movies.append(film)
    sorted_movies = sorted(movies)
    return sorted_movies

def get_series():
    series = []
    for film in movies_and_series:
        if isinstance(film, Series):
            series.append(film)
    sorted_series = sorted(series)
    return sorted_series

def search(element):
    for i in movies_and_series:
        if i.title == element:
            return i
    None
    #print("Twojego filmu bądź serialu nie ma w bazie.")

def generate_views():
    element = random.choice(movies_and_series)
    element.number_of_plays += random.randint(1, 10)

def ten_generate():
    for i in range(10):
        generate_views()

def top_titles(quantity):
    movies_and_series_sorted = sorted(movies_and_series, key=lambda x: x.number_of_plays, reverse=True)
    return movies_and_series_sorted[:quantity]

for _ in range(10):
    generate_views()

for o in top_titles(5):
    print(f"{o.title}, {o.number_of_plays}")



