
x = 10

# Called by g()
def f():
   return x

# g() has its own variable
# named as x and calls f()
def g():
   x = 20
   return f()

print(g())
