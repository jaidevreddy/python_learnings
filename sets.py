myset = set([1,2,3,4,5])
otherset = {1,2,3,4,5}

print(myset)
print(otherset)

sets = set([1,2,3,4,5,1,1,1,1])
print(sets)

tupleset = set([1,2,3,(1,2,3)])
print(tupleset)
print(2 in tupleset)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
s3.add("a")
s3.remove(3)
s3.discard(6)
print(s3)

popset = {'a','b','c'}
popset.pop()
print(popset)