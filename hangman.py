from random import *

words = ['apple','mango','watermelon','orange']

def choose(list1):
    word = choice(list1)

    letters = list(word)

    return letters

def thegame(list1):

    life = 6

    while life > 0:

        for i in list1:
            print(f"your have {life} lifes, category fruits")

            underscore = "_" * (len(list1))

            print(underscore)

