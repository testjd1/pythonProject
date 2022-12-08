# Ex03_json.py

f = open('./data/temp.json','rt',encoding='utf-8-sig')
data = f.read()
f.close()
print(data)
print(type(data))       # 'str'
import json
ditems = json.loads(data)
print(ditems)
print(type(ditems))      # 'dict'

for k,val in ditems.items():    # key / value 요소분해 해서 저장
    print(k,': ',val)                # 이순신 :  {'No': 3, 'Job': '연구원'}
    print(k,', 직업: ', val['Job'])   # 이순신 , 직업:  연구원