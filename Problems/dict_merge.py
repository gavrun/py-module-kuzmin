dict1 = { 'name': 'One', 'age': '23', 'feature': 'blue' }
dict2 = { 'name': 'One Love', 'age': '24', 'feature': 'blue' }
more3 = { 'more': 'abc', 'evenmore': '5' }

print(dict1)

dict1.update(dict2)
print(dict1)

dict1.update(more3)
print(dict1)

# union piping
a = {'x': 1}
b = {'y': 2}
c = a | b
print(c)  # Output: {'x': 1, 'y': 2}


x = { 'a': 1 }
y = { 'a': 2 }
z = { 'a': 3 }

print(x | y | z)
print(z | y | x)

