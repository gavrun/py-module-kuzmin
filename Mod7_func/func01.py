# Application of standard functions
x1 = pow(2,5)
print("x1 =", x1)

mylist = [11,22,33,44,55,66]
mylist.append(77) # Function that performs direct changes in objects
                  # should be called without assigning the returned value
print(mylist)
mylistnew = mylist.append(88) # Returns None
print(mylistnew)              #None
print(mylist)


#Function in Python - an object that takes arguments and returns the value

# Def simply performs assignment during execution
# DEF instructions are not interpreted until they are reached
# and performed by the flow of execution, i.e.Program code inside the DEF instructions
# is not performed until the function is called later

def add(x, y):
    #a +=2
    return x + y

a, b = 1, 2
s = add(a,b)
print("The amount {0} and {1} is equal to {2} ".format(a,b,s))

ob = add        # Binding an object of function with another object
print(ob(3,5))  # Calling the function using a new name


# The function can be of any complexity and return any objects:
# lists, motorcades and functions

def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc

newf = newfunc(100) # Newf is a function
print(newf(200))


def add(x, y):
    print("Sump {0} and {1} is equal to {2}".format(x,y,x+y))

a, b = 11, 22
add(a,b)

s = add(a,b)
print("The sum of n {0} and {1} is equal to {2} ".format(a,b,s))

# Def can appear wherever instructions may appear,
# Even inside other instructions

x = 3
y = -3

if x > 0:
    if y > 0:               # x> 0, y> 0
       def func():
           print("First quarter")
    else:                   # x> 0, y <0
        def func():
            print("The fourth quarter")
else:
    if y > 0:               # x <0, y> 0
        def func():
            print("The second quarter")
    else:                   # x <0, y <0
        def func():
            print("The third quarter")

#func()
