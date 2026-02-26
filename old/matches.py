series = input("enter product series number: ")

match series:
    case '01':
        print('product 1')
    case '02':
        print("product 2")
    case _:
        print("no product found")


name = input("enter your name: ")
age = input("enter your age:")
client = {"name":name, "age":age}

movie = {"title":'matrix', "cast":{"mainlead":"keanu reeves", "director":"lana and lily"}}

items = [client, movie,"book"]

for i in items:
    match i:
        case {"name":name, 
              "age":age}:
            print(name,age)
        case {"title":title, 
              "cast":{"mainlead":mainlead, 
                      "director":director}}:
            print(title, mainlead, director)
        case _:
            print("there is nothing like this")
