
def prime_count(number):
    if number < 2:
        
        return 0

    prime_number = [2]
    itteration = 3

    while itteration <= number:
        for n in range(3, itteration, 2):
            if itteration % n == 0:
                itteration += 2
                break
        else:
            prime_number.append(itteration)
            itteration += 2

    print(prime_number)
    return len(prime_number)


print(prime_count(15))        