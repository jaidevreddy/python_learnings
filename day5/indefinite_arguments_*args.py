#question 1

def sum_squares(*args):
    
    total = 0
    
    for n in args:
        squared = n ** 2
        total += squared
    
    return total


#question 2

def absolute_sum(*args):
    
    total = 0 
    
    for n in args:
        
        total += abs(n)
    
    return total

#question 3

def personal_numbers(name,*args):
    
    sum_numbers = 0
    
    for n in args:
        
        sum_numbers += n 
    
    return f"{name}, the sum of your numbers is {sum_numbers}" 