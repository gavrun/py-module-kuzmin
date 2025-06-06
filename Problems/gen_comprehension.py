import sys

# list comprehension

# my_list = []
# for num in range(5, 10):
#     my_list.append(num * num)    

my_list = [num * num for num in range(5, 10)]

print(sys.getsizeof(my_list))

# generator comprehension

my_list_gen = (num * num for num in range(5, 10))

print(sys.getsizeof(my_list_gen))



