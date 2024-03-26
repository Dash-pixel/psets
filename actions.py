X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    return set of (i, j) (coordinates where something can be placed)
    """
    set_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                set_moves.add((i, j))
    return set_moves

print(actions(board))
