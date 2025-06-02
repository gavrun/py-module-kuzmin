# Create an empty list 
beatles = []
print("Step 1:", beatles)

# Add initial members
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Use a loop to add Stu Sutcliffe and Pete Best
for member in ["Stu Sutcliffe", "Pete Best"]:
    new_member = input(f"Add {member}: ")  # prompt user 
    beatles.append(new_member)
print("Step 3:", beatles)

# Remove Stu Sutcliffe and Pete Best
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# Insert Ringo Starr at the beginning
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Print final length
print("The Fab", len(beatles))
