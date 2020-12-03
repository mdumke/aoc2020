#!/usr/bin/env python

"""Day 3: Toboggan Trajectory"""

import math

with open('input.txt') as f:
    forest = [l.rstrip() for l in f.readlines()]


def count_trees(forest, slope):
    n, m = len(forest), len(forest[0])
    i, j = 0, 0
    trees = 0

    while (i < n):
        trees += forest[i][j] == '#'
        i += slope[0]
        j = (j + slope[1]) % m

    return trees


print('part 1:', count_trees(forest, (1, 3)))
print('part 2:', math.prod(
    [count_trees(forest, slope)
     for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]]))
