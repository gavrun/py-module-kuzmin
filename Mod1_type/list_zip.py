sample = [1, 2, 3]
a = [8, 7, 5.5, 1000, 3.50, 200]
mylist = ["List item 1", 2, 3.14]

dd = [ [sample], [a], [mylist] ]
dd = [ sample, a, mylist ]
print(dd)
dd[1][2] = 34
print(dd)

ddd = list(zip(sample, a, mylist))
'''
zip() returns an iterator of tuples, where the i-th tuple contains the i-th element
from each sequence of arguments or iterables'''

print(ddd)
ddd[1][2] = 34
print(ddd[0][2][3])