
board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    return set of (i, j) (coordinates where something can be placed)
    """
    set_moves = set()
    for i in board:
        for j in i:
            if j == EMPTY:
                set_moves.add((i, j))
    return set_moves
