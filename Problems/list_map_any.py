# find/check whether elements in a list

def is_equal_to_3(x):
    return x == 3

votes = [1, 2, 1, 2, 3, 1]

results = map(is_equal_to_3, votes)

if any(results):
    print('Someone voted for 3!')


# find the first element in a list that matches certain criteria

my_numbers = [100, 4, 298, 27, -100, 19]

def is_less_than_20(x):
    return x < 20

less_than_20 = list(filter(is_less_than_20, my_numbers))

print(is_less_than_20[0])


# 
my_numbers2 = [100, 4, 298, 27, -100, 19]

x = next(n for n in my_numbers2 in n < 20)
print(x)


