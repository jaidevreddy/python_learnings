mylist = ['a','b','c']

for items in enumerate(mylist):
    print(items)

for index, items in enumerate(mylist):
    print(index, items)

for index , items in enumerate(range(50,61)):
    print(index, items)


mytuples = list(enumerate(mylist))
print(mytuples[0][1])