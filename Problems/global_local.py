# global
count = 0

def modify_count(command):  # 'inc', 'reset', 'big_inc', 'change_big_inc'
    starting_value = 0
    inc_amount = 1
    big_inc_amount = 10

    def inc():
        global count
        count += inc_amount

    def reset():
        global count
        count = starting_value

    def big_inc():
        global count
        count += big_inc_amount

    def change_big_inc_amount(new_amount):
        nonlocal big_inc_amount
        big_inc_amount = new_amount

    if command == 'inc':
        inc()
    elif command == 'reset':
        reset()
    elif command == 'big_inc':
        big_inc()
    elif command == 'change_big_inc':
        change_big_inc_amount(5)
        print(f'big_inc_amount: {big_inc_amount}')

modify_count('inc')
modify_count('inc')
modify_count('inc')

print(count)  # → 3

modify_count('reset')
modify_count('big_inc')

print(count)  # → 10

modify_count('change_big_inc')
modify_count('big_inc')

print(count)  # → 25 (10 + 15, т.к. big_inc_amount modified 5)
