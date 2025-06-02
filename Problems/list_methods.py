# adding elements to lists

my_list = [1, 2, 3, 4, 5]

my_other_list = [6, 7, 8]
my_tuple = (9, 10, 11)

print(my_list)

my_list.append(6)

my_list.extend(my_other_list)
my_list.extend(my_tuple)

my_list.insert(2, 2.5)
my_list.insert(0, 0)

print(my_list)


# removing elements from lists

my_list = [1, 2, 3, 4, 5]

print(my_list)

last_element = my_list.pop(0)

print(last_element)
print(my_list)

my_list_2 = ['a', 'b', 'c', 'd', 'e', 'c', 'c']

my_list_2.remove('c')

print(my_list_2)


# removing elements from lists

my_list = [1, 2, 1, 3, 4, 5, 1]

def remove_all(list, value):
    occurences = my_list.count(value)
    for elem in range(occurences):
        my_list.remove(value)

remove_all(my_list, 1)
print(my_list)




