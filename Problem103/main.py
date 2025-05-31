import random


def generate_pswd(length, charset, options):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    lettersupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*'

    chars = letters + lettersupper + numbers + symbols
    pswd_chars = []

    for _ in range(length):
        char = chars[random.randint(0, len(chars) - 1)]
        # print(f'Selected letter: {letter}')
        pswd_chars.append(char)

    return ''.join(pswd_chars)


def generate_pswd_cat(length, charset, options):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    lettersupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*'

    # chars = letters + lettersupper + numbers + symbols
    number_each_category = length // 4
    remaining_chars = length % 4
    
    pswd_chars = []
    
    for _ in range(number_each_category):
        charL = letters[random.randint(0, len(letters) - 1)]
        charLU = lettersupper[random.randint(0, len(lettersupper) - 1)]
        charN = numbers[random.randint(0, len(numbers) - 1)]
        charS = symbols[random.randint(0, len(symbols) - 1)]
        
        pswd_chars.append(charL)
        pswd_chars.append(charLU)
        pswd_chars.append(charN)
        pswd_chars.append(charS)

    while remaining_chars > 0:
        charL = letters[random.randint(0, len(letters) - 1)]
        pswd_chars.append(charL)
        remaining_chars -= 1

    return ''.join(pswd_chars)

def generate_pswd_chk(length, charset, options):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    lettersupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*'

    chars = letters + lettersupper + numbers + symbols
    pswd_chars = []

    while length > 0:
        char = chars[random.randint(0, len(chars) - 1)]

        if char in letters:
            pswd_chars.append(char)
            length -= 1
            continue
        if char in lettersupper:
            pswd_chars.append(char)
            length -= 1
            continue
        if char in numbers:
            pswd_chars.append(char)
            length -= 1
            continue
        if char in symbols:
            pswd_chars.append(char)
            length -= 1
            continue

    return ''.join(pswd_chars)

def generate_pswd_lscmp(length, charset, options):
    charsets = {
        'letters': 'abcdefghijklmnopqrstuvwxyz',
        'lettersupper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'numbers': '0123456789',
        'symbols': '!@#$%^&*',
    }

    required_chars = [random.choice(chars) for chars in charsets.values()]
    
    charset = ''.join(charsets.values())
    rest_chars = [random.choice(charset) for _ in range(length - len(required_chars))]

    pswd_chars = required_chars + rest_chars
    random.shuffle(pswd_chars)

    return ''.join(pswd_chars)

# main
pswd1 = generate_pswd(5, None, None)
print(f'Generated password: {pswd1}')
pswd2 = generate_pswd(8, None, None)
print(f'Generated password: {pswd2}')
pswd3 = generate_pswd(17, None, None)
print(f'Generated password: {pswd3}\n')

pswd11 = generate_pswd_cat(5, None, None)
print(f'Generated password: {pswd11}')
pswd21 = generate_pswd_cat(8, None, None)
print(f'Generated password: {pswd21}')
pswd31 = generate_pswd_cat(17, None, None)
print(f'Generated password: {pswd31}\n')

pswd12= generate_pswd_chk(5, None, None)
print(f'Generated password: {pswd12}')
pswd22 = generate_pswd_chk(8, None, None)
print(f'Generated password: {pswd22}')
pswd32 = generate_pswd_chk(17, None, None)
print(f'Generated password: {pswd32}\n')

pswd10= generate_pswd_lscmp(5, None, None)
print(f'Generated password: {pswd10}')
pswd20 = generate_pswd_lscmp(8, None, None)
print(f'Generated password: {pswd20}')
pswd30 = generate_pswd_lscmp(17, None, None)
print(f'Generated password: {pswd30}\n')

