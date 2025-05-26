# classes

class Coords():
    x = 0
    y = 0 

class Circle():
    pi = 3.141
    radius = 0.0
    coords = Coords()
    color = ""
    filled = False
    positions = []

    def circumfrence(self):
        return self.radius * Circle.pi * 2

    def myFunc(self):
        print(f"MyFunc was Invoked - Radius - {self.radius}")


# class Circle():
#     radius = 0
#     x = 0
#     y = 0
#     color = ""
#     filled = False

# circles = []

# for x in range(0,10):
#     c = Circle()
#     c.radius = int(input("Enter the circle radius: "))
#     circles.append(c)

# print(circles[6].radius)

