"""
        숫자형 종류
            - 정수형
            - 실수형
            - 복소수형 1 + 2j, 3i  ( 많이 사용안함 )
            - 8진수   0o25  = 21
            - 16진수  0x25  = 37
"""

# 파이션의 모든 자료형은 객체로 취급한다
# 실행 : alt + shift + F10

""" 1. 기초 연산자 
        + : 더하기
        - : 빼기
        * : 곱하기
        / : 나누기(실수값 결과)
        // : 나누기(정수값 결과)
        % : 나머지
        ** : 자승 (n제곱)
    
    2. 관계연산자
        <   >   <=  >=  ==  !=
    
    3. 논리연산자
        not     or      and
        
    4. 이진(비트) 연산자
        ~   :  이진 not   
        |   :  이진 or
        &   :  이진 and
        ^   :  이진 xor
        <<  :  shift
        >>  :  shift
        
    5. 대입연산자
        =
        +=  -=  *=  /=  //= %=
        &=  |=  ^=
        >>= <<=
    
    6. 기타연산자 : 딕셔너리, 문자열, 리스트, 튜플 등의 자료형에서 사용
        in      : 요소에 포함되면 true, 없으면 false
        not in  : 요소에 포함되지 않으면 false, 없으면 true
      

    [참고] 증가(++), 감소(--) 연산자 없음    
    [참고] is / not is 사용하지 못하게 에러 발생함     
"""

a = 5
b = 2

print('a + b =', a+b)
print('a - b =', a-b)
print('a * b =', a*b)
print('a / b =', a/b)
print('a //b =', a//b)
print('a % b =', a%b)
print('a **b =', a**b)

""" [ 출력결과 ] 
        a + b = 7
        a - b = 3
        a * b = 10
        a / b = 2.5
        a // b = 2
        a % b = 1
        a ** b = 25
"""

print ('H' in 'Hello')          # True
print ('H' not in 'Hello')      # False


# 출력 포맷

y = 8.3/ 2.7
z = 8.3 // 2.7
print(y,'/',z)
print('실수 1 : {}, 정수 1 : {}'.format(y,z))
print('실수 1 : {0}, 정수 1 : {1}'.format(y,z))         # {1} : 소숫점 1자리까지 출력
print('실수 1 : {1}, 정수 1 : {0}'.format(y,z))
print('실수 1 : {0:.1f}, 정수 1 : {1}'.format(y,z))    # {0:.1f} : 소숫점 1자리까지 출력

# 1.
a = 777
b = 777
print(a==b)

# 2.
del a
#print(a)

# 3.
a = 3.5
b = int(3.5)
print(a**((a//b) * 2))
print(((a-b)*a)//b)
print(((a-b)*a)%b)
print((a*4)%(b*4))

# 4.
# celsius = float(input("섭씨온도를 입력하세요:"))
# celsius = input("섭씨온도를 입력하세요:") # -> 실수 값 입력시 오류
# fahrenheit = (( 9 / 5) * celsius) + 32
# print("섭씨온도:",celsius, "화씨온도:", fahrenheit)


# 5.
a = "True"
print(type(a))


# 6 .
a = 10.6
b = 10.5
print(a * b)
print(type(a + b))

# 7.
a = "3.5"
b = 4
print(a * b)

# 8.
a = "3.5"
b = "1.5"
print(a+b)

# 9.
a = '3'
b = float(a)
print(b ** int(a))

# 11.
a = '20'
b = '4'
# print(type(float(a / b)))   # -> 문자 / 문자라서 오류


# 12.
a_3 = 5
print(a_3)
aBc = 5
print(aBc)