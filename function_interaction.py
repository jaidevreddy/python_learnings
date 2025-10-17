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
    

