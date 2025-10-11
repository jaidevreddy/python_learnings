word = input('enter your name: ')

nameslist = [letter for letter in word]

print(nameslist)


numbers = range(0,21,2)
even_numbers = [num for num in numbers]
print(even_numbers)

mylist = [n if n*2 >10 else 'no' for n in numbers ]
print(mylist)

feet = [10,20,30,40,50]
meters = [ f * 0.3048 for f in feet]

print(meters)

