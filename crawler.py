#-*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import thorrTime
import time

# 크롬 드라이버 동작
driver = webdriver.Chrome('./chromedriver')

searchKeyword = u"블록체인"

# 공지사항에 최근 공지를 조회
endDate = thorrTime.nowDate() # 현재의 시간
startDate = thorrTime.beforeMonth(6) # 과거의 시간
# 검색을 하기 위해서는 과거 - 현재 순으로 시간을 입력해준다
getUrl = u"https://search.kisa.or.kr/search/searchDetail.jsp?indent=on&version=2.2&start=0&rows=10&fl=*%2Cscore&hl=on&hl_fl=subject&debugQuery=&explainOther=&qt=standard&facet=false&facet_field=cat1&sortField=wdate&cat3=02&field=all&cat1=&keyword={}&keyword2={}&cat2=&startDate={}&endDate={}".format(searchKeyword,searchKeyword,startDate,endDate)

# 1. 아예 get 요청으로 공지사항 리스트를 불러오자 z
driver.get(getUrl)
html = driver.page_source
soupData = BeautifulSoup(html, 'html.parser')

# 2. count는 읽어올 게시글 수
count = str(soupData.select('#contents > div.content_inner > div.section.mbi_wrap > div.section.result.first > h1 > span:nth-child(2)'))
count=re.sub('<.+?>', '', count, 0).strip()
# re.sub('패턴','바꿀 문자열','문자열',바꿀횟수)
count = int(count[1:-1])

# 3. 공지 데이터 가져오기
noticeTitleList = []
noticeLinkList = []
noticeContentsList = []

for i in range(1, 11 if count>10 else count+1, 1):
    noticetitle = soupData.select("#contents > div.content_inner > div.section.mbi_wrap > div.section.result.first > ul > li:nth-child({}) > dl > dt > a".format(i))
    noticetitle = re.sub('<.+?>', '', str(noticetitle), 0).strip()
    noticetitle = noticetitle[1:-1]
    noticeTitleList.append(noticetitle)

for href in soupData.find("div", class_="section result first").find_all("li"):
    noticeLink = href.find('a')["href"]
    noticeLinkList.append(noticeLink)

print(noticeLinkList)

# 5. 각 링크 데이터 조회하는거 추가하기
for linkcount in range(len(noticeLinkList)):
    driver.get(noticeLinkList[linkcount])
    noticeData = driver.page_source
    noticeSoup = BeautifulSoup(noticeData, 'html.parser')
    noticeContent = noticeSoup.select("#content_inner > div > table.bbs_view.clr_m4 > tbody > tr:nth-child(5)")
    noticeContent = re.sub('<.+?>', '', str(noticeContent), 0).strip()
    noticeContentsList.append(noticeContent)
    time.sleep(1)

# 4. csv 파일로 내용 정리하기
result = []

if len(noticeTitleList) == len(noticeLinkList):
    for i in range(len(noticeTitleList)):
        result.append([noticeTitleList[i],noticeLinkList[i],noticeContentsList[i]])
data = pd.DataFrame(result)
data.columns = ["Title", "Link", "Contents"]
data.to_csv(u'KISA크롤링결과.csv', encoding="utf-8")