"""Day 13: Shuttle Search"""

import math


def get_next_bus(buses, start):
    return min([(bus - start % bus, bus) for bus in buses if bus != 'x'])


def match_offset(time, cycle, bus, offset):
    for i in range(bus):
        if (time + i * cycle + offset) % bus == 0:
            return time + i * cycle, cycle * bus


def find_earliest_target_pattern(buses):
    time = cycle = buses[0]
    for offset, bus in enumerate(buses[1:], 1):
        if bus != 'x':
            time, cycle = match_offset(time, cycle, bus, offset)
    return time


if __name__ == '__main__':
    with open('input.txt') as f:
        start = int(next(f))
        buses = [int(n) if n.isdigit() else n
                 for n in next(f).strip().split(',')]

    print('part 1:', math.prod(get_next_bus(buses, start)))
    print('part 2:', find_earliest_target_pattern(buses))
