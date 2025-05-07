# Integer variables
a = 10
b = 3

# Integer division, modulo, and exponentiation
print("a // b =", a // b)      # integer division (quotient)
print("a % b =", a % b)        # remainder
print("a ** b =", a ** b)      # exponentiation

# String and integer concatenation error
try:
    param = "string" + 15
except TypeError as e:
    print("Error:", e)  # you cannot concatenate string and int directly

# Correct way: convert integer to string
param = "string" + str(15)
print("Correct concatenation:", param)

# User input and number addition
n1 = input("Enter the first number: ")   # input is always a string
n2 = input("Enter the second number: ")

n3 = float(n1) + float(n2)               # convert strings to floats
print(n1 + " plus " + n2 + " =", n3)     # display result
