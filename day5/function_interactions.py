from random import shuffle

sticks = ['-','--','---','----']


def mix(my_list):

    shuffle(my_list)
    return my_list


def choose_number():

    number = ''

    while number not in ['1','2','3','4']:
        number = input("choose your number")


    return int(number)


def choose_stick(a_list,number):

    if a_list[number - 1] == '-':
        print('you got the shortest')
    else:
        print(f"you got {a_list[number-1]}")



mixed_list = mix(sticks)
number = choose_number()

choose_stick(mixed_list,number)


# question 1

from random import *


def throw_dice():
    
    dice = [1,2,3,4,5,6]
    
    num_1 = choice(dice)
    num_2 = choice(dice)
    
    return num_1,num_2
    
def roll_result(num1,num2):
    
    add = num1 + num2
    
    if add <=6:
        return(f"The sum of your dice is {add}. Unfortunate")
    elif add > 6 and add < 10:
        return(f"The sum of your dice is {add}. You have a good chance")
    elif add >=10:
        return(f"The sum of your dice is {add}. It looks like a winning roll")


num1, num2 = throw_dice()

roll_result(num1,num2)


#question 2


numbers = [1,2,15,7,2]


def reduce_list(my_list):
    
    unique_list = list(set(my_list))
    unique_list.remove(max(unique_list))
    
    return unique_list
    

def average(my_list):
    
    avg = sum(my_list)/len(my_list)
    return float(avg)
    
a_list = reduce_list(numbers)

avg = average(a_list)


#question 3

from random import choice

secret_codes = [1,2,3]

def toss_coin():
    
    coin = ["Heads","Tails"]
    toss = choice(coin)
    
    return toss

def luck (toss,my_list):
    
    if toss == 'Tails':
        print("List will self-destruct")
        my_list.clear()
        return my_list
    else:
        print("List was saved")
        return my_list

toss = toss_coin()
code = luck(toss,secret_codes)
print(code)