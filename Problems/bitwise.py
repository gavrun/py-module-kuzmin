# bit operations

# i: 00000000000000000000000000001111
# j: 00000000000000000000000000010110

i = 15
j = 22

# 
log = i and j

# each pair of corresponding bits separately
bit = i & j

# 00000000000000000000000000000110

#
logneg = not i

#
bitneg = ~i


###

x = x & y	
x = x &= y
x = x | y	
x = x |= y
x = x ^ y	
x = x ^= y


# bit mask (to detect the state of a bit)

flag_register
the_mask = 8

# reset bit
flag_register = flag_register & ~the_mask
flag_register &= ~the_mask

# set bit
x | 1 = 1
x | 0 = x
flag_register = flag_register | the_mask
flag_register |= the_mask

# negate bit
x ^ 1 = ~x
x ^ 0 = x
flag_register = flag_register ^ the_mask
flag_register ^= the_mask

if flag_register & the_mask:
    # Bit is set.
else:
    # Bit is reset.

# bit shift 

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

#

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

#

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

