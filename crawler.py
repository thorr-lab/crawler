# -*- coding: utf-8 -*-
from selenium import webdriver
import thorrTime

# 크롬 드라이버 동작
driver = webdriver.Chrome('./chromedriver')

# KISA 링크 
# driver.get('https://www.kisa.or.kr/main.jsp')

# 한글이 안되는 경우 string 앞에 u를 붙여준다.
searchKeyword = u"블록체인"

# # 검색 창에 검색
driver.find_element_by_xpath('//*[@id="srch"]').send_keys(searchKeyword)
driver.find_element_by_xpath('//*[@id="srchBtn"]').click()

# 공지사항에 최근 블록체인 공지를 조회
endDate = thorrTime.nowDate() # 현재의 시간
startDate = thorrTime.beforeMonth(6) # 과거의 시간
# 검색을 하기 위해서는 과거 - 현재 순으로 시간을 입력해준다
getUrl = u"https://search.kisa.or.kr/search/searchDetail.jsp?indent=on&version=2.2&start=0&rows=10&fl=*%2Cscore&hl=on&hl_fl=subject&debugQuery=&explainOther=&qt=standard&facet=false&facet_field=cat1&sortField=wdate&cat3=02&field=all&cat1=&keyword={}&keyword2={}&cat2=&startDate={}&endDate={}".format(searchKeyword,searchKeyword,startDate,endDate)
getUrl = getUrl.encode('utf-8')

# 1. 아예 get 요청으로 공지사항 리스트를 불러오자
driver.get(getUrl)

# # 총 검색해야하는 갯수, 현재 동작 안하는 변수
# totalBoardCount = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[3]/div[2]/h1') 
# print(totalBoardCount)

# 동적페이지에서 결과를 얻어냈고, 해당 페이지의 결과를 request 혹은 bs4 를 사용해서 불러와야겠다

