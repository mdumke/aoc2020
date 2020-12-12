import re


def manhattan(x, y):
    return abs(x) + abs(y)


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


def update_position(x, y, dx, dy, n):
    for _ in range(n):
        x, y = x + dx, y + dy
    return x, y


def compute_destination_part2(actions):
    position = (0, 0)
    waypoint = (10, 1)

    for op, n in actions:
        if op == 'F':
            position = update_position(*position, *waypoint, n)
        if op in 'NSEW':
            waypoint = translate(*waypoint, op, n)
        if op in 'LR':
            waypoint = rotate(*waypoint, op, n)

    return manhattan(*position)


if __name__ == '__main__':
    with open('input.txt') as f:
        actions = [(op, int(n))
                   for op, n in re.findall(r'(\w)(\d+)', f.read())]

    print('part 2:', compute_destination_part2(actions))
