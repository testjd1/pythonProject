'''
1. 다음 코드의 실행 결과를 쓰시오.

fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)
'''

'''
2. 다음 코드의 실행 결과를 쓰시오. 
number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5:
    print(type(number[0]))
elif number[3] == 4:
    print(number[2:-1])
'''
'''
3. 다음 코드의 실행 결과를 쓰시오. 
num = 0
i = 1
while i < 8:
    if i % 3 == 0:
        break
    i += 1
    num += i

print(num)
'''
'''

4. 다음 코드의 실행 결과를 쓰시오. 
result = 0
for i in range(5, -5, -2):
    if i < -3:
        result += 1
    else:
        result -= 1
print(result)
'''
'''

5. 다음 코드의 실행 결과를 쓰시오. 
num = ""
for i in range(10):
    if i <= 5 and (i % 2)==0:
        continue
    elif i == 7 or i == 10:
        continue
    else:
        num = str(i) + num
print(num)

'''
'''
6. 다음 코드의 실행 결과를 쓰시오. 
coupon = 0
money = 20000
coffee = 3500
while money > coffee:
    if coupon < 4:
        money = money - coffee
        coupon += 1
    else:
        money += 2800
        coupon = 0
print(money)
'''
'''
7. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? 
list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:
    for j in list_data_b:
        result = i + j

print(result)
'''