"""Day 11: Seating System"""

from itertools import product

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def is_valid_position(x, y, list2d):
    return 0 <= x < len(list2d) and 0 <= y < len(list2d[0])


def any_is_occupied(x, y, dx, dy, seats):
    while True:
        x, y = x + dx, y + dy

        if not is_valid_position(x, y, seats) or seats[x][y] == EMPTY:
            return False

        if seats[x][y] == OCCUPIED:
            return True


def adjacent_is_occupied(x, y, dx, dy, seats):
    return is_valid_position(x+dx, y+dy, seats) and seats[x+dx][y+dy] == OCCUPIED


def count_neighbors(x, y, pattern, counting_strategy):
    return sum([counting_strategy(x, y, dx, dy, pattern)
                for dx, dy in product([-1, 0, 1], repeat=2) if (dx, dy) != (0, 0)])


def update_position(x, y, pattern, tolerance, strategy):
    num_neighbors = count_neighbors(x, y, pattern, strategy)
    state = pattern[x][y]

    if state == EMPTY and num_neighbors == 0:
        return OCCUPIED
    elif state == OCCUPIED and num_neighbors >= tolerance:
        return EMPTY

    return state


def count_occupied(pattern, tolerance, strategy):
    while True:
        next_pattern = [[update_position(x, y, pattern, tolerance, strategy)
                         for y in range(len(pattern[0]))]
                        for x in range(len(pattern))]

        if next_pattern == pattern:
            return sum(row.count(OCCUPIED) for row in pattern)

        pattern = next_pattern


if __name__ == '__main__':
    with open('input.txt') as f:
        seats = f.read().splitlines()

    print('part 1:', count_occupied(seats, 4, adjacent_is_occupied))
    print('part 2:', count_occupied(seats, 5, any_is_occupied))