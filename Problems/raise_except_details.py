def repeat_string(s, num=1):
    if type(s) is not str:
        raise TypeError('Use a string as the first argument')
    if type(num) is not int:
        raise TypeError('Use an int as the second argument')
    return s * num

# print(repeat_string('Hey-', 3), '!')

try:
    print(repeat_string('Hey-', 3), '!')
except Exception as e:
    if 'first argument' in str(e):
        print(str(e))
    elif 'second argument' in str(e):
        print(str(e))
        print(type(e))
        print(e.args)
