import os
import requests
from tmdb import URLMaker
from pprint import pprint

key = os.environ.get('TMDB_KEY')
maker= URLMaker(key)
url = maker.get_url('movie', 'popular', region = 'KR', language = 'ko')
response = requests.get(url)
popular = response.json()

def recommendation(title):

    movie_id = maker.movie_id(title)
    if not movie_id:
        return None
    url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={key}&language=ko&page=1'
    response2 = requests.get(url2)
    data = response2.json()
    

    result = []
    for recommend in data['results']:
        result.append(recommend['original_title'])
        
    return result


if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    #=> None
