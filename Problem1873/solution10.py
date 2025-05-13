# https://codeforces.com/problemset/problem/1873/B

from math import prod

num_of_tests = int(input())

for _ in range(num_of_tests):
    num_in_array = int(input())
    array_of_int = list(map(int, input().split()))
    
    max_product = 0

    for idx in range(num_in_array):
        new_array_of_int = array_of_int.copy()
        new_array_of_int[idx] += 1 # only one can be changed
        
        temp_product = prod(new_array_of_int)
        max_product = max(max_product, temp_product)

    print(max_product)
