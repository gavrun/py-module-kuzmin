#

my_list0 = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list0) - 1):
        if my_list0[i] > my_list0[i + 1]:
            swapped = True  # a swap occurred!
            my_list0[i], my_list0[i + 1] = my_list0[i + 1], my_list0[i]

print(my_list0)

#

my_list1 = [8, 10, 6, 2, 4]
my_list1.sort()
print(my_list1)

#

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)


