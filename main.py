from module.movie import Movie
from module.movie_facade import MovieFacade

movies = MovieFacade.get_movies()

for movie in movies:
    assert isinstance(movie, Movie)
    
print("ok")