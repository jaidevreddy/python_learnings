from random import *

random0 = randint(1,50)
print(random)

random1 = round(uniform(1,50),1)
print(random1)

random2 = round(random(),2)
print(random2)

color = ['black', 'blue', 'red', 'green']
print(choice(color))

listnum = list(range(5,50,5))
print(listnum)
shuffle(listnum)
print(listnum)


names = ['aegon','barathion','cersie','drogon','emilia']
shuffle(names)
picked = names[:3]
print(picked)

for i in picked:
    names.remove(i)

print(names)
