x = 12 # Global variable (law enforcement of the assignment of local X)
L = [1,2,3]

# Function Announcement - Global Name
def get_int(msg): # msg - local
    while True:
        try:
           # x = int (incut (msg)) # local variable
            return x
        except ValueError as err:
                print(err)

def min_of_cubes(x, y):

    # Identifiers 'x' and 'y' are:
    # - local for min_of_cubes ()
    # - non -inkal for cube ()

    def cube(a):
        return a**3  # 'A' - local identifier of the Cube () function

    return min(cube(x), cube(y), cube(c))  # Function min () is located
                                           # in the built -in area
                                           # Visibility and visible everywhere

# Identifiers 'A', 'B' and 'C' have a global area of ​​visibility
a, b, c = 2, 3, 4
print("min_of_cubes = ", min_of_cubes(a, b))  #8

x = 8
# Calling the function
age = get_int("enter your age: ")
print(age)

#x =16

# We try to change the global variable 'c'
a, b, c = 3, 4, 5
def sum_of_2(a, b):
    с = 10
    return a + b + с

print(sum_of_2(a, b))  #17
print(a, b, c)         #345
# By default, identifiers from another area of ​​visibility are available only for reading,
# When trying to appropriate, the function creates a local identifier.

# How to change a global variable?

# Using Global Instructions

def workL(x):
    # L.Append (x) # Global object changes
    #L = x # L is classified as a local object and the global prolongs (variable) will not be excluded!
    global L
    L = 777         # Global variable
    print(L, " local value")

workL(23)
print(L, "Global meaning")

y, z = 1, 2 # Global variables in the module
def all_global():
    global xx    # Declared global for assignment
    xx = y + z   # Declare y, z is not required

all_global()
print('xx = ', xx)


# Using instructions Nonlocal
# to change variables

def tester(start):
    state = start       # Appeal to a non -varic
    def nested(label):  
        nonlocal state    # Fun variables must exist
        print(label, state) # Extracts the value of the state from the region
        state += 1          #UnboundLocalError:LocalVariable 'state'ReferencedBeforeAssignmentИли
                            # Change the value of the variable declared as nonlocal
    return nested       # visibility of the cramping function

F = tester(0)
F("start1")
F("start2")

G = tester(50)
G("book1")
G("book2")
      
