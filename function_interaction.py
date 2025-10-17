from random import *

sticks = ['-','--','---','----']

def mix(shuf):
    shuffle(shuf)
    return shuf

def try_your_luck():
    a_try = ''
    while a_try not in ['1','2','3','4']:
        a_try = input("choose a number: ")
    
    return int(a_try)
    
def check_stick(list1,selected):
    if list1[selected-1] == '-':
        print("your turn to do the task")
    else:
        print(f"you picked {list1[selected-1]} and no work for you")


stick_mix = mix(sticks)
choose_stick = try_your_luck()
you_got = check_stick(stick_mix,choose_stick)

