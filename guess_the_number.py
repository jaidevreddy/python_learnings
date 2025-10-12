from random import *

name = input("Enter Your Name: ")
print(f"Well {name}, i've thought of a number between 1 to 100\nyou have only 8 tries to guess it")

random = randint(1,101)
life = 8

while life>0:
    i = int(input("guess the number: "))

    if i > 100 or i < 0:
        print("your out of the number range")
        life -= 1
        print(f"you have {life} chances left")
    elif i>random:
        print(f"Wrong the value is lesser")
        life -= 1
        print(f"you have {life} chances left")
    elif i<random:
        print(f"Wrong the value is greater")
        life -= 1
        print(f"you have {life} chances left")
    elif i == random:
        print(f"Thats correct, you have guessed the right number\nwith {life} chance left")
        break

else:
    print("\n")
    print(f"Your out of chances\nThe actual number is {random}")





