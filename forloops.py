list = ['a','b','c']

for letters in list:
    letter_num = list.index(letters) + 1
    print(f"letters {letter_num}: {letters}")


nameslist = ['paul','laura','julie','louis','fede']

for name in nameslist:
    if name.startswith('l'):
        print(name)