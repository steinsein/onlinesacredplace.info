import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl

# 디씨 HIT 갤 게시물 정보 스크래핑
URL = "https://gall.dcinside.com/board/lists/?id=hit"
# 크롬드라이버 경로 설정
chromedriver = "./chromedriver.exe"

# 크롬드라이버 설정
def driver_open(chromedriver):
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920x1080")
    options.add_argument("headless")
    options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(chromedriver, options=options)
    return driver

# 게시물 페이지 수 구하기
def get_last_page(URL):
    driver = driver_open(chromedriver)
    driver.get(URL)
    last_page = driver.find_element(By.CLASS_NAME,"sp_pagingicon.page_end")
    n = int(last_page.get_attribute('href')[-3:])
    return n

# 전체 게시물 정보 수집
def scrapping_titleinfo(URL):
    n = get_last_page(URL)
    # n = 4
    print(f"마지막 페이지:{n}")
    time.sleep(2)
    driver = driver_open(chromedriver)
    print("사이트 접근 성공")
    time.sleep(2)
    nums = []
    titles = []
    reply_nums = []
    writers = []
    dates = []
    gall_cnts = []
    gall_recomms = []
    post_urls = []
    rl = '운영자'
    for i in range(1, n+1):
        url = URL + f"&page={i}"
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        gall_listwrap = soup.find("div", "gall_listwrap list")
        titleinfos = gall_listwrap.find_all("table")
        for titleinfo in titleinfos:
            posts = titleinfo.find_all("tr")
            for post in posts:
                post2 = post.find("td", "gall_num")
                name = post.find("td", "gall_writer ub-writer")
                if not post2 == None:
                    if not name == None:
                        if not name.get_text() == rl:
                            num = post2.get_text()
                            nums.append(num)
                            title = "None" if post.find("td", "gall_tit ub-word") == None else post.find("td", "gall_tit ub-word").get_text()
                            titles.append(title)
                            reply_num = post.find("span", "reply_num").get_text()
                            reply_nums.append(reply_num[1:-1])
                            writer = name.get_text()
                            writers.append(writer)
                            date = post.find("td", {"class": "gall_date", "title": True})["title"]
                            dates.append(date)
                            gall_cnt = post.find("td", "gall_count").get_text()
                            gall_cnts.append(gall_cnt)
                            gall_recomm = post.find("td", "gall_recommend").get_text()
                            gall_recomms.append(gall_recomm)
                            post_url = post.find("a", class_="reply_numbox")["href"]
                            post_urls.append(post_url)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        print(f"{i}번째 수집완료")
        time.sleep(2)
    titleifo_dics = {
        "번호":nums,
        "제목":titles,
        "댓글수":reply_nums,
        "글쓴이":writers,
        "작성일":dates,
        "조회수":gall_cnts,
        "추천":gall_recomms,
        "주소":post_urls,
    }
    return titleifo_dics

#엑셀, csv 파일로 저장
def save_data(dics,name):
    df = pd.DataFrame(dics)
    df.to_csv(f"./{name}.csv")
    df.to_excel(f"./{name}.xlsx")
    return df

# print(scrapping_titleinfo(URL))
titleifo_dics = scrapping_titleinfo(URL)
df = save_data(titleifo_dics,"hitgall_list")