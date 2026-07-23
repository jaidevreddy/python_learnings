list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

for index, name in enumerate(list_names):
    
    print(f'{name} is found at index {index}')



indices_list = list(enumerate("Python"))


list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

for index, name in enumerate(list_names):
    
    if name[0] == 'M' or name[0] == 'm':
        print(index)