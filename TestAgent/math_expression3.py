def continued_fraction(x, depth, print_steps=False):
    """Calculate the continued fraction recursively."""
    if depth == 0:
        return x
    result = x + 1 / continued_fraction(x, depth - 1, print_steps)
    if print_steps:
        print(f"Depth {depth}: {result}")
    return result

x = float(input("Enter value for x: "))

depth = 4  # Number of levels in the continued fraction
result = 1 / continued_fraction(x, depth, print_steps=True)
print("result =", result)
