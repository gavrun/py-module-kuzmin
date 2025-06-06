from functools import reduce
import sys
  
def factorial(n):
    """
    Operator (imperative) definition of a factorial
    """
    if n == 1: return 1
    else: return n * factorial( n - 1 )
 
""" Functional definition """
factorial2 = lambda x: ( ( x == 1 ) and 1 ) or x * factorial2( x - 1 )
factorial3 = lambda z: reduce( lambda x, y: x * y, range( 1, z + 1 ) )

n = int(input("number?: "))
 
print("n={} => n!={}".format(n, factorial(n)))
print("n={} => n!={}".format(n, factorial2(n)))
print("n={} => n!={}".format(n, factorial3(n)))
