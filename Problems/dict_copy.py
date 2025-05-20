dict1 = {'a': 1, 'b': 2, 'c': 3 }
dict2 = {'d': 4, 'e': 5, 'f': 6 }

dict3 = dict1
dict4 = dict1.copy()

print(dict1)
print(dict2)
print(dict3)
print(dict4)
print()

print(dict1)
print(dict2)
# dict3['c'] = 0
print(dict3)
dict4['c'] = 0
print(dict4)

