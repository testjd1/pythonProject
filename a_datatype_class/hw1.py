import math
import numpy

'''
1. 사용자로부터 5개의숫자를읽어서리스트에저장하고숫자들의평균을계산하여출력한다.
또숫자중에서평균을출력하여보자.
정수를입력하세요: 10
정수를입력하세요: 20
정수를입력하세요: 30
정수를입력하세요: 40
정수를입력하세요: 50
평균= 30.0



sum = 0
for i in range(5):
    k = int(input('정수를 입력하세요 : '))
    sum += k
print('평균 = {}'.format(sum/5))
'''


'''
2. 2. 사용자에게서받은문자들을 역순으로 출력한다. 
문자열입력: abcde
결과 :edcba

s = str(input('문자열 입력 : '))
reverse_s = ''
for c in s:
    reverse_s = c+ reverse_s
print(reverse_s)
'''

'''
3. 사용자에게서받은정수들의평균과표준편차를계산하여출력한다. 
평균과표준편차를프로그램을 작성하세요
정수리스트입력: 10 20 30 40 50
평균= 30.0
표준편차 15.81
jung = list(map(int,input('정수 리스트 입력 : ').split()))
sum = 0;
k = 0
for i in jung:
    sum += i
    k = k+1
avg = sum/k
print('평균 : {}'.format(avg))
sum = 0
hab = 0

for i in jung:
    hab = (i-avg)*(i-avg)
    sum += hab
print(k)
print('표준 편차 : {}'.format(math.sqrt(sum/k)))
'''



'''

4. 전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자.
 
문자열을입력하시오: NUMBER
686237

number =0
sum = ''
m = str(input('문자열을 입력하시오 :'))
m = m.lower()       # 입력받은 문자열 소문자로 변환
print(m)
for i in m:
    if i == 'a' or i == 'b' or i == 'c':
        number = 2
        sum= sum+str(number)
    elif i == 'd' or i == 'e' or i == 'f':
        number = 3
        sum= sum+str(number)
    elif i == 'g' or i == 'h' or i == 'i':
        number = 4
        sum= sum+str(number)
    elif i == 'j' or i == 'k' or i == 'l':
        number = 5
        sum= sum+str(number)
    elif i == 'm' or i == 'n' or i == 'o':
        number = 6
        sum= sum+str(number)
    elif i == 'p' or i == 'q' or i == 'r' or i =='s':
        number = 7
        sum= sum+str(number)
    elif i == 't' or i == 'u' or i == 'v':
        number = 8
        sum= sum+str(number)
    elif i == 'w' or i == 'x' or i == 'y' or i =='z':
        number = 9
        sum= sum+str(number)
    else:
        sum = sum + i


print(sum)
'''
#1
sum = 0
for i in range(5):
    sum += eval(input('정수를입력하세요: '))
print("평균= {0}".format(sum/5))

#2
print(input("문자들을 입력하시오: ")[::-1])

#3
import numpy
list = [int(x) for x in input('정수리스트입력: ').split()]
print('평균= {0}\n표준편차 {1}'.format(numpy.mean(list), numpy.std(list)))

#4
string = input('문자열을입력하시오: ')
p = {'':1, 'a':2, 'b':2, 'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,'i':4,
'j':5,'k':5,'l':5,'m':6,'n':6,'o':6,'p':7,'q':7,'r':7,'s':7,'t':8,'u':8,
'v':8,'w':9,'x':9,'y':9,'z':9}
for char in string:
    print(p.get(char.lower()), end='')


