def convert_upper_keys(d):
    return [ key.upper() for key in d.keys() ]

print(convert_upper_keys({'name': 'One', 'age': 7, 'feature': 'black'}))
