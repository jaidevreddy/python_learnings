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