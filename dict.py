dict = {"k1":["a","b","c"], "k2":["d","e","f"]}

res = dict["k1"][2]

print(dict["k1"])
print(dict["k1"][1])
print(res)
print(dict["k2"][1].upper())

dict["k3"] = "g"

print(dict)