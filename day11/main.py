"""Day 11: Seating System"""

from itertools import product


def is_valid_position(x, y, list2d):
    return 0 <= x < len(list2d) and 0 <= y < len(list2d[0])


def checksum(pattern):
    return hash(''.join([''.join(line) for line in pattern]))


def count(symbol, pattern):
    return sum([s == symbol for row in pattern for s in row])


def any_is_occupied(x, y, dx, dy, seats):
    while True:
        x, y = x + dx, y + dy

        if not is_valid_position(x, y, seats) or seats[x][y] == 'L':
            return False

        if seats[x][y] == '#':
            return True


def adjacent_is_occupied(x, y, dx, dy, seats):
    return is_valid_position(x+dx, y+dy, seats) and seats[x+dx][y+dy] == '#'


def count_neighbors(x, y, seats, counting_policy):
    return sum([counting_policy(x, y, dx, dy, seats)
                for dx, dy in product([-1, 0, 1], repeat=2) if (dx, dy) != (0, 0)])


def update_position(x, y, pattern, tolerance, strategy):
    symbol = pattern[x][y]
    num_neighbors = count_neighbors(x, y, pattern, strategy)

    if num_neighbors == 0 and symbol == 'L':
        symbol = '#'
    elif num_neighbors >= tolerance and symbol == '#':
        symbol = 'L'

    return symbol


def stabilize(pattern, tolerance, strategy):
    while True:
        next_pattern = [
            [update_position(i, j, pattern, tolerance, strategy)
             for j in range(len(pattern[0]))]
            for i in range(len(pattern))]

        if checksum(next_pattern) == checksum(pattern):
            return pattern

        pattern = next_pattern


if __name__ == '__main__':
    with open('input.txt') as f:
        seats = f.read().splitlines()

    print('part 1:', count('#', stabilize(seats, 4, adjacent_is_occupied)))
    print('part 2:', count('#', stabilize(seats, 5, any_is_occupied)))
