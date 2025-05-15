def combine(d1, d2):
    d_combined = {}
    for key in d1:
        d_combined[key] = d1[key]
    for key in d2:
        d_combined[key] = d2[key]
    return d_combined

def combine_verbose(d1, d2):
    d_combined = {}
    #
    for key in d1:
        if key in d2:
            print('can t use duplicated keys')
        else:
            d_combined[key] = d1[key]
    for key in d2:
        d_combined[key] = d2[key]
    return d_combined

dict1 = {'a': 1, 'b': 2, 'c': 3 }
dict2 = { 'a': 10, 'b': 20, 'c': 30, 'c': 100, 'd': 200, 'e': 300 }

print(combine(dict1, dict2))
print()

print(combine_verbose(dict1, dict2))
