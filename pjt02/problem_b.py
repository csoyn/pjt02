import os
import requests
from tmdb import URLMaker
from pprint import pprint

key = os.environ.get('TMDB_KEY')

maker  = URLMaker(key)
url = maker.get_url('movie', 'popular', region = 'KR', language = 'ko')
response = requests.get(url)
popular = response.json()

def vote_average_movies():
    result =[]
    for popular_movie in popular['results']:
        if popular_movie['vote_average'] >=8:
            result.append(popular_movie['original_title'])
    return result


if __name__ == '__main__':
    pprint(vote_average_movies())    
