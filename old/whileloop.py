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

while answer == 'y':
    pass

print ("hello world")


letter = []

while True:
    reply = input('enter your letter: ')
    if reply == "1":
        print("you decide to end")
        break
    
    parts = reply.split()
    letter.extend(parts)
    print(letter)

while True:
    reply = input('enter your letter: ')
    if reply == 'n':
        continue
    if reply == "1":
        print("you decided to end the loop")
        break
    parts = reply.split()
    letter.extend(parts)
    print(letter)


