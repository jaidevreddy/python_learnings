from random import * 

guess = 8
secret_number = randint(1,10)
user_guess = 0 

name = input("enter your name: ")

print(f"\nHey {name} i have guessed a number between 1-100, you have 8 tries to guess\n") 

while guess >= 1:

    print(f"you have {guess} tries left")
    user_guess = int(input("Enter your guess: "))
    guess -= 1

    if user_guess > secret_number:
        print("the number you have guessed is higher\n")
    elif user_guess < secret_number:
        print("the number you have guesed is lower\n")
    else:
        print(f"\nCongrats you guessed it in {8-guess} tries")
        break


if secret_number != user_guess:
    print(f"We are out of tries, the number was {secret_number}")