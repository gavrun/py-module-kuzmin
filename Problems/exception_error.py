# code

value = int(input('Enter a natural number: '))
print('The reciprocal of', value, 'is', 1/value)

# exception 

# Traceback (most recent call last):
#   File "code.py", line 1, in 
#     value = int(input('Enter a natural number: '))
# ValueError: invalid literal for int() with base 10: ''

# type

type(value) is int --> True

# one try one except

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')

# one try many except(s)

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 

# default exception

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')

