# with no mapping 

weights_in_lbs = [10, 20, 30, 40, 50]
weights_in_kg = []

for w in weights_in_lbs:
    new_weight = 0.453592 * w
    weights_in_kg.append(new_weight)

print(weights_in_kg)


# apply functions to every element in a list

weights_in_lbs2 = [10, 20, 30, 40, 50]
weights_in_kg2 = []

def lbs_to_kg(lbs):
    return 0.453592 * lbs

weights_in_kg2 = list(map(lbs_to_kg, weights_in_lbs2))

print(weights_in_kg2)

