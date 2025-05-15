# Application of cycles to calculate the amount of sequence elements

lst = [1, 3, 5, 7, 9]
sum1 = 0
for i in lst:
   sum1 += i

print(sum1)


sum2 = 0
while lst:
    sum2 += lst[0]
    lst = lst[1:]

print(sum2)


# The use of iterators

lst = [1, 3, 5, 7, 9]
lst2 = lst[:]

sum1 = 0
for i in lst:
   sum1 += i

print(sum1)

sum2 = 0
iter_obj = iter(lst2)

while True:
    try:
        i = next(iter_obj)
        sum2 += i
    except StopIteration:
       break

print(sum2)

# 1. Sequences

fruits = ["Orange", "apples", "tangerines", "lemons"]
#  enumerate(iterable, start=0) - Returns an iterator where each element is a pair of “number” - “value”.
# The number is counted from Start
# Get a sequence of motorcies (number, element):
print(tuple(enumerate(fruits, start=1)))
print(list(enumerate(fruits, start=1)))

# Using Enumerate (), you can "give" the serial number to the element of the collection in the cycle
for i, item in enumerate(fruits, start=1):
    print(i, item)

# Using sorted (), you can derive the elements of the collection in an increase in the order
for item in sorted(fruits):
    print(item)    


# 2. Dictionary

employee = {"Full name": "Petov Sergey Viktorovich",
             "Department": "Sales",
             "Date of birth": "12/16/1998"}

# By default, the FOR cycle moves through the keys
# enumerate() и sorted() Similarly work with keys only
for attr in sorted(employee):
    print(attr)  # Get a key value - Employee [attr]

# Using items () you can immediately receive a couple of the key-value
for attr, value in employee.items():
    print(attr, ":\t", value)
