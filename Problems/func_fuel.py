def liters_100km_to_miles_gallon(liters):
    miles_per_100km = 100 * 1000 / 1609.344  # 100 km in Miles
    gallons = liters / 3.785411784           # Litter in Gallons
    return miles_per_100km / gallons

def miles_gallon_to_liters_100km(miles):
    km_per_gallon = miles * 1609.344 / 1000  # Miles in Kilometers
    liters = 3.785411784                     # Gallon in Liters
    return (100 * liters) / km_per_gallon

# Test

print(liters_100km_to_miles_gallon(3.9))   # -> 60.31
print(liters_100km_to_miles_gallon(7.5))   # -> 31.36
print(liters_100km_to_miles_gallon(10.))   # -> 23.52

print(miles_gallon_to_liters_100km(60.3))  # -> 3.90
print(miles_gallon_to_liters_100km(31.4))  # -> 7.49
print(miles_gallon_to_liters_100km(23.5))  # -> 10.00
