from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies?hl=ko&gl=KR"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1600 위치로 스크롤 내리기(해상도 길이에 맞게 안 내려도 됨)
# browser.execute_script("window.scrollTo(0, 1600)") # mac 해상도 2560x1600

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
# 로딩된 페이지의 맨 아래로 스크롤 내림(내려진 후의 추가 로딩 화면은 포함x)
time.sleep(10)

interval = 2  # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행:
while True:
    # 스크롤을 가장 아래에 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(interval)
    
    # 현재  문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
    
print("스크롤 완료")

from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs={"class":["ULeU3b neq64b", "Vpfmgd"]}) # 리스트형으로 묶으면 두 개의 클래스를 중 하나라도 맞으면 참
# movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))


# while True:
#     conti = input("계속 진행할까요? : ")
#     if "y" == conti:
#         break
#     else:
#         pass
# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    titles = movie.find("div", attrs={"class":["Epkrse", "Epkrse "]})
    if titles != None:
        title = titles.get_text()
        # 할인 전 가격
        original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
        if original_price:
            original_price = original_price.get_text()
        else:
            # print(title, " <할인되지 앟은 영화 제외>")
            continue
        
        # 할인된 가격
        price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()
        
        # 링크
        link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc"})["href"]
        # 올바른 링크 : https://play.google.com + link
        
        print(f"제목 : {title}")
        print(f"할인 전 금액 : {original_price}")
        print(f"할인 후 금액 : {price}")
        print("링크 : ", "https://play.google.com" + link)
        print("-" * 120)

browser.quit()

# for movie in movies:
#     title = movie.find("div", attrs=["title"])
#     print(title.text)

# 브라우저 창 유지를 위해 설정
# while True:
#     pass