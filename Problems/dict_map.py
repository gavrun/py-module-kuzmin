def create_sq_map(num):
    return { x: x * x for x in range(1, num + 1) }

print(create_sq_map(99))
