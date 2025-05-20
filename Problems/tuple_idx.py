# counting tuples
tuple1 = (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1)
print(tuple1.count(2))

# counting lists
list1 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
print(list1.count(3))

print()

# indexing tuples
print(tuple1[1])
print(tuple1.index(3))

value = 4
if value in tuple1:
    print(tuple1.index(value))
else:
    print("Not found")
