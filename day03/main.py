"""Day 3: Toboggan Trajectory"""

import math


def count_trees(forest, dx, dy):
    return sum([row[(i * dy) % len(forest[0])] == '#'
                for i, row in enumerate(forest[::dx])])


if __name__ == '__main__':
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    with open('input.txt') as f:
        forest = f.read().splitlines()

    print('part 1:', count_trees(forest, 1, 3))
    print('part 2:', math.prod([count_trees(forest, *s) for s in slopes]))
