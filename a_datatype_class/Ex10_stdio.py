"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""


#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = int(input('나이를 입력 ->'))
#age += 1
'''
# print('나이 : ',age)
height = eval(input('키를 입력 -> '))
print('키 : ',height)
print(type(height))
'''
print('1+2')
print(eval('1+2'))

#----------------------------------
'''
# 단을 입력받아 구구단을 구하기
dan = int(input('단을 입력해주세요 : '))
for i in range(0,9):
    #print('{} * {} = {} '.format(dan,i+1,dan*(i+1)))
    print(dan,' * ', (i+1), ' = ' , dan*(i+1))
'''

#-----------------------------------------
# print() 함수
print('안녕' + '친구')
print('안녕','친구')
print('안녕' '친구')

for i in range(5):
    print(i,end='/')                        #0/1/2/3/4/
print()
for i in range(5):
    print(i, end = '/' if i<4 else "" )     #0/1/2/3/4


# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# java  클래스명        문자열1        문자열2
#                       [0]             [1]


# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#
#                                   0      1      2      3

a = 3
print(a)



