# A vowel eater!

# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to upper case
user_word = user_word.upper()

# Loop through each letter in the word
for letter in user_word:
    # Check if the letter is a vowel
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue  # Skip the vowel
    # Print the consonant (uneaten letter)
    print(letter)
