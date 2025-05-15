import math

""" Creating a structure
there is no special keyword struct (like in C++, C#) in this language!
"""
# Using a class to simulate a structure

class Point:
    x = 0
    y = 0

# creating two points as class object variables
point_A = Point()
point_B = Point()

point_A.x = 1
point_A.y = 5

point_B.x = 4
point_B.y = 7

# calculating the distance between the points
d1 = math.sqrt((point_A.x-point_B.x)**2 + (point_A.y-point_B.y)**2)

print(d1)

# Using a dictionary to simulate a structure
# creating two points as dictionary objects
pD1 = {'x':1, 'y':5}
pD2 = {'x':4, 'y':7}

# calculate distance between points
d2 = math.sqrt((pD1['x']-pD2['x'])**2 + (pD1['y']-pD2['y'])**2)

print(d2)
