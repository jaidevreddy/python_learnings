name = input("Enter Your name: ")
sales = int(input("enter your sales for the month: "))

print(f"hey {name} you this months sales is ${sales} and your commision for the month is ${round(sales*13/100,2)}")