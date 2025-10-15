def check(number):
    value = number in range (100,1001)
    return value

sum = 949+30
result = check(sum)
print(result)

def check3(num):
    for n in num:
        if n in range(100,1000):
            return True
        else:
            pass
    
    else:
        return False


result = check3([1000,100,2342,5836])
print(result)

def checking(val):
    list1 = []
    for i in val:
        if i in range(100,1000):
            list1.append(i)
        else:
            pass
    
    return list1

res = checking([1000,100,2342,600])
print(res)


def positive(val):
    for i in val:
        if i<0:
            return False
        else:
            pass
    
    else:
        return True
    
numbers_list = [100,-1030,-2342,123091,234432432]
numbers = [100,100,324]
check = positive(numbers)
print(check)

def sum_less(list1):
    sum = 0
    for i in list1:
        if 0 < i and i < 1000:
            sum = i + sum
        else:
            pass
    
    return sum
    

numbers = [100,-100,324]
res = sum_less(numbers)
print(res)

def count_even(list1):
    count = 0
    for i in list1:
        if i%2 == 0:
            count = count + 1
        else:
            pass
    return count

numbers = [100,2240,324]
even_count = count_even(numbers)
print(even_count)