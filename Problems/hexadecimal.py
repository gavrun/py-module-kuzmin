# Hexadecimal literals 
num1 = 0xA     # 10 in decimal
num2 = 0x1F    # 31 in decimal

print("Hexadecimal literals:")
print("a =", hex(num1), "(decimal:", num1, ")")
print("b =", hex(num2), "(decimal:", num2, ")")
print()

# Conversion between hexadecimal and decimal

decimal_value = 255
hex_string = "2A"

print("Decimal to Hexadecimal:")
print("255 →", hex(decimal_value))  # 0xff

print("Hexadecimal string to Decimal:")
print("'2A' →", int(hex_string, 16))  # 42
print()

# Bitwise Operations 

a = 0x3C  # 60 in decimal → 00111100
b = 0x0F  # 15 in decimal → 00001111

print("Bitwise Operations with Hex:")
print("a =", hex(a), "(decimal:", a, ")")
print("b =", hex(b), "(decimal:", b, ")")
print("a & b =", hex(a & b), "(decimal:", a & b, ")")  # 0x0C = 12
print("a | b =", hex(a | b), "(decimal:", a | b, ")")  # 0x3F = 63
print("a ^ b =", hex(a ^ b), "(decimal:", a ^ b, ")")  # 0x33 = 51
print("~a =", hex(~a), "(decimal:", ~a, ")")           # -0x3D = -61
print()

# Bit Shifting with Hex

h = 0x10  # 16 in decimal

print("Bit Shifting with Hex:")
print("h =", hex(h), "(decimal:", h, ")")
print("h << 1 =", hex(h << 1), "(decimal:", h << 1, ")")  # 0x20 = 32
print("h >> 2 =", hex(h >> 2), "(decimal:", h >> 2, ")")  # 0x4 = 4
print()

# Color Codes (HTML/CSS)

print("Hexadecimal Use Case: RGB Colors")
red = 0xFF0000
green = 0x00FF00
blue = 0x0000FF
white = 0xFFFFFF
black = 0x000000

print("Red:", hex(red))
print("Green:", hex(green))
print("Blue:", hex(blue))
print("White:", hex(white))
print("Black:", hex(black))
print()

# A 24-bit RGB color in hex (white)
color = 0x4A7FBC  # Red: 0x4A, Green: 0x7F, Blue: 0xBC

# Extract each channel using bit shifting and masking
red   = (color >> 16) & 0xFF  # Move red bits to lowest byte, mask with 0xFF
green = (color >> 8)  & 0xFF  # Move green bits to lowest byte, mask
blue  = color        & 0xFF   # Mask lower byte directly

print("Hex color:", hex(color))
print("Red:", red, "(hex:", hex(red) + ")")
print("Green:", green, "(hex:", hex(green) + ")")
print("Blue:", blue, "(hex:", hex(blue) + ")")
