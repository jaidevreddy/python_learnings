name = input("enter you name: ")
sales = int(input("enter you sales number: "))

print(f"hey {name}, you have made a total sales of ${sales} this month and you commision is ${round(sales*13/100,2)}")