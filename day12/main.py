"""Day 12: Rain Risk"""

import re


def manhattan(x, y):
    return abs(x) + abs(y)


def translate_coord(x, y, direction, n):
    return {

        'N': (x, y + n),
        'S': (x, y - n),
        'E': (x + n, y),
        'W': (x - n, y)}[direction]


def rotate_coord(x, y, op, n):
    return {
        90: (y, -x),
        180: (-x, -y),
        270: (-y, x)
    }[n if op == 'R' else 360 - n]


def move_in_direction(x, y, dx, dy, n):
    for _ in range(n):
        x, y = x + dx, y + dy
    return x, y


def update_orientation(current, op, n):
    index = 'NESW'.find(current)
    direction = 1 if op == 'R' else -1
    return 'NESW'[(index + (n // 90) * direction) % 4]


def get_distance_part1(actions):
    position = (0, 0)
    orientation = 'E'

    for op, n in actions:
        if op == 'F':
            position = translate_coord(*position, orientation, n)
        if op in 'NSEW':
            position = translate_coord(*position, op, n)
        if op in 'LR':
            orientation = update_orientation(orientation, op, n)

    return manhattan(*position)


def get_distance_part2(actions):
    position = (0, 0)
    waypoint = (10, 1)

    for op, n in actions:
        if op == 'F':
            position = move_in_direction(*position, *waypoint, n)
        if op in 'NSEW':
            waypoint = translate_coord(*waypoint, op, n)
        if op in 'LR':
            waypoint = rotate_coord(*waypoint, op, n)

    return manhattan(*position)


if __name__ == '__main__':
    with open('input.txt') as f:
        actions = [(op, int(n))
                   for op, n in re.findall(r'(\w)(\d+)', f.read())]

    print('part 1:', get_distance_part1(actions))
    print('part 2:', get_distance_part2(actions))
