# simple

def create_counter():
    count = 0

    def print_and_inc():
        nonlocal count
        print(f'Counted {count}')
        count += 1

    return print_and_inc

c = create_counter()

c()
c()
c()
c()
c()
print()

# dictionary

def create_counter_dict():
    count1 = 0
    big_int_amount = 5

    def inc():
        nonlocal count1
        count1 += 1

    def reset():
        nonlocal count1
        count1 = 0

    def print_count():
        print(f'Counted {count1}')

    def change_big_int_amount(new_amount):
        nonlocal big_int_amount
        big_int_amount = new_amount
        print(f'Changed {big_int_amount}')

    return {
        'inc': inc,
        'reset': reset,
        'print_count': print_count,
        'change_big_int_amount': change_big_int_amount
    }

cd = create_counter_dict()

cd['inc']()
cd['inc']()
cd['inc']()
cd['print_count']()
cd['reset']()
cd['change_big_int_amount'](6)
cd['print_count']()
