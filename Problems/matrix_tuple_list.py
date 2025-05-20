tuple_matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

list_tuple_matrix = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]

list_tuple_matrix.append([10, 11, 12])
print(list_tuple_matrix)

list_tuple_matrix.pop()
print(list_tuple_matrix)

tuple_list_matrix = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

tuple_list_matrix[0].append(4)
print(tuple_list_matrix)

tuple_list_matrix[0].pop(-1)
print(tuple_list_matrix)


dict_matrix = {
    'a': {1: 1, 2: 2, 3: 3},
    'b': {1: 4, 2: 5, 3: 6},
    'c': {1: 7, 2: 8, 3: 9}
}

print(dict_matrix['b'][2])


# set matrix by frozenset
set_matrix = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6]),
    frozenset([7, 8, 9])
}

print(set_matrix)
