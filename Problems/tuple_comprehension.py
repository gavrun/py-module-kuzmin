#
tuple1 = (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1)
tuple2 = ('a', 'b', 'c', 'd', 'e')

for letter in tuple2:
    print(letter)

# constructor func
a = [1, 2, 3]
b = tuple(a)
print(b)

# generator comprehension
list3 = ['a', 'b', 'c', 'd', 'e']
tuple3 = ('a', 'b', 'c', 'd', 'e')
print(list3)
print(tuple3)
list4 = list(x.upper() for x in list3)
tuple4 = tuple(x.upper() for x in tuple3)
print(list4)
print(tuple4)
