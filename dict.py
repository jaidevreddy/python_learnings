my_dictionary = {'c1':'value','c2':'value1','c3':'value2'}

result = my_dictionary['c1']
print(result)

customer = {'name':'john','last_name':'lennon','weight':88,'height':176.5}
query = customer['last_name']
print(query)

dic = {'k1':['a','b','c'],'k2':['d','e','f']}
letter = dic['k1'][0].upper()
print(letter)

dic1 = {1:88,2:[1,2,3.1],3:{'s1':[1,2,3],'s2':'5'}}
print(dic1[3]['s1'][1])

dict = {'s1':1, 's2':2}
number = 3
dict['s3'] = number
dict['s2'] = number
print(dict)

print(dict.keys())
print(dict.values())