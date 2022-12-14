import requests
from bs4 import BeautifulSoup
import time
import re

# Project) 웹 스크래핑을 이용하여 나만의 비서를 만드시오.

# [조건]
# 1. 네이버에서 오늘 부천의 날씨정보를 가져온다
# 2. 헤드라인 뉴스 3건을 가져온다
# 3. IT 뉴스 3건을 가져온다
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다.

def create_soup(url):
    headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("  (링크 : {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    weather_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%B2%9C+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=hJsEkdp0Yihss5L9gGwssssssBR-291564"
    dust_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EB%B6%80%EC%B2%9C%EC%8B%9C+%EC%86%8C%EC%82%AC%EB%B3%B8%EB%8F%99+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EB%B6%80%EC%B2%9C%EC%8B%9C+%EC%9B%90%EB%AF%B8%EB%8F%99+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&tqi=hJsYvdp0Jy0ssasmG1sssssssJ0-443099"
    weather_soup = create_soup(weather_url)
    dust_soup = create_soup(dust_url)
    # 흐림, 어제보다 oo 높아요
    cast = weather_soup.find("p", attrs={"class":"summary"}).get_text()
    # 현재 00c (최저 00 / 최고 00)
    curr_temp = weather_soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("°", "")
    min_temp = weather_soup.find("span", attrs={"class":"lowest"}).get_text() # 최저 온도
    max_temp = weather_soup.find("span", attrs={"class":"highest"}).get_text() # 최고 온도
    # 오전 강수 확률 00% / 오후 강수 확률 00%
    weathers = weather_soup.find_all("span", attrs={"class":"weather_left"})
    am_weather = weathers[0].get_text() # 오전 강수
    pm_weather = weathers[1].get_text() # 오후 강수
    # 미세먼지 농도
    dust_list = dust_soup.find("div", attrs={"class":"detail_content"})
    dust_value = dust_list.find_all("span", attrs={"class":"num _value"})
    dust_text = dust_list.find_all("span", attrs={"class":"text _text"})
    fine_dust_value = dust_value[0].get_text()
    fine_dust_text = dust_text[0].get_text()
    ultrafine_dust_value = dust_value[1].get_text()
    ultrafine_dust_text = dust_text[1].get_text()
    
    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(am_weather, pm_weather))
    print()
    print("미세먼지 :", fine_dust_value, fine_dust_text)
    print("초미세먼지 :", ultrafine_dust_value, ultrafine_dust_text)
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    news_list = soup.find_all("div", attrs={"class":"cjs_journal_wrap _item_contents"})
    for index, news_titles in enumerate(news_list):
        if index < 5:
            title = news_titles.find("div", attrs={"class":"cjs_t"}).get_text()
            link = news_titles.find("a")["href"]
            # print(f"----------뉴스{index+1}----------")
            print_news(index, title, link)
        else:
            break
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3) # 3개까지만 가져오기
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a 태그의 정보를 사용
            
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때, index기준 4~7까지 잘라서 가져옴
        print(sentence.get_text().strip())
    
    print()
    
    print("(한글지문)")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때, index기준 0~3까지 잘라서 가져옴
        print(sentence.get_text().strip())
    print()
    
if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    scrape_it_news() # IT 뉴스 정보 가져오기
    scrape_english() # 오늘의 영어 회화 가져오기