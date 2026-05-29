import json
import argparse
import tkinter as tk
from solver import solve
from utils import load_grid, update_grid, colours


class Game:
    def __init__(self, cheats, setup):
        #
        self.grid = load_grid()
        self.cheats = cheats
        self.setup = setup
        self.count = 0        
        self.root = tk.Tk()
        self.root.title('Lights Off')
        self.root.config(bg='black')
        self.buttons = self.make_buttons()
        self.count_label = tk.Label(
            self.root,
            text=f'Moves: {self.count}',
            fg='white',
            bg='black'
        )
        self.count_label.grid(row=5, column=0, columnspan=5, pady=10)

        #
        if self.cheats:
            self.show_solution()

        #
        self.root.mainloop()       
        if self.setup:
            with open('grid.json', 'w') as f:
                json.dump(self.grid, f)

    def make_buttons(self):
        buttons = []
        
        for i in range(5):
            row = []
            for j in range(5):
                button = tk.Button(
                    self.root,
                    bg=colours[self.grid[i][j]],
                    width=10,
                    height=5,
                    activebackground=colours[self.grid[i][j]],
                    command=lambda i=i, j=j: self.toggle_button(i, j)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            buttons.append(row)

        return buttons
    
    def update_buttons(self):
        # Update the button colours based on the new grid state
        for x in range(5):
            for y in range(5):
                self.buttons[x][y].config(
                    bg=colours[self.grid[x][y]],
                    activebackground=colours[self.grid[x][y]]
                )

    def toggle_button(self, i, j):
        self.count += 1
        update_grid(self.grid, i, j, self.setup)
        self.update_buttons()
        self.count_label.config(text=f'Moves: {self.count}')

    def show_solution(self):
        solution = solve(self.grid)
        for move in solution:
            self.buttons[move[0]][move[1]].config(text='Press')


def main(args):
    if args.solve:
        game = Game(cheats=True, setup=False)
    else:
        game = Game(cheats=False, setup=args.setup)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lights Off Game')
    parser.add_argument(
        '--setup', action='store_true', help='Set up the grid configuration'
    )
    parser.add_argument(
        '--solve', action='store_true', help='Solve the grid configuration'
    )
    args = parser.parse_args()
    main(args)

    