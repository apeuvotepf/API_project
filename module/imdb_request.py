import requests
from module.response import Response
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

class IMDbRequest:
    _base_url = "https://imdb-api.com"
        
    @classmethod
    def get_movies(cls, movie_to_search_for):
        response =  requests.get(cls._base_url+f"/en/API/SearchMovie/{API_KEY}/{movie_to_search_for}")
        
        return Response(status_code=response.status_code, content=response.json())
    
    
    @classmethod
    def get_rate_from_id(cls, id):
        response = requests.get(cls._base_url+f"/en/API/MetacriticReviews/{API_KEY}/{id}")
        return Response(status_code=response.status_code, content=response.json())
