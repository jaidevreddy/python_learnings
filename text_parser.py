text = input("enter your text: ").lower()
letters = []

words = text.split()


letters.append(input("enter your first letter: "))
letters.append(input("enter your second letter: "))
letters.append(input("enter your third letter: "))

count_1 = text.count(letters[0])
count_2 = text.count(letters[1])
count_3 = text.count(letters[2])


word_count = len(words)


first_letter = text[0]
last_letter = text[-1]


reverse = words[::-1]
reverse = " ".join(reverse)

python_detect = {True:"Yes", False:"No"}
check = "python" in words
final_check = python_detect[check]


print(" ")
print(f"{letters[0]} count is {count_1}")
print(f"{letters[1]} count is {count_2}")
print(f"{letters[2]} count is {count_2}")


print(" ")
print(f"word count is {word_count}")

print(" ")
print(f"the first letter is '{first_letter}' and last letter is '{last_letter}'")

print(" ")
print(f"reverse order: {reverse}")

print(" ")
print(f"python exists: {final_check}")

