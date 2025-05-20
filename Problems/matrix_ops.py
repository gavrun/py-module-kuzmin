matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# iterate over matrix
for row in matrix: 
    for item in row:
        print(item, end=' ')

# comprehension on matrix
print([ [ x for x in row ] for row in matrix ])

