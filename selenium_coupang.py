from selenium import webdriver
from selenium.webdriver.common.by import By  # 레서드를 하나로 묶어주는 역할
import time

driver = webdriver.Chrome()

# 쿠팡의 식품 카테고리로 이동
driver.get("https://www.coupang.com/np/categories/194276")
time.sleep() # 드라이버의 독점 Chrome 창이 뜨기까지 시간이 걸리기 때문에 이거 해주면 좋다.

lis = driver.find_element(By.ID, 'productList').find_elements(By.TAG_NAME, 'li')

for li in lis:
    try:
        print('Product: ' + li.find_element(By.CLASS_NAME, 'name').text)
        print('Price: ' + li.find_element(By.CLASS_NAME, 'price-value').text)
        print('Delivery: ' + li.find_element(By.CLASS_NAME, 'delivery').text)
        print('URL: ' + li.find_element(By.CLASS_NAME, 'baby-product-link').get_attribute('href'))
        print('-'*100)
        
    except Exception:
        pass
    
driver.quit()