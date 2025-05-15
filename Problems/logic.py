var = 1


# example 1:
print(var > 0)
print(not (var <= 0))


# example 2:
print(var != 0)
print(not (var == 0))


# De Morgan's laws
# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

# example 3:
i = 1
j = not not i
print(i,j)

