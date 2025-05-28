
x = 10

def f(y):
    #global x
    x = 5
    global z
    z = 5
    print(f'f(y): y == {y}')
    def h(a):
        x = 1000
        def p(b):
            #nonlocal x
            #x = 1
            return b + x
        print(f'p(500) == {p(500)}')
        print(f'h() has access to z: {z}')
        return a + x
    print(f'h(50) == {h(50)}')
    #g()
    return x


def g():
    #f(0)
    print(f'g() has access to z: {z}')


print(f'gloabl x {x}')
print(f'return value of f(7) == {f(7)}')
print(f'global x {x}')
#print(f.h(9))
#print(y)
print(g())

