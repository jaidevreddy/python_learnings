def greet():
    print("hello ")

greet()

def greetperson(name):
    print("Hello " + name)

ename = input("enter your name: ")
greetperson(ename)

def square(number):
    print(f"answer: {number**2}")

num = int(input("enter number"))
square(num)


coffee_price = [('cappuccino',1.5),
                ('espreso',1.2),
                ('mocha',1.9)]

def most_expensive_coffee(value):
    highest_price = max(value)
    return highest_price



res = most_expensive_coffee(coffee_price)

print (res)

def most_exp_coffee(price_list):

    highest_price = 0
    expensive_coffee = ''

    for coffee, prices in price_list:
        if prices > highest_price:
            highest_price = prices
            expensive_coffee = coffee
        else:
            pass

    return (expensive_coffee, highest_price)

coffee , prices = most_exp_coffee(coffee_price)

print(f'the most expensive coffee is {coffee} and it costs {prices}')