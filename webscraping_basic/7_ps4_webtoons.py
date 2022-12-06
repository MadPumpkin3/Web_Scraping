import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title인 모든 "a" element 를 반환
count = 0
for cartoon in cartoons:
    count += 1
    print(cartoon.get_text())
print(f'현재 웹사이트에 있는 네이버 웹툰의 갯수는 {count}개 이다.')

