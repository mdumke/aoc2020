import re
from collections import defaultdict

directions = {
    'e': (1, 0),
    'w': (-1, 0),
    'se': (0.5, -1),
    'sw': (-0.5, -1),
    'ne': (0.5, 1),
    'nw': (-0.5, 1)}

def evaluate(steps):
    current = [0, 0]
    for step in steps:
        current[0] += step[0]
        current[1] += step[1]
    return tuple(current)


def flip_tiles(moves):
    tiles = defaultdict(int)
    for tile in [evaluate(steps) for steps in moves]:
        tiles[tile] = (tiles[tile] + 1) % 2
    return tiles


if __name__ == '__main__':
    with open('input.txt') as f:
        moves = [[directions[d] for d in re.findall('(se|sw|ne|nw|e|w)', line)]
                 for line in f.read().splitlines()]

    print('part 1:', sum(flip_tiles(moves).values()))

