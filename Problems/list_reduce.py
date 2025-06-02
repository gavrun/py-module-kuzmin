from functools import reduce

# by a loop

my_list = [8, 10, 54, -11, 7]
total = 0

for x in my_list:
    total += x

print(total)

# with reduce function

def get_sum(acc, x):
    print(f'Accumulator value: {acc}, X: {x}')
    return acc + x

total2 = reduce(get_sum, my_list)

print(total2)

# more examples

my_numbers = [8, 10, 54, -11, 7]

my_strings = ['Hello', 'my', 'name', 'is', 'Shaun']

numbers_and_strings = ['a', 1, 'b', 2, 'c', 3]

people = [
    { "id": "123", "name": "John Doe", "age": 55 },
    { "id": "312", "name": "Sue Lee", "age": 34 },
    { "id": "221", "name": "Dan King", "age": 45 },
    { "id": "112", "name": "Betty Smith", "age": 59 },
]

list_of_lists = [
    [1, 2, 3],
    ['Hi', 'Hello', 'Goodbye'],
    [True, True, False],
]


def add_string(acc, x):
    print(f'accumulator: {acc}, X: {x}')
    return f'{acc},{x}'

joined_str = reduce(add_string, my_numbers)
print(joined_str)


def add_char_count(acc, str):
    return acc + len(str)

total_char_count = reduce(add_char_count, my_strings, 0)
print(total_char_count)



def list_to_dict(acc, pair):
    x = pair[1]          # element
    index = pair[0]      # element's index

    if type(x) is str:
        return {
            **acc,
            x: numbers_and_strings[index + 1]  # next element = value
        }
    else:
        return acc

my_dictionary = reduce(list_to_dict, enumerate(numbers_and_strings), {})
print(my_dictionary)


next(p for p in people if p['id'] == '123')

def index_list(acc, x):
    return {
        **acc,
        x['id']: x
    }

indexed_people = reduce(index_list, people, {})
person = indexed_people['123']
print(indexed_people)
print(person)


def rotate_matrix(acc, row):
    return [
        [*acc[0], row[0]],
        [*acc[1], row[1]],
        [*acc[2], row[2]],
    ]

rotated_list_of_lists = reduce(rotate_matrix, list_of_lists, [[],[],[],])
print(rotated_list_of_lists)


original_list = [1, 2, 3]

def make_same_list(acc, x):
    return [*acc, x]

new_list = reduce(make_same_list, original_list, [])
print(new_list)

