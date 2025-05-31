class Coords:
    def __init__(self):
        self.x = 0
        self.y = 0

class Circle:
    def __init__(self):
        self.pi = 3.141
        self.radius = 0.0
        self.coords = Coords()
        self.color = ""
        self.filled = False
        self.positions = []

    def circumfrence(self):
        return self.radius * self.pi * 2

    def myFunc(self):
        print(f"MyFunc was Invoked - Radius - {self.radius}")

