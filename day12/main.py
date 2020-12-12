"""Day 12: Rain Risk"""


def translate(x, y, direction, n):
    return {
        'N': (x, y + n),
        'S': (x, y - n),
        'E': (x + n, y),
        'W': (x - n, y)
    }[direction]


def rotate(x, y, op, n):
    return {
        90: (y, -x),
        180: (-x, -y),
        270: (-y, x)
    }[n if op == 'R' else 360 - n]


def turn(direction, side, degrees):
    return {
        'N': 'NESW',
        'E': 'ESWN',
        'S': 'SWNE',
        'W': 'WNES'
    }[direction][(degrees if side == 'R' else 360 - degrees) // 90]


def get_distance_strategy1(actions):
    x, y = 0, 0
    direction = 'E'
    for op, n in actions:
        if op == 'F':
            x, y = translate(x, y, direction, n)
        if op in 'NSEW':
            x, y = translate(x, y, op, n)
        if op in 'LR':
            direction = turn(direction, op, n)
    return abs(x) + abs(y)


def get_distance_strategy2(actions):
    x, y = 0, 0
    waypoint = 10, 1
    for op, n in actions:
        if op == 'F':
            x, y = x + waypoint[0] * n, y + waypoint[1] * n
        if op in 'NSEW':
            waypoint = translate(*waypoint, op, n)
        if op in 'LR':
            waypoint = rotate(*waypoint, op, n)
    return abs(x) + abs(y)


if __name__ == '__main__':
    with open('input.txt') as f:
        actions = [(l[0], int(l[1:])) for l in f.read().splitlines()]

    print('part 1:', get_distance_strategy1(actions))
    print('part 2:', get_distance_strategy2(actions))
