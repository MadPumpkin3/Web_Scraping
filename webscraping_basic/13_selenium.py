from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

time.sleep(5)
# 1. 네이버로 이동
browser.get("http://naver.com")

time.sleep(5)
# 2. 로그인 버튼 이동
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

# 3. 아이디와 패스워드를 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

# 5. id를 새로 입력
# browser.find_element(By.ID, "id").send_keys("my_id")
browser.find_element(By.ID, "id").clear() # 해당 element의 값을 지원주는 것(네이버 아이디가 적혀져 있어서 지워줌)
time.sleep(5)
browser.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source) # browser.page_source : 현재 페이지에 있는 모든 html 내용을 모두 가져오는 것

# 7. 브라우저 종료
browser.quit()