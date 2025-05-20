a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

a.extend(b)
a.extend(c)
print(a)

# unpack elements
# d = []
d = [0, *a, 100, -6, *b, *c]
print(d)

# list element
e = [0, a, 100, -6, b, c]
print(e)
