# recursion depth

def repeat(func, number):
    func()
    repeat(func, number - 1)

def hello():
    print('Hello')

# repeat(hello, 10) # maximum recursion depth exceeded

# recursion

def repeat2(func, number):
    if number > 0:
        func()
        repeat2(func, number - 1)

def hello2():
    print('Hello')

repeat2(hello2, 10)

# recursion extra

def repeat3(func, number, n):
    if n < number:
        func(n)
        repeat3(func, number, n + 1)

def hello3(n):
    print(f'Hello {n}')

repeat3(hello3, 10, 0)


# recursion over a list

numbers = [1, 2, 3, 4, 5, 6]

def for_in(lst, func, i):
    if i < len(lst):
        func(lst[i])
        for_in(lst, func, i + 1)

def for_in_b(lst, func, i):
    if i >= 0:
        func(lst[i])
        for_in_b(lst, func, i - 1)

def prt_txt(x):
    print(f'test {x}')

for_in(numbers, prt_txt, 0)
for_in_b(numbers, prt_txt, 0)


