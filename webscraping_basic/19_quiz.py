import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%B6%80%EC%B2%9C+%EB%A7%A4%EB%A7%A4"
headers = {"user=agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

reals = soup.find_all("ol", attrs={"class":"list_place"})
print(len(reals))

for real in reals:
    trans_data = real.find("div", attrs={"class":"wrap_tit"}).get_text()
    trans = trans_data[2:4]
    area_data = real.find("span", attrs={"title":"공급 1,047.86평 / 전용 888.44평"}).get_text()
    area = area_data