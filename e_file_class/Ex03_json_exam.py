f = open('./data/sample.json','rt',encoding='utf-8-sig')
data = f.read()
f.close()
# print(data)
# print(type(data))       # 'str'
import json
ditems = json.loads(data)
# print(ditems)
sum = 0
count = 0
for k,v in ditems.items():
    print(k , ' : ',v)
    sum += v['price']*v['count']
    count += v['count']

print('총합은 : ' , sum)
print('총 개수는 : ',count)