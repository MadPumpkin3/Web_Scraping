import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%B6%80%EC%B2%9C+%EB%A7%A4%EB%A7%A4"
headers = {"user=agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

reals = soup.find_all("div", attrs={"class":"cont_place"})
count = 0

for real in reals:
    count += 1
    trans_data = real.find("div", attrs={"class":"wrap_tit"}).get_text()
    trans = trans_data[2:4]  # 거래 종류
    area_height_data = real.find_all("span", attrs={"class":"f_eb"}) # 면적 및 층 정보
    area = area_height_data[1].get_text() # 면적
    height = area_height_data[2].get_text() # 층
    valus_data = real.find("span", attrs={"class":"f_red"}).get_text()
    valus = valus_data # 가격
    address_data = real.find("div", attrs={"class":"info_more"}).get_text()
    address = address_data[9:] # 주소
    print("="*10, f"매물 {count}", "="*10)
    print("거래 :",trans)
    print(f"면적 : {area} (공급/전용)")
    print(f"가격 : {valus} (만원)")
    print("주소 :",address)
    print("층 :",height)