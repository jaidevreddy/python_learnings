sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
caps = sentence.upper()
print(caps)


word_list = ["Simple","is","better","than","complex."]
space = " ".join(word_list)
print(space)


sentence = "If the implementation is hard to explain, it might be a bad idea."
replaced_sen = sentence.replace("hard","easy").replace("bad","good")
print(replaced_sen)