msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

#------------------------------------------
# (1) unpacking : 요소 분해
a,b,c = msg
print(a)        # 행
print(b)        # 복
print(c)        # 해

a,b,c = li
print(a)        # a
print(b)        # b
print(c)        # c

a,b,c = tpl
print(a)        # ㄱ
print(b)        # ㄴ
print(c)        # ㄷ

a,b,c = di
print(a)        # k
print(b)        # j
print(c)        # l

alist = [(1,2),(3,4),(5,6)]
for temp in alist:
    print(temp)

for first,second in alist:
    print("{} + {} = {}".format(first,second,first+second))

# -------------------------
# (2) enumereate() 함수
#       -> 요소와 인덱스를 같이
'''
 [참고] 자바에서
 Iterator -> Enumerator(이전버전)

'''
blist = ['개발자', '코더', '전문가','노가다']

for value in blist:
    print(value) # 개발자 코더 전문가 노가다

for value in enumerate(blist):
    print(value)    # (0,'개발자) (1,'코더') ...

for idx,value in enumerate(blist):
    print(idx,value)    # 0 개발자 1 코더 ...

# -------------------------------------
# (3) zip() 함수
days = ['월','화','수']
doit = ['잠자기', '밥먹기','숨쉬기','멍때리기']

print(zip(days,doit))
print(list(zip(days,doit)))
print(dict(zip(days,doit)))

for yoil,halil in zip(days,doit):
    print(yoil)
    print(halil)

mon = [11,12,1]
print(list(zip(days,doit,mon)))