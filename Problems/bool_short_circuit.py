x = 10

if x == 10 or print('hello'):
    print('x is 10')

if x == 10 and print('hello'):
    print('x is 10')

# short-circuit evaluation

def check_1():
    print("condition 1")
    return False

def check_2():
    print("condition 2")
    return True

if check_1() or check_2():
    print("one or both true")

if check_1() and check_2():
    print("both true")
else:
    print("both not true")

a = 0

if a != 0 or 10 / a > 2: # ZeroDivisionError
    pass
if a != 0 and 10 / a > 2:
    pass
