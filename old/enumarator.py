mylist = ['a','b','c']

for items in enumerate(mylist):
    print(items)

for index, items in enumerate(mylist):
    print(index, items)

for index , items in enumerate(range(50,61)):
    print(index, items)


mytuples = list(enumerate(mylist))
print(mytuples[0][1])

list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

for index, name in enumerate(list_names):
    if name[0] == 'M':
        print(index)