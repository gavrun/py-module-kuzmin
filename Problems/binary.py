# Binary Literals

# Binary literals 
num1 = 0b1100     # 12 in decimal
num2 = 0b1010     # 10 in decimal

print("Binary literals:")
print("a =", bin(num1))  # 0b1100
print("b =", bin(num2))  # 0b1010
print()

# Bitwise AND
a = 0b1100  # 12
b = 0b1010  # 10
and_result = a & b  # 0b1000 = 8

print("Bitwise AND:")
print("a =", bin(a))
print("b =", bin(b))
print("a & b =", bin(and_result), "(decimal:", and_result, ")")
print()

# Bitwise OR
c = 0b1100
d = 0b1010
or_result = c | d  # 0b1110 = 14

print("Bitwise OR:")
print("c =", bin(c))
print("d =", bin(d))
print("c | d =", bin(or_result), "(decimal:", or_result, ")")
print()

# Bitwise XOR
e = 0b1100
f = 0b1010
xor_result = e ^ f  # 0b0110 = 6

print("Bitwise XOR:")
print("e =", bin(e))
print("f =", bin(f))
print("e ^ f =", bin(xor_result), "(decimal:", xor_result, ")")
print()

# Bitwise NOT
g = 0b1100
not_result = ~g  # Inverts all bits (two's complement)

print("Bitwise NOT:")
print("g =", bin(g))
print("~g =", bin(not_result), "(decimal:", not_result, ")")
print()

# Bit Shifting
h = 0b1100

print("Bit Shifting:")
print("h =", bin(h))
print("h << 1 =", bin(h << 1), "(decimal:", h << 1, ")")  # Multiply by 2
print("h << 2 =", bin(h << 2), "(decimal:", h << 2, ")")  # Multiply by 4
print("h >> 2 =", bin(h >> 2), "(decimal:", h >> 2, ")")  # Divide by 4
print()

# Binary/Decimal Conversion
decimal_number = 25
binary_string = "11001"

print("Binary/Decimal Conversion:")
print("Decimal 25 to binary:", bin(decimal_number))
print("Binary '11001' to decimal:", int(binary_string, 2))
print()

# Bit Masking
flag = 0b1010     # Binary: 1010
mask = 0b1000     # Mask to operate on the 4th bit

print("Bit Masking:")
print("Initial flag:", bin(flag))

# Check if bit is set
print("Check bit set:", bool(flag & mask))

# Set the bit
flag |= mask
print("After setting bit:", bin(flag)) # 0b1010 | 0b1000 → 0b1010

# Reset the bit
flag &= ~mask
print("After resetting bit:", bin(flag)) # 0b1010 & ~0b1000 → 0b0010

# Toggle (flip) the bit
flag ^= mask
print("After toggling bit:", bin(flag)) # 0b0010 ^ 0b1000 → 0b1010
print()
