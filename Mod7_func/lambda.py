
# the same way with the help of function and lambda-expression
def func(x, y, z):
    return x + y + z

# and lambda-expression
f = lambda x, y, z: x + y + z
print((lambda x, y, z: x + y + z)(5,2,3))

print(f(10,12,13))

# can be used arguments with values ​​by default:
x = (lambda a="aaa", b="bbb", c="ccc": a + b + c)
print(x("www"))     #Wwwbbbccc

# Place other expressions inside Lambda
lower = (lambda x, y: x if x < y else y)
print(lower(23,45))         #23
print(lower("k23","a45"))   # 45

"""
The use of lambda exploration
"""

# Implementation of sorting by the required field

elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")] 
elements.sort()
print(elements)

# on the serial number and name
elements.sort(key=lambda e: (e[1], e[2])) 
print(elements)

# by name, without taking into account the register of symbols, and the serial number:
elements.sort(key=lambda e: (e[2].lower(), e[1])) 
print(elements)

# performing actions on demand - instead of creating three named functions
L = [lambda x: x**2,          # Built -in definitions of functions
     lambda x: x**3, 
     lambda x: x**4]          # List of three functions

for f in L:
    print(f(2))    #  4, 8, 16

print(L[0](3))     #  9

#invested expressions
def action(x):
    return (lambda y: x + y) # Create and Return F-J

act = action(99)
act1 = action(-99)
print(act)    # <function <lambda>At0X00A16A88>
print(act(2))
print(act1(99))


"""
Joint use of Lambda and other functions
"""
# Max and Min functions have a key to the sorting parameter
# Key - a link to a function of 1 returning value by which follows
# Compare the values
lst = ["Java", "Basic", "C++", "Python"]
print(max(lst, key=lambda x: x.count("a")))  # Element LST, in which
                                             # the most "a"

# Filter () - filtering elements of the sequence
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)           # [5,7,97,77,23,73,61]

# Getting General Data
arr1 = [1, 3, 4, 5, 7] 
arr2 = [2, 3, 5, 6] 
result = list(filter(lambda x: x in arr1, arr2))  
print ("Intersection : ", result)   # [3,5]


# The MAP function applies to each element of the list the conveyed function
"""
Changing the list elements by your anonymous function"""
mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
print (kilometer_distances)     # [16,104,2784,384,144]


# Reduce () function accepts 2 arguments: function and sequence and
# sequentially applies the function-argument to the list elements, returns a single value.
# Python 3 Functools module functions
"""
Calculation of the sum of all elements of the list using Reduce:"""
from functools import reduce
items = [1,2,3,4,5]
sum_all = reduce(lambda x,y: x + y, items)
 
print (sum_all)     #15

