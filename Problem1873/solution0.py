# https://codeforces.com/problemset/problem/1873/B

testcase_cnt = int(input())
for _ in range(testcase_cnt):
    _ = int(input()) 
    arr = input().split()
    arr_new = []
    for elem in arr:
        elem = int(elem)
        arr_new.append(elem)
    print(arr_new)
