text = input("enter any text: ").lower()
letter1 = input("enter first letter: ").lower()
letter2 = input("enter second letter: ").lower()
letter3 = input("enter third letter: ").lower()

count1 = text.count(letter1)
count2 = text.count(letter2)
count3 = text.count(letter3)

print(f'The Letter "{letter1}" appears {count1} Times')
print(f'The Letter "{letter2}" appears {count2} Times')
print(f'The Letter "{letter3}" appears {count3} Times')

word_list = text.split()
wordcount = len(word_list)
print(f"the total words are {wordcount}")

print(f"the first word is {word_list[0]} and last word is {word_list[-1]}")

word_list.reverse()
reversetext = " ".join(word_list)
print(reversetext)

ispython = "python" in text 
dic = {True: "Yes" , False: "No"}
print(f"Python Exists: {dic[ispython]}")