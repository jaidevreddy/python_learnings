text = input("Enter your text: ").lower()
letters = []
print("\n")

letters.append(input("enter first letter for count: "))
letters.append(input("enter second letter for count: "))
letters.append(input("enter third letter for count: "))
print('\n')
print("how many times each of the chosen letters appears:")
print(f'the letter "{letters[0]}" repeats: "{text.count(letters[0])}"')
print(f'the letter "{letters[1]}" repeats: "{text.count(letters[1])}"')
print(f'the letter "{letters[2]}" repeats: "{text.count(letters[2])}"')
print('\n')

words = text.split()
print(f'Total number of word in the the text is {len(words)}')
print('\n')



