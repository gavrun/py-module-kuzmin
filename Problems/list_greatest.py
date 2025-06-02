# to find the greater value in the list

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

# with slicing

my_list1 = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest1 = my_list1[0]

for i in my_list1[1:]:
    if i > largest1:
        largest1 = i

print(largest1)

