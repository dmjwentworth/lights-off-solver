import json
import argparse
import tkinter as tk
from solver import solve
from utils import generate_random_grid, update_grid, colours, solved


class Game:
    def __init__(self, solve_mode):
        # Initialise the game state
        self.solve_mode = solve_mode
        if self.solve_mode:
            self.grid = solved
            self.setup = True
        else:
            self.solution, self.grid = generate_random_grid()
            self.setup = False

        # Initialise the GUI
        self.count = 0       
        self.streak = 0 
        self.root = tk.Tk()
        self.root.title('Lights Off')
        self.root.config(bg='black')
        self.buttons = self.make_buttons()
        self.count_label, self.streak_label = self.make_labels()

        # Start the GUI event loop
        self.root.mainloop()       

    def make_labels(self):
        # Create labels for move count and current streak
        count_label = tk.Label(
            self.root,
            text=f'Moves: 0',
            fg='white',
            bg='black'
        )
        count_label.grid(row=5, column=0, columnspan=5, pady=10)

        streak_label = tk.Label(
            self.root,
            text=f'Current Streak: 0',
            fg='white',
            bg='black'
        )
        streak_label.grid(row=6, column=0, columnspan=5, pady=10)

        return count_label, streak_label

    def make_buttons(self):
        # Create a 5x5 grid of buttons based on the current grid state
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

        button = tk.Button(
            self.root,
            text='I`m stuck',
            bg='red',
            fg='white',
            command=self.show_solution
        )
        button.grid(row=7, column=0, columnspan=5, pady=10)

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
        # Toggle the button at (i, j) and update the grid and button states
        if not self.setup:
            self.count += 1
        update_grid(self.grid, i, j, self.setup)
        self.update_buttons()
        self.count_label.config(text=f'Moves: {self.count}')

    def show_solution(self):
        # Get the solution from the solver and display it on the buttons
        self.setup = False
        if self.solve_mode:
            self.solution = solve(self.grid)
        for move in self.solution:
            self.buttons[move[0]][move[1]].config(text='Press')


def main(args):
    game = Game(solve_mode=args.solve)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lights Off Game')
    parser.add_argument(
        '--solve',
        action='store_true',
        help='Solve the grid configuration',
    )
    args = parser.parse_args()
    main(args)

