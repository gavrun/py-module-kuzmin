# generator lazy iterator

def square_num(list_of_nums):
    my_list = []
    for num in list_of_nums:
        my_list.append(num * num)
    return my_list

squared_list = square_num([1,2,3,4,5,6,7,8,9])

print(squared_list)

#

def square_num(list_of_nums):
    for num in list_of_nums:
        yield (num * num)

gen_object = square_num([1,2,3,4,5,6,7,8,9])
next(gen_object)
print(next(gen_object))

for x in gen_object:
    print(x)

