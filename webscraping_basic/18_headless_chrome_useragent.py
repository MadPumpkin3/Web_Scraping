from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# headless를 사용하면 user-agent가 'Chrome'이 아닌 'HeadlessChrome' 설정되면서 웹사이트 접속이 '차단'될 수 있다.
# 기존 user-agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
# headless 적용 user-agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/108.0.5359.124 Safari/537.36

options = webdriver.ChromeOptions()
options.headless = True
# 브라우저를 직접 띄어 실행하는 selenium의 단점을 보완하기 위해 브라우저를 안 띄우고 백그라운드에서 브라우저를 실행하는 방법(메모리 절약 가능)
options.add_argument("window-size=2560x1600")
# 백그라운드에서 실행되는 브라우저의 크기를 지정
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
# headless로 인한 user-agent 문제를 해결하기 위한 방법

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

detected_value = browser.find_element(By.ID, "detected_value")
print(detected_value.text)
browser.quit()

# 추가 정리
# XPath : element의 경로, 특징(id, class, text)를 가지고 이동

