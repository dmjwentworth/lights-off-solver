import json
import argparse
import tkinter as tk

colours = ['gray', 'blue']


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


class Game:
    def __init__(self, interactive, setup):
        self.grid = load_grid()
        self.interactive = interactive
        self.setup = setup
        self.count = 0
        if self.interactive:
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
                    command=lambda i=i, j=j : self.toggle_button(i, j)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            buttons.append(row)
        
        return buttons
    
    def update_buttons(self):
        # Update the button colors based on the new grid state
        for x in range(5):
            for y in range(5):
                self.buttons[x][y].config(
                    bg=colours[self.grid[x][y]],
                    activebackground=colours[self.grid[x][y]]
                )

    def toggle_button(self, i, j):
        self.count += 1
        update_grid(self.grid, i, j, self.setup)
        if self.interactive:
            self.update_buttons()
            self.count_label.config(text=f'Moves: {self.count}')

    def run(self):
        if self.interactive:
            self.root.mainloop()
            if self.setup:
                with open('grid.json', 'w') as f:
                    json.dump(self.grid, f)


def main(args):
    game = Game(interactive=True, setup=args.setup)
    game.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lights Off Game')
    parser.add_argument('--setup', action='store_true', help='Set up the grid configuration')
    args = parser.parse_args()
    main(args)
    