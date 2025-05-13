numbers_list_1 = [1, 1.0, 1 + 1j]
numbers_list_2 = [1, 1.0, 1 + 1j]

for x in numbers_list_1:
    for y in numbers_list_2:
        print(f'{type(x)} + {type(y)} = {type(x + y)}')