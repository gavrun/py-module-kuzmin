import random

int_list = []

for _ in range(200_000):
    val = random.randint(0, 10000)
    if not val in int_list:
        int_list.append(val)
        if len(int_list) % 1000 == 0:
            print(len(int_list))
print(int_list)
