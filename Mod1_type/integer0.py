# Integers

# There is no real limit to the length of an integer value
# Limited by the amount of memory available to the system
print(1231231231231231231231231231231231231231231231239999999 + 1)

# Python interprets a sequence of decimal digits without a prefix as a decimal number:
print(10)
# prefixes are used for other representations
print(0o10) # 8
print(0x10) # 16
print(0b10) # 2

print(type(10))
# Real numbers

# float represents double-precision floating-point numbers
print(0.1 + 0.2) # 0.30000000000000004
# floats cannot be reliably compared for value equality,
# since they have limited precision
print(0.1 + 0.1 + 0.1 == 0.3) # False

# Complex numbers
# are defined as follows: <real number>+<imaginary part>j.
print (2+3j) # (2+3j)
print(type(2+3j)) # <class 'complex'>

# Immutable types

a = 1
b = 2
c = "start"
print(a)
# an identifier is some integer value by which an object is
# uniquely addressed
print(id(a))
a = b
b = b + 1
print(id(a))
print(a)
print(type(a))
a = c
print(id(a))
print(a)
print(type(a))

# Mutable types

list1 = [2, 3, 4]
print(id(list1))

list2 = list1 # The assignment operator copies the object reference, creating a shallow copy
print(id(list2))
list1[1] = 33
print(list1) # The list1 variable has changed
print(list2) # The list2 variable has also changed
print(id(list1))

list3 = list1[:] # creates a copy of the list - gets a slice from the beginning to the end of the list - deep copy
list1[1] = 333
print(list1) # Variable list1 has changed
print(list3) # Variable list3 has not changed
print(id(list1))
print(id(list3))

list1 = list1 * 2
print(list1)
print(id(list1))

list1 = 8
print(list1) # Variable list1 has changed
print(list2) # Variable list2 has not changed
print(id(list1))
print(id(list2))

mylist = [11,22,33,44,55,66]
mylist.append(77) # function that performs direct changes to objects
# should be called without assigning a return value
print(mylist)

# Type None - used to indicate the absence of a value
# Example. Returned from functions that do not explicitly return anything
mylistnew = mylist.append(88) # returns None
print(mylistnew) # None
print(mylist)
