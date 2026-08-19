def alphabets(value):

    alphabets_list = list(set(value))
    alphabets_list.sort()
    return alphabets_list


result = alphabets("entertainment")
print(result)
