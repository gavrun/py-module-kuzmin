# View available methods for tuple
print("Tuple methods:", dir(tuple))

# Get help on tuple methods
help(tuple.count)
help(tuple.index)

# Create a tuple of numbers
seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)

# Use count and index
print("Count of 8:", seq.count(8))       # how many times 8 appears
print("Index of 44:", seq.index(44))     # index of first occurrence of 44

# Convert tuple to list
listseq = list(seq)

# Check the type after conversion
print("Converted to list:", listseq)
print("Type:", type(listseq))            # should be <class 'list'>

# Use list methods on the converted tuple
listseq.append(100)
listseq.sort()
print("Modified list:", listseq)
