# lists

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)
print(numbers[2])


# only leaf nodes have data

tree_leafs = [ [ [1, 2, 3],[] ], [5, 6], [7], 0 ]
print(tree_leafs)

# data and leaf nodes

tree = [ 1, [2], [ 3, [], [] ] ]
print(tree)

# nested lists

my_file_system_tree1 = [
    'Users',
    [
        'SW',
        [
            'Docs',
            ['my-presentation.txt']
        ],
        ['Photos'],
        ['Repos'],
    ],
    ['SE'],
    ['AP'],
]

print(my_file_system_tree1)


# nested dictionaries

my_file_system_tree2 = {
    'Users': {
        'SW': {
            'Docs': {
                'my-presentation.txt': {}
            },
            'Photos': {},
            'Repos': {}
        },
        'SE': {},
        'AP': {}
    }
}

print(my_file_system_tree2)


# printing trees

my_tree = {
    'value': 1,
    'children': [
        {'value': 2},
        {
            'value': 3,
            'children': [
                {'value': 4},
                {'value': 5}
            ]
        }
    ]
}

def print_tree(tree):
    print(tree['value'])
    if 'children' not in tree:
        return
    for subtree in tree['children']:
        print_tree(subtree)
    # return

print_tree(my_tree)
