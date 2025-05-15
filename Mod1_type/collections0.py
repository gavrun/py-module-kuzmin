# Indexing and slicing
s = "Python"
print(s[-1]) # The last character is 'n'
print(s[0:2]) # The slice includes the first 2 characters - 'Py'
print(s[2:-1]) # From 3rd to the second-to-last character - 'tho'
print(s[0:-1:2]) # From 1st to the second-to-last character through 2 - 'Pto'

# The [start] and [end] parameters can be omitted
# In this case, the slice is taken from the beginning to the end of the string
print(s[:3]) # The first 3 characters are 'Pyt'
print(s[3:]) # From the 3rd character to the end - 'hon'

# Slicing can be used to get a string in reverse order:
print(s[::-1]) # nohtyP

# Tuples

t1 = 1,2,3
t2 = (4,5,6)
print(t1, "\n", t2)
print((101, 102, 103)) # pass a tuple of values ​​to a function

t1 += 11,22,33 # a new tuple with the result of the operation, assigned to a reference to a new object
print(t1)

# extracting elements
print(t1[2], ";", t1[-4] ) # the same element
print(t1[2:]) # getting elements using a slice
print(t1[2:4])

# nesting tuples, allow nesting with any depth

t3 = t1[3:], 101, t2[1:]
print(t3)
print(t3[0][2])

things = (1, -7.5, ("abc", (5, "ABC"), "queue"))
print(things[2][1][1][2])

# assigning names to indexes

MANUFACTURER, MODEL, SEATING = (0, 1, 2) # the sequence on the right is unpacked
MINIMUM, MAXIMUM = (0, 1)
aircraft = ("Airbus", "A320-200", (100, 220))
print(aircraft [SEATING] [MAXIMUM])

# Named tuples
# can be referenced by name, allowing you to create complex aggregates from data items

import collections
Sale = collections.namedtuple("Sale", "productid customerid date quantity price")

# creating sale objects

sales = []
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2008-09-15", 1, 18.49))

total = 0
for sale in sales:
    total += sale.quantity * sale.price
    print("Total ${0:.2f}".format(total))

Aircraft = collections.namedtuple("Aircraft", "manufacturer model seating")
Seating = collections.namedtuple("Seating", "minimum maximum")
aircraft = Aircraft("Airbus", "A320-200", Seating(100, 220))
#print(aircraft.seating.maximum)

# Lists
# A list is an ordered mutable sequence of elements
L = [-17.5, "kilo", 49, "V", ["ram", 5, "echo"], 7]
#print(L[1][0])
#print(L[4][2])
#print(L[4][2][1])

# extract two or more parts of a list at once
# unpack with the unpack operator (*)
first, *rest = [9, 2, -4, 8, 7]
#print((first, rest)) # (9, [2, -4, 8, 7])
first, *mid, last = "Charles Philip Arthur George Windsor".split()
#print(first, mid, last) # ('Charles', ['Philip', 'Arthur', 'George'], 'Windsor')
*directories, executable = "/usr/local/bin/gvim".split("/")
print(directories, executable)

def product(a, b, c):
    return a * b * c # * - multiplication operator

print(product(2, 3, 5)) # normal call with three arguments
L = [2, 3, 5] # passing one unpacked element
print(product(*L))
print(product(2, *L[1:])) # first - normal, second unpacks slice

# Dictionaries

#several ways to create dictionaries - they all create the same dictionary:
d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id": 1948, "name": "Washer", "size": 3}
#print(d1)

mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14} #Create a dictionary with numeric and integer indices
print(mydict)

mydict["pi"] = 3.15 #Change the dictionary element at index "pi".
#print(mylist)

dp = {} # empty dictionary
# filling the dictionary
dp['color'] = 'red'
dp['index'] = 101
print(dp)

dp['name'] = input("Enter name: ")
dp['age'] = int(input("Enter age: "))
print(dp)
