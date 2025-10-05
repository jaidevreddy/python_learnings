my_tuples = (1,2,(1,2,3),4,5)
print(my_tuples)

print(my_tuples[2][0])

tuple1 = list(my_tuples)
tuple1[2] = list(my_tuples[2])
print(type(tuple1))

tuple1[2][1] = 1
tuple1[1] = 1
print(tuple1)

convtuple = tuple(tuple1)
print(type(convtuple))

t = (1,2,3)

x,y,z =t
print (x)
print(x+y+z)

t = ('a','b','a')

print(t.count('a'))
indexing = t.index('a',1)
print(indexing)