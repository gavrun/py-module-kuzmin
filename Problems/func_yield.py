# generator  

def gen_func():
    i = 1
    print("first")
    yield i

    print("second")
    i += 1
    yield i

    print("third")
    i += 1
    yield i

for value in gen_func():
    print(value)

