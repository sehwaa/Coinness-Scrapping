# webdriver를 통해서 chrome 창을 하나 자동으로 띄워줌
from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("../Downloads/chromedriver 2") #chrome webdriver가 설치된 경로
driver.get("https://coinness.live/")

time.sleep(3)

# 더보기 버튼 계속 클릭
count = 0
while count < 1:
    time.sleep(5)
    more_btn = driver.find_element_by_xpath("//button[@class='sc-jcVcSv fZwKox pc-only']")
    more_btn.click()
    count += 1

# 데이터 수집
# 웹 드라이버가 렌더링한 모든 html 소스를 가져오기
html_doc = driver.page_source
# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')
# find(attrs={}) : attrs는 속성으로 검색 의미
# soup.find(attrs={"class": "sc-dlfnuX ekpcff"})은, class 이름이 sc-dlfnuX ekpcff인 태그를 찾으라는 의미
main_text = soup.find(attrs={"class": "sc-dlfnuX ekpcff"})

#.contents: 찾은 태그의 하위 노드들을 리스트 형태로 반환함
for c in main_text.contents:
    date = c.find(attrs={"class": "sc-hKgJU6U cRhYVI"})
    if date is not None: 
        print(date.get_text())
    
    feeds = c.find(attrs={"class": "sc-iUuxjF dZUdAm"})
    if feeds is not None:
        for feed in feeds.contents:
            try:
                clock = feed.find(attrs={"class": "sc-iBPTik uPtFx"}).get_text()
                print(clock)
            except:
                continue
