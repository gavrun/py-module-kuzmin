#

var = 10

def print_var():
    print(var)  # ← access to the external variable

print_var()  # 10

#

var = 10

def set_var():
    var = 5       # ← Local variable VAR is created
    print(var)

set_var()       # 5
print(var)      # 10 (external variable remained unchanged)

#

var = 10

def broken():
    print(var)  # Error: the variable is used before the definition
    var = 5

broken()

#

var = 10

def modify():
    global var
    var = 5       # ← Now we change the global variable

modify()
print(var)       # 5

#

def outer():
    count = 0

    def inner():
        count = 1  # This is a new local variable
        print("Inner:", count)

    inner()
    print("Outer:", count)

outer()

#

def outer():
    count = 0

    def inner():
        nonlocal count
        count = 1  # Changes the variable from Outer
        print("Inner:", count)

    inner()
    print("Outer:", count)

outer()

#

count = 0

def outer():
    def inner():
        nonlocal count  # Error: Count not in Enclosing Scope, but in Global
        count = 1
    inner()

outer()

#

def make_counter():
    count = 0  # external function

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

c1 = make_counter()
print(c1())  # 1
print(c1())  # 2
print(c1())  # 3

c2 = make_counter()
print(c2())  # 1 (new counter)
print(c1())  # 4 (Old continues to work)


#

def broken_counter():
    count = 0

    def counter():
        count += 1  # Error!Trying to change the external variable
        return count

    return counter

c = broken_counter()
# c() → UnboundLocalError



