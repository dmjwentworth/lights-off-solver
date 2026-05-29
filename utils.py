import json
import numpy as np

solved = np.zeros((5, 5), dtype=int)
colours = ['gray', 'blue']


def int_to_pos(num):
    return num // 5, num % 5


def load_grid():
    # Load the grid configuration from the JSON file
    try:
        with open('grid.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, return a default grid
        return [[0 for _ in range(5)] for _ in range(5)]


def update_grid(grid, i, j, setup=False):
    # Update the grid based on the button press
    if setup:
        grid[i][j] = 1 - grid[i][j]
    else:
        for x, y in [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < 5 and 0 <= y < 5:
                grid[x][y] = 1 - grid[x][y]

