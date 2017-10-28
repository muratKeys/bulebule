from io import StringIO

import numpy
import pytest

from mazes import load_maze
from mazes import read_walls


MAZE_OSHWDEM_00 = """OSHWDEM Maze Generator v1.2 R42263
+---+---+---+---+---+
| A |               |
+   +   +---+---+   +
|   |   |       |   |
+   +   +   B   +   +
|       |       |   |
+   +   +---+   +---+
|   |       |       |
+   +   +---+---+   +
|   |               |
+---+---+---+---+---+
"""


def test_load_maze_oshwdem():
    result = load_maze(StringIO(MAZE_OSHWDEM_00))
    assert (result == numpy.array([
        [28, 12, 10, 10, 24],
        [20, 20, 12, 24, 20],
        [4, 16,  6, 16, 22],
        [20,  4, 26,  6, 24],
        [22,  6, 10, 10, 18],
    ])).all()


@pytest.mark.parametrize('x,y,direction,walls', [
    (0, 0, 'E', (True, False, True)),
    (1, 0, 'E', (True, False, True)),
    (2, 0, 'E', (False, False, True)),
    (0, 0, 'N', (True, True, False)),
    (0, 1, 'N', (True, False, False)),
    (3, 2, 'N', (True, True, True)),
    (3, 3, 'S', (True, True, False)),
    (4, 4, 'W', (False, False, True)),
])
def test_read_walls(x, y, direction, walls):
    maze = load_maze(StringIO(MAZE_OSHWDEM_00))
    assert read_walls(maze, x, y, direction) == walls