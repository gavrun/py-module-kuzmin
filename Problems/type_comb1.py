numbers_list_1 = [1, 1.0, 1 + 1j]
numbers_list_2 = [1, 1.0, 1 + 1j]

for x in numbers_list_1:
    for y in numbers_list_2:
        print(f'{type(x).__name__} + {type(y).__name__} = {type(x + y).__name__}')
        print(f'{type(x).__name__} - {type(y).__name__} = {type(x - y).__name__}')
        print(f'{type(x).__name__} * {type(y).__name__} = {type(x * y).__name__}')
        print(f'{type(x).__name__} / {type(y).__name__} = {type(x / y).__name__}')
        print(f'{type(x).__name__} ** {type(y).__name__} = {type(x ** y).__name__}')
        # print(f'{type(x).__name__} // {type(y).__name__} = {type(x // y).__name__}')
        # print(f'{type(x).__name__} % {type(y).__name__} = {type(x % y).__name__}')
        