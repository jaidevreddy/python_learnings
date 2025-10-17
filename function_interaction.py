from random import *

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


def throw_dice():
    dice1 = randint(1,7)
    dice2 = randint(1,7)
    
    return dice1 , dice2
    
def roll_result(d1,d2):
    sumd = d1 + d2
    
    if sumd <= 6:
        return f"The sum of your dice is {sumd}. Unfortunate"
    elif sumd < 10:
        return f"The sum of your dice is {sumd}. You have a good chance"
    elif sumd >=10:
        return f"The sum of your dice is {sumd}. It looks like a winning roll"
    
die1, die2 = throw_dice()
message = roll_result(die1, die2)

print(f"the die one shows {die1} and die 2 shows {die2}")
print(message)
    

    





