from module.movie import Movie
from module.imdb_request import IMDbRequest
import numpy as np

class MovieFacade:
    
    def get_movies(movie_to_search_for):
        movies_content = IMDbRequest.get_movies(movie_to_search_for).content['results']
        movies = []
        print(movies_content)
        if movies_content is not None:
            for movie_content in movies_content:
                id = movie_content["id"]
                rate_responses = IMDbRequest.get_rate_from_id(id)
                mean_rate = MovieFacade.get_mean_rates(rate_responses)
                movie = Movie(id, movie_content['title'], movie_content['description'], mean_rate, movie_content['image'])
                movie.set_replacement_text_for_nan_rate()
                movies.append(movie)
            return movies
        else:
            return None
    
    def get_mean_rates(rate_responses):
        all_rates = []
        for rat_response in rate_responses.content['items']:
            rate = rat_response['rate']
            all_rates.append(float(rate))
        return np.mean(all_rates)
            
        