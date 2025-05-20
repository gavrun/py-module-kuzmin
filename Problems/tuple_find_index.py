def find_index(t, val):
    indices = []
    index = 0
    for value in t:
        if value == val:
            indices.append(index)
        index += 1
    return indices

def find_index_enum(t, val):
    indices = []
    for i, tuple_value in enumerate(t):
        if tuple_value == val:
            indices.append(i)
    return indices

tuple = (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1)

print(find_index(tuple, 1))
print(find_index_enum(tuple, 1))

# output [0, 3, 6, 9, 12]
