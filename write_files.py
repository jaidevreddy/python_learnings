my_file = open('test2.xlsx','w')

my_file.write("I am the new text")

my_file.close()

my_file = open('test1.txt','a')

my_file.write("\nhello starting and where it ended")

my_file.close()

my_file = open('test1.txt','r')

my_file.write("hello")

my_file.close()