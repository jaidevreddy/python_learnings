def exercise2(word):

    word_list = [word]
    word_list.sort()
    final_list = []

    for i in word_list:
        if i not in word_list:
            final_list.append(i)
            output = " ".join(final_list)
            return output
        
    
