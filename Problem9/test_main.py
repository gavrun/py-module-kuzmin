from fibo import Fibo
from itertools import islice

from main import integers, primes


def test_fibo():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    result = list(islice(Fibo(), 10))
    assert result == expected, f"Fibo failed: {result}"

def test_integers():
    expected = list(range(10))
    result = list(islice(integers(), 10))
    assert result == expected, f"Integers failed: {result}"

def test_primes():
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    result = list(islice(primes(), 10))
    assert result == expected, f"Primes failed: {result}"


if __name__ == "__main__":
    test_fibo()
    test_integers()
    test_primes()
    print()
    print("Tests passed.")

