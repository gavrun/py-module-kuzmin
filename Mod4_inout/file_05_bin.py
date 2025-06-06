import sys
import random as r
from array import array

ROWS = 2
COLS = 2

matrix = []
for idx in range(0, ROWS):
    matrix.append([])
    for idy in range(0, COLS):
        sign = 1.0
        if r.choice([True, False]):
            sign = -1.0
        matrix[idx].append(sign * r.uniform(sys.float_info.min, sys.float_info.max))

print(matrix)

with open('matrix.dat', 'wb') as file_handle:
    for idx in range(0, ROWS):
        float_array = array('d', matrix[idx])
        float_array.tofile(file_handle)


new_matrix = []
with open('matrix.dat', 'rb') as file_handle:
    for idx in range(0, ROWS):
        float_array = array('d')
        float_array.fromfile(file_handle, COLS)
        new_matrix.append(list(float_array))

print(new_matrix)
