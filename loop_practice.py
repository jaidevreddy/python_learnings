# Write a Python program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:

    if i>=500:
        break
    elif i % 5 == 0:
        if i <=150:
            print(i)

print("\n")

# Print multiplication table of a given number

num = 2

for i in range(1,11,1):
    mul_table = i * num

    print(mul_table)


print("")

# Calculate sum of all numbers from 1 to a given number

# Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

num = 10
s = 0

for i in range(1,num+1):
   
   s += i

print(f'sum = {s}')


print("")

#  Display numbers from -10 to -1 using for loop

for i in range(10,0,-1):

    print(f'-{i}')


print("")

# Display a message “Done” after the successful execution of the for loop


for i in range(1,6):

    print(i)
    if i == 5:
        print('Done!')


print("")

# Print elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(my_list[1::2])


print("")

# Find the factorial of a given number

# Write a Python program to use for loop to find the factorial of a given number.

# The factorial (symbol: !) means multiplying all numbers from the chosen number down to 1.

num  = 5

sum = 1

for i in range(1,num+1):

    s *= i

print(s)