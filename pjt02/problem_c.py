import os
import requests
from tmdb import URLMaker
from pprint import pprint

key = os.environ.get('TMDB_KEY')

def ranking():
    maker  = URLMaker('key')
    url = maker.get_url('movie', 'popular', region = 'KR', language = 'ko')
    response = requests.get(url)
    popular = response.json()

    vote_list = []
    for popular_movie in popular['results']:
        vote_list.append(popular_movie['vote_average'])
    # print(vote_list)
    sorted_list = sorted(vote_list, reverse= True)
    rank_list = sorted_list[0:5]

    result =[]
    for popular_movie in popular['results']:
        for rank in rank_list:
            if popular_movie['vote_average'] == rank:
                result.append(popular_movie['original_title'])
    return result        



if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())