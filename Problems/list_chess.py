#

board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

#

board = [[0 for i in range(8)] for j in range(8)]

print('board = [')
for i in range(len(board)):
    print(board[i], end=',\n')
print(']')

