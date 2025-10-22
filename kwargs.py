def a_sum(**kwargs):

    total = 0

    for key, value in kwargs.items():
        print(f"{key} = {value}")

        total = total + value
    
    return total


print(a_sum(x=1,y=2,z=3))