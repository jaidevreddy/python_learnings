coffee_prices = [('espresso',1.5),('cappuccino',2.5),('mocha',1.8)]

def expenive_coffee(price_list):

    expensive = 0
    expensive_coffee = ''

    for coffee, price in price_list:
        if price > expensive:
            expensive = price
            expensive_coffee = coffee
        else:
            pass

    return expensive_coffee,expensive


coffee, price= expenive_coffee(coffee_prices)
print(f"the most expensive coffee is {coffee}, it costs {price}")

    
