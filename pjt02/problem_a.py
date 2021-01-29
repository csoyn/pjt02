import requests
from tmdb import URLMaker
import os
def popular_count():

    key = os.environ.get('TMDB_KEY')
    
    maker  = URLMaker(key)
    url = maker.get_url('movie', 'popular', region = 'KR', language = 'ko')
    response = requests.get(url)

    popular = response.json()

    return len(popular['results'])


if __name__ == '__main__':
    print(popular_count())