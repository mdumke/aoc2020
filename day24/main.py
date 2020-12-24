"""Day 24: Lobby Layout"""


import re
from functools import reduce
from collections import defaultdict

BLACK, WHITE = 1, 0

DIRECTIONS = {
    'e': (1, 0),
    'w': (-1, 0),
    'se': (0.5, -1),
    'sw': (-0.5, -1),
    'ne': (0.5, 1),
    'nw': (-0.5, 1)}


def add(coord1, coord2):
    return coord1[0] + coord2[0], coord1[1] + coord2[1]


def final_coord(steps):
    """return coord after following STEPS from origin"""
    return reduce(add, steps, (0, 0))


def get_initial_state(moves):
    """return initial BLACK/WHITE tiles"""
    tiles = defaultdict(int)
    for tile in [final_coord(steps) for steps in moves]:
        tiles[tile] = (tiles[tile] + 1) % 2
    return tiles


def get_neighboring_colors(tile, tiles):
    """return colors of all six neighbors of TILE"""
    return [tiles[add(tile, step)] for step in DIRECTIONS.values()]


def get_all_neighbors(tiles):
    """return all tiles that are adjacent to any existing tile"""
    return {(x := tile[0] + n[0], y := tile[1] + n[1]): tiles.get((x, y)) or 0
            for tile in tiles for n in DIRECTIONS.values()}


def update_tile(tile, color, tiles):
    """return new state BLACK/WHITE of given tile"""
    black_neighbors = sum(get_neighboring_colors(tile, tiles))

    if color == BLACK:
        return black_neighbors in [1, 2]
    if color == WHITE:
        return black_neighbors == 2


def update_floor(tiles):
    """returns tiles after update step"""
    new_tiles = defaultdict(int)

    # add neighbors, because they may have to flip
    new_tiles.update({**get_all_neighbors(tiles), **tiles})

    # check update conditions
    for tile, color in new_tiles.items():
        new_tiles[tile] = update_tile(tile, color, tiles)

    return new_tiles


def evolve(tiles, epochs):
    """return state of floor after EPOCHS iterations"""
    for _ in range(epochs):
        tiles = update_floor(tiles)
    return tiles


with open('input.txt') as f:
    moves = [[DIRECTIONS[d] for d in re.findall('(se|sw|ne|nw|e|w)', line)]
             for line in f.read().splitlines()]

    tiles = get_initial_state(moves)
    print('part 1:', sum(tiles.values()))
    print('part 2:', sum(evolve(tiles, 100).values()))
