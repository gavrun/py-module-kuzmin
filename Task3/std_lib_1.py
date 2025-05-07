# Step 1: Import modules
import math
import statistics
import random

# Step 2: Create a list of 10 integers
numbers = [12, 45, 23, 67, 34, 89, 10, 56, 78, 31]

# Step 3: Perform statistical calculations
total = sum(numbers)                              # Sum of all numbers
average = statistics.mean(numbers)                # Mean (average)
median_value = statistics.median(numbers)         # Median value
std_dev = statistics.stdev(numbers)               # Standard deviation

# Display the results
print("List of numbers:", numbers)
print("Sum:", total)
print("Mean:", average)
print("Median:", median_value)
print("Standard Deviation:", std_dev)

# Step 4: Generate a random number from 1 to 100
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)
