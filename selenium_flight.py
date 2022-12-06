import time
from selenium import webdriver
from selenium.webdriver.common.by import By # By = 텍스트 or XPATH or 태그 메인 등 사용하는 확장자를 정해주는 것
# 여기서는 By를 활용해서 XPATH를 사용하기 위해 가져옴.
from selenium.webdriver.support.ui import WebDriverWait # 어떤 element가 나올 때까지 기다리는 조건을 정의하는 것
from selenium.webdriver.support import expected_conditions as EC # 어떤 element가 나올 때까지 기다리는 조건을 정의하는 것

def wait_until(xpath_str): # 해당 조건의 element가 나올 때 까지의 대기 시간 명령 코드를 함수로 제작
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

browser = webdriver.Chrome()
browser.maximize_window

url = 'https://flight.naver.com/'
browser.get(url)

begin_data = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_data.click()

# time.sleep(10) # 10초 대기 (새로운 웹이 로딩되기 전에 명령어 대로 작동하려해서 오류가 생김, 로딩 시간을 기다려 주는 방식으로 해결)
# WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "27"]'))) # time.sleep 대신에 써도 됨.
wait_until('//b[text() = "27"]') # 나올 때 까지 30초 대기
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')
day27[0].click()

day30 = browser.find_elements(By.XPATH, '//b[text() = "30"]')
day30[0].click()

arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

# time.sleep(10)
# WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//button[text() = "국내"]'))) # time.sleep 대신에 써도 됨.
wait_until('//button[text() = "국내"]')
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]') # 구하려는 텍스트와 '완전히 일치'하는 element를 구하는 것
domestic.click()

jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]') # 구하려는 텍스트의 '일부 내용을 포함'하는 emelment를 구하는 것
jeju.click()

search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
# 위 코드 : 해당 조건을 가진 element가 기다리는 조건 시간(30초) 동안 나올 때까지 기다려 보는것 (+안 나오면 다른 코드를 활용해서 경고 또는 차선 설정)
# WebDriverWait(해당 브라우저, 기다리는 시간) : 해당 시간 동안 기다려 달라는 명령문
# until() : 기다리는 조건 입력
# @class = class에서 element를 구할 경우 앞에 '@' 사용하기
# ((By.XPATH ~ )) = 괄호 두 개를 써서 튜플 형태로 만듬.(이유는 모름...)
print(elem.text)

browser.quit()