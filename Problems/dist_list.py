dict = { 'name': "Bob", 'Name': "Dick" }

for key in dict:
    print(f'{key}: {dict[key]}')

keys = dict.keys()
value = dict.values()

for value in dict.values():
    print(value)

items = dict.items()

print(items) # items are tuples in a list

for key, value in dict.items():
    print(f'{key}: {value}')
