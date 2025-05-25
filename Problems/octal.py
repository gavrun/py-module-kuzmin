# Octal literals 
num1 = 0o10  # 8 in decimal
num2 = 0o20  # 16 in decimal

print("Octal literals:")
print("a =", oct(num1), "(decimal:", num1, ")")
print("b =", oct(num2), "(decimal:", num2, ")")
print()

# Conversion between octal and decimal

decimal_val = 64
octal_str = "75"

print("Decimal to Octal:")
print("64 →", oct(decimal_val))  # 0o100

print("Octal string to Decimal:")
print("'75' (octal) →", int(octal_str, 8))  # 61
print()

# Bitwise Operations

a = 0o12  # 10 in decimal (binary: 1010)
b = 0o07  # 7  in decimal (binary: 0111)

print("Bitwise Operations with Octal:")
print("a =", oct(a), "(decimal:", a, ")")
print("b =", oct(b), "(decimal:", b, ")")
print("a & b =", oct(a & b), "(decimal:", a & b, ")")  # 0o2 = 2
print("a | b =", oct(a | b), "(decimal:", a | b, ")")  # 0o17 = 15
print("a ^ b =", oct(a ^ b), "(decimal:", a ^ b, ")")  # 0o15 = 13
print()

# File Permissions (Unix-style)

# Common symbolic permissions:
# rwxr-xr-- → 0o754

file_perm = 0o754
print("Unix-style file permissions:")
print("0o754 (octal) →", bin(file_perm))  # See binary layout
print("User (read/write/execute):", (file_perm >> 6) & 0b111)
print("Group (read/execute):", (file_perm >> 3) & 0b111)
print("Other (read-only):", file_perm & 0b111)
print()
