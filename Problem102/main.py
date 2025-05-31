import random


word_list = [
    'Abiu',
    'Acai',
    'Acerola',
    'Akebi',
    'Ackee',
    'African Cherry Orange',
    'American Mayapple',
    'Apple',
    'Apricot',
    'Aratiles',
    'Araza',
    'Avocado',
    'Banana',
    'Bilberry',
    'Blackberry',
    'Blackcurrant',
    'Black sapote',
    'Blueberry',
    'Boysenberry',
    'Breadfruit',
    'Buddhas hand',
    'Cactus pear',
    'Canistel',
    'Catmon',
    'Cempedak',
    'Cherimoya',
    'Cherry',
    'Chico fruit',
    'Citron',
    'Cloudberry',
    'Coco de mer',
    'Coconut',
    'Crab apple',
    'Cranberry',
    'Currant',
    'Damson',
    'Date',
    'Dragonfruit',
    'Durian',
    'Elderberry',
    'Feijoa',
    'Fig',
    'Finger Lime',
    'Gac',
    'Goji berry',
    'Gooseberry',
    'Grape',
    'Raisin',
    'Grapefruit',
    'Grewia asiatica',
    'Guava',
    'Hala fruit',
    'Haws fruit of Hawthorn',
    'Honeyberry',
    'Huckleberry',
    'Jabuticaba',
    'Jackfruit',
    'Jambul',
    'Japanese plum',
    'Jostaberry',
    'Jujube',
    'Juniper berry',
    'Kaffir lime',
    'Kiwano ',
    'Kiwifruit',
    'Kumquat',
    'Lanzones',
    'Lemon',
    'Lime',
    'Loganberry',
    'Longan',
    'Loquat',
    'Lulo',
    'Lychee',
    'Magellan Barberry',
    'Macopa',
    'Mamey apple',
    'Mamey Sapote',
    'Mango',
    'Mangosteen',
    'Marionberry',
    'Medlar',
    'Melon',
    'Cantaloupe',
    'Galia melon',
    'Honeydew',
    'Mouse melon',
    'Muskmelon',
    'Watermelon',
    'Miracle fruit',
    'Mohsina',
    'Momordica fruit',
    'Monstera deliciosa',
    'Mulberry',
    'Nance',
    'Nectarine',
    'Orange',
    'Blood orange',
    'Clementine',
    'Mandarine',
    'Tangerine',
    'Papaya',
    'Passionfruit',
    'Pawpaw',
    'Peach',
    'Pear',
    'Persimmon',
    'Pineapple',
    'Pineberry',
    'Plantain',
    'Plum',
    'Prune',
    'Plumcot',
    'Pomegranate',
    'Pomelo',
    'Quince',
    'Raspberry',
    'Salmonberry',
    'Rambutan',
    'Redcurrant',
    'Rose apple',
    'Salal berry',
    'Salak',
    'Santol',
    'Sapodilla',
    'Sapote',
    'Sarguelas',
    'Saskatoon',
    'Satsuma',
    'Sloe',
    'Soursop',
    'Star apple',
    'Star fruit',
    'Strawberry',
    'Sugar apple',
    'Suriname cherry',
    'Tamarillo',
    'Tamarind',
    'Tangelo',
    'Tayberry',
    'Thimbleberry',
    'Ugli fruit',
    'White currant',
    'White sapote',
    'Ximenia',
    'Yuzu',
]

word_index = random.randint(0, len(word_list) - 1)
word_selected = word_list[word_index].lower()


print('Guess a fruit!\n')
# print(f'DEBUG: Selected word: {word_selected.upper()}\n')

def get_chars(word, guesses):
    """word str, guesses list"""
    display_str = ''
    for letter in word:
        if letter in guesses:
            display_str += f' {letter} '
        elif letter == ' ':
            display_str += f' {letter} '
        else:
            display_str += ' _ '
    return display_str

def get_guess(guesses):
    """guesses list"""
    while True:
        guess = input('\nEnter a letter: ')
        if len(guess) != 1:
            print('Not valid. Input only 1 char\n')
        elif not guess.isalpha():
            print('Not valid. Input only chars\n')
        elif guess in guesses:
            print('Already used. Input another char\n')
        else:
            return guess.lower()

# def is_loss(word, guesses):
#     return not is_win(word, guesses)

def is_win(word, guesses):
    return all([x in guesses for x in word])

def is_guess_correct(word, guess):
    """word str, guess str, return bool"""
    return guess in word

def apply_color(text):
    """red color char"""
    return f'\033[31m{text}]\033[0m'

# main
user_guesses = [' ',]
turns_left = int(len(word_selected) * 1.2)

while turns_left > 0:
    print(f'Turns left: {turns_left}')
    
    print(f'WORD: {get_chars(word_selected, user_guesses)}')

    new_guess = get_guess(user_guesses)
    user_guesses.append(new_guess)
    
    if not is_guess_correct(word_selected, new_guess):
        print('Incorrect\n')
    else:
        print('Correct\n')

    turns_left -= 1

    if is_win(word_selected, user_guesses):
        print(f'{get_chars(word_selected, user_guesses).upper()}\n')
        print('Win!')
        break

if not is_win(word_selected, user_guesses):
    print('Loss.')

