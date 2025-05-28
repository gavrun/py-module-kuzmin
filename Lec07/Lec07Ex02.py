#print('Hello World'); a = 10; b = 10

a = 10

code = """
3 + a * 7
"""
print(eval(code))

program = """
a = 10
b = 3 + a * 7
for val in range(50, b):
    print(val)
"""
exec(program)
