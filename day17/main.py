"""Day 17: Conway Cubes"""

import numpy as np


def is_valid_coord(coord, shape):
    return all(0 <= dim < shape[i] for i, dim in enumerate(coord))


def shift_coord(coord, offset):
    return tuple(dim + offset for dim in coord)


def expand(dimensions, width):
    return tuple(np.array(dimensions) + [width] * len(dimensions))


def iterate_coords(shape, padding=0):
    if len(shape) == 1:
        for i in range(-padding, shape[0]+padding):
            yield (i,)
    else:
        for i in range(-padding, shape[0]+padding):
            for coord in iterate_coords(shape[1:], padding):
                yield(i, *coord)


def get_neighbors(grid):
    for coord in iterate_coords(grid.shape, padding=1):
        neighbors_idxs = tuple([slice(max(0, dim-1), dim+2) for dim in coord])

        if is_valid_coord(coord, grid.shape):
            store = grid[coord]
            grid[coord] = 0
            neighbors = grid[neighbors_idxs].copy()
            is_active = store
            grid[coord] = store
        else:
            neighbors = grid[neighbors_idxs].copy()
            is_active = 0

        yield coord, is_active, neighbors


def evolve(grid, generations=1):
    for _ in range(generations):
        new_grid = np.zeros(expand(grid.shape, 2))

        for coord, is_active, neighbors in get_neighbors(grid):
            if is_active:
                new_grid[shift_coord(coord, 1)] = neighbors.sum() in [2, 3]
            else:
                new_grid[shift_coord(coord, 1)] = neighbors.sum() == 3

        grid = new_grid

    return grid


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = np.array([[symbol == '#' for symbol in line]
                         for line in f.read().splitlines()])

    print('part 1:', evolve(grid[None], 6).sum())
    print('part 2:', evolve(grid[None, None], 6).sum())
