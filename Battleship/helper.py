

MISS = "⛔"
HIT = "🔥"
SHIP = "🚢"
H2O = "🌊"

from random import randint as rint


def show_board(board):
    for row in board:
        print(''.join(row))

def create_board(size):
    board = []
    for i in range(size):
        board.append([H2O] * size)
    return board
    # return [[H2O, H2O], [H2O, H2O]] OR [[H2O, H2O], [H2O, H2O]]

def place_ship(board):
    row, col = get_coordinates(board, True)
    board[0][0] = SHIP

def get_coordinates(board, rnd):
    if rnd:
        row = rint(0, len(board) - 1)
        col = rint(0, len(board) - 1)
    else:
        print("Please enter your designated attack coordinates")
        row = int(input("X coordinate: "))
        col = int(input("Y coordinate: "))
    return row, col

def attack(board):
    # input: get attack coordinates
    row, col = get_coordinates()

    # process: check to see hit/miss mark board
    if board[row][col] == SHIP:
        board[row][col] = HIT
        print("You successfully targetted and hit the opponents ship with a cannonball!")
    elif board[row][col] == H2O:
        board[row][col] = MISS
        print("Sadly, you missed.  Do better next time!")
    else:
        pass
