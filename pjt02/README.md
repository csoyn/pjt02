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

😎**Review**

1. a번은 tmdb.py를 활용하여 요청 url을 잘 만들 수 있는가를 물어보는 문제였던거 같다.
2. tmdb.py에 있는 함수들을 잘 익히고, 나중에 혼자서 만들 수 있도록 해야징 －O－



## Problem_b

> 특정 조건에 맞는 영화출력

```python
result = []
for popular_movie in popular['results']: 			# 영화정보가 담긴 하나씩 담긴 딕셔너리
    if popular_movie['vote_average'] >= 8:			# 평점 조건
        result.append(popular_movie['original_title']) # 조건에 맞는 영화
return result
```

😎**Review**

- 어렵지않게 할 수 있는 문제 였던거 같다. pjt01 때 보다 딕셔너리랑 친해진 느낌...ㅎㅎ



## Problem_c

> 평점 순 정렬

```python
vote_list = []
    for popular_movie in popular['results']:
        vote_list.append(popular_movie['vote_average'])			# 새로 평점리스트 만들고
    sorted_list = sorted(vote_list, reverse= True)				# 내림차순으로 sort
    rank_list = sorted_list[0:5]								# 앞에서 5개

    result =[]
    for popular_movie in popular['results']:					
        for rank in rank_list:
            if popular_movie['vote_average'] == rank:		   # 일단은 중복값문제 있지만
                result.append(popular_movie['original_title']) # 제목 가져옴
```

**Review**

🙄   하c...이 문제부터 꼬이기 시작함.

- 필요한 정보가 `vote_average` 와 `original_title` 이었음.
- 그래서 결과물을 딕셔너리 형태로 만들고 딕셔너리`vote_average` 의  `values`를 정렬하고 5개를 자르고
- `original_title` 을 뽑으려고 함....
- 하지만  딕셔너리가 `keys()`로만 정렬이 되더라...ㅎㅎㅎㅎㅎ
- 그래서 아예 딕셔너리를 버리고 그냥 `list`로 하자 해서 했으나,
- 이 문제에선 중복값이 없었지만, 중복값이 있다면 밑에는 틀린코드 
- 평점말고 다른 변수를 추가해서 merge 하면 되긴할거 같다.



## Problem_d

> 제목 검색, 영화 추천



```python
movie_id = maker.movie_id(title) # 하 이시키
    if not movie_id:
        return None
    url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={key}&language=ko&page=1'
    response2 = requests.get(url2)
    data = response2.json()
```

**Review**

😂 장난 아니고, 얘한테 2시간 쏟음...

- 그 이유는 바로...`id`!!!!!!!!!!!!!!!!!!!!!!!!!!!!
- 일단 a,b에 썼던 popular 데이터에 기생충이 있나보다 하고 불러왔으나, 기생충이 없었음
- 그래서 TMDB에서  id가 있는 데이터를 불러와서 id변수를 만들고, url 수정해서 recommendation 데이터도 가져와서 기뻐함.
- 근데 가져온 데이터에도 기생충이 없었음........ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
- TMDB사이트에서  다른 데이터를 찾기 시작함....근데 없어....이미 1시간넘게 써버림ㅋㅋㅋㅋㅋㅋㅋ
- 심지어 파트너도 못찾아서 같이 1시간 30분을 넘게 헤맬 때!!!!! 
- `tmdb.py`에서 ` def movie_id(self, title)`를 발견함........
- 기뻐서 파트너에게 알려줬고, 파트너도 허탈해했다😥😥
- 일단 이걸로 하면 되겠다 싶었는데
- 얘도 만만치 않았음...이미 나는 멘붕이었고.........
- 그래서 완성 했는데 이번엔, `None`을 만들어야 했다ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
- 진짜 `if`문을 넣긴 했는데 한숨만 나온다..



## Problem_e뜻

> 배우, 감독 리스트 출력

```python
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
```

**Review**

- 문제를 잘읽자 ^^  Directing 만 뽑아오라는데 왜 다 뽑아오니 서윤아ㅎㅎㅎ





## Problem_f

> 추가정보 수집

나중에 꼭 해보겠습니다.

[to be updated in time ]

