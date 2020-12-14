"""Day 1: Report Repair"""

import math
from itertools import combinations


def sum_to(target: int, n: int, values: [int]) -> [int]:
    """return n values that sum to target"""
    for group in combinations(values, n):
        if sum(group) == target:
            return group


if __name__ == '__main__':
    with open('input.txt') as f:
        values = [int(line) for line in f.readlines()]

    print('part 1:', math.prod(sum_to(2020, 2, values)))
    print('part 2:', math.prod(sum_to(2020, 3, values)))
