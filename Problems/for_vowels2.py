# A vowel eater!

word_without_vowels = ""

# Prompt the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to upper case
user_word = user_word.upper()

# Loop through each letter in the word
for letter in user_word:
    # If the letter is a vowel, skip it
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    # Otherwise, add the letter to the result
    word_without_vowels += letter

# Print the result
print(word_without_vowels)
