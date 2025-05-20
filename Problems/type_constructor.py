# functions that construct objects of a particular type

int("42")         # Converts string to int → 42
float("3.14")     # Converts string to float → 3.14
str(100)          # Converts int to string → "100"
list("abc")       # Converts iterable to list → ['a', 'b', 'c']
tuple([1, 2, 3])  # Converts list to tuple → (1, 2, 3)
dict([("a", 1)])  # Constructs a dictionary
set([1, 2, 2, 3]) # Creates a set → {1, 2, 3}

a = [1, 2, 3]
b = tuple(a)
print(b)
