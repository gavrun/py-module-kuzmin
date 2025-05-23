def repeat_string(s, num=1):
    if type(s) is not str:
        raise TypeError('Use a string as the first argument')
    if type(num) is not int:
        raise TypeError('Use an int as the second argument')
    return s * num

print(repeat_string('Hey-', 3), '!')
