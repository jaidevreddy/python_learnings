name = ['Hanna','Bruce','Tony']
age = [65,29,42,55]
city = ['New York','London','Berlin']

combine = list(zip(name,age,city))

print(combine)

for name , age , city in combine:
    print(f'{name} is {age} and lives in {city}')

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

combine = list(zip(capitals,countries))

for capitals, countries in combine:
    print(f"The capital of {countries} is {capitals}")

