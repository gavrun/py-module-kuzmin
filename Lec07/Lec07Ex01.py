import time
import math
from decimal import Decimal, getcontext


def sqrt(arg):
    '''
    @requires: arg is a number
    #@returns: result > 0
    @returns: result, s.t., result * result == arg

    Parameters
    ----------
    arg : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    return 1

def f(x, y):
    '''
    @requires: P = { x is an integer ∧ y is integer ∧ x is even ∧ x >=0 }
    ##@returns: Q = { x > 42 ∧ y is even }
    ##@returns: Q = { x > -42 ∧ y is even } = Q1
    #@returns: Q = { x = 5 ∧ y is even } = Q2
    @returns: Q = { x = 5 ∧ y >= 6 ∧ y is even } = Q3
    #@returns: Q = { x = 5 ∧ y = 2 * x } = Q4
    # Q2 => Q1
    @returns: Q = { x = 5 ∧ y >= 6 ∧ y % 4 = 2 } = Q4
    
    Counterexample:
        x = 10; P: True
        Q: False
        

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    '''
    # { x_0 is an integer ∧ y_0 is integer ∧ x_0 is even ∧ x_0 >=0 }
    x = x + 3
    # { x_1 is an integer ∧ y_0 is integer ∧ x_1 = x_0 + 3 ∧ x_1 >=3 }
    y = 2 * x
    #{ x_1 is an integer ∧ y_1 is integer ∧ y_1 = 2 * x_1 ∧ x_1 = x_0 + 3 ∧ x_1 >=3 } 
    #  y_1 = 2 * x_1 ∧ x_1 >=3     y_1 / 2 >=3  y_1 >= 6
    x = 5
    #{ x is an integer ∧ y is integer ∧ x = 5 ∧ y >= 6}
    return x, y


def f(x, y):
    # { 2 * (x + 3) > 5} = { 2x +6 > 5} = {2x > -1} = {x > -1/2}
    x = x + 3
    # { 2 * x > 5 } = { x > 2.5}
    y = 2 * x
    # { y > 5 }
    x = 5
    # { y > x }
    return x, y


def f2(x):
    # { (x != 0 ∧ x > 0) ∨ (x = 0 ∧ 0 > -1)} = {x > 0 ∨ x = 0} = {x >= 0}
    z = 0
    #{ (x != 0 ∧ x > 0) ∨ (x = 0 ∧ z > -1)}
    if x != 0:
        # {x > 0}
        z = x
        # {z > 0}
    else:
        # {z + 1 > 0} = {z > -1}
        z += 1
        # {z > 0}
    # {z > 0}
    return z

def f3(n):
    """
    @requires: n >= 0
    @returns: r = n!

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    i = 0
    #{n >= 0 ∧ i = 0}
    r = 1
    #{n >= 0 ∧ i = 0 ∧ r = 1}
    while i < n:
        # Loop invariant: r = i! ∧ i <= n
        # Base case:  r = 1 ∧ 0 <= n
        # Induction step:
        #   r_k = i_k! ∧ i_k <= n is true at iteration k
        #   To prove: r_(k+1) = i_(k+1)! ∧ i_(k+1) <= n
        #   i_(k+1) = i_k + 1
        #   r_(k+1) = r_k * i_(k+1)
        #   r_k = i_k!
        
        #   r_(k+1) = r_k * i_(k+1)
        #   r_(k+1) = (i_(k+1)-1)! * i_(k+1) = i(k+1)!  
        #
        #  i >= n ∧ r = i! ∧ i <= n    i = n ∧ r = i!   r = n!
        #
        #  D: n - i
        #    1) D >= 0 n >= 0 i = 0      n - 1 >= 0
        #    2) D_k = n_k - i_k     D_(k+1) = n_(k+1) - i_(k+1)
        #       D_(k+1) - D_k = n - i_(k+1) - n +i_k
        #                     = -1
        #    3) n - i = 0  => i == n
        i += 1
        r = r * i
    return r


a = 4
b = -7
# res = f(a, b)
# print(type(res))
# print(res[0], res[1])

c, d = f(a, b)
print(c, d)

a = 0
b = 0
if not f(a, b) == (5, 6):
    raise ValueError()
else:
    print('Test passed')

'''
f(0, 0)
f(0, 1)
f(0, 2)
f(0, 3)
f(0, 4)
...
f(1, 0)
f(1, 1)
f(1, 2)
...
f(0, -1)
f(0, -2)
f(0, -3)
...
   11
123456
    78
------
    34

+ for integers
      12
  +    3
  -------
1 CPU clock cycle

    22231212
  + 97662143
  -------
1 CPU clock cycle
'''

# start = time.time()
# for _ in range(10_000_000):
#     a = 945345345345345345345345435345345435253534534525353452345345345435234535345342535345324565873284623897461298376487926487213648721676842354765627354675476815476523176423
#     b = 723487623198764512369754657601764897723389471897461283764897264897263874126487364873269871264987632784624986287462879642786427893648723647826478126349872648716298476237
#     c = a + b
# end = time.time()
# print(f'Elapsed time: {end - start} s')

# C# float: -1.5e45 to +?? precision: 7 - 8 decimal digits

a = -2147483648.0
print(f'-2147483648.0 - 0.0000000000000000000005 = {-2147483648.0 - 0.0000000000000000000005}')
a = 1237651236254786534826735476325482376542376457862547862537468523764523876452376845328745238746523764.44
b = 1237651236254786500000000000000000000000000000000000000000000000000000000000000000000000000000000000.00
print(f'a = {a}, b = {b}, a - b = {a - b}')
a *= a
a *= -a
print(a)
n1 = a - a
print(n1)
n2 = a / 1.e400
print(n2)
print(n1 == n2)
print(n1 is math.nan)
print(math.isnan(n1))
print(math.isnan(n2))
print(math.isnan(a))

account = 0.0
amount = 0.1
# while round(account) != 10000000.0:
#     account += amount
#     #print(account)
# while account <= 100.0:
#     account += amount
#     #print(account)
account = 0
amount = 10
while account != 10000:
    account += amount
    #print(account)
print(account / 100)


EPSILON = 0.0001
initial_balance = 1000
amount = 0.1
balance = initial_balance
while not(1001 - EPSILON < balance < 1001 + EPSILON):
    balance += amount
    #print(balance)
print(balance)

getcontext().prec = 600
initial_balance = Decimal(0)
#amount = Decimal(0.1) # Still results in an infinite loop because a Decimal object is
# created from a 0.1 floating point which does not represent 0.1 exactly
amount = Decimal(1) / Decimal(10)
balance = initial_balance
while balance != Decimal(1001):
    balance += amount
    print(balance)
print(balance)

a = Decimal("3.141592653589793238462643383279502884197123123123123123123123123213123123547656757865768678")
print(a)
print(getcontext().prec)
getcontext().prec = 10
b = Decimal("3.141592653589793238462643383279502884197123123123123123123123123213123123547656757865768678")
print(b)
