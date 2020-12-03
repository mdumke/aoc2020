"""Day 3: Toboggan Trajectory"""

import math


with open('input.txt') as f:
    forest = f.read().splitlines()

print('part 1:', sum([
    row[(i * 3) % len(forest[0])] == '#' for i, row in enumerate(forest)]))

print('part 2:', math.prod([
    sum([row[(i * dy) % len(forest[0])] == '#' for i, row in enumerate(forest[::dx])])
    for dx, dy in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]]))
