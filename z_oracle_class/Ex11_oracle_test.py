# Ex11_oracle_test
import cx_Oracle as oci

'''
[ 파이썬 + 디비 절차 ]
1. 연결객체 얻어오기 ( Connection )
2. sql 문장
3. cursor 객체 얻어오기
4. 실행
5. cursor 객체 닫기
6. 연결객체 닫기
'''
# 1. 연결객체 얻어오기 ( Connection )
conn = oci.connect('scott/tiger@127.0.0.1/xe')
print(conn.version)

# 2. sql 문장
sql = 'select * from emp'

# 3. cursor 객체 얻어오기
cursor =conn.cursor()

# 4. 실행
cursor.execute(sql)
datas = cursor.fetchall()
# print(datas)
for row in datas:
    print(row)
# 5. cursor 객체 닫기
cursor.close()

# 6. 연결객체 닫기
conn.close()