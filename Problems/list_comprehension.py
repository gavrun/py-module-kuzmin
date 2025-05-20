# 
numbers = [1, 2, 3, 4, 5, 6]
doubled1 = []

for x in numbers:
    doubled1.append(x * 2)

print(doubled1)

#
# doubled2 = []
# numbers2 = numbers.copy()

for x in range(len(numbers)):
    numbers[x] = numbers[x] * 2

print(numbers)

# comprehension
numbers3 = [1, 2, 3, 4, 5, 6]
doubled3 = [x * 2 for x in numbers3]
print(doubled3)

# filtering
numbers4 = [1, 2, 3, 4, 5, 6]
num_even = []

for x in numbers4:
    if x % 2 == 0:
        num_even.append(x)

print(num_even)

# comprehension filtering
num_even2 = [x for x in numbers4 if x % 2 == 0]

# 
persons = [{'name': 'One', 'age': 1}, {'name': 'Two', 'age': 7}, {'name': 'Three', 'age': 5}]
names = []

for p in persons:
    names.append(p['name'])

print(names)

# comprehension
names2 = [p['name'] for p in persons]
print(names2)

# comprehension filtering
names3 = [p for p in persons if p['age'] > 5]
print(names3)
