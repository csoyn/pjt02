import requests
from tmdb import URLMaker
from pprint import pprint

maker  = URLMaker('5484e9c8428f08f7e60d1a972a7f7f35')
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
