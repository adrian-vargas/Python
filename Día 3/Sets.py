mi_set=set({(-1,-2.-3),1,1,1,2,3,4,5})
print(type(mi_set))
print(mi_set)

tu_set={1,2,3}
print(type(tu_set))
print(tu_set)

print(len(mi_set))
print(2 in mi_set)
s1={1,2,3}
s2={4,5,6}
s3=s1.union(s2)
print(s3)
s2.add(7)
print(s2)
s2.remove(4)
print(s2)
s2.remove(6)
print(s2)
s2.discard(4)
print(s2)
sorteo=s1.pop()
print(sorteo)
s2.clear()
print(s2)