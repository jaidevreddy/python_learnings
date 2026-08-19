def return_distincts(a,b,c):

    sum = a + b + c
    integer_list = [a,b,c]
        

    if sum > 15:
        return max(integer_list)
    elif sum < 10:
        return min(integer_list)
    else:
        integer_list.sort()
        return integer_list[1]


result = return_distincts(2,5,9)

print (result)