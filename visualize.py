"""
Utilities to visualize patterns.

See examples below.

Run `python visualize.py` to create demo output.
"""

import itertools

from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np


FIGSIZE = (5, 5)
MAX_COLOR_VALUE = 2


def plot(cell_colors, shape, path="pattern.png"):
    array = to_array(cell_colors, shape)
    fig, ax = plt.subplots(figsize=FIGSIZE)
    quad = ax.pcolormesh(array, edgecolors="grey", rasterized=True, cmap="gist_ncar_r")
    ax.axis("off")
    fig.savefig(path)


def to_array(cell_colors, shape):
    array = np.zeros(shape)
    for coordinate, value in cell_colors.items():
        array[coordinate] = value
    array = np.flipud(array)
    return array


def animate(cell_colors_iterable, shape, path="pattern_animation.html"):

    initial_cell_colors = dict()
    initial_frame = to_array(initial_cell_colors, shape)

    fig, ax = plt.subplots(figsize=FIGSIZE)
    quad = ax.pcolormesh(
        initial_frame,
        edgecolors="grey",
        rasterized=True,
        cmap="gist_ncar_r",
        vmin=0,
        vmax=MAX_COLOR_VALUE,
    )
    ax.axis("off")

    def update(frame):
        array = to_array(frame, shape)
        quad.set_array(array)
        return quad

    frames = itertools.chain([initial_cell_colors], cell_colors_iterable)

    ani = animation.FuncAnimation(
        fig=fig, func=update, frames=frames, cache_frame_data=False
    )

    with open(path, "w") as fh:
        fh.write(ani.to_jshtml())


if __name__ == "__main__":
    # Shape of the grid
    shape = (3, 3)

    # Single frame
    cell_color = 1
    cell_colors = {(0, 0): cell_color, (1, 1): cell_color}
    plot(cell_colors, shape, path="./visualizations/pattern.png")

    # Animation of multiple frames
    cell_colors_iterable = [
        cell_colors,
        {(2, 2): cell_color},
        {(0, 2): cell_color},
        {(2, 0): cell_color},
    ]
    animate(cell_colors_iterable, shape, path="./visualizations/animation.html")
