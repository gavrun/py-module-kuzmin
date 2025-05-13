# https://codeforces.com/problemset/problem/1873/B

testcase_cnt = int(input())
for _ in range(testcase_cnt):
    _ = int(input())
    arr = input().split()
    for idx in range(len(arr)):
        arr[idx] = int(arr[idx])
    print(arr)
