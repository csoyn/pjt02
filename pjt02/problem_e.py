import requests
from tmdb import URLMaker
from pprint import pprint


key = '5484e9c8428f08f7e60d1a972a7f7f35'
maker= URLMaker(key)
url = maker.get_url('movie', 'popular', region = 'KR', language = 'ko')
response = requests.get(url)
popular = response.json()

def credits(title):
    pass

    movie_id = maker.movie_id(title)
    if not movie_id:
        return None

    url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={key}&language=ko&page=1'
    response2 = requests.get(url2)
    data_e = response2.json()

    cast_list = []
    for casts in data_e['cast'] :
        if casts['cast_id'] < 10 :
            cast_list.append(casts['name'])

    crew_list = []
    for crews in data_e['crew'] :
        if crews['department'] == 'Directing':
            crew_list.append(crews['name'])

    result = {'cast' : cast_list,
            'crew' : crew_list }

    return result
# print(type(data_e))


if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None