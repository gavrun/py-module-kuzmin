# filtering

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,15,20]

filtered = filter(lambda x: x % 5 == 0, numbers)

filtered = list(filtered)
print(filtered)
