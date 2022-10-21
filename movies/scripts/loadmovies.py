import csv
from movies.models import Movie

FILENAME = "seeddata/top5.csv"
CACHE_DIR = "http://airline.uaa490.org/movie-images/"

def run():

    def cached_url(p):
        base = p[p.rfind('/')+1:]
        return f'{CACHE_DIR}{base}'

    print(f'Reading file: {FILENAME}')
    with open(FILENAME) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'\t{row["title"]}', end="... ")
            title = row["title"]
            year = int(row["year"])
            rating = float(row["rating"])
            director = row["director"]
            plot = row["plot"]
            url = cached_url(row["url"])
            if Movie.objects.filter(         
                movie_title=title, release_year=year, director=director, movie_poster_url=url, movie_plot=plot, rating=rating).exists():
                print(f'already in database.')
            else:
                m = Movie(movie_title=title, release_year=year, director=director, movie_poster_url=url, movie_plot=plot, rating=rating)
                m.save()
                print(f'added to database.')

	