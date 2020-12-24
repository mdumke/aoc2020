"""Day 24: Lobby Layout"""


import re
from collections import defaultdict

BLACK, WHITE = 1, 0


directions = {
    'e': (1, 0),
    'w': (-1, 0),
    'se': (0.5, -1),
    'sw': (-0.5, -1),
    'ne': (0.5, 1),
    'nw': (-0.5, 1)}


neighbors = [
    (1, 0),
    (-1, 0),
    (0.5, -1),
    (-0.5, -1),
    (0.5, 1),
    (-0.5, 1)]


def evaluate(steps):
    current = [0, 0]

    for step in steps:
        current[0] += step[0]
        current[1] += step[1]

    return tuple(current)


def get_neighbors(tile, tiles):
    return {(x := tile[0] + n[0], y := tile[1] + n[1]): tiles.get((x, y)) or 0
            for n in neighbors}


def get_all_neighbors(tiles):
    return {(x := tile[0] + n[0], y := tile[1] + n[1]): tiles.get((x, y)) or 0
            for tile in tiles for n in neighbors}


def evolve_tile(tile, color, tiles):
    black_neighbors = sum(get_neighbors(tile, tiles).values())

    if color == BLACK:
        return black_neighbors in [1, 2]
    if color == WHITE:
        return black_neighbors == 2


def evolve(tiles):
    new_tiles = defaultdict(int)

    # add neighbors, because they may have to flip
    new_tiles.update({**get_all_neighbors(tiles), **tiles})

    # check update conditions
    for tile, color in new_tiles.items():
        new_tiles[tile] = evolve_tile(tile, color, tiles)

    return new_tiles


with open('input.txt') as f:
    moves = [[directions[d] for d in re.findall('(se|sw|ne|nw|e|w)', line)]
             for line in f.read().splitlines()]

    tiles = defaultdict(int)

    for tile in [evaluate(steps) for steps in moves]:
        tiles[tile] = (tiles[tile] + 1) % 2

    print('part 1:', sum(tiles.values()))

    for i in range(100):
        tiles = evolve(tiles)

    print('part 2:', sum(tiles.values()))
