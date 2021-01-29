#  Project02 (01.29)

> 파이썬을 활용한 데이터 수집 Ⅱ



#### 🎬Prologue

- 저번주 플젝에서 느낀 바 = 이번 프로젝트에 적용 할 거

  🐾  조용한 환경 & 시간에 너무 쫓기지 말기 & 간식 구비하기

-  학습목표 

​    🐾 요청과 응답 & 데이터구조



## Problem_a

>  영화개수 카운트

```python
maker  = URLMaker(key) 				# class URLMaker 만들기
url = maker.get_url('movie', 'popular', region = 'KR', language = 'ko') # 요청url
# https://api.themoviedb.org/3/movie/popular?api_key=<<api_key>>&language=en-US&page=1
response = requests.get(url)											# 응답
```

**Review**

1. a번은 tmdb.py를 활용하여 요청 url을 잘 만들 수 있는가를 물어보는 문제였던거 같다.
2. tmdb.py에 있는 함수들을 잘 익히고, 나중에 혼자서 만들 수 있도록 해야징 －O－



## Problem_b

> 특정 조건에 맞는 영화출력

```python
result =
for popular_movie in popular['results']:
    if popular_movie['vote_average'] >=8:
        result.append(popular_movie['original_title'])
return result
```

**Review**



## Problem_c

> 평점 순 정렬

```python

```





## Problem_d

> 제목 검색, 영화 추천

```python

```







## Problem_e

> 배우, 감독 리스트 출력

```python

```







## Problem_f

> 추가정보 수집



