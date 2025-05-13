secret_number = 777

print(
"""
+================================+
| So, what is the secret number? |
+================================+
""")

guess = int(input("Enter your guess: "))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess = int(input("Try again: "))

print(secret_number)
print("Well done! You are free now.")
