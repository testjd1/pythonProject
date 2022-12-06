# 2 .
a = [3, "apple", 2016, 4]
b = a.pop(0)
c = a.pop(1)
print(b + c)

# 3.
dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())	# 2 4 6 8 10
dict_values = list(dict_1.values())# 1 2 3 4 6
dict_2 = dict()
for i in range(len(dict_keys)):
	dict_2[dict_values[i]] = dict_keys[i]

print(dict_2[2])


# 4.
animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs= [4, 0, 2, 4, 8]
animal_legs_dict = {}
for i in range(len(animal)):
	animal_legs_dict[legs[i]] = animal[i]
	animal_legs_dict['ant'] = 6

print(animal_legs_dict)

# 5.
Mydict = {'1' : 1, '2' : 2}
Copy = Mydict
Mydict['1'] = 5
result= Mydict['1'] + Copy['1']
print(result)

# 6.
a = list(range(10))
print(a)
a.append(a[3])
print(a)
a.pop(a[3])
print(a)
a.insert(3, a[-1])

a.pop()
print(a)

#7.
data_1 = {'one' : (1,2,3,4,5,6), 'two' : [1,2,3,4,5,6], 'three' : {'four' : 4, 'five' : 5}}
for k in ['one','two','three']:
	try:
		print(data_1[k][:1])
	except TypeError:
		print("error")

for k in ['one', 'two','three']:
	try:
		data_1[k][-1] = "a"
		print(data_1[k][-1])
	except TypeError :
		print("error")