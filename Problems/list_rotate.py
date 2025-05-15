def rotate_left(l):
    l.append(l.pop(0))
    return l

def rotate_right(l):
    last_element = l[-1]
    l.insert(0, last_element)
    return l

def rotate(l, number_of_rotations, direction='left'):
    if direction == 'left':
        for _ in range(number_of_rotations):
            rotate_left(l)
    elif direction == 'right':
        for _ in range(number_of_rotations):
            rotate_right(l)
    return l

numbers = [1, 2, 3, 4]
print(rotate(numbers, 1))
print(rotate(numbers, 2, 'right'))
