import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # csv파일을 엑셀 프로그램으로 열고 싶으면 encoding을 "utf-8-sig"로 바꾸자(기본 "utf8"
# newline : 공백라인을 없이 저장(csv 파일은 기본적으로 데이터 간 enter로 공백라인이 생긴다)
writer = csv.writer(f) # 스크래핑한 데이터를 csv파일로 바꿔서 넣어주는 라이브러리 

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") 
# split("\t") : 데이터 사이 간에 tab으로 구분되어 있는 것을 split 형태로 바꿔주는 것 ["N", "종목명", "현재가", ...]
print(type(title)) # title 변수가 리스트형인지 확인 
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url+ str(page))
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip(줄 바꾸기를 위한 td는 필요 없기 때문에 td 태그가 1이하인 것은 거르기)
            continue
        data = [column.get_text().strip() for column in columns] # strip : 불필요한 것들은 제거하는 함수
        # print(data)
        writer.writerow(data) # 반복문과 조건문을 통해 얻은 data를 배열로 정렬하여 넣는다. (무조건 리스트 형태로 넣어야 한다.)