def double(x):
    return x * 2

def to_upper(s):
    return s.upper()

def value_or_iterable(func):
    def enhanced_func(x):
        if hasattr(x, '__iter__') and type(x) is not str:
            return list(map(func, x))
        else:
            return func(x)
    return enhanced_func


double_enchanced = value_or_iterable(double)
to_upper_enchanced = value_or_iterable(to_upper)

print(double_enchanced(10))
# print(to_upper_enchanced([10, 20, 30, 40]))

print(to_upper_enchanced("hello"))
print(to_upper_enchanced(["hello", "world"]))

