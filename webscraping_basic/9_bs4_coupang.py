import requests  # HTML의 데이터를 다운로드 받는 라이브러리(BeautifulSoup과 한 몸)
import re
from bs4 import BeautifulSoup # 다운로드 받은 HTML 데이터에서 필요한 데이터를 추출하는 라이브러리(requests와 한 몸)
import time

headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
# 중요! 쿠팡의 경우 headers 옵션에 해당 데이터를 추가하기 > {"Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=194176&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) # re(정규식)활용 : compile(^) = OO으로 시작하는 단어
print(items[0].find("div", attrs={"class":"name"}).get_text())