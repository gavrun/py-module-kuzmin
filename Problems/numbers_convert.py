def print_number_notations(starting, till):
    for x in range(starting, till + 1):
        print(f'{x} - {bin(x)} - {oct(x)} - {hex(x)}')


for x in range(16):
    print(f'{x} - {bin(x)} - {oct(x)} - {hex(x)}')
print()

print_number_notations(0, 128)
print()
