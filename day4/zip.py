capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

country_capitals = list(zip(capitals, countries))

for capital , country in country_capitals:
    
    print(f'The capital of {country} is {capital}')


brands = ['nike','H&M','Google']
products = ['shoes','clothes','software']

my_zip = (zip(brands,products))


spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
portuguese = ["um", "dois", "três", "quatro", "cinco"]
english = ["one", "two", "three", "four", "five"]

numbers = list(zip(spanish,portuguese,english)) 