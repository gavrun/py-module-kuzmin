x = 10

if x > 5: 
    y = "yes"
else:
    y = "no"
print(y)

# ternary
y = "yes" if x > 11 else "no"
print(y)

y = "no" if not x > 5 else "yes"
print(y)

y = "yes" if x > 5 else "no" if x < 5 else "maybe"
print(y)

y = "no" if not x > 5 else "yes" if x != 5 else "maybe"
print(y)

