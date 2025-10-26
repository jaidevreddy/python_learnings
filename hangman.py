from random import *

words = ['apple','mango','watermelon','orange']

def choose(list1):
    word = choice(list1)

    letters = list(word)

    return letters

def thegame(list1):

    life = 6

    while life > 0:

        print(f"your have {life} lifes, category fruits")

        underscore_list = "_" * (len(list1))
        list(underscore_list)

        for i in list1:

            guess = input("Enter you letter: ").lower()
        
        for n in range(len(list1))

        underscore = " ".join(underscore_list)
        print(underscore)


       

        
         
            


            


