# no memoization 

def factorial_recurse(x):
    print(f'Calculating {x}!')
    if x <= 1:
        return 1
    return x * factorial_recurse(x - 1)

# print(f'100! is {factorial_recurse(10)}')

for n in range(50):
    print(f'{n + 1}! is {factorial_recurse(n + 1)}')

# with memoization

memo_previous_results = []

def factorial_memo(x):
    try:
        memo_current_result = next(call['result'] for call in memo_previous_results if call['x'] == x)
        print(f'Reusing {x}!')
        return memo_current_result
    except StopIteration:
        print(f'Calculating {x}!')
        if x <= 1:
            return 1
        memo_new_result = x * factorial_memo(x - 1)
        memo_previous_results.append({'x': x, 'result': memo_new_result})
        return memo_new_result

# print(f'10! is {factorial_memo(10)}')

for n in range(50):
    print(f'{n + 1}! is {factorial_memo(n + 1)}')


# no memoization 

def fibonacci_recurse(x):
    if x <= 1:
        return 1
    
    return fibonacci_recurse(x - 1) + fibonacci_recurse(x - 2)

print()
print(f'fib of 5 is {fibonacci_recurse(5)}')


# with memoization list

fib_previous_results = []

def fibonacci_memo(x):
    try:
        fib_exist_result = next(call['result'] for call in fib_previous_results if call['x'] == x)
        return fib_exist_result
    except:
        if x <= 1:
            fib_new_result = 1
        else:
            fib_new_result =  fibonacci_memo(x - 1) + fibonacci_memo(x - 2)
        return fib_new_result

print()
print(f'fib(list) of 5 is {fibonacci_memo(5)}')


# with memoization dictionary

fib_previous_results = {}

def fibonacci_memo2(x):
    try:
        fib_exist_result = fib_previous_results[x]
        return fib_exist_result
    except KeyError:
        if x <= 1:
            fib_new_result = 1
        else:
            fib_new_result =  fibonacci_memo2(x - 1) + fibonacci_memo2(x - 2)
        return fib_new_result

print()
print(f'fib(dict) of 5 is {fibonacci_memo2(5)}')



