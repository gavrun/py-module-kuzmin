# Original list
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print("Original list:", list1)

# Sort list in descending order (modifies the list)
list1.sort(reverse=True)
print("Sorted descending:", list1)

# Use sorted() to keep the original list unchanged
list2 = [3, 5, 6, 2, 33, 6, 11]
sorted_list = sorted(list2)

print("Original list2:", list2)       # remains unchanged
print("Sorted version:", sorted_list) # new sorted list

