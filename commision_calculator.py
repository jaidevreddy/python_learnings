name = input("Enter your name: ")
sales = float(input("Enter your sales: "))

commision = sales * 13/100

print(f"hey {name} your sales commision for this month is ${round(commision,2)}")