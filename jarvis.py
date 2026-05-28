import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from play import Game, colours
plt.style.use('dark_background')


class Jarvis(Game):
    def __init__(self):
        super().__init__(interactive=False, setup=False)
        self.fig, self.ax = plt.subplots()
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.move_history = []

    def show(self):
        self.ax.imshow(self.grid, cmap='Blues', vmin=0, vmax=1)
        plt.show()


def main(args):
    jarvis = Jarvis()
    jarvis.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lights Off Game')
    args = parser.parse_args()
    main(args)