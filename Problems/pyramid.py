blocks = int(input("Enter the number of blocks: "))

height = 0
new_layer = height + 1

while blocks >= new_layer:
    height += 1
    blocks -= height
else:
    print("The height of the pyramid:", height)
