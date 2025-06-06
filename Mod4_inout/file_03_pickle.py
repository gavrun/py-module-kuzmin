# serializatsiz objects - Pickle module
# Example 1.

D = {'a': 1, 'b': 2}
# To save the dictionary in the file, we will transfer it directly to the pickle module function

F = open('datafile.pkl', 'wb')

import pickle
pickle.dump(D, F)           # Module Pickle will write into a file any object
F.close()

# Reading the dictionary back

F = open('datafile.pkl', 'rb')
E = pickle.load(F)          # Downloads any objects from the file
print(E)

# Example 2.

filename = "datafile_pickle.txt"
# List of purchases
shoplist = {"Fruits": ["apples", "pears"],
            "Vegetables": ["carrots", "tomatoes"],
            "Budget": 2300}

# Entry into a file
with open(filename, "wb") as fh:
    pickle.dump(shoplist, fh)  # Place the object in the file

# Read from the storage
shoplist_2 = []
with open(filename, "rb") as fh:
    shoplist_2 = pickle.load(fh)  # upload an object from a file
print(shoplist_2)
