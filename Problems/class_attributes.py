from Circle import Circle
from Circle import Coords

c1 = Circle()
c2 = Circle()

print(c1.coords.x)

c1.positions.append(Coords())
c1.positions[0].x = 10

print(c1.positions[0].x)

