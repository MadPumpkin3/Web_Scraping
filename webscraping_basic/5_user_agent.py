# 사이트에 사용자가 접속할 때, 사이트는 사용자의 헤더 정보에 따라 다른 화면을 보여준다.(데스크탑 > 기본 사이트 화면, 스마트폰 > 온라인 전용 화면)
# www.whatismybrowser.com > user agent string = 브라우저 접속 시 유저 agent 정보

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
print("응답코드 :", res.status_code)

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)