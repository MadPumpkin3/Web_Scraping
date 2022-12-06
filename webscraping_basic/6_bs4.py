# beautifulsoup4 = 스크래핑을 하기 위한 패키지
# lxml = 구문을 분석하는 파서
# (requests.get한 주소).text = html 문서 값
# 파서란? : 검색해봐야함.

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 우리가 가져온 html 문서를 lxml파서를 통해서 BeautifulSop 객체로 만든 것
# <-- 해당 사이트의 구조를 잘 알고 있을 때 사용하는 방법 -->
# print(soup.title) # html 문서에 있는 element 바로 접근
# print(soup.title.get_text()) # html 문서에 title에 있는 text를 바로 가져오는 것
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력 / soup객체가 가지고 있는 모든 내용 중에서 처음으로 발견되는 'a'태그(element)를 가져오는 것
# print(soup.a.attrs) # attrs : a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href속성 '값' 정보를 출력 / element 내 '키:값'에서 특정 키의 값을 가지고 오고 싶을 때 ["키"] 입력

# <-- 해당 사이트의 구조를 잘 모르고 있을 때 사용하는 방법 -->
# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a element를 찾아줘 
# find : 설정한 조건에 해당하는 값 중에 '처음'으로 발견되는 element를 가져오기
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 '어떤' element를 찾아줘 
# class명이 1개 밖에 없을 때는 element(태그) 없이 가능

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling) # next_sibling : 해당 element에서 다음 element로 출력
# (웹페이지상 줄바꿈이 있을 경우, sibling 한 번으로는 결과가 안 뜰 수 있음)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank1.next_sibling.next_sibling.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # previous_sibling : 해당 element에서 이전 element 출력
# print(rank2.a.get_text())
# print(rank1.parent) # parent : 해당 element 기준에서 부모 element로 이동 후, 모든 자식 element 출력
# rank2 = rank1.find_next_sibling("li") 
# find_next_sibling('n') : 해당 element 기준에서 다음 element 중 n(태그) 조건에 맞는 첫 번째 element 출력
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li") 
# find_previous_sibling('n') : 해당 element 기준에서 이전 element 중 n(태그) 조건에 맞는 첫 번째 element 출력
# print(rank2.a.get_text())

# print(rank1.find_next_siblings('li'))

webtoon = soup.find("a", text = "재벌집 막내아들-10화") 
# find("a", text = "n") : a 태그이면서 "n" text가 포함된 태그들의 내용을 가져옴.
print(webtoon) 