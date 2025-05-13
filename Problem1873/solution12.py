# https://codeforces.com/problemset/problem/1873/B

from math import prod

num_of_tests = int(input())

for _ in range(num_of_tests):
    num_in_array = int(input())
    array_of_int = list(map(int, input().split()))

    # product of each index
    max_product = max(
        prod(
            array_of_int[:idx] + [array_of_int[idx] + 1] + array_of_int[idx + 1:] # list copy with incremented element
        )
        for idx in range(num_in_array)
    )

    print(max_product)
