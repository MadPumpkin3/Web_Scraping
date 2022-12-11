# 터미널로 진행한 selenium 기본 기능 기록

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # 키 값을 직접 입력할 수 있는 명령어

browser = webdriver.Chrome()
browser.get("https://www.naver.com/")

elem = browser.find_element(By.CLASS_NAME, "link_longin")

elem = browser.find_element(By.ID, "query")
elem.send_keys("나도코딩") # 해당 element의 키 값을 입력해주는 함수(네이버 검색 창에 '나도코딩'이라고 입력 됨.)
elem.send_keys(Keys.ENTER) # 해당 element에서 키 값을 ENTER로 해주는 것(네이버 검색창에서 ENTER 치는 것과 동일한 작동)

elem = browser.find_elements(By.TAG_NAME, "a")

for e in elem:
    e.get_attribute("href") # 해당 element가 가지는 attribute의 값을 가지고 올 수 있음.

browser.get("http://daum.net")

elem = browser.find_element(By.NAME, "q")
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
browser.back()

elem = browser.find_element(By.NAME, "q")
elem.send_keys("나도코딩")
elem = browser.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')  # XPATH를 활용하여 '검색'버튼을 가져옴.
elem.click()

browser.click() # 내가 제어하는 웹브라우저에서 원는 element를 대신 클릭해주는 함수
browser.back() # 내가 제어하는 웹브라우저의 현재 사이트에서 뒤로가기
browser.forward # 내가 제어하는 웹브라우저의 현재 사이트에서 앞으로가기
browser.refresh() # 내가 제어하는 웹브라우저를 새로고침한다.
browser.close() # 현재 열려있는 탭만 닫음.
browser.quit() # 브라우저 자체를 닫음.