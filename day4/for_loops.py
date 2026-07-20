alphabets = ['a', 'b', 'c', 'd', 'e']

for letter in alphabets:
   letter_number = alphabets.index(letter) + 1
   print(f"letter {letter_number}: {letter}")

names = ['paul','laura','louis','fede','juila']

for name in names:

    if name.startswith('l'):
        print(name)
    else:
        print(f"the name {name} doesnt begin with letter 'l'")


numbers = [1,2,3,4,5]
my_value = 0

for number in numbers:

    my_value = my_value + number

print(my_value)

word = 'python'

for letter in word:
    print(letter)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a) 


dic = {'key1':'a','key2':'b','key3':'c'}

for item in dic:
    print(item)

dic = {'key1':'a','key2':'b','key3':'c'}

for item in dic.values():
    print(item)

dic = {'key1':'a','key2':'b','key3':'c'}

for item in dic.items():
    print(item)


students = ["Norville", "Fred", "Velma", "Daphne"] 

for name in students:
    print(f"Hello {name}")


list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_numbers = 0

for value in list_numbers:
    sum_numbers = sum_numbers + value


list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_even = 0
sum_odd = 0

for value in list_numbers:
    
    if value%2 == 0:
        sum_even = sum_even + value
    else:
        sum_odd = sum_odd + value