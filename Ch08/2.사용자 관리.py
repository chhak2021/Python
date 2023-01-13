"""
날짜 : 2023/01/13
이름 : 김철학
내용 : 파이썬 사용자 관리 프로그램 실습
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234', 
                        db='java2db', 
                        charset='utf8')

while True:
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0

    try:
        answer = int(input('선택 : '))
    except:
        print('숫자를 입력하세요.')
        continue

    if answer == 0:
        break
    elif answer == 1:
        user = list(input('아이디, 이름, 휴대폰, 나이 순으로 입력 : ').split())

        cur = conn.cursor()
        sql = "insert into `user3` values ('%s', '%s', '%s', '%s')"
        cur.execute(sql % (user[0], user[1], user[2], user[3]))
        conn.commit()

        print('등록완료...')

    elif answer == 2:
        cur = conn.cursor()        
        cur.execute("select * from `user3`")
        conn.commit()

        print('----------------------------')
        for row in cur.fetchall():            
            print('|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3]))            

        print('조회완료...')

    elif answer == 3:
        name = input('이름 검색 : ')
        cur = conn.cursor()        
        cur.execute("select * from `user3` where `name`='%s'" % name)
        conn.commit()

        print('----------------------------')
        for row in cur.fetchall():            
            print('|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3]))            

        print('검색완료...')
    elif answer == 4:
        name = input('삭제 이름 : ')
        cur = conn.cursor()        
        cur.execute("delete from `user3` where `name`='%s'" % name)
        conn.commit()
        print('삭제완료...')
    else:
        print('0 ~ 4 중에서 입력하세요.')
    

# 데이터베이스 종료
conn.close()
print('프로그램 종료...')