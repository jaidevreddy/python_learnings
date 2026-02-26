def exercise2(word):

    word_list = []
    final_list = []

    for i in word:
        word_list.append(i)
    
    word_list.sort()

    for item in word_list:

        if item not in final_list:
            final_list.append(item)

    output = " ".join(final_list)
    return output

    
print(exercise2('alphabets'))