def matrix_max(m):
    current_max = m[0][0]
    for row in m:
        for x in row:
            if x > current_max:
                current_max = x
    return current_max

def matrix_min(m):
    return min([ min(row) for row in m ])

def matrix_length(m):
    return sum([len(row) for row in m])

def matrix_size(m):
    return {
        'rows': len(m),
        'cols': len(m[0])
    }

def matrix_transpose(m):
    return [ [row[i] for row in m] for i in range(len(m[0])) ]

matrix1 = (
    [56, 4, 12],
    [-124, 3, 19],
    [89, 100, 3]
)
print(matrix_max(matrix1))
print(matrix_min(matrix1))
print(matrix_length(matrix1))
print(matrix_size(matrix1))
print(matrix_transpose(matrix1))
