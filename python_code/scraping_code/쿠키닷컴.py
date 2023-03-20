import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl

# 쿠키닷컴 게시글 사이트 주소
URL = "https://gall.dcinside.com/board/view/?id=hit&no=12&page=1"
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


# 댓글 페이지 수 구하기
def get_last_page(URL):
    driver = driver_open(chromedriver)
    driver.get(URL)
    last_page = driver.find_element(By.CLASS_NAME,"sp_pagingicon.page_end")
    n = int(last_page.get_attribute('href')[-8:-5])
    return n


# 전체 댓글 수집
def scrapping_comments(URL):
    n = get_last_page(URL)
    print(f"마지막 페이지:{n}")
    time.sleep(2)
    driver = driver_open(chromedriver)
    driver.get(URL)
    print("사이트 접근 성공")
    time.sleep(2)
    nicks = []
    usertxts = []
    dates = []
    for i in range(1, n+1):
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        comment_box = soup.find("div","comment_box")
        comments = comment_box.find_all("li")
        for comment in comments:
            if comment.get("class") == ["ub-content"]:
                #삭제된 댓글 제외
                if comment.find(class_="del_reply") is None:
                    nick = comment.find("div","cmt_nickbox").text
                    nicks.append(nick)
                    usertxt = comment.select_one("div.clear.cmt_txtbox").text
                    usertxts.append(usertxt)
                    date = comment.find("span","date_time").text
                    dates.append(date)
                else:
                    pass
            # 닉네임이 댓글도리인 경우 제외
            elif comment.get('class') == ['ub-content','dory']:
                pass
            else:
                pass
        print(f"{i}번째 수집완료")
        driver.execute_script(f"viewComments({i+1},'D')")
        time.sleep(2)
    comment_dics = {
        "닉네임":nicks,
        "댓글":usertxts,
        "날짜":dates,
    }
    return comment_dics

#엑셀, csv 파일로 저장
def save_data(dics,name):
    df = pd.DataFrame(dics)
    df.to_csv(f"./{name}.csv")
    df.to_excel(f"./{name}.xlsx")
    return df