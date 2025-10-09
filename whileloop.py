coins = 5

while coins > 0:
    print(f'i have {coins} coins')
    coins -= 1
else:
    print("you have no more coins left")

answer = 'y'

while answer =='y':
    answer = input("do you want to continue (y/n)")
    if answer == 'y':
        print("you deicded to continue") 
else:
    print("you decide to end")   
