dict1 = {'a': 1, 'b': 2, 'c': 3 }
dict2 = {'d': 4, 'e': 5, 'f': 6 }
dict3 = {'a': 100, 'c': 35, 'f': 0 }

print(dict1)
print(dict2)
print(dict3)

#
new_dict4 = { key: value for key, value in dict1.items() }
print(new_dict4)

new_dict5 = { key: value * 2 for key, value in dict1.items() }
print(new_dict5)

new_dict6 = { key.upper(): value * 2 for key, value in dict1.items() }
print(new_dict6)

new_dict7 = { key: value for key, value in dict1.items() if value % 2 != 0}
print(new_dict7)

new_dict8 = { key: value for key, value in dict1.items() if key == 'a'}
print(new_dict8)

