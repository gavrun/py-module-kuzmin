# Physical (analytical) approach - Fermat's principle

import math

# Data input
dist1_yd = float(input("Enter the shortest distance between the lifeguard and the water's edge (yards): "))
print(dist1_yd)

dist2_ft = float(input("Enter the shortest distance from a drowning person to the shore (feet): "))
print(dist2_ft)

hight_yd = float(input("Enter the lateral offset between the lifeguard and a drowning person (yards): "))
print(hight_yd)

vel_sand_mph = float(input("Enter the speed of the lifeguard on the sand (mph): "))
print(vel_sand_mph)

dec_n = float(input("Enter the deceleration coefficient of the lifeguard when moving in water (const): "))
print(dec_n)

theta1_deg = float(input("Enter the direction angle of the lifeguard's movement on the sand (degrees): "))
print(theta1_deg)

# Unit conversion
dist1 = dist1_yd * 3  # yards > feet
hight = hight_yd * 3  
vel_sand = vel_sand_mph * 5280 / 3600  # miles per hour > feet per second
theta1_rad = math.radians(theta1_deg)

# Calculations
x_path = dist1 * math.tan(theta1_rad)
L1 = math.sqrt(x_path ** 2 + dist1 ** 2 )
L2 = math.sqrt((hight - x_path) ** 2 + dist2_ft ** 2)
time = (L1 + dec_n * L2) / vel_sand

# Output of the result
print(f"\nIf the lifeguard starts moving at an angle {int(round(theta1_deg))} degrees,"
      f" he will reach a drowning person in {round(time, 1)} seconds")
