#tuple1 = 1,2
tuple1 = (0, "ojo", 2.5, [])
#tuple1[3].extend([2, 5, "sam"])
names = ["jide", "seyi", "janet"]
tuple1 = tuple1 + (1, 6)
names += tuple1
names = tuple(names)
#print(type(tuple1))
#help(tuple1)
#print(names.index("janet"))
#print(names)


x = {1, 1, 2, 2, 3, 3, 4, 5, 1, "sam"}
y = {1, 3, 7, 9, 10, 2}
#y = set()
x.add(10)
print(x.difference(y))