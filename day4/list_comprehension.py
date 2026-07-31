feet = [10,20,30,40,50]

meteres = [n*0.3048 for n in feet]
print(meteres)

values = [1, 2, 3, 4, 5, 6, 9.5] 
square_values = [n**2 for n in values]

values = [1, 2, 3, 4, 5, 6, 9.5] 
even_values = [n for n in values if n%2 == 0]

temperature_fahrenheit = [32, 212, 275]
degrees_celsius = [(tempd-32)*(5/9) for tempd in temperature_fahrenheit]