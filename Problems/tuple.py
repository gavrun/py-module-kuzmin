# lists
l = [1, 2, 3]

# tuples
t1 = (1, 2, 3)
print(t1)

t_empty = ()
t_element = (99, )
print(t_empty)
print(t_element)

# ref
t0 = t1
print(t0)

# functional approach
t2 = (1, [10, 20], 3)
print(t2)

t3 = t2[1], t1[0]
print(t3)

print(t1[1:])
