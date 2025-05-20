dict_default = { 'name': 'N/A', 'age': '1', 'feature': 'blue' }
dict = { 'name': 'One Love', 'age': '24', 'feature': 'red' }

print(dict_default)
print(dict)

# merge reverse 
print(dict_default | dict)

# call individually
dict.setdefault('name', 'N/A')

