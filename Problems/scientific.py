# Scientific notation

# use `base` and `e` or `E` to represent "× 10^" exponent

small_number = 1.23e-5   # 1.23 × 10⁻⁵ = 0.0000123
large_number = 6.78e+6   # 6.78 × 10⁶ = 6,780,000

print("Scientific Notation Literals:")
print("1.23e-5 =", small_number)
print("6.78e+6 =", large_number)
print()

# Convert Scientific Format

value = 123456789.0
small = 0.00000042

print("Formatted Scientific Notation (with format specifiers):")
print("value =", format(value, ".2e"))     # 1.23e+08
print("small =", format(small, ".2e"))     # 4.20e-07
print()

# Convert Scientific to Decimal

sci_1 = 5.2e3    # 5200.0
sci_2 = 3.0e-4   # 0.0003

print("Scientific → Decimal:")
print("5.2e3 =", sci_1)
print("3.0e-4 =", sci_2)
print()

# Real-world scientific examples

number = 93000000

print("Basic Scientific Notation Formatting:")
print("Default scientific format:", format(number, "e"))   # 9.300000e+07
print("2 decimal places:", format(number, ".2e"))          # 9.30e+07
print("3 decimals, width 12:", format(number, "12.3e"))    # '   9.300e+07'
print("Capital E format:", format(number, ".2E"))          # 9.30E+07
print()

speed_of_light = 2.998e8      # meters per second (m/s)
plancks_constant = 6.626e-34  # J·s
earth_mass = 5.972e24         # kilograms

# A tiny mass like 2 grams releases a huge amount of energy (~1.8e+12 J)
mass_kg = 0.002  # 2 grams = 0.002 kg

energy = mass_kg * speed_of_light**2

print("Scientific Constants:")
print("Speed of Light:", speed_of_light, "m/s")
print("Planck's Constant:", plancks_constant, "J·s")
print("Mass of Earth:", earth_mass, "kg")
print()

print("Einstein's E = mc²:")
print("Mass =", mass_kg, "kg")
print("Speed of light =", format(speed_of_light, ".2e"), "m/s")
print("Energy released =", format(energy, ".3e"), "joules")  # Very large value
print()

