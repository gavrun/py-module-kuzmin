from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|", " | ".join(f"  {str(cell)}  " for cell in row), "|")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                raise ValueError
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = 'O'
                        return
            print("That square is already occupied! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")

def make_list_of_free_fields(board):
    return [(i, j) for i in range(3) for j in range(3) if isinstance(board[i][j], int)]

def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = free_fields[randrange(len(free_fields))]
        board[move[0]][move[1]] = 'X'

# --- Game Loop ---
def play_game():
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]  # Computer starts with 'X' in the center
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You won!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer won!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

# main
play_game()
