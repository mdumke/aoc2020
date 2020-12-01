#!/usr/bin/env python

import math
from itertools import combinations


def sum_to(target, n, values):
    """return the product of n values that sum to target"""
    for tupl in combinations(values, n):
        if sum(tupl) == target:
            return tupl


def get_puzzle_input():
    """return a list of integers"""
    with open('input.txt') as f:
        values = [int(line) for line in f.readlines()]

    return values


if __name__ == '__main__':
    values = get_puzzle_input()
    print('part 1:', math.prod(sum_to(2020, 2, values)))
    print('part 2:', math.prod(sum_to(2020, 3, values)))
