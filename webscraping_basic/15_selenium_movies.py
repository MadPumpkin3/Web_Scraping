# requests로 동적화면(실시간으로 업데이트 되는 화면) 진행하기(효율이 좋지 않음)

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies"
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Language":"ko-KR,ko"}

res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)

# for movie in movies:
#     title = movie.find("div", attrs=["title"])
#     print(title.text)