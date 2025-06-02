# with no filter

my_numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_less_than_3 = []

for number in my_numbers:
    if number < 4:
        numbers_less_than_3.append(number)

print(numbers_less_than_3)


# get all the elements in a list that match specific criteria

my_numbers2 = [1, 2, 3, 4, 5, 6, 7]

def is_less_than_4(x):
    return x < 4

numbers_less_than_4 = list(filter(is_less_than_4, my_numbers2))
print(numbers_less_than_4)


