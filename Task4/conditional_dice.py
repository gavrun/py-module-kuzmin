from random import randint
import time

# Input player names
player1 = input("Enter name of player 1: ")
player2 = input("Enter name of player 2: ")

# Player 1 rolls the die
print(player1, "is rolling the die...")
time.sleep(2)
roll1 = randint(1, 6)
print("Rolled:", roll1)

# Player 2 rolls the die
print(player2, "is rolling the die...")
time.sleep(2)
roll2 = randint(1, 6)
print("Rolled:", roll2)

# Determine the winner
if roll1 > roll2:
    print(player1, "wins!")
elif roll1 < roll2:
    print(player2, "wins!")
else:
    print("It's a tie!")
