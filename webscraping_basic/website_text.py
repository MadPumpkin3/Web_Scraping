import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies?hl=ko&gl=KR"
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Language":"ko-KR,ko"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")

data = soup.find_all("div", attrs={"class":"Epkrse "})

print(data.text())