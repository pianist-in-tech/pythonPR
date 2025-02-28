#unmutable, used for fixed collections, faster than lists, fixed size
#tuple doesn't support item assignment

#tuple
coord = (4,5)

#indexing and slicing (same as lists)

#unpacking
x, y = coord
print(x, y)

#tuple with multiple elements
data = (1, "Python", 3.14)
print(data[1])

data1 = (1, [2,3],4)
data1[1].append(5)
print(data1)