from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url) # url로 이동

time.sleep(5)
# 사이트 팝업 직접 끄기 (내가 직접 만듬)
spam = browser.find_element(By.XPATH,'//button[@title = "한 달간 안보기"]')
spam.click()

time.sleep(5)
# 가는 날 선택 클릭
browser.find_element(By.XPATH, '//button[text() = "가는 날"]').click()

time.sleep(5)
# 이번달 27일, 28일 선택
# browser.find_elements(By.XPATH, '//b[text() = "26"]')[0].click() # [0] -> 이번달
# time.sleep(5)
# browser.find_elements(By.XPATH, '//b[text() = "28"]')[0].click() # [0] -> 이번달

# 다음달 27일 28일 선택
# browser.find_elements(By.XPATH, '//b[text() = "26"]')[1].click() # [1] -> 다음달
# time.sleep(5)
# browser.find_elements(By.XPATH, '//b[text() = "28"]')[1].click() # [1] -> 다음달

# 이번달 27일, 다음달 28일 선택
browser.find_elements(By.XPATH, '//b[text() = "26"]')[0].click() # [0] -> 이번달
time.sleep(5)
browser.find_elements(By.XPATH, '//b[text() = "28"]')[1].click() # [1] -> 다음달

browser.find_element(By.XPATH, '//b[text() = "도착"]').click()
time.sleep(5)
browser.find_element(By.XPATH, '//button[text() = "국내"]').click()
browser.find_element(By.XPATH, '//i[text() = "제주"]').click()
time.sleep(5)
browser.find_element(By.XPATH, '//span[text() = "항공권 검색"]').click()

while True:
    pass