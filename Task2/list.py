# Create a list of numbers
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]

# View available methods for list
print("List methods:", dir(list))
print()
# str.join(iterable)
print("List methods:\n" + "\n".join(dir(list)))

# Get help for some common methods
help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list.reverse)

# Indexing: modify elements
list1[0] = 100        # change first element
print("Modified list:", list1)

# Append new element to the end
list1.append(77)
print("After append:", list1)

# Insert element at specific position
list1.insert(3, 55)   # insert 55 at index 3
print("After insert:", list1)

# Remove element by index
del list1[2]          # remove element at index 2
print("After deletion:", list1)

# Remove last element
list1.pop()           # pop removes and returns the last element
print("After pop:", list1)

