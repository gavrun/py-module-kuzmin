# Generators - list comprehension

# List generators allow you to create and quickly fill out lists

# Example 1. We get a list of numbers from 1 to 10 (using the RANGE function):
numbers = []
for i in range(1, 11):
    numbers.append(i)

# If only even numbers are needed:
numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i)

# Listen generators: expression returns in general:
# [ expression for item in list if conditional ]

# A simple example - there is a list - let's make a list
a = [1, 2, 3]   # a - an object
b = [i+10 for i in a]
print(a, '\n', b)    # [1, 2, 3]  [11, 12, 13] - The generator creates a new list, and does not change the existing

# Decision of example 1
# All from 1 to 10:
numbers = [i for i in range(1, 11)]
print(numbers)

# Only even:
numbers = [i for i in range(1, 11) if i % 2 == 0]
print(numbers)


# Example 2. There is a dictionary - we get lists:
a = {1:10, 2:20, 3:30}
b = [[i,a[i]] for i in a]
c = [j for i in b for j in i]
print(a, '\n', b, '\n', c)


# Dictionary generators: return the dictionary (external brackets - figured):
#{ key:value for item in list if conditional }

# Example.
# A list of dictionaries in which one of the values ​​is used as an identifier:
data = [
  {'id': 10, 'data': '...'},
  {'id': 11, 'data': '...'},
  {'id': 12, 'data': '...'},
  {'id': 10, 'data': '...'},
  {'id': 11, 'data': '...'},
]
# It needs to be removed repetitions
# Solution based on the Generator of the Dictionary:
# creates a dictionary, the keys of which are fields that have taken as a unique identifier,
# Then, using the Values ​​() method, we get all the values ​​from the created dictionary
dd = { d['id']:d for d in data }.values()
print(dd)



