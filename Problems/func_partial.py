# partial function

# def add(x, y, z):
#     return x + y + z

# add10 = add(10)
# print(add10(20, 30))

# add10and20 = add(10, 20)
# print(add10and20(30))

# partial function

def add(x, y, z):
    return x + y + z

def add_partial(x):
    def add_partial_inner(y, z):
        return add(x, y, z)
    return add_partial_inner
    
add10 = add_partial(10)
print(add10(20, 30))

# partial curry function

def add(x, y, z):
    return x + y + z

def add_partial(x):
    def add_partial_inner_1(y):
        def add_partial_inner_2(z):
            return add(x, y, z)
        
        return add_partial_inner_2
    return add_partial_inner_1
    
add10 = add_partial(10)
add10and20 = add10(20)
print(add10and20(30))


# example

person = {
    'name': 'Name',
    'age': 18,
}

def get_person_entry(dict, key, default_value):
    if key in dict:
        return dict[key]
    else:
        return default_value
    

print(get_person_entry(person, 'name', 'N/A'))

# print(get_person_entry(building, 'name', 'N/A'))
# print(get_person_entry(car, 'name', 'N/A'))
# print(get_person_entry(job, 'name', 'N/A'))

# 

def get_person_entry_partial(dict, key, default_value):
    def get_person_entry_inner(dict):
        if key in dict:
            return get_person_entry(dict, key, default_value)
    return get_person_entry_inner

get_person_name = get_person_entry_partial('name', 'N/A')

print(get_person_name(person))

# print(get_person_name(building))
# print(get_person_name(car))
# print(get_person_name(job))


# example functools

from functools import partial

def add(x, y, z):
    return x + y + z

add10 = partial(add, 10)
print(add10(add, 20, 30))

def get_person_entry(dict, key, default_value):
    if key in dict:
        return dict[key]
    else:
        return default_value

get_person_name = partial(get_person_entry, key='name', default_value='N/A')
print(get_person_name(person))


