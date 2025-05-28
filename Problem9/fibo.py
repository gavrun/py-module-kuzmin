
class Fibo:
    """Iterator enumerates Fibonacci numbers: 0, 1, 1, 2, 3, ..."""
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current
