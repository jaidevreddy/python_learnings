def check_3_digit(list):

    three_digit_list = []

    for n in list:
        if n in range(100,1000):
            three_digit_list.append(n)
        else:
            pass

    return three_digit_list

list = [12,53,123]
result = check_3_digit(list)
print(result)


def all_positives(list1):
    
    for n in list1:
        if n < 0:
            return False
        else:
            pass
    
    return True

numbers = [1,2,3,-1,4,-2,4,3]

result = all_positives(numbers)
print(result)


def sum_less(list1):
    
    sum = 0
    
    for n in list1:
        if n > 0 and n < 1000:
            sum = n + sum
        else:
            pass
    
    return sum 
    
numbers = [1,42,413,312313,315,313,3]
result = sum_less(numbers)
print(result)


def count_even(list1):
    
    count = 0
    for n in list1:
        if n % 2 == 0:
            count = count + 1
        else:
            pass
    
    return count 

numbers = [1,2,4,2,4,5,6,8,4,5]
result = count_even(numbers)
print(result)