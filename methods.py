text = "we are learning methods"
text2 = "ABCD"

caps = text.upper()
caps1 = text[0].upper()
print(caps)
print(caps1)

small = text2.lower()
small2 = text2[0].lower()
print(small)
print(small2)

split = text.split()
split2 = text.split("e")
print(split)
print(split2)

a = "string"
b = "methods"
c = " ".join([a,b])
print(c)

e = "E"
join = "".join([text2,e])
print(join)


find = text.find("x")
find2 = text.find("a")
print(find)
print(find2)

replace = text.replace("methods", "python")
replace1 = text.replace("e","x")
print(replace)
print(replace1)
