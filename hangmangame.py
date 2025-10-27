from random import choice

words_list = ['apple','samsung','google','nokia']

def chooseword(list1):

    select = choice(list1)

    word = list(select)

    return word


def thegame(list1):

    life = 6
    underscore_list = ['_'] * len(list1)
    incorrect_letters = []

    print(f"you have {life} lifes")

    while life > 0:

        print(f"Life: {life}")
        print(f" ".join(underscore_list))
        print(f"Incorrect letters : {",".join(incorrect_letters)}") 

        guess = input("Enter your letter: ").lower()

        if guess in list1:

            for i in range(len(list1)):
                if list1[i] == guess:
                    underscore_list[i] = guess
                
        else:
             incorrect_letters.append(guess)
             life -= 1
        

        if '_' not in underscore_list:
            return (f"congrats you have guessed he word" + f'\n {"".join(underscore_list)}')
        
    else:
        return (f"Game over \n the actual word is {''.join(list1)}")
    


word = chooseword(words_list)
game = thegame(word)

print(game)



