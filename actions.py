X = "X"
O = "O"
EMPTY = None

board = [[X, X, O],
        [X, X, O],
        [O, O, EMPTY]]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    #case before last, but im doing utility in the wrong place and not calling terminal board
    turn = X
    possible_moves = {(3, 3)}
    move_util_set = set() #also use set to ignore all the other results

    for move in possible_moves:
        new_board = [[X, X, O],
                    [X, X, O],
                    [O, O, X]]
        if terminal(new_board):
            score = 1
        else:
            score = minimax(new_board) #this is bs it returns the score.
        move_util_set.add((move), score)

    if turn == X:
        bestmove = max(move_util_set, key=lambda x: x[1])
        return bestmove[1]
    if turn == O:
        bestmove = min(move_util_set, key=lambda x: x[1])
        return bestmove[1]
