def greet():
    print("hello ")


greet()

def greetperson(name):
    print("Hello " + name)

ename = input("enter your name: ")
greetperson(ename)

def square(number):
    print(f"answer: {number**2}")

num = int(input("enter your number for finding the power of 2: "))
square(num)

