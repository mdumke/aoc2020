"""Day 11: Seating System"""

from itertools import product

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def is_valid_position(x, y, list2d):
    return 0 <= x < len(list2d) and 0 <= y < len(list2d[0])


def count_occupied(seats):
    return sum(row.count(OCCUPIED) for row in seats)


def is_occupied(x, y, dx, dy, seats, only_adjacent):
    """return True if a seat in direction dx, dy is occupied"""
    while True:
        x, y = x + dx, y + dy

        if not is_valid_position(x, y, seats) or seats[x][y] == EMPTY:
            return False

        if seats[x][y] == OCCUPIED:
            return True

        if only_adjacent:
            return False


def count_neighbors(x, y, pattern, only_adjacent):
    """return number of occupied seats visible from position x, y"""
    return sum([is_occupied(x, y, dx, dy, pattern, only_adjacent)
                for dx, dy in product([-1, 0, 1], repeat=2) if (dx, dy) != (0, 0)])


def update_position(x, y, pattern, tolerance, only_adjacent):
    """return seat status after next iteration"""
    num_neighbors = count_neighbors(x, y, pattern, only_adjacent)
    state = pattern[x][y]

    if state == EMPTY and num_neighbors == 0:
        return OCCUPIED
    elif state == OCCUPIED and num_neighbors >= tolerance:
        return EMPTY

    return state


def stabilize(pattern, tolerance, only_adjacent=True):
    """return final seat pattern after convergence"""
    while True:
        next_pattern = [[update_position(x, y, pattern, tolerance, only_adjacent)
                         for y in range(len(pattern[0]))]
                        for x in range(len(pattern))]

        if next_pattern == pattern:
            return pattern

        pattern = next_pattern


if __name__ == '__main__':
    with open('input.txt') as f:
        seats = f.read().splitlines()

    print('part 1:', count_occupied(stabilize(seats, 4)))
    print('part 2:', count_occupied(stabilize(seats, 5, only_adjacent=False)))
