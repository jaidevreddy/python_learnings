list = ["a","b","c"]

lenght = len(list)
print(lenght)

result = list[0]
res = list[0:2]
res1 = list[::-1]
res2 = list[:2]
res3 = list[::-2]
res4 = list[0::]
print(result)
print(res)
print(res1)
print(res2)
print(res3)
print(res4)

list1 = ["d","e","f"]
list2 = list + list1
print(list2)

list2[0] = "alpha"
print(list2)

list2.append("g")
print(list2)

list2.pop()
delete = list2.pop(0)
print(list2)
print(delete)

list3 = [2,1,4,3,9,7,6,5,10,8]
list3.sort()
print(list3)