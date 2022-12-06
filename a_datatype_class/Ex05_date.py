
import datetime                 # datetime 만 임포트
from builtins import type

today = datetime.date.today()
print('today is ', today)

from datetime import date,timedelta       # datetime에서 date 만 임포트
today = date.today()
print('today is ', today)

# 날짜 구하기
print('년도 : ',today.year)
print('월 : ',today.month)
print('일 : ',today.day)
print('요일 :',today.weekday())
# 날짜 계산
print('어제 : ', today + timedelta(days=-1))

# 일주일 전 날짜
print('일주일 전 : ', today + timedelta(days=-7))
print('일주일 전: ', today + timedelta(weeks=-1))

# 10일 후 날짜
print('10일 후 : ', today + timedelta(days=+10))


from datetime import datetime
day = datetime.today()
print(day)  # -> 년월일시분초
'''
import datetime
day2 = datetime.datetime.today()
print(day2)
'''
# 날짜 -> 문자열 ( strftime())
print(day.strftime('%Y년 %m월 %D일 %H시 %M분')) # 2022년 12월 05일 10시 39분
print(day.strftime('%y년 %m월 %d일 %H시 %M분')) # 22년 12월 05일 10시 40분
print(day.strftime('%y년 %m월 %D일 %H시 %M분')) # 22년 12월 12/05/22일 10시 40분
print(day.strftime('%y년 %m월 %D일 %h시 %M분')) # 22년 12월 12/05/22일 Dec시 40분
# 문자열을 날짜형태 (strptime() 이용 )
naljja = '2022-12-25 12:50:59'
print(type(naljja))
mydate = datetime.strftime(naljja,'%Y-%m-%d : %H: %M: %S')
print(mydate)
print(type(mydate))