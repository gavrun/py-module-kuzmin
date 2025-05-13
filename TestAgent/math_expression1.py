x = float(input("Enter value for x: "))

def frac(x, i=5):
    if i <= 0:
        return x
    return x + (1 / frac(x, i - 1))

result = 1 / frac(x)

check = 1 / (x + (1 / (x + (1 / (x + (1 / (x + (1 / x))))))))

st0 = 1 / x
st1 = x + (1 / x)
st2 = x + (1 / (x + (1 / x)))
st3 = x + (1 / (x + (1 / (x + (1 / x)))))
st4 = 1 / (x + (1 / (x + (1 / (x + (1 / x))))))

print("result =", result)
print("check =", check)
print(st0, st1, st2, st3, st4)
