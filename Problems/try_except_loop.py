# input1 = input("Enter number 1 ")
# input2 = input("Enter number 2 ")

# x = int(input1)
# y = int(input2)

# total = x + y
# print(f'Sum of {x} and {y} is {total}')

# refactor

# first_number_valid = False

# while not first_number_valid:
#     try:
#         input1 = input("Enter number 1 ")
#         x = int(input1)
#         first_number_valid = True
#     except ValueError:
#         print("That is not a number")

# second_number_valid = False
# while not second_number_valid:
#     try:
#         input2 = input("Enter number 2 ")
#         y = int(input2)
#         second_number_valid = True
#     except ValueError:
#         print("That is not a number")

# total = x + y
# print(f'Sum of {x} and {y} is {total}')

# refactor

def input_number(prompt):
    while True:
        try:
            _input = input(prompt)
            _value = int(_input)
        except ValueError:
            print("That is not a number")
    return _value

x = input_number("Enter a number: ") 
y = input_number("Enter another number: ") 

total = x + y
print(f'Sum of {x} and {y} is {total}')
