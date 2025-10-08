list = ['a','b','c']

for letters in list:
    letter_num = list.index(letters) + 1
    print(f"letters {letter_num}: {letters}")


nameslist = ['paul','laura','julie','louis','fede']

for name in nameslist:
    if name.startswith('l'):
        print(name)


numbers = [1,2,3,4,5]
myvalue = 0

for num in numbers:
    myvalue = myvalue + num

print(myvalue)


word = "python"

for letter in word:
    print(letter)

for letter in "code":
    print(letter)

for num in [[1,2],[3,4],[5,6]]:
    print(num)

for a, b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)


dict = {'k1':'a','k2':'b','k3':'c'}

for items in dict:
    print(items)
for items in dict.items():
    print(items)
for items in dict.values():
    print(items)
for a, b in dict.items():
    print(a + " " +b)