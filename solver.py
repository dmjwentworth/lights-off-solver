import numpy as np
from play import update_grid


def count_lights_on(grid):
    np_grid = np.array(grid)
    return np.sum(np_grid)


def find_best_move(grid):
    candidates = []
    lights_on = []
    lights_on_initial = count_lights_on(grid)
    for i in range(5):
        for j in range(5):
            np_grid = np.array(grid)
            update_grid(np_grid, i, j)
            count = count_lights_on(np_grid)
            if count < lights_on_initial:
                candidates.append((i, j))
                lights_on.append(count)
    if not candidates:
        return None
    best_index = np.argmin(lights_on)
    return candidates[best_index]


def solve(grid):
    np_grid = np.array(grid)
    solution = []
    best_move = find_best_move(np_grid)
    while best_move is not None:
        solution.append(best_move)
        update_grid(np_grid, best_move[0], best_move[1])
        best_move = find_best_move(np_grid)
    return solution


def main():
    grid = [
        [0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0]
    ]
    solution = solve(grid)
    print("Solution:")
    for move in solution:
        print(f"Toggle ({move[0]}, {move[1]})")


if __name__ == '__main__':
    main()