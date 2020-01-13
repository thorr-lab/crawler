#-*- coding:utf-8 -*-
import datetime

# 현재 시간을 계산하는 함수
def nowDate():
    dt = datetime.datetime.now()
    year = dt.year
    month = "0{}".format(dt.month)if dt.month<10 else dt.month
    day = "0{}".format(dt.day) if dt.day<10 else dt.day
    hour = "0{}".format(dt.hour) if dt.hour<10 else dt.hour
    minute = "0{}".format(dt.minute) if dt.minute<10 else dt.minute 
    second = "0{}".format(dt.second) if dt.second<10 else dt.second 
    timeString = "{}{}{}{}{}{}".format(year,month,day,hour,minute,second)
    return timeString

## 몇달 이전의 시간을 계산해주는 함수
def beforeMonth(bMonth):
    dt = datetime.datetime.now()
    year = dt.year
    month = dt.month
    if month < bMonth:
        # To-Do List
        # - 12개월 이상의 값을 입력해도 동작할 수 있게끔 수정 예정
        year -= 1
        bMonth -= month
        month = 12 - bMonth
    else:
        month -= bMonth
    month = "0{}".format(month)if month<10 else month
    day = "0{}".format(dt.day) if dt.day<10 else dt.day
    hour = "0{}".format(dt.hour) if dt.hour<10 else dt.hour
    minute = "0{}".format(dt.minute) if dt.minute<10 else dt.minute 
    second = "0{}".format(dt.second) if dt.second<10 else dt.second 
    timeString = "{}{}{}{}{}{}".format(year,month,day,hour,minute,second)
    return timeString
