numbers = { 2, 3, 5, 7, 11, 13, 17, 19 }

for number in numbers:
    print(number)

empty_set_no = {}
empty_set_yes = set()
print(type(empty_set_no))
print(type(empty_set_yes))

create_set = set([2, 2, 3, 5, 7, 11, 11, 13, 17, 19])
print(create_set)

# forbidden_set1 = { 2, [3, 5] 7, 11, 13, 17, 19 }
# forbidden_set2 = { {'a': 1}, 2, 3, 5, 7, 11, 13, 17, 19  }

numbers2 = { 2, 3, 5, 7, 11, 13, 17, 19 }

if 11 in numbers2:
    print('yes')
else:
    print('no')

