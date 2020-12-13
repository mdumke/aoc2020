"""Day 13: Shuttle Search"""

import math
import numpy as np


def get_next_bus(buses, start):
    return min([(bus - start % bus, bus) for bus in buses if bus != 'x'])


def first_match(start, step, target, offset):
    i = 0
    while i < target:
        if (start + (i * step) + offset) % target == 0:
            return start + i * step, step * target
        i += 1


def find_earliest_target_pattern(buses):
    n = rep = buses[0]
    for offset, bus in enumerate(buses[1:], 1):
        if bus != 'x':
            n, rep = first_match(n, rep, bus, offset)
    return n


if __name__ == '__main__':
    with open('input.txt') as f:
        start = int(next(f))
        buses = [int(n) if n.isdigit()
                 else n for n in f.read().strip().split(',')]


print('part 1:', math.prod(get_next_bus(buses, start)))
print('part 2:', find_earliest_target_pattern(buses))
