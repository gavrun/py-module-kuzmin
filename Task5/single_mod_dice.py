from random import randint
import time

def get_players():
    player1 = input("Enter name of player 1:")
    player2 = input("Enter name of player 2:")

    return player1, player2

def play_game(player1, player2):
    score1 = 0
    score2 = 0

    for i in range(5):
        print(f"\nRound {i + 1}")

        print(player1, "is rolling the die...")
        time.sleep(1)
        roll1 = randint(1, 6)
        print("Rolled:", roll1)

        print(player2, "is rolling the die...")
        time.sleep(1)
        roll2 = randint(1, 6)
        print("Rolled:", roll2)

        if roll1 > roll2:
            print(player1, "wins this round!")
            score1 += 1
        elif roll2 > roll1:
            print(player2, "wins this round!")
            score2 += 1
        else:
            print("It's a tie!")

    return score1, score2

def find_winner(player1, player2, score1, score2):
    print("\nFinal result:")

    if score1 > score2:
        print(player1, "wins the game!")
    elif score2 > score1:
        print(player2, "wins the game!")
    else:
        print("The game is a tie!")

# Main 
p1, p2 = get_players()
s1, s2 = play_game(p1, p2)
find_winner(p1, p2, s1, s2)
