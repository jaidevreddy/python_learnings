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