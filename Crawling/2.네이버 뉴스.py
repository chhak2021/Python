"""
날짜 : 2023/01/16
이름 : 김철학
내용 : 파이썬 네이버 뉴스 크롤링 실습하기
"""
import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

# 엑셀파일 생성
workbook = Workbook()
sheet = workbook.active

pg = 1
count = 1

while True:
    # HTML 요청
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&page=%d' % pg
    html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    #print(html)

    # 문서 객체 생성
    dom = bs(html, 'html.parser')

    currentPage = dom.select_one('#main_content > div.paging > strong').text
    
    if pg != int(currentPage):
        break

    # 데이터 파싱
    tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
    print('tit :', tit)

    lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')
    for li in lis:
        tag_a = li.select_one('dl > dt:not(.photo) > a')
        title = tag_a.text
        href = tag_a['href']

        sheet.append([count, title.strip(), href.strip()])
        print('%d건...' % count)
        #print('count :', count)
        #print('title :', title.strip())
        #print('href :', href.strip())
        count += 1   
        
    pg += 1

# 엑셀 저장/종료
workbook.save('C:/Users/java2/Desktop/NaverNews.xlsx')
workbook.close()

print('프로그램 종료...')