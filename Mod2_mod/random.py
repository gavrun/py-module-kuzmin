# Simulating a dice roll
"""
A module is connected to a program using the import statement
It has two forms: import and from-import
"""
import random # module import
n1 = random.randint(1, 6)

import random as rnd # module import as an alias
n2 = rnd.randint(1, 6)

from random import randint # function import
#randint = "problem"
n3 = randint(1, 6)

from random import * # all module functions import
n4 = randint(1, 6)

from random import randint as rnd # function import as an alias
n5 = rnd(1, 6)

#n3 = randint

print('Rolled:', n1, n2, n3, n4, n5)