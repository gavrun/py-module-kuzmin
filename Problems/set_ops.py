prime_numbers = { 2, 3, 5, 7, 11, 13, 17, 19 }
comp_numbers = { 4, 6, 8, 9, 10, 12, 14, 15, 16 }

# union
union = prime_numbers | comp_numbers
print(union)

# intersection
intersection = prime_numbers & comp_numbers
print(intersection)

# difference 
difference = prime_numbers - comp_numbers
print(difference)

# symmetric difference
symm_difference = prime_numbers - comp_numbers
print(symm_difference)

