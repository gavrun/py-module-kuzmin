# https://www.wolframalpha.com/input/?i=collatz+conjecture
# https://mathworld.wolfram.com/CollatzProblem.html

def collatz_steps(n):
    steps = 0
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    print(n)  # Print the last value, which expected to be 1
    print(f"steps = {steps}")

# Input
n = int(input("Enter a number: "))
collatz_steps(n)
