text = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"
result = text.lstrip(",:%_#")
print(result)


fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(3,'orange')
print(fruits)


phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

isolated_sets = phone_brands.isdisjoint(tv_brands)
print(isolated_sets) 