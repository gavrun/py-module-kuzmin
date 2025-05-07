# Example of float formatting with format()
a = 1 / 3
print("{:7.3f}".format(a))  # 7 total width, 3 digits after decimal

# Formatting multiple values
a = 2 / 3
b = 2 / 9

print("{:7.3f} {:7.3f}".format(a, b))       # fixed-point format
print("{:10.3e} {:10.3e}".format(a, b))     # scientific notation

# Updated output for number addition program using format()
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")

n3 = float(n1) + float(n2)

# Using format() for clean output
print("{} plus {} = {:.2f}".format(n1, n2, n3))  # {:.2f} means 2 decimal places
