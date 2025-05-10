from random import randint
import time

# Input player names
player1 = input("Enter name of player 1: ")
player2 = input("Enter name of player 2: ")

# Initialize scores
score1 = 0
score2 = 0

# Play 5 rounds
for i in range(5):
    print(f"\nRound {i + 1}")

    # Player 1 rolls
    print(player1, "is rolling the die...")
    time.sleep(1)
    roll1 = randint(1, 6)
    print("Rolled:", roll1)

    # Player 2 rolls
    print(player2, "is rolling the die...")
    time.sleep(1)
    roll2 = randint(1, 6)
    print("Rolled:", roll2)

    # Update scores
    if roll1 > roll2:
        print(player1, "wins this round!")
        score1 += 1
    elif roll2 > roll1:
        print(player2, "wins this round!")
        score2 += 1
    else:
        print("It's a tie!")

# Final result
print("\nFinal result:")
if score1 > score2:
    print(player1, "wins the game!")
elif score2 > score1:
    print(player2, "wins the game!")
else:
    print("The game is a tie!")
