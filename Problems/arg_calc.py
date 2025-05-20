def calculate(ops, *num):
    if ops == 'add':
        total = 0 
        for x in num:
            total += x
        return total
    elif ops == 'subtract':
        total = num[0]
        for x in num[1:]:
            total -= x
        return total
    elif ops == 'multiply':
        total = 1
        for x in num:
            total *= x
        return total
    
print(calculate('add', 1, 2, 3))
print(calculate('subtract', 1, 2, 3))
print(calculate('multiply', 1, 2, 3))
