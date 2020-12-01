#!/usr/bin/env python

from itertools import combinations

def problem1(values):
    """return the product of two values summing to 2020"""
    for a, b in combinations(values, 2):
        if a + b == 2020:
            return a * b


def problem2(values):
    """return the product of three values summing to 2020"""
    for a, b, c  in combinations(values, 3):
        if a + b + c == 2020:
            return a * b * c


def get_puzzle_input():
    """return a list of integers"""
    with open('input.txt') as f:
        values = [int(line) for line in f.readlines()]

    return values


if __name__ == '__main__':
    values = get_puzzle_input()
    print('solution 1:', problem1(values))
    print('solution 2:', problem2(values))
