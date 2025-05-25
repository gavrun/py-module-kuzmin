
# Integer and Binary values
# i = 00000000000000000000000000001111 (15)
# j = 00000000000000000000000000010110 (22)
i = 15
j = 22

# Logical AND — returns the second operand if the first is truthy
logical_and = i and j  # Returns 22 (not 0 or 1)

# Bitwise AND — operates on each bit
bitwise_and = i & j  # Result: 00000000000000000000000000000110 = 6

# Logical NOT — returns False if the operand is truthy
logical_not = not i  # Result: False because i is non-zero

# Bitwise NOT — inverts each bit (gives negative due to two's complement)
bitwise_not = ~i  # Result: -16

print("logical_and:", logical_and)
print("bitwise_and:", bitwise_and)
print("logical_not:", logical_not)
print("bitwise_not:", bitwise_not)


# Compound Bitwise Operations

x = 12  # 1100 in binary
y = 10  # 1010 in binary

# Bitwise AND and assignment
x = x & y      # x becomes 8 (1000)
print("x after x & y:", x)

# Reset x for next examples
x = 12

# Bitwise OR and assignment
x |= y         # x becomes 14 (1110)
print("x after x |= y:", x)

# Reset x
x = 12

# Bitwise XOR and assignment
x ^= y         # x becomes 6 (0110)
print("x after x ^= y:", x)


# Bit Masking 

flag_register = 0b1010  # Example register: 1010 (binary)
the_mask = 0b1000       # Mask to check/set/reset the 4th bit

# Reset the masked bit to 0
flag_register = flag_register & ~the_mask
# Same as:
flag_register &= ~the_mask

# Set the masked bit to 1
flag_register = flag_register | the_mask
# Same as:
flag_register |= the_mask

# Toggle (invert) the masked bit
flag_register = flag_register ^ the_mask
# Same as:
flag_register ^= the_mask

# Check if the masked bit is set
if flag_register & the_mask:
    print("Bit is set.")
else:
    print("Bit is reset.")


# Bit Shifting

var = 17  # Binary: 10001
var_right = var >> 1  # Right shift by 1 (divides by 2): 1000 = 8
var_left = var << 2   # Left shift by 2 (multiplies by 4): 1000100 = 68

print("Original:", var, "Left Shift:", var_left, "Right Shift:", var_right)


# Logical Expressions

x = 1
y = 0

# Expression: ((x == y) and (x == y)) or not(x == y)
# Simplifies to: (False and False) or True → True
z = ((x == y) and (x == y)) or not(x == y)
print("not(z):", not(z))  # Output: False


# Bitwise Examples

x = 4  # 0100
y = 1  # 0001

a = x & y     # 0000 → 0
b = x | y     # 0101 → 5
c = ~x        # two's complement → -5
d = x ^ 5     # 0100 ^ 0101 = 0001 → 1
e = x >> 2    # 0100 >> 2 = 0001 → 1
f = x << 2    # 0100 << 2 = 10000 → 16

print("Results:", a, b, c, d, e, f)
