from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def weit_unitil(xpath_str):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url) # url로 이동

weit_unitil('//button[@title = "한 달간 안보기"]')
# 사이트 팝업 직접 끄기 (내가 직접 만듬)
spam = browser.find_element(By.XPATH,'//button[@title = "한 달간 안보기"]')
spam.click()

weit_unitil('//button[text() = "가는 날"]')
# 가는 날 선택 클릭
browser.find_element(By.XPATH, '//button[text() = "가는 날"]').click()

# 이번달 27일, 28일 선택
# browser.find_elements(By.XPATH, '//b[text() = "26"]')[0].click() # [0] -> 이번달
# time.sleep(5)
# browser.find_elements(By.XPATH, '//b[text() = "28"]')[0].click() # [0] -> 이번달

# 다음달 27일 28일 선택
# browser.find_elements(By.XPATH, '//b[text() = "26"]')[1].click() # [1] -> 다음달
# time.sleep(5)
# browser.find_elements(By.XPATH, '//b[text() = "28"]')[1].click() # [1] -> 다음달

weit_unitil('//b[text() = "26"]')
# 이번달 27일, 다음달 28일 선택
browser.find_elements(By.XPATH, '//b[text() = "26"]')[0].click() # [0] -> 이번달
weit_unitil('//b[text() = "28"]')
browser.find_elements(By.XPATH, '//b[text() = "28"]')[1].click() # [1] -> 다음달
weit_unitil('//b[text() = "도착"]')
browser.find_element(By.XPATH, '//b[text() = "도착"]').click()
weit_unitil('//button[text() = "국내"]')
browser.find_element(By.XPATH, '//button[text() = "국내"]').click()
weit_unitil('//i[text() = "제주"]')
browser.find_element(By.XPATH, '//i[text() = "제주"]').click()
weit_unitil('//span[text() = "항공권 검색"]')
browser.find_element(By.XPATH, '//span[text() = "항공권 검색"]').click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div')))
    # 성공했을 때 동작 수행
    print(elem.text) # 첫 번째 결과 출력
finally:
    browser.quit()
    # 실패했을 때, 브라우저 바로 종료

# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div')
# print(elem.text)