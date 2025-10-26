from random import *

words = ['apple','mango','watermelon','orange']

incorrect_letter = []

def choose(list1):
    word = choice(list1)

    letters = list(word)

    return letters

def thegame(list1):

    life = 6

    underscore_list = ["_"] * (len(list1))
    print('\n')
    print(f"You have {life} lifes to guess")

    while life > 0:
        
        print('\n')
        print(f"Life: {life}")

        print("→ word: " + " ".join(underscore_list))
        print(f"incorrect letters: {",".join(set(incorrect_letter))}")

        guess = input("Enter your letter: ").lower()

        if guess in list1:

            for i in range(len(list1)):

                if list1[i] == guess:

                    underscore_list[i] = guess
        else:
            incorrect_letter.append(guess)
            life -= 1


        if '_' not in underscore_list:
            msg = (f"Congrate you have guessed the word" + "\n→ "+"".join(underscore_list))
            return msg
    else:
        print("Your out of lifes, better luch next time")
        return("the word was "+"".join(list1))

    


word = choose(words)

game = thegame(word)
print(game)




        

        

       

        
         
            


            


