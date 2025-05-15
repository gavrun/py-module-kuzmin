sample = [1, ["another", "ist"], ("a", "tuple")] # List consists of an integer, another list, and a tuple
print(sample[2]) # ('a', 'tuple')
print(sample)

slist1 = list() # returns an empty list - same as slist1 = []

mylist = ["List item 1", 2, 3.14] # This list contains a string, an integer, and a float
print("This is a list:", mylist)

mylist[0] = "List item 1 again" # Change the first (zero) element of the mylist sheet
print(mylist)

mylist[-1] = 3.18 # Change the last element of the sheet
print(mylist)

print(mylist[:]) # Read all elements

print(mylist[0:2]) # Read the zeroth and first elements

print(mylist[-3:-1]) #Read elements from zero (-3) to second (-1) (not inclusive)

print(mylist[1:]) #Read elements from first to last

x = 2
if x in mylist: # operator for checking for presence in (or not in)
    print('is', x)
else:
    print('isn not', x)

# 1. List methods

a = [8, 7, 5.5, 1000, 3.50, 200]
a[0] = 7
print(a) # [7, 7, 5.5, 1000, 3.50, 200]
print(a.index(7)) # 0
print(a.count(7)) # 2

a.insert(2, 1000) # same for slice a[2:2] = [1000]
print(a) # [7, 7, 1000, 5.5, 1000, 3.5, 200]

a.append(5.5)
print(a) # [7, 7, 1000, 5.5, 1000, 3.5, 200, 5.5]

a += [0, 0]
print(a) # [7, 7, 1000, 5.5, 1000, 3.5, 200, 5.5, 0, 0]

L = list('cde')
L.extend('fgh') # Appends all elements of the iterable to the end of L +=
print(L) # ['c', 'd', 'e', ​​'f', 'g', 'h']

b = a.pop() # return the last element, removing it from the list
print(b) # 0

b = a.pop(6) # return the 6th element (index), removing it from the list
print(b) # 200

print(a) # [7, 7, 1000, 5.5, 1000, 3.5, 5.5, 0]

a.sort() # sorts the original object (with the reverse = True parameter - descending)
print(a) # [0, 3.5, 5.5, 5.5, 7, 7, 1000, 1000]
print(a.sort()) # returns None

b1 = [21,15,7,8]
a1 = sorted(b1) # creates a new list containing a sorted version of the list given to it
print(a1,'---', b1) # [7, 8, 15, 21] --- [21, 15, 7, 8]

a.remove(1000) # finds the first instance of the given value in the list and removes that value from the list
print(a) # [0, 3.5, 5.5, 5.5, 7, 7, 1000]
'''If remove doesn't find any elements to remove, it throws an error'''

del a[2:4] # Removes elements with indices 2 through 3 from the list - same as above a[2:4] = []
print(a) # [0, 3.5, 7, 7, 1000]

a.reverse()
print(a) # [1000, 7, 7, 3.5, 0]

# 2. Comparisons and Equality
# Simple Comparison
a = [1, 5, 10]
b = [1, 5, 10]
print(a == b)# True

b[0] = 5
print(b) # [5, 5, 10]
print(a < b) # True

# Nested comparison
a[0] = [3, "aaa"]
b[0] = [3, "bb"]
print(a, b) # ([[3, 'aaa'], 5, 10], [[3, 'bb'], 5, 10])
print(a < b) # True