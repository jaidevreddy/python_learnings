my_file = open('test2.xlsx','w')

my_file.write("I am the new text")

my_file.close()

my_file = open('test1.txt','a')

my_file.write("\nhello starting and where it ended")

my_file.close()

my_file = open('test1.txt','r')

print(my_file.read())

my_file.close()

my_file = open('my_file.txt','w')

my_file.write('New text')

my_file.close()

my_file = open('my_file.txt','r')

print(my_file.read())

my_file.close()

my_file = open('my_file.txt','a')

my_file.write('New login')

my_file.close()

my_file = open('my_file.txt','r')

print(my_file.read())

my_file.close()

record_last_session = ["John", "12/20/2022", "08:17:32 pm", "No loading errors"]

my_file = open('register.txt','a')

for i in record_last_session:

    my_file.writelines(f"{i}\t")

my_file.close()

my_file = open('regt.txt','r')

print(my_file.read())

my_file.close