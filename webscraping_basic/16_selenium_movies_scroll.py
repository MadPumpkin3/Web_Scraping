# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies"
# headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Language":"ko-KR,ko"}

# res = requests.get(url, headers=headers)
# res.raise_for_status
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
# print(len(movies))

# # with open("movie.html", "w", encoding="utf8") as f:
# #     # f.write(res.text)
# #     f.write(soup.prettify()) # html 문서를 예쁘게 출력

# for movie in movies:
#     title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
#     print(title)

# # for movie in movies:
# #     title = movie.find("div", attrs=["title"])
# #     print(title.text)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies"
browser.get(url)
chains = webdriver.ActionChains(browser)

# 스크롤 내리기
# 모니터(해상도) 높이인 1600 위치로 스크롤 내리기
movies = browser.find_elements(By.CLASS_NAME, "ULeU3b neq64b")

chains.move_to_element(movies[3]).click()

chains.pause(5)


while True:
    pass