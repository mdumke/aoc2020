import re


def manhattan(x, y):
    return abs(x) + abs(y)


def update_position(x, y, direction, n):
    if direction == 'N':
        return x, y + n
    if direction == 'S':
        return x, y - n
    if direction == 'E':
        return x + n, y
    if direction == 'W':
        return x - n, y


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


def compute_destination_distance(instructions):
    position = (0, 0)
    orientation = 'E'

    for op, n in instructions:
        position, orientation = move(*position, orientation, op, n)

    return manhattan(*position)


if __name__ == '__main__':
    with open('input.txt') as f:
        ops = [(op, int(n)) for op, n in re.findall(r'(\w)(\d+)', f.read())]

    print('part 1:', compute_destination_distance(ops))
