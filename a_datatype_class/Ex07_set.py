# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다
#       - { }

s = set()               # 빈 집합을 생성
s = set([1,2,3,1,1])
print(s)

s1={1,2,3,1,1}
print(s1)
s2 = {3,4,5,6,3,4}
print(s1& s2)       # {3}
print(s2 and s1)       # {1,2,3} => why?
print(s1 | s2)      # {1, 2, 3, 4, 5, 6}
print(s1 - s2)      # {1, 2}
print(s2 - s1)      # 4,5,6


# ******************
# print(s[0]) => 오류, set 은 순서를 저장 하지 않아서 오류 뜸