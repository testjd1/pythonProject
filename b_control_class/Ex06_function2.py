
# [추가] 함수도 객체이다
def case1():
    print('case-1')

def case2():
    print('case-2')

def case3():
    print('case-3')

f = {
        'a1' : case1,
        'a2' : case2,
        'a3' : case3
}
print(f['a2'])
f['a2']()

byunsu = 'a3'
f[byunsu]()


#---------------------------------------
# 글로벌 변수와 지역변수
# #(1)
# temp = '글로벌'
# def func():
#     print('1>',temp)
# func()
# print('2>',temp)

#(2)
# temp = '글로벌'
# def func():
#    # print('0>',temp) 이미 지역 변수 내에 선언되어 있는데 그 전에 출력 못함
#     temp='지역'
#     print('1>',temp)    # 지역
# func()
# print('2>',temp)        # 글로벌

# (3)
temp = '글로벌'
def func():
    global temp
    temp='지역'
    print('1>',temp)    # 지역
func()
print('2>',temp)        # 지역

'''
#----------------------------------------------
# 람다함수 - 한번 사용하고 버리는 함수
# 파이션에서는 람다함수를 한 줄로 작성???

    파이썬 3.x부터는 람다를 권장하지 않는다고.
    몇몇 개발자들이 람다함수 사용시 직관적이지 않다는 이유라는데
    
    종종 사용됨
'''
def f(x,y):
    return x*y
print(f(3,2))

f = lambda x,y:x*y
print(f(3,2))



#-----------------------------------------------------------
"""  맵리듀스
    (1) map()
         ` 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
         ` 형식 : map(함수명, 리스트형식의 입력값)
         ` 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
           파이썬 2.x에서는 list 없이도 리스트 형식으로 반환
    (2) reduce()
         ` 리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수    
    
    파이썬 2.x에서는 많이 사용하던 함수이지만, 최근 문법의 복잡성으로 권장하지 않는 추세란다.
"""

def calc(x):
    return x*2
data = [1,2,3,4,5]
res = list(map(calc,data))
print(res)


# reduce() 찍먹
from functools import reduce
def f(x,y):
    return x*y
data = [1,2,3,4,5]
print(reduce(f,data))


tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
def quiz_1(tuple_1, tuple_2):
	result = []
	for i in (tuple_1 + tuple_2):
		result.append(i)
	return result

print(quiz_1(tuple_1, tuple_2))

print('------------------1')
def even_filter(alist):
    result = []
    for i in alist:
        if i%2 ==0:
            result.append(i)
    return result

print(even_filter([1, 2, 4, 5, 8, 9, 10]))

print('------------------2')

def is_prime_number(num):

    for i in range(2,num):
        if num%i == 0:
            return 'False'
        else:
            return 'True'



print(is_prime_number(60))
print(is_prime_number(61))

print('---------------------3')
def count_vowel(bk):
    alist = ['a','e','i','o','u']
    cnt = 0
    for i in bk:
        if i in alist:
            cnt += 1
    return cnt

print(count_vowel("pythonian"))