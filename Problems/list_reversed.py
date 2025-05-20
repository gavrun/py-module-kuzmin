def reverse_half(l):
    midpoint = int(len(l) / 2) # odd length .5
                               # even length .0
    first_half = l[:midpoint]
    last_half = l[midpoint:]

    return [*last_half, *first_half]

print(reverse_half([1, 2, 3, 4]))
print(reverse_half([1, 2, 3, 4, 5]))
