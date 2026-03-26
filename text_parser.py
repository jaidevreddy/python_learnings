text = input("enter your text: ").lower()
letters = input("enter three letters: ").lower()

text_list = text.split()
letters = tuple(letters)
letter_1, letter_2, letter_3 = letters

count_1 = text.count(letter_1)
count_2 = text.count(letter_2)
count_3 = text.count(letter_3)


text_count = len(text_list)


first_letter = text[0]
last_letter = text[-1]


text_reverse = text_list
reverse = " ".join(text_reverse)

python_detect = {True:"Yes", False:"No"}

text_list = "python" == True 


print(first_letter)
print(last_letter)
