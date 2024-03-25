X = "X"
O = "O"

board = [[None, X, None],
[None, X, None],
[X, X, None]]


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    set_of_lines = set()
    diog = []
    diog2 = []
    for i in range(3):
        vert = []
        horiz = []
        for j in range(3):
            vert.append(board[i][j])
            horiz.append(board[j][i])
        set_of_lines.add(tuple(vert))
        set_of_lines.add(tuple(horiz))
        diog.append(board[i][i])
        diog2.append(board[i][-i-1])
    set_of_lines.add(tuple(diog))
    set_of_lines.add(tuple(diog2))

    if (X, X, X) in set_of_lines:
        print('X')
        return X
    elif (O, O, O) in set_of_lines:
        return O
    else:
        print('no value found')
        return None


winner(board)
