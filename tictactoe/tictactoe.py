"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Initialize counters for X's and O's
    X_count = 0
    O_count = 0

    # Iterate over each cell and count the number of X's and O's
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "X":
                X_count += 1
            elif board[i][j] == "O":
                O_count += 1

    # If the counts are equal, it is X's turn; otherwise, it is O's turn
    if X_count == O_count:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize empty set for possible actions
    possible_actions = set()

    # Loop through each cell in the board
    for i in range(len(board)):
        for j in range(len(board)):
            # For each cell, if it is empty, add its coordinates (i, j) to the set of possible actions
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    # Return set of possible actions
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create a deep copy of the board
    new_board = copy.deepcopy(board)

    # Determine the current player
    current_player = player(new_board)

    # If action is valid (i.e., the cell at the action's coordinates is empty), update the cell with the current player's symbol
    if action in actions(new_board):
        new_board[action[0]][action[1]] = current_player
    else:
        raise ValueError("Invalid action")

    # Return the new board
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check each row to see if all elements are the same and not empty. If so, return the value in that row.
    if (board[0][0] == board[0][1] == board[0][2]) and board[0][0] != EMPTY:
        return board[0][0]

    elif (board[1][0] == board[1][1] == board[1][2]) and board[1][0] != EMPTY:
        return board[1][0]

    elif (board[2][0] == board[2][1] == board[2][2]) and board[2][0] != EMPTY:
        return board[2][0]

    # Check each column to see if all elements are the same and not empty. If so, return the value in that column.
    if (board[0][0] == board[1][0] == board[2][0]) and board[0][0] != EMPTY:
        return board[0][0]

    elif (board[0][1] == board[1][1] == board[2][1]) and board[0][1] != EMPTY:
        return board[0][1]

    elif (board[0][2] == board[1][2] == board[2][2]) and board[0][2] != EMPTY:
        return board[0][2]

    # Check the two diagonals to see if all elements are the same and not empty. If so, return the value in that diagonal.
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]
    elif (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != EMPTY:
        return board[0][2]

    # If no winner found, return None
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    game_winner = winner(board)

    # If a winner identified, return True
    if game_winner is not None:
        return True

    # If no winner identified and no possible actions remain, return True
    elif game_winner is None and len(actions(board)) == 0:
        return True

    # If no winner identified and possible actions remain, return False
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)

    if game_winner == "X":
        return 1
    elif game_winner == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check if board is in a terminal state. If so, return None for the action since no further action can be taken
    if terminal(board) == True:
        return None

    # If board is not in a terminal state, determine the current player
    else:
        current_player = player(board)

        # If current player is X, you want to maximize the score
        if current_player == "X":
            value, action = max_value(board)

        # If current player is O, you want to minimize the score
        elif current_player == "O":
            value, action = min_value(board)

        return action


def max_value(board):
    """
    If the current player is X, return the action that results in the highest score
    """
    v = float("-inf")
    best_action = None

    if terminal(board):
        return utility(board), None

    for action in actions(board):
        new_value = min_value(result(board, action))
        if new_value[0] > v:
            v = new_value[0]
            best_action = action

    return v, best_action


def min_value(board):
    """
    If the current player is O, return the action that results in the lowest score
    """
    v = float("inf")
    best_action = None

    if terminal(board):
        return utility(board), None

    for action in actions(board):
        new_value = max_value(result(board, action))
        if new_value[0] < v:
            v = new_value[0]
            best_action = action

    return v, best_action
