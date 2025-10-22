def a_sum(**kwargs):

    total = 0

    for key, value in kwargs.items():
        print(f"{key} = {value}")

        total = total + value
    
    return total


print(a_sum(x=1,y=2,z=3))


def test(num1,num2,*args,**kwargs):

    print(f"the first value is {num1}")
    print(f"the second value is {num2}")

    for arg in args:
        print(f"{arg}")
    
    for key, value in kwargs.items():
        print(f"{key} = {value}")


test(1,2,100,200,300,400,500,x='one',y='two',z='three')

list_args = [1,2,3,4,5]
dict_kwargs = {'x':'one','y':'two','z':'three'}

test(1,2,*list_args,**dict_kwargs)