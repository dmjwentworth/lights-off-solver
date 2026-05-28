import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from play import Game
from solver import solve
plt.style.use('dark_background')


class Jarvis(Game):
    def __init__(self):
        super().__init__(interactive=False, setup=False)
        self.fig, self.ax = plt.subplots()
        self.moves = solve(self.grid)

    def init_frame(self):
        self.ax.clear()
        self.ax.imshow(self.grid, cmap='Blues', vmin=0, vmax=1)

    def animate(self, i):
        move = self.moves[i]
        print(f"Move {i + 1}: Toggle ({move[0]}, {move[1]})")
        self.toggle_button(move[0], move[1])
        self.ax.clear()
        self.ax.imshow(self.grid, cmap='Blues', vmin=0, vmax=1)
        plt.draw()

    def show(self):
        anim = FuncAnimation(
            self.fig,
            self.animate,
            frames=len(self.moves),
            init_func=self.init_frame,
            interval=700,
            repeat=False
        )
        plt.show()


def main():
    jarvis = Jarvis()
    jarvis.show()


if __name__ == '__main__':
    main()