series = input("enter product series number: ")

match series:
    case '01':
        print('product 1')
    case '02':
        print("product 2")
    case _:
        print("no product found")