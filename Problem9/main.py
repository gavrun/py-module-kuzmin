from fibo import Fibo
from itertools import islice


def integers():
    """Generator of all non-negative integers: 0, 1, 2, 3, ..."""
    i = 0
    while True:
        yield i
        i += 1


def primes():
    """Prime Number Generator: 2, 3, 5, 7, ..."""
    yield 2
    primes_released = [2]
    candidate = 3
    while True:
        is_prime = True
        for p in primes_released:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes_released.append(candidate)
            yield candidate
        candidate += 2


print("First 10 Fibonacci numbers:")
fibo_iter = Fibo()
print(list(islice(fibo_iter, 10)))

print("\nFirst 10 non-negative numbers:")
print(list(islice(integers(), 10)))

print("\nFirst 10 prime numbers:")
print(list(islice(primes(), 10)))

