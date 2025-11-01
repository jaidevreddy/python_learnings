my_file = open('test.txt')

print(my_file.read())

print("")
my_file.close()

my_file = open('test.txt')

one_line = my_file.readline()
print(one_line)

print("")
my_file.close()

my_file = open('test.txt')
for i in my_file:

    print(i)
    
print("")
my_file.close()

my_file = open('test.txt')
all = my_file.readlines()
print(all)
all_del = all.pop()
print(all_del)
print(all)

print("")
my_file.close()

my_file = open('test.txt')

j = 0 

for i in my_file:

    j = j + 1
    if j == 2:
        print(i)


my_file.close()