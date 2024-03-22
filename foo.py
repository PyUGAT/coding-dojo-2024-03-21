"""
Implementation goes here.
#GRID 5x5
"""

from dataclasses import dataclass


def setup_grid(size):
    grid = []
    for x in range(size):
        grid.append([])
        for y in range(size):
            grid[x].append("w")

    return grid


@dataclass
class State:
    grid: list[list[str]]
    ant_position: tuple[int, int]
    ant_facing: str


def create_initial_state(size: int) -> State:
    return State(
        grid=setup_grid(size),
        ant_position=(size // 2, size // 2),
        ant_facing="north",
    )


def move_ant(state):
    state.grid = [
        ["w", "w", "w"],
        ["w", "b", "w"],
        ["w", "w", "w"],
    ]
    state.ant_position = (2, 1)
    state.ant_facing = "east"
    return state


D = ("north", "east", "south", "west")
L = {"b": D, "w": D[::-1]}
K = {k: v.index for k, v in L.items()}


def get_new_direction(x, a):
    return L[a][K[a](x) - 1]


D = ("north", "east", "south", "west", "north")
P = list(zip(D, D[1:]))
L = {"w": dict(P), "b": {v: k for k, v in P}}


def get_new_direction(a, b):
    return L[b][a]


def get_new_direction(a, b, x=lambda y: y.index):
    D = "north", "east", "south", "west"
    return D[x(D)(a) + x("b w")(b) - 1 & 3]
    return D[D.index(a) + "b w".index(b) - 1 & 3]
    return D[D.index(a) + 1 - 2 * (b == "b") & 3]
    return D[(D.index(a) + 1 - 2 * (119 - ord(b)) // 21) % 4]
    return D[(D.index(a) + 1 - 2 * (b == "b")) % 4]
    return D[(D.index(a) + {"w": 1}.get(b, -1)) % 4]
    return D[(D.index(a) + {"w": 1, "b": -1}[b]) % 4]


def get_new_direction(
    a, b, x=lambda y: y.index, D=("north", "east", "south", "west") * 2
):
    return D[x(D)(a) + x("b w")(b) - 1]
    return D[x(D)(a) + x("b w")(b) - 1 & 3]


def get_new_direction(a, b):
    D = "north", "east", "south", "west"

    D[1::]

    return (lambda D=("north", "east", "south", "west"): D[x(D)(a) + x("b w")(b) - 1])()
    return D[x(D)(a) + x("b w")(b) - 1 & 3]


# get_new_direction(a, "b") ==
# get_new_direction(get_new_direction(get_new_direction(a, "w")))


def get_new_direction(a, b):
    return D[a[0] + b]
    # nb 0 we 0  st 4
    # sw 1 we 0  st 4
    # sb 0 ea 1  st 4
    # nw 1 ea 1  st 4
    # eb 0 nor 2 th 5
    # ww 1 nor 2 th 5
    # wb 0 sou 3 th 5
    # ew 1 sou 3 th 5


#    d = DIRECTIONS[:: 1 - 2 * (c == "w")]
