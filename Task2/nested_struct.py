# Create a nested dictionary for a person
rec = {
    'name': {'firstname': 'Bob', 'lastname': 'Smith'},
    'job': ['dev', 'mgr'],
    'age': 25
}

# Access nested values
print("Full name:", rec['name']['firstname'], rec['name']['lastname'])
print("First name:", rec['name']['firstname'])
print("Job list:", rec['job'])

# Add a new job to the list
rec['job'].append('janitor')
print("Updated jobs:", rec['job'])

# Print the full record
print("Full record:", rec)
