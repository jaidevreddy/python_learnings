dictionary = {"k1":["a","b","c"], "k2":["d","e","f"]}

res = dictionary["k1"][2]

print(dictionary["k1"])
print(dictionary["k1"][1])
print(res)
print(dictionary["k2"][1].upper())

dictionary["k3"] = "g"

print(dictionary)