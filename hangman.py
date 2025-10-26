from random import *

words = ['apple','mango','watermelon','orange']

def choose(list1):
    word = choice(list1)

    letters = list(word)

    return letters

def thegame(list1):

    life = 6

    underscore_list = "_" * (len(list1))

    while life > 0:

        print(f"You have {life} lifes to guess")

        print(" ".join(underscore_list))

        guess = input("Enter your letter: ")

        if guess in list1:

            for i in range(len(list1)):

                if list1[i] == guess:

                    list1[i] = guess 




        

        

       

        
         
            


            


