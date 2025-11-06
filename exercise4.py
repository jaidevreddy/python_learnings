def count_prime(num):

    prime_number = [2]
    iteration = 3 

    if num < 2:
        return 0
    
    while iteration <= num:

        for n in range (3,iteration,2):
            if iteration % n == 0:
                iteration = iteration + 2
                break
        else:
            prime_number.append(iteration)
            iteration += 2
        
    
    print(prime_number)
    return len(prime_number)

prit(count_prime(100))
