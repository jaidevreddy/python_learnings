text = input("Enter your text: ").lower()
print("\n")
letters = []

letters.append(input("Enter your first letter: ").lower())
letters.append(input("Enter your second letter: ").lower())
letters.append(input("Enter your last letter: ").lower())
print("\n")

word = input("Enter the word you want to check if it exists in the text: ")
print("\n")

print(f"The count of {letters[0]} is: {text.count(letters[0])}")
print(f"The count of {letters[1]} is: {text.count(letters[1])}")
print(f"The count of {letters[2]} is: {text.count(letters[2])}")
print("\n")

words = text.split()
print(f"The total number of words are: {len(words)}")
print("\n")

first_letter = text[0]
last_letter = text[-1]
print(f"The first letter is {first_letter} and the last letter is {last_letter}")
print("\n")

reverse = words.reverse()
reverse = " ".join(words)
print(f"Word in inverted order: {reverse}")
print("\n")

python_check_dict = {True:"Yes the word python exist", False:"No the word python doesn't exist"}
python_check = "python" in words
print(f"{python_check_dict[python_check]}")
print("\n")

word_check_dict = {True:f"Yes the word {word} exists", False:f"No the word {word} doesn't exist"}
word_check = word in words
print(f"{word_check_dict[word_check]}")



