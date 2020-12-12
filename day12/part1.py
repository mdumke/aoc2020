import re


def manhattan(x, y):
    return abs(x) + abs(y)


def update_position(x, y, direction, n):
    return {
        'N': (x, y + n),
        'S': (x, y - n),
        'E': (x + n, y),
        'W': (x - n, y)}[direction]


def rotate(orientation, op, n):
    current = 'NESW'.find(orientation)
    direction = 1 if op == 'R' else -1
    return 'NESW'[(current + (n // 90) * direction) % 4]


def move(x, y, orientation, op, n):
    if op == 'F':
        return update_position(x, y, orientation, n), orientation
    if op in 'NSEW':
        return update_position(x, y, op, n), orientation
    if op in 'LR':
        return (x, y), rotate(orientation, op, n)


def compute_destination_distance(actions):
    position = (0, 0)
    orientation = 'E'

    for action in actions:
        position, orientation = move(*position, orientation, *action)

    return manhattan(*position)


if __name__ == '__main__':
    with open('input.txt') as f:
        actions = [(op, int(n))
                   for op, n in re.findall(r'(\w)(\d+)', f.read())]

    print('part 1:', compute_destination_distance(actions))
