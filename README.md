# 웹 크롤러
> '자동화된 툴을 가지고, 웹 사이트에서 정보를 가져오는 프로그램'

### 제작동기
> 회사 업무에서 검색할 일이 많아서 검색 결과를 요약하기 위해서

### 환경
> Python, Selenium, BS4, Chrome Driver, VS Code

### Python 한글 세팅
- 파이썬의 기본 문자열 인식 방식 : unicode
- 코드 젤 위에 다음과 같이 작성한다.
```python
#-*- coding:utf-8 -*-
```
- 파이썬 내부에서 한글 입력시 유니코드 문자로 인코딩을 해주자
```python
string = u"나 문자열임"
```

### re 라이브러리 에러, 'TypeError: expected string or bytes-like object'
들어가는 값이 str()로 감싸지면 해결됌
``` python
# 이렇게 하면 에러남
re.sub('패턴','바꿀 문자열','들어가는 값',바꿀횟수)
# 이렇게 하면 고쳐짐
re.sub('패턴','바꿀 문자열',str('들어가는 값'),바꿀횟수)
```

### Install Link

- Python : https://www.python.org/
- Selenium, BS4, request
    ``` shell
    pip install selenium
    pip install bs4
    pip install requests
    ```
- 크롬 드라이버 설치시 크롬을 키고 주소창에 chrome://settings/help 를 입력해 버전을 확인하고 그 버전을 설치.
- Chrome Driver : https://chromedriver.chromium.org/downloads

### Develop Story
- 2020.01.01 : README 작성, 크롬 드라이버 실행 테스트
- 2020.01.03 : 기간 검색을 위한 datetime 라이브러리 사용
- 2020.01.04 : time.py 세부 내용 수정
- 2020.01.05 : Story Update
- 2020.01.07 : time.py -> thorrTime.py, '몇 달전 함수' 생성
- 2020.01.08 : driver.py, thorrTime.py 적용 후 테스트
- 2020.01.11 : dirver.py. 페이지 넘버 조회 기능 추가, 정규표현식 사용 및 추가 아이디어 생각


### Reference
- crawler 
    - 셀레니움 : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
    - href 부분 크롤 방법 : https://toentoi.tistory.com/43
- requests
    - reqeusts 사용법 : https://dgkim5360.tistory.com/entry/python-requests
- robots.txt
    - 작성양식 : https://support.google.com/webmasters/answer/6062596?hl=ko
- 정규표현식 
    - 사용방법 : https://wikidocs.net/4308