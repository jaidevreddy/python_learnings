sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
result = sentence.upper()
print(result)

word_list = ["Simple","is","better","than","complex."]
result = " ".join(word_list)
print(result)

sentence = "If the implementation is hard to explain, it might be a bad idea."
result = sentence.replace("hard","easy").replace("bad","good")
print(result)