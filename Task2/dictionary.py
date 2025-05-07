# Create a dictionary with 3 key-value pairs
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}

# Access values by keys
print("Food:", D['food'])
print("Quantity before update:", D['quantity'])

# Modify value by key
D['quantity'] += 10
print("Quantity after update:", D['quantity'])

# Create an empty dictionary
dp = {}

# Fill dictionary with user input
dp['name'] = input("Enter your name: ")
dp['age'] = int(input("Enter your age: "))

print("Filled dictionary:", dp)

