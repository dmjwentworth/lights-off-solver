import json
import numpy as np

np_solved = np.zeros((5, 5), dtype=int)
solved = np_solved.tolist()
colours = ['gray', 'blue']


def int_to_pos(num):
    return num // 5, num % 5


def update_grid(grid, i, j, setup=False):
    # Update the grid based on the button press
    if setup:
        grid[i][j] = 1 - grid[i][j]
    else:
        for x, y in [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < 5 and 0 <= y < 5:
                grid[x][y] = 1 - grid[x][y]


def generate_random_grid():
    # Generate a random grid by applying random moves to the solved state
    np_grid = np.copy(np_solved)
    # Number of moves to apply, between 1 and 25
    N = np.random.randint(1, 26)
    # Randomly select N unique moves from the 25 possible positions
    moves = np.random.choice(25, N, replace=False)
    moves = [int_to_pos(move) for move in moves]
    for i, j in moves:
        update_grid(np_grid, i, j)
    # return the list of moves and the resulting grid as a list of lists
    return moves, np_grid.tolist()

