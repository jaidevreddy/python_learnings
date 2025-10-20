def sums(*args):
    total = 0

    for num in args:
        total = total + num
    
    return total

print(sums(6,7,8))