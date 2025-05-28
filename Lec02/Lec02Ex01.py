from string import Template

import math

alpha = 9
b = 3

c = alpha + b # This is a comment
# Line 2 of the comment

print(c)

# c.my()
a:int = 9_000_000_000
b:int = 31
f1:float = '"Hell\'o'
f2 = 3.14
print(type(f1), id(f1))
print(type(a), id(a))
str1 = "\"Hello'all"
str2 = 'a'
str3 = '' # ""
print(f1, str1)
print(type(str2), str2)
print(type(str3), str3)
print(a, b, str1, sep='_______', end='\n\n')

print(a + (a > b))
print('The value of a is: ' + str(a))
print('The value of a is: {:*^20}'.format(str(a)))
print('The value of a is: %d' % a)
print('The value of a is: {:016,}, and the value of f2 is {:.6f}'.format(a, f2))
print(f'The value of a is: {a:016,}, and the value of f2 is {f2:.6f}')
print(f'The value of b in hex is {b:#X}, in octal {b:o}, in binary {b:09_b}, in decimal {b}')
print(f'Humidity is {0.7:.0%}')
print(f'g is {9.8:.2e}')

message = 'World'
temp = Template('Hello $wld')
print(temp.substitute(wld=message))

# postcondition: prints max of a and b 
if a > b:
		print(a)
		res = a
		if a > 0:
				print("Positive!")
else:
		print(b)
		res = b

res = a if a > b else b
print(res)

# val = input('Enter a number => ')
# print(type(val), id(val), val)
# print(float(val) + 2)

x = 0
cont = True
while x < 100 and cont:
    x += 4 # x = x + 1
    if x == 8:
        continue
    print(x)
    if x > 70:
        break

s1 = 'Hello'
#s1[0] = 'Y'
print(s1[0])
# s2 = 'Hell' + input()
s3 = 'o'
s2 = str('Hell' + s3)
print(f's1: {type(s1)} {id(s1)} {s1}')
print(f's2: {type(s2)} {id(s2)} {s2}')
print(f's1 == s2 {s1 == s2} s1 is s2 {s1 is s2}')
s2 = 'World'
print(f's1 == s2 {s1 == s2} s1 is s2 {s1 is s2}')

lst = [2, 5, 'Hello', 3.5, 5]
print(type(lst))
print(lst)
print(lst[0])
lst[0] = True
print(lst)
lst.append(9)
print(lst)

for elem in lst:
    elem = 0
    print(elem)

print(lst)

for idx in range(10, 0, 2):
    print(idx)

for idx in range(len(lst)):
    print(lst[idx], end=' ')
print()
print(math.sin(math.pi / 2))
