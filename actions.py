board = [[EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY]]

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    set_of_lines = set()
    diog = []
    diog2 = []
    for i in board:
        vert = []
        horiz = []
        for j in i:
            vert.append(board[i][j])
            horiz.append(board[j][i])
        set_of_lines.add(tuple(vert))
        set_of_lines.add(tuple(horiz))
        diog.append(board[i][i])
        diog2.append(board[i][-i-1])
    set_of_lines.add(tuple(diog))
    set_of_lines.add(tuple(diog2))

    if (X, X, X) in set_of_lines:
        return X
    elif (O, O, O) in set_of_lines:
        return O
    else:
        return None


winner(board)
