"""
Tests go here.

To run tests

```console
pytest  # manually
ptw .   # them automatically
```
"""

from foo import setup_grid, create_initial_state, move_ant, get_new_direction


def test_setup_3by3():
    assert setup_grid(3) == [
        ["w", "w", "w"],
        ["w", "w", "w"],
        ["w", "w", "w"],
    ]


def test_setup_5by5():
    assert setup_grid(5) == [
        ["w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w"],
    ]


def test_setup_initial_state():
    state = create_initial_state(5)
    assert state.grid == [
        ["w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w"],
    ]
    assert state.ant_position == (2, 2)
    assert state.ant_facing == "north"


def test_setup_initial_state():
    state = create_initial_state(3)
    assert state.grid == [
        ["w", "w", "w"],
        ["w", "w", "w"],
        ["w", "w", "w"],
    ]
    assert state.ant_position == (1, 1)
    assert state.ant_facing == "north"


def test_ant_moves_away_from_white_field():
    state = create_initial_state(3)
    new_state = move_ant(state)
    assert new_state.grid == [
        ["w", "w", "w"],
        ["w", "b", "w"],
        ["w", "w", "w"],
    ]
    assert new_state.ant_position == (2, 1)
    assert new_state.ant_facing == "east"


def test_get_new_direction():
    assert get_new_direction("north", "w") == "east"


def test_get_new_direction2():
    assert get_new_direction("east", "w") == "south"


def test_get_new_direction3():
    assert get_new_direction("north", "b") == "west"


def test_get_new_direction4():
    assert get_new_direction("west", "w") == "north"
