import re


def manhattan(x, y):
    return abs(x) + abs(y)


def update_position(position, waypoint, n):
    def add(x, y, dx, dy):
        return x + dx, y + dy

    for _ in range(n):
        position = add(*position, *waypoint)

    return position


def translate_waypoint(x, y, op, n):
    return {
        'N': (x, y + n),
        'S': (x, y - n),
        'E': (x + n, y),
        'W': (x - n, y)}[op]


def rotate_waypoint(x, y, op, n):
    return [None, (y, -x), (-x, -y), (-y, x)][n // 90 if op == 'R' else 4 - n // 90]


def move(position, waypoint, op, n):
    if op == 'F':
        return update_position(position, waypoint, n), waypoint
    if op in 'NSEW':
        return position, translate_waypoint(*waypoint, op, n)
    if op in 'LR':
        return position, rotate_waypoint(*waypoint, op, n)


def compute_destination_distance(actions):
    position = (0, 0)
    waypoint = (10, 1)

    for action in actions:
        position, waypoint = move(position, waypoint, *action)

    return manhattan(*position)


if __name__ == '__main__':
    with open('input.txt') as f:
        actions = [(op, int(n))
                   for op, n in re.findall(r'(\w)(\d+)', f.read())]

    print('part 2:', compute_destination_distance(actions))
