if a > b:
    print(a)
    res = a
    if a > 0:
        print("Positive!")
else:
    print(b)
    res = b

res = a if a > b else b
print(res)
