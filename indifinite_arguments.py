def sums(*args):
    total = 0

    for num in args:
        total = total + num
    
    return total

print(sums(6,7,8))

def sum_squares(*args):

    total = 0

    for sq in args:
        total = sq**2 + total

        return total
    
