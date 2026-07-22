answer = 'y'

while answer == 'y':
    answer = input("do you want to continue: (y/n)")
else:
    print("thank you")


name = input("Enter your name: ")

for letter in name: 
    if letter == 'r':
        break
    print(letter)


name = input("Enter your name: ")

for letter in name: 
    if letter == 'r':
        continue
    print(letter)


number = 10

while number >=0:
    print(number)
    number -= 1 

number = 0 

while number <=10:
    print(number)
    number += 1

number = 50 

while number >=0:
    if number % 5 == 0:
        print(number)
    
    number -= 1  
  

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for number in list_numbers:
    
    if number < 0:
        continue 
    
    print(number)


list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for number in list_numbers:
    
    if number < 0:
        break 
    
    print(number)