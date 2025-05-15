# Modeling a cube throwing
"""
Connection of the module to the program is performed using the IMPORT operator
He has two forms: Import and from-Import
"""
import random           # The import of the module
n1 = random.randint(1, 6)

import random as rnd    # Import of the module as a pseudonym
n2 = rnd.randint(1, 6)

from random import randint  # Import of function
#randint = "problem"
n3 = randint(1, 6)

from random import *        # import of all functions of the module
n4 = randint(1, 6)

from random import randint as rnd   # Import functions How nickname
n5 = rnd(1, 6)

#n3 = randint

print('Dealt:', n1, n2, n3, n4, n5)
