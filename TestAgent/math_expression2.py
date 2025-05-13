x = float(input("Enter value for x: "))

def frac_recursive(x, i=5):
    """Calculate the nested fraction recursively."""
    if i <= 0:
        return x
    return x + (1 / frac_recursive(x, i - 1))

result = 1 / frac_recursive(x)

check = 1 / (x + (1 / (x + (1 / (x + (1 / (x + (1 / x))))))))

st0 = 1 / x
st1 = x + (1 / x)
st2 = x + (1 / (x + (1 / x)))
st3 = x + (1 / (x + (1 / (x + (1 / x)))))
st4 = 1 / (x + (1 / (x + (1 / (x + (1 / x))))))

print("result =", result)
print("check =", check)
print(st0, st1, st2, st3, st4)
