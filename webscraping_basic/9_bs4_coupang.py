import requests  # HTML의 데이터를 다운로드 받는 라이브러리(BeautifulSoup과 한 몸)
import re
from bs4 import BeautifulSoup # 다운로드 받은 HTML 데이터에서 필요한 데이터를 추출하는 라이브러리(requests와 한 몸)
import time

headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
# 중요! 쿠팡의 경우 headers 옵션에 해당 데이터를 추가하기 > {"Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) # re(정규식)활용 : compile(^) = OO으로 시작하는 단어(이유 : 광고 상품은 class 명이 약간 다르기 때문에)
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    
    # 광고 제품은 제외
    ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
    best_seller = item.find("dl", attrs={"class":"best-seller-search-product-wrap"})
    if ad_badge:
        print("  < 광고 상품은 제외합니다.")
        continue
    
    if best_seller:
        # print("  < 베스트셀러 상품은 제외합니다.")
        continue
    
    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    
    # 애플 제품 제외
    if "Apple" in name:
        print("  < Apple 상품 제외합니다.")
        continue
    
    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        print("  < 평점 없는 상품 제외합니다.")
        continue
    
    rate_count = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
    if rate_count:
        rate_count = rate_count.get_text() # 예: (26) 문자형이 있어 정수형으로 못 바꿈
        rate_count = rate_count[1:-1]
        # print("리뷰 수", rate_count)
    else:
        print("  < 평점 수 없는 상품 제외합니다.")
        continue
    
    if float(rate) >= 4.5 and int(rate_count) >= 100:
        print(name, price, rate, rate_count)