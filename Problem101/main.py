import json


initial_msg = 'Welcome to Notes app\n'
print(initial_msg)

option_msg = 'Select option\n' \
'1. View list\n' \
'2. Add item\n' \
'3. Remove item\n' \
'0. Quit\n' \
'\nEnter option number (1, 2, 3, or 0): \n'

# notes_list = [
#     {
#         'name': 'Apples',
#         'quantity': '1',
#     }
# ]
with open('notes.json', 'r') as file:
    notes_list = json.load(file)


def view_list(notes_list):
    for index, item in enumerate(notes_list):
        print(f'{index + 1}. {item['name']} - {item['quantity']}')
    print()

def add_to_list(notes_list):
    list_item_name = input('Enter name of a thing: ')
    list_item_quantity = input('Enter quantity of that thing: ')
    new_item = {
        'name': list_item_name,
        'quantity': list_item_quantity,
    }
    notes_list.append(new_item)
    print()

def rem_from_list(notes_list):
    view_list(notes_list)
    print()
    rm_item_num = input('Enter item number to remove: ')
    try:
        rm_item_int = int(rm_item_num)
    except ValueError:
        print('Not valid')
    else:
        if rm_item_int > len(notes_list):
            print('Not valid')
        else:
            del notes_list[rm_item_int - 1]
            print('Removed')

while True:
    option_num = input(option_msg)

    if option_num == '1':
        print('Listing items..\n')
        view_list(notes_list)
    elif option_num == '2':
        print('Adding item..\n')
        add_to_list(notes_list)
    elif option_num == '3':
        print('Removing item..\n')
        rem_from_list(notes_list)
    elif option_num == '0':
        print('Exiting..')
        break
    else:
        print('Try again with a valid option\n')

    with open('notes.json', 'w') as file:
        json.dump(notes_list, file)
    
    # print()

