#!/usr/bin/env python3
from helper import *
import os, time

# create board
size = 5
bot = create_board(size)
user = create_board(size)

# place ship
place_ship(bot)
place_ship(user)

# show_board
show_board(bot)
show_board(user)

def ships_left(board):
    for row in board:
        for col in row:
            if col == SHIP:
                return True
    return False

# Attack Function:
while ships_left(bot) and ships_left(user):
    attack(bot)
    attack(user)


    # output:
    os.system('clear')
    show_board(bot)
    show_board(user)


# for row in bot:
#     for col in row:
#         if col == HIT:
#             print(HIT*10)
#         else:
#             print()

