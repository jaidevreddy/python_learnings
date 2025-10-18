# from random import *

# sticks = ['-','--','---','----']

# def mix(shuf):
#     shuffle(shuf)
#     return shuf

# def try_your_luck():
#     a_try = ''
#     while a_try not in ['1','2','3','4']:
#         a_try = input("choose a number: ")
    
#     return int(a_try)
    
# def check_stick(list1,selected):
#     if list1[selected-1] == '-':
#         print("your turn to do the task")
#     else:
#         print(f"you picked {list1[selected-1]} and no work for you")


# stick_mix = mix(sticks)
# choose_stick = try_your_luck()
# you_got = check_stick(stick_mix,choose_stick)


# def throw_dice():
#     dice1 = randint(1,7)
#     dice2 = randint(1,7)
    
#     return dice1 , dice2
    
# def roll_result(d1,d2):
#     sumd = d1 + d2
    
#     if sumd <= 6:
#         return f"The sum of your dice is {sumd}. Unfortunate"
#     elif sumd < 10:
#         return f"The sum of your dice is {sumd}. You have a good chance"
#     elif sumd >=10:
#         return f"The sum of your dice is {sumd}. It looks like a winning roll"
    
die1, die2 = throw_dice()
message = roll_result(die1, die2)

print(f"the die one shows {die1} and die 2 shows {die2}")
print(message)
    

def reduce_list(list1):
    new_list = []
    for i in list1:
        if i not in new_list:
            new_list.append(i)
        else:
            pass
    
    big_value = max(new_list)
    new_list.remove(big_value)
    return new_list

num = [1,2,15,7,2]

red = reduce_list(num)
print(red)

def average(list1):
    total = sum(list1)/len(list1)
    return total

print(average(red))

import random 

def toss_coin():
    toss = random.choice(['Tails','Heads'])
    return toss

def luck(toss, list1):

    if toss == 'Tails':
        print(f"List will self-destruct")
        return []
    elif toss == 'Heads':
        print(f'List was saved')
        return list1
    
secret_code = [0,0,1]

toss = toss_coin()
print(toss)
code = luck(toss,secret_code)
print(code)



