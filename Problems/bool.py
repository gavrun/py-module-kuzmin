x = 10
y = 7
z = 10

if x == y: 
    print("equal")
else:
    print("not equal")

if x is y: 
    print("same")
else:
    print("not same")

if x == z: 
    print("equal")
else:
    print("not equal")

if x is z: 
    print("same")
else:
    print("not same")

a = {'a':1, 'b':2}
b = a
c = {'a':1, 'b':2}

if a is b: 
    print("same")
else:
    print("not same")

if a is c: 
    print("same")
else:
    print("not same")

if a == c: 
    print("equal")
else:
    print("not equal")

