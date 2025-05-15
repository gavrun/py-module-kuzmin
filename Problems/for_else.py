for j in range(5):
    print(j)
else:
    print("else:", j)
print()

# if the control variable doesn't exist before the loop starts, it won't exist when the execution reaches the else branch

#i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i) # here
print()
