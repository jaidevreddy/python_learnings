text = input("Enter your text: ").lower()
letters = []
print("\n")

letters.append(input("enter first letter for count: ").lower())
letters.append(input("enter second letter for count: ").lower())
letters.append(input("enter third letter for count: ").lower())
print('\n')
print("how many times each of the chosen letters appears:")
print(f'the letter "{letters[0]}" repeats: "{text.count(letters[0])}"')
print(f'the letter "{letters[1]}" repeats: "{text.count(letters[1])}"')
print(f'the letter "{letters[2]}" repeats: "{text.count(letters[2])}"')
print('\n')

words = text.split()
print(f'Total number of word in the the text is "{len(words)}"')
print('\n')

first_letter = text[0]
last_letter = text[-1]
print(f'the fisrt letter is "{first_letter}" and the last letter is "{last_letter}"')
print("\n")

words.reverse()
reversed = " ".join(words)
print('Reversed Text:')
print(f'{reversed}')
print('\n')

Python_present = {True:"Yes the word python exist", False:"The word python doesnt exist"}
check_python = "python" in text
print(f'{Python_present[check_python]}')
print('\n')

word = input('enter the word you want to check is exist: ').lower()
word = word.split()
theword = "".join(word)
word_dict = {True:"exists", False:"doesn't exist"}
word_check = word[0] in text
print(f'The word {theword} {word_dict[word_check]} in the text')


