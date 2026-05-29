import numpy as np
from tqdm import tqdm
from itertools import combinations
from utils import int_to_pos, update_grid, solved


def check_games_of_N_moves(grid, N):
    for moves in tqdm(combinations(range(25), N)):
        np_grid = np.array(grid, dtype=int)
        for move in moves:
            x, y = int_to_pos(move)
            update_grid(np_grid, x, y)
        
        if np.array_equal(np_grid, solved):
            print(f"\nFound a solution with {N} moves: {moves}")
            return moves
    
    print(f"No solution found with {N} moves.")
    return None


def solve(grid):
    if np.array_equal(np.array(grid, dtype=int), solved):
        print("The grid is already solved.")
        return []

    for N in range(1, 26):
        print(f"\033[1;34mChecking for solutions with {N} moves...\033[0m")
        moves = check_games_of_N_moves(grid, N)
        if moves is not None:
            moves = [int_to_pos(move) for move in moves]
            return moves
    
    print("No solution found.")
    return None


def main():
    grid = [
        [0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0]
    ]
    
    moves = solve(grid)
    if moves is not None:
        print(f"Solution found:\n{moves}")
    else:
        print("No solution found.")


if __name__ == '__main__':
    main()

