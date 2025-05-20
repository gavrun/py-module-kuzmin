dict1 = {'a': 1, 'b': 2, 'c': 3 }
dict2 = {'d': 4, 'e': 5, 'f': 6 }
dict3 = {'a': 100, 'c': 35, 'f': 0 }

print(dict1)
print(dict2)
print(dict3)

new_dict4 = {
    'dict1': dict1,
    'dict2': dict2,
    'dict3': dict3
}
print(new_dict4)

# merge
new_dict5 = dict1 | dict2 | dict3
print(new_dict5)

# unpack 
new_dict4 = {
    'a': 0 # backup value
    **dict1,
    'b': 99,
    **dict2,
    **dict3,
    'f': 999 # overriding value
}
print(new_dict4)
