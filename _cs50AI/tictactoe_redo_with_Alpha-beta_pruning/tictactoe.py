"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    board[i][j]
    """
    X_count = 0
    O_count = 0
    for i in board:
        for j in i:
            if j == X:
                X_count += 1
            if j == O:
                O_count += 1
    if X_count > O_count:
        return O
    else:
        return X


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

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    if (i or j) not in range(3):
        raise NotImplementedError
    if new_board[i][j] == EMPTY:
        new_board[i][j] = player(board)
        return new_board
    else:
        raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.

    While this solution looks not very efficient --> i know i could return earlier without sets
    i decided to write it this way because it treats every possible win in the same way
    which might be more consistent logically, although not very pretty
    it is fairly understandable
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
        return X
    elif (O, O, O) in set_of_lines:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for i in board:
        if EMPTY in i:
            return False
    return True
    # so the question is why do we check for whether there is a winner


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    i = winner(board) # a little bit strange here
    if i == X:
        return 1
    elif i == O:
        return (-1)
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    THIS CODE IS AWFUL =)
    """
    if terminal(board):
        return None

    def recursion(board):
        turn = player(board)
        possible_moves = actions(board)
        move_util_set = set() #also use set to ignore all the other results

        for move in possible_moves:
            new_board = result(board, move)
            if terminal(new_board):
                score = utility(new_board)
            else:
                score = recursion(new_board)[1] #this is bs - returns the score. but by design function shoud return best move
            move_util_set.add((move, score))
            if turn == X and score == 1:
                break
            if turn == O and score == -1:
                break

        if turn == X:
            bestmove = max(move_util_set, key=lambda x: x[1])
            return bestmove
        if turn == O:
            bestmove = min(move_util_set, key=lambda x: x[1])
            return bestmove

    return recursion(board)[0]
