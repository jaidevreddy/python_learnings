def power(num1,num2):
    
    return num1 ** num2

result = power(2,3)
print(result)



def usd_to_eur(amount):
    return amount * 0.90

dollars = 100
euros = usd_to_eur(dollars)
print(euros)


def reverse_word(word):
    
    output = word[::-1].upper()
    return output
    
word = reverse_word("Python")
print(word)