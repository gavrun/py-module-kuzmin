import json
import os
import sys


dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'items.json')


def view_budget(data):
    print('Current budget balance by category..')
    for category in data['categories']:
        category_expenses = [ e['amount'] for e in data['expenses'] if e['category'] == category['name'] ]
        total_expenses = sum(category_expenses)
        print(f'Category {category['name']}: ${category['amount'] - total_expenses}')
    return data


def add_budget_item(data):
    print('New budget category and limit..')
    name = input('Enter name to add: ')
    amount = int(input('Enter amount to add: '))
    new_budget_item = {
        'name': name,
        'amount': amount,
    }
    data['categories'].append(new_budget_item)
    return data


def remove_budget_item(data):
    print('Removing budget category..')
    name = input('Enter name to remove: ')
    data['categories'] = [ c for c in data['categories'] if c['name'] != name ]
    return data


def add_expense(data):
    print('New budget expense and amount..')
    name = input('Enter name to add: ')
    category = input('Enter category to add: ')
    amount = int(input('Enter amount to add: '))
    new_expense_item = {
        'name': name,
        'category': category,
        'amount': amount,
    }
    data['expenses'].append(new_expense_item)
    return data


def remove_expense(data):
    print('Removing expense item..')
    name = input('Enter name to remove: ')
    amount = int(input('Enter amount to remove: '))
    data['expenses'] = [ e for e in data['expenses'] if e['name'] != name ]
    return data


def exit(data):
    print('Exiting..')
    sys.exit()


menu_actions = [
    {
        'name': 'View Budget',
        'action': view_budget,
    },
    {
        'name': 'Add Budget Item',
        'action': add_budget_item,
    },
    {
        'name': 'Remove Budget Item',
        'action': remove_budget_item,
    },
    {
        'name': 'Add Expense',
        'action': add_expense,
    },
    {
        'name': 'Remove Expense',
        'action': remove_expense,
    },
    {
        'name': 'Exit',
        'action': exit,
    },
]


def run_terminal(actions):
    with open(file_path, 'r') as file:
        items_data = json.load(file)

    while True:
        print('\nMenu:')
        for i, action in enumerate(actions):
            print(f'{i + 1}. {action['name']}')
        
        user_choice = int(input('\nSelect action:\n'))

        selected_action = actions[user_choice - 1]
        # print()

        updated_data = selected_action['action'](items_data)

        with open(file_path, 'w') as file:
            json.dump(updated_data, file)


# main
run_terminal(menu_actions)


