my_file = open('test.txt')

# print(my_file.read())

# one_line = my_file.readline()
# print(one_line)

# for i in my_file:

#     print(i)

# all = my_file.readlines()
# all = all.pop()
# print(all)

j = 0 

for i in my_file:

    j = j + 1
    if j == 2:
        print(i)

    


my_file.close()