def create_set(l):
    set_dict = {}
    for value in l:
        set_dict[value] = True
    return set_dict

def add_to_set(s, value):
    s[value] = True

def discard_from_set(s, value):
    s.pop(value)

s = create_set([1, 2, 3])
print(1 in s)

add_to_set(s, 4)
print(4 in s)

discard_from_set(s, 4)
print(4 in s)
