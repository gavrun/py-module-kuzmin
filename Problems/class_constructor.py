class Coords():
    x = 0
    y = 0 
import logging

class Shape():
    coords = Coords()
    color = ""
    filled = False

    def area(self):
        pass

class Circle(Shape):
    "This object holds information for a Circle shape."
    _pi = 3.141
    radius = 0.0

    def __init__(self, r):
        logging.warning('New Circle Created')
        self.radius = r

    def __str__(self):
        return "A Circle with radius: " + str(self.radius) + " and color: " + self.color

    def circumfrence(self):
        return self.radius * Circle._pi * 2

    def area(self):
        return (self.radius ^ 2) * Circle._pi

    def __myFunc(self):
        print(f"MyFunc was Invoked - Radius - {self.radius}")

class Rect(Shape):
    length = 0.0
    width = 0.0

    def __init__(self,l,w):
        self.length = c
        self.width = w

    def area(self):
        return self.length * self.width

class Square(Rect):

    def __init__(self,s):
        super().__init__(s,s)

