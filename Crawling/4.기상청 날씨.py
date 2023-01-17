"""
날짜 : 2023/01/17
이름 : 김철학
내용 : 파이썬 기상청 날씨 크롤링 실습하기
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1',
                        user='root',
                        password='1234',
                        db='java2db',
                        charset='utf8')

# SQL 실행객체 생성
cur = conn.cursor()

# 가상 브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 지역명 출력
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    # SQL 실행
    sql = "INSERT INTO `weather` SET "
    sql += "`col1`={},".format('null' if tds[0].text.strip() == '' else "'"+tds[0].text+"'")
    sql += "`col2`={},".format('null' if tds[1].text.strip() == '' else "'"+tds[1].text+"'")
    sql += "`col3`={},".format('null' if tds[2].text.strip() == '' else "'"+tds[2].text+"'")
    sql += "`col4`={},".format('null' if tds[3].text.strip() == '' else "'"+tds[3].text+"'")
    sql += "`col5`={},".format('null' if tds[4].text.strip() == '' else "'"+tds[4].text+"'")
    sql += "`col6`={},".format('null' if tds[5].text.strip() == '' else "'"+tds[5].text+"'")
    sql += "`col7`={},".format('null' if tds[6].text.strip() == '' else "'"+tds[6].text+"'")
    sql += "`col8`={},".format('null' if tds[7].text.strip() == '' else "'"+tds[7].text+"'")
    sql += "`col9`={},".format('null' if tds[8].text.strip() == '' else "'"+tds[8].text+"'")
    sql += "`col10`={},".format('null' if tds[9].text.strip() == '' else "'"+tds[9].text+"'")
    sql += "`col11`={},".format('null' if tds[10].text.strip() == '' else "'"+tds[10].text+"'")
    sql += "`col12`={},".format('null' if tds[11].text.strip() == '' else "'"+tds[11].text+"'")
    sql += "`col13`={},".format('null' if tds[12].text.strip() == '' else "'"+tds[12].text+"'")
    sql += "`col14`={},".format('null' if tds[13].text.strip() == '' else "'"+tds[13].text+"'")
    sql += "`rdate`=NOW();"  

    cur.execute(sql)
    conn.commit()
    print('Insert 완료...')


# 데이터베이스 종료
conn.close()

# 가상 브라우저 종료
browser.close()

print('프로그램 종료...')