# composition

def first(list):
    return list[0]

def get_name(dict):
    return dict['name']

def reverse(str):
    return str[::-1]

users = [
    {
        'name': 'Shaun',
        'age': 123,
        'hair_color': 'brown',
    }, {
        'name': 'Bob',
        'age': 44,
        'hair_color': 'blue',
    }, {
        'name': 'Sue',
        'age': 76,
        'hair_color': 'black'
    }
]

print(first(users))
print(get_name(first(users)))
print(reverse(get_name(first(users))))


# composition by lists/arrays

functions_to_compose = [
    reverse,
    first,
    get_name
]

result = users

for func in functions_to_compose:
    result = func(result)

#

def compose(funcs):
    def composed_funcs(data):
        result = data
        for func in funcs:
            result = func(result)
        return result
    return composed_funcs

last = compose([reverse, get_name, first])
print(last(user_data))

# pipeline equivalent to reverse(first(get_likes(first(get_name(users)))))

first_like_of_last_user = compose(
    reverse,
    first,
    get_likes,
    first,
    get_name
)
print(first_like_of_first_user(users))


