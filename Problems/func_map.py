# not functional

numbers = [1,2,3,4,5]
squared = []

for n in numbers:
    squared.append(n**2)

print(squared)


# functional

def square_func(n):
    return n ** 2

numbers2 = [1,2,3,4,5]
squared2 = []

squared2 = map(square_func, numbers2)

# print(next(squared2))
for i in squared2:
    print(i)

squared2 = list(squared2)
print(squared2)
