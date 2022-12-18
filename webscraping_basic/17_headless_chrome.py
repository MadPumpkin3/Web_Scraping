from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.headless = True
# 브라우저를 직접 띄어 실행하는 selenium의 단점을 보완하기 위해 브라우저를 안 띄우고 백그라운드에서 브라우저를 실행하는 방법(메모리 절약 가능)
options.add_argument("window-size=2560x1600")
# 백그라운드에서 실행되는 브라우저의 크기를 지정

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies?hl=ko&gl=KR"
browser.get(url)

time.sleep(5)

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
browser.get_screenshot_as_file("google_movie.png") # 백그라운드로 실행되는 브라우저의 해당 부분 실행 장면을 캡처

from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

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