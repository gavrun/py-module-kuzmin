
"""
Closing is a "procedure, along with a set of data tied to it",
In contrast to objects in object programming, as: "Data together
With a set of procedures attached to them "

The meaning of the closure is that the definition of the function "freezes"
the context surrounding it at the time of determination
"""
# 1) Parameterization of the creation of a function
def multiplier( n ):    
    """
    multiplier returns the multiplication function to n
    """
    def mul( k ):
        return n * k
    return mul
 
mul3 = multiplier(3)    # mul3 - a function multiplying by 3
mul5 = multiplier(5)    # mul5 - a function multiplying by 5

print(mul3(5), mul5(5))  # 15 25

''' Analogue with use lambda'''
multiplier = lambda n: lambda k: n * k
mul4 = multiplier(4)
print(mul4(7))          # 28

# 2) Using the default parameter value at the function determination point

n = 3
def mult( k, mul = n ):     # value 3 "frozen" in the function 
    return mul * k

# Assignment of values ​​to the parameter by default will not lead to a change
# Previously a certain function:
n = 7
print(mult(3))      # 9 
n = 13
print(mult(5))      # 15

# but the function itself can be redefined
n = 10
mult = lambda k, mul=n: mul * k     
print(mult(3))      # 30
