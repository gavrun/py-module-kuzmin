def any_has_value(dictionaries, key, value):
    values = [ x.get(key, None) for x in dictionaries]
    return any(v == value for v in values)

dict1 = [
    {'a':1, 'b':2, 'c':3},
    {'a':1, 'b':2, 'c':4},
    {'a':1, 'b':2, 'c':3},
    {'a':1, 'b':2, 'c':3}
]
print(any_has_value(dict1, 'c', 4))
print(any_has_value(dict1, 'c', 5))

#

def all_greater_than(numbers, value):
    return all([ x > value for x in numbers ])

dict2 = [2, 3, 4, 5, 6]
print(all_greater_than(dict2, 1))
print(all_greater_than(dict2, 2))

#

all([True, True, True])
any([True, False])
any([True, True, True])
any([False, False, False])
