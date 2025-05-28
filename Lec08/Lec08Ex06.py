def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    prev = 1
    pprev = 0
    for val in range(2, n + 1):
        res = prev + pprev
        pprev = prev
        prev = res
    return res

fib = {0: 1, 1: 1}
def fibonacci_memo(n):
    if n <= 1:
        return fib[n]
    else:
        for val in range(2, n + 1):
            fib[val] = fib[val - 1] + fib[val - 2]
        return fib[n]
    

print(fibonacci_memo(10))

# Example usage:
num_terms = 40
for i in range(num_terms + 1):
    print(fibonacci_memo(i))
    
    