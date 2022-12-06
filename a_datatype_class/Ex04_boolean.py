# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry = True
sleepy = False
print (not hungry)      # False
print ( hungry and sleepy)  # False
print(hungry or sleepy)     # True




"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False

"""
if('아'):
    print('True')       # 값이 있으므로 True
else:
    print('False')

if([]):                 # 값이 없으므로 False2
    print('True2')
else:
    print('False2')

if 0:                 # 값이 없으므로 False3
    print('True3')
else:
    print('False3')

if -1:                 # 값을 리턴하므로 True4
    print('True4')
else:
    print('False4')

msg = '행복합시다'
if msg.find('행'):       # find () -> 인덱스 찾음
    print('ok')         # find('행') -> 0 => if 0: 이므로 no return
else:
    print('no')

if(msg.find('가')):    # msg.find('가') = -1 -> if -1: 이므로 return true
    print('ok')
else:
    print('no')

# 값 있나 없나 구분하는 법

if msg.find('행') >=0:       # 값이 있으므로 ok1
    print('ok1')
else:
    print('no1')

if (msg.find('가')) >=0:     # 값이 없으므로 no2
    print('ok2')
else:
    print('no2')


